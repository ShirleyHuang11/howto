---
name: retry-a-failed-tool-call
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/agents/handle-tool-call-errors]
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent retries failed tool calls only when doing so is safe, bounded, and likely to work. Success means transient failures recover automatically while non-idempotent or invalid calls stop or repair instead of duplicating side effects.

## Preconditions

- Tool calls are wrapped in structured success/error envelopes.
- Each tool declares whether it is read-only, idempotent write, or non-idempotent write.
- You can run a test harness with stubbed `429`, timeout, validation, and success responses.

## Steps

1. **Define retry eligibility per tool.** Add metadata such as `{"read_only": true, "idempotent": true, "max_retries": 3}` to every tool. → *Expect:* each registered tool has an explicit retry policy.
2. **Require idempotency keys for retried writes.** For write tools, pass a stable key like `run_id + tool_call_id + normalized_args_hash`. ⚠️ *Irreversible:* do not retry external writes such as purchases, emails, or deletes unless the upstream API honors the idempotency key. → *Expect:* retried writes use the same idempotency key and do not create duplicate records.
3. **Retry only transient error classes.** Retry `429`, timeout, connection reset, and selected `5xx`; do not retry `400`, schema validation, `401`, `403`, or policy denial. → *Expect:* the retry wrapper returns `retry_decision="retry"` only for configured transient errors.
4. **Use exponential backoff with jitter.** For example, sleep `min(base * 2**attempt + random_jitter, max_delay)` and respect provider `Retry-After` headers. → *Expect:* retry timestamps increase and do not exceed `max_delay`.
5. **Revalidate the final result.** After a retry succeeds, validate the tool result schema before giving it to the model. → *Expect:* the recovered call produces `ok=true` and data that passes schema validation.
6. **Surface exhausted retries clearly.** Return `{"ok": false, "error": {"type": "retry_exhausted", "attempts": 3}}` and stop or ask the user depending on the task. → *Expect:* the agent does not silently continue with missing data.

## Decision points

- Tool is read-only and error is transient → retry with backoff.
- Tool is a write and has no idempotency support → do not retry; ask for human confirmation or operator handling.
- Error includes `Retry-After` → use that delay unless it exceeds your run budget.
- Retry budget is exhausted → stop the step and report a retry-exhausted observation.

## Failure modes & recovery

- **F1 Duplicate side effect:** detect two external records from one intended action → disable retries for that tool until idempotency is implemented.
- **F2 Provider throttling escalates:** detect repeated `429` after retries → reduce concurrency and honor longer retry windows.
- **F3 Retrying bad input:** detect repeated `400` or schema errors → route to argument repair, not retry.
- **F4 Hidden partial success:** detect timeout after a write where upstream state is unknown → query status by idempotency key before attempting another write.

## Verification

Run deterministic tests with a fake clock: a read tool that returns `429, 429, success` must be called exactly three times with increasing delays; a `400` validation error must be called once; a write retry must reuse the same idempotency key; and exhausted retries must return a `retry_exhausted` error object that validates against the error schema.

## Variations

- `HTTP APIs`: use status codes, `Retry-After`, and idempotency headers.
- `database tools`: retry serialization failures and deadlocks, but not uniqueness or permission errors.
- `queue workers`: let the queue own retry delay, but still record retry eligibility and poison-message limits.

## Safety & privacy

Medium risk because retries can multiply cost and duplicate external actions. Cap attempts, use jitter, require idempotency for writes, log sanitized arguments only, and require review before retrying payments, messages, deletions, or user-visible changes.
