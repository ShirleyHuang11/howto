---
name: handle-tool-call-errors
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent turns failed tool calls into structured, recoverable observations instead of crashing or hallucinating a result. Success means every tool failure is classified, logged, and either retried, repaired, or surfaced to the user with a clear stop reason.

## Preconditions

- An agent runtime with tool/function calling and a test harness that can stub tool responses.
- A typed tool result envelope such as `{ "ok": true, "data": ... }` or `{ "ok": false, "error": { "type": "...", "retryable": true } }`.
- You can call the model and run automated tests for at least one failure path.

## Steps

1. **Wrap every tool handler in a common error envelope.** Return machine-readable errors instead of raw exceptions, for example `{"ok": false, "error": {"type": "timeout", "message": "request timed out", "retryable": true}}`. → *Expect:* a failed tool call still returns valid JSON matching the error schema.
2. **Classify errors by recovery policy.** Map failures to `retryable`, `needs_model_repair`, `needs_user_input`, `permission_denied`, or `fatal`. → *Expect:* each fixture error has exactly one policy label.
3. **Send the model only safe diagnostic detail.** Include the tool name, policy, and sanitized message; remove stack traces, secrets, and raw user records. → *Expect:* the next agent turn contains no API keys, bearer tokens, or unredacted PII.
4. **Teach the agent how to recover.** In the system/developer instruction, require it to retry transient errors, correct invalid arguments, ask for missing user input, and stop on permission or fatal errors. → *Expect:* the agent selects a recovery action rather than inventing a successful tool result.
5. **Add a circuit breaker.** Stop after `max_tool_failures` or repeated identical errors, such as `3` failed calls to the same tool with the same normalized message. → *Expect:* the run ends with `status="failed"` and `reason="tool_failure_limit"` when the limit is reached.
6. **Log the failed call and recovery action.** Store `trace_id`, `tool_name`, sanitized arguments hash, error type, retry count, and final outcome. → *Expect:* one trace row exists for each failed tool attempt.

## Decision points

- Error is `timeout`, `429`, or `5xx` → retry with backoff if the idempotency policy allows it.
- Error is schema validation or missing required argument → ask the model to repair the arguments once, then revalidate.
- Error is `403`, destructive action denied, or missing consent → stop and request explicit user authorization.
- Same tool fails repeatedly with the same error → stop and return a bounded failure summary.

## Failure modes & recovery

- **F1 Raw exception leaks:** detect stack traces or secrets in agent observations → redact at the tool boundary and add a regression test with a fake secret.
- **F2 Hallucinated success:** detect final answers that cite failed tool data as real → require the final response to reference only `ok=true` tool results.
- **F3 Retry storm:** detect repeated calls without delay or cap → enforce exponential backoff and `max_tool_failures`.
- **F4 Non-idempotent duplicate:** detect repeated writes with different external IDs → require idempotency keys before retrying write tools.

## Verification

Run a test suite that stubs one timeout, one invalid-arguments error, and one permission error. The timeout is retried no more than the configured limit, the invalid call is repaired and passes JSON Schema validation, the permission error stops without another tool call, and every failed attempt produces a trace record with a sanitized error envelope.

## Variations

- `OpenAI`: use tool-call IDs and return a tool message containing the structured error envelope.
- `Anthropic`: return the tool result block with `is_error` semantics plus the same JSON payload.
- `LangGraph`: model the error policy as explicit edges from a tool node to retry, repair, user-input, or terminal nodes.

## Safety & privacy

Medium risk because tool errors often contain private arguments, stack traces, and provider details. Redact secrets before model exposure, cap retries to control spend, require idempotency for write tools, and stop for permission or irreversible-action failures instead of letting the agent improvise.
