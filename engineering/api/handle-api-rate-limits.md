---
name: handle-api-rate-limits
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Make API clients respect provider rate limits, recover from `429` responses, and avoid turning retries into traffic spikes.

## Preconditions

- The provider's rate-limit headers and quotas are documented or observable.
- The client code can centralize HTTP request handling.
- Metrics or logs can record response status and retry counts.

## Steps

1. **Read the provider limit contract.** Identify quota window, burst rules, and headers such as `Retry-After`, `X-RateLimit-Remaining`, or `RateLimit-Reset`. → *Expect:* the client knows which signal controls waiting.
2. **Centralize request throttling.** Route outbound calls through one client wrapper or queue. → *Expect:* every call path shares the same limiter.
3. **Honor `Retry-After`.** On `429`, sleep for the header duration when present before retrying. → *Expect:* retries resume after the provider's requested delay.
4. **Add exponential backoff with jitter.** Use bounded delays such as `min(base * 2**attempt + jitter, max_delay)`. → *Expect:* concurrent workers do not retry at the same instant.
5. **Cap retries and surface failure.** Stop after a small number of attempts and return a typed rate-limit error. → *Expect:* callers can defer work or show a user-safe message.
6. **Prevent avoidable calls.** Cache read responses where allowed and batch requests when the API supports it. → *Expect:* request volume drops under normal usage.
7. **Measure the behavior.** Emit metrics for `429`, retry attempts, wait time, and exhausted retries. → *Expect:* dashboards show rate-limit pressure before incidents.

## Decision points

- Provider sends `Retry-After` date instead of seconds → parse HTTP-date and clamp negative waits to zero.
- Requests are user-triggered → return a clear retry-later response instead of blocking too long.
- Requests are background jobs → requeue with scheduled delay.
- Multiple app instances share a quota → use a shared limiter such as Redis, not only in-process counters.

## Failure modes & recovery

- **F1 Retry storm:** detect many workers retrying simultaneously → add jitter and a shared limiter.
- **F2 Ignored provider delay:** detect repeated `429` despite retries → honor `Retry-After` and reduce concurrency.
- **F3 Infinite retry loop:** detect jobs never failing or completing → cap attempts and dead-letter exhausted jobs.
- **F4 Quota unexpectedly low:** detect `403` or quota-exceeded messages → check account plan, scopes, and provider dashboard.

## Verification

A test server returning `429` with `Retry-After: 2` causes the client test to wait or schedule at least 2 seconds before retry, caps attempts, and exits 0; production metrics show no sustained unbounded retry loop.

## Variations

- `GitHub API`: inspect `x-ratelimit-remaining`, `x-ratelimit-reset`, and secondary rate-limit responses.
- `Node.js`: use `p-retry`, `bottleneck`, or a project-standard queue.
- `Python`: use `tenacity` or `backoff` with explicit retry predicates.

## Safety & privacy

Medium risk because bad retry behavior can cause outages or account suspension. Keep logs free of auth headers, coordinate limits across workers, and prefer backpressure over uncontrolled retries.
