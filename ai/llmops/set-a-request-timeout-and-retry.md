---
name: set-a-request-timeout-and-retry
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You configure LLM request timeouts and retries so transient failures recover while users do not wait indefinitely. The retry policy is bounded, observable, and safe for idempotent operations.

## Preconditions

- A central LLM client or gateway wrapper.
- Provider-specific timeout and error handling support.
- A target user-facing latency budget or batch deadline.

## Steps

1. **Set an end-to-end deadline.** Define the maximum time the caller will wait, such as `10s` for chat UI or `5min` for offline batch. → *Expect:* every request has a deadline before the provider call starts.
2. **Set provider request timeouts.** Configure connect, read, and total timeouts in the SDK or HTTP client below the end-to-end deadline. → *Expect:* a stuck network call raises a timeout exception.
3. **Retry only safe failure classes.** Retry 429, 500, 502, 503, network reset, and timeout when no side effect has occurred; do not retry unchanged 400 or context errors. → *Expect:* retry decisions match a policy table.
4. **Use exponential backoff with jitter.** Limit attempts and cumulative sleep so retries cannot exceed the deadline. → *Expect:* logs show attempt number, sleep time, and final outcome.
5. **Propagate cancellation.** If the user or upstream service cancels, abort the provider request and stop retries. → *Expect:* canceled calls end quickly and are marked canceled.
6. **Add idempotency for side-effecting flows.** For tool-using agents or write operations, attach idempotency keys and checkpoint before retrying. → *Expect:* retries cannot duplicate external actions.
7. **Test with simulated failures.** Mock timeouts, 429s, 500s, bad requests, and cancellation. → *Expect:* each test follows the configured policy.

## Decision points

- User-facing UI is interactive → use shorter deadlines and show a retry option.
- Offline batch can wait → use longer deadlines but keep attempt and cost caps.
- Provider returns 429 frequently → reduce concurrency rather than only increasing retries.
- Request includes non-idempotent tool execution → do not retry past the side-effect boundary.
- Deadline expires → return a structured timeout instead of continuing in the background unless explicitly queued.

## Failure modes & recovery

- **F1 Infinite retry loop:** detect attempts exceed policy → enforce max attempts and total deadline.
- **F2 Retry after bad request:** detect repeated 400s → classify context and validation errors as non-retryable.
- **F3 User cancellation ignored:** detect provider calls after disconnect → wire cancellation tokens through all layers.
- **F4 Thundering herd:** detect synchronized retries → add jitter and concurrency limits.
- **F5 Duplicate side effect:** detect external write happened twice → add idempotency keys and retry checkpoints.

## Verification

Timeout and retry handling passes when automated tests prove timeout exceptions occur within the configured deadline, retryable errors retry no more than the maximum attempts, non-retryable errors fail once, cancellation stops further work, and idempotency tests prevent duplicate side effects.

## Variations

- `Anthropic`: configure SDK or HTTP client timeout and handle provider rate-limit errors.
- `OpenAI`: use client timeout options and classify rate-limit, server, and bad-request errors.
- `gateway`: enforce a global deadline across routing, retries, and fallbacks.
- `streaming`: apply both idle chunk timeout and total stream timeout.

## Safety & privacy

Medium risk because retries spend money and may duplicate actions. Bound attempts, avoid retrying non-idempotent operations, stop on cancellation, log metadata without sensitive content, and prefer backpressure over retry storms.
