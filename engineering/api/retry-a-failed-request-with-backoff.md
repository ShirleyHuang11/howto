---
name: retry-a-failed-request-with-backoff
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Retry transient HTTP failures with bounded exponential backoff while avoiding duplicate side effects and hiding permanent errors.

## Preconditions

- The request operation and idempotency behavior are understood.
- The HTTP client can set timeouts and inspect status codes.
- Tests can use a mock server or fake transport.

## Steps

1. **Classify retryable failures.** Retry timeouts, connection resets, `408`, `429`, and most `5xx`; do not retry normal `4xx` validation or auth failures. → *Expect:* permanent bad requests fail quickly.
2. **Require idempotency for writes.** For `POST` creates, send an `Idempotency-Key` when the API supports it. → *Expect:* retried writes do not create duplicate resources.
3. **Set a request timeout.** Configure connect and total timeouts, for example `timeout=10` seconds. → *Expect:* stuck sockets do not hang workers forever.
4. **Implement exponential backoff with jitter.** Try delays such as 0.5s, 1s, 2s, 4s plus random jitter, capped at a maximum. → *Expect:* retries spread out under partial outages.
5. **Honor server retry hints.** If `Retry-After` is present, use it within a configured maximum. → *Expect:* client behavior matches provider guidance.
6. **Cap attempts and report context.** Stop after a fixed count and return status, attempt count, and request ID when available. → *Expect:* failures are observable without logging secrets.
7. **Test the retry matrix.** Mock two `503`s followed by `200`, then a permanent `400`. → *Expect:* transient case succeeds after retries and permanent case is not retried.

## Decision points

- Request is non-idempotent and no idempotency key exists → do not automatically retry after the request may have reached the server.
- User is waiting interactively → use fewer attempts and shorter total delay.
- Background job → requeue with scheduled delay after local retry cap.
- Provider sends request IDs → include them in error logs and support tickets.

## Failure modes & recovery

- **F1 Duplicate side effects:** detect repeated orders or charges → add idempotency keys and reconcile duplicates manually.
- **F2 Retry hides outage:** detect long user waits with eventual failure → reduce interactive retry budget and surface status.
- **F3 Thundering retry:** detect synchronized spikes after outage → add jitter and shared rate limiting.
- **F4 Retrying auth errors:** detect repeated `401` attempts → exclude auth and validation statuses from retry policy.

## Verification

The retry unit test exits 0 and proves: a mock sequence `503, 503, 200` is attempted three times, a mock `400` is attempted once, and a write request includes an idempotency key.

## Variations

- `Python`: use `tenacity` with `retry_if_exception_type` and `retry_if_result` predicates.
- `Node.js`: use `p-retry` or a project HTTP wrapper with `AbortController`.
- `Queues`: let the job queue handle long backoff after a short in-process retry.

## Safety & privacy

Medium risk because retries can multiply writes and traffic. Do not retry unsafe writes without idempotency, redact auth headers, cap total retry time, and include request IDs instead of payload secrets in logs.
