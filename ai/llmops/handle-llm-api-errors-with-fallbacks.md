---
name: handle-llm-api-errors-with-fallbacks
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You wrap LLM API calls with retries, timeouts, fallback models, and validation so transient failures recover without hiding bad outputs. The system returns a structured success or failure reason.

## Preconditions

- A central LLM call wrapper used by the application.
- Provider error codes and retry guidance for the selected APIs.
- At least one fallback model or degraded behavior path.

## Steps

1. **Classify errors by retryability.** Map 429, 500, 502, 503, and network resets to retryable; map 400, auth failures, safety blocks, and validation failures to non-retryable or limited-retry. → *Expect:* an error policy table in code.
2. **Add bounded exponential backoff.** Retry retryable failures with jitter, a maximum attempt count, and total deadline. → *Expect:* transient failures retry without exceeding the request timeout.
3. **Set request and operation timeouts.** Use per-provider request timeouts plus an overall application deadline. → *Expect:* hung calls return a controlled timeout error.
4. **Validate before accepting a response.** Parse JSON, check schema, verify citations, or enforce tool-call constraints before returning success. → *Expect:* malformed responses are retried or rejected according to policy.
5. **Route to fallbacks deliberately.** [BRANCH: smaller model | alternate provider | cached response | human review] Use fallbacks only when they meet the task's safety and quality requirements. ⚠️ *Data leaves your control:* alternate providers receive the prompt too; confirm privacy approval before cross-provider fallback. → *Expect:* logs show primary failure and fallback outcome.
6. **Expose structured failure to callers.** Return error type, retryable flag, request id, and user-safe message. → *Expect:* downstream code can decide whether to retry, degrade, or show an error.
7. **Test failure injection.** Simulate 429s, 500s, timeouts, malformed JSON, and auth failures. → *Expect:* each case follows the policy table.

## Decision points

- Error is rate limit → retry with backoff and reduce concurrency.
- Error is context length → do not retry unchanged; trim or summarize input.
- Error is auth or permission → fail fast and alert operators.
- Primary provider is down → use approved fallback or degrade gracefully.
- Fallback quality is below threshold → return failure rather than silently shipping worse output.

## Failure modes & recovery

- **F1 Retry storm:** detect many concurrent retries after 429 → add jitter, concurrency limits, and circuit breakers.
- **F2 Bad fallback answer:** detect fallback fails evals → restrict fallback to safe tasks or require human review.
- **F3 Non-idempotent tool repeated:** detect duplicated side effects → never retry after tool execution without idempotency keys.
- **F4 Timeout too long:** detect user requests hanging → set shorter per-call and overall deadlines.
- **F5 Sensitive cross-provider leak:** detect fallback sends restricted data to an unapproved provider → disable fallback and audit logs.

## Verification

The wrapper passes when automated failure-injection tests confirm retryable errors retry within limits, non-retryable errors fail fast, fallbacks are used only for approved cases, invalid outputs are not returned as success, and every failure includes a structured reason.

## Variations

- `Anthropic`: inspect SDK exceptions and request ids; retry documented transient errors.
- `OpenAI`: handle rate-limit, server, timeout, and bad-request classes distinctly.
- `open model`: fallback may be another local checkpoint or a queue for later processing.
- `agent tools`: add idempotency keys and checkpointing before any side-effecting retry.

## Safety & privacy

Medium risk because fallbacks can send data to additional systems and retries can duplicate side effects or spend. Keep provider allowlists, cap attempts, log request ids without raw sensitive prompts, and require review for cross-provider fallback involving user or proprietary data.
