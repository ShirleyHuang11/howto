---
name: rate-limit-an-llm-endpoint
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You protect an LLM endpoint from abuse, provider throttling, and spend spikes by enforcing request and token limits before work is sent downstream.

## Preconditions

- An API gateway, service middleware, or edge worker where requests can be rejected before model calls.
- Stable identity keys such as API key, user ID, tenant ID, IP, or session ID.
- A shared store such as Redis for distributed counters.
- Known provider limits for requests per minute, tokens per minute, and concurrent requests.

## Steps

1. **Choose rate-limit dimensions.** Define limits by identity, route, model class, and token estimate, not just raw request count. → *Expect:* a table such as `tenant: 60 rpm, 120k tpm, 8 concurrent`.
2. **Estimate tokens before admission.** Count input tokens and add requested `max_tokens` to reserve worst-case capacity. → *Expect:* each incoming request has `estimated_tokens` before any provider call.
3. **Implement atomic counters.** Use Redis token bucket, leaky bucket, or sliding window scripts with TTLs for request and token dimensions. → *Expect:* concurrent requests update limits atomically without oversubscription.
4. **Return clear limit responses.** Reject excess requests with HTTP `429`, `Retry-After`, and a machine-readable error code. → *Expect:* clients can back off without guessing.
5. **Add concurrency limits.** Acquire a short-lived lease before starting generation and release it on completion or timeout. → *Expect:* long generations cannot exhaust worker or provider concurrency.
6. **Coordinate with provider limits.** Set your internal limit below provider quotas and add jittered retries only for safe, idempotent requests. → *Expect:* provider 429s become rare under normal load.
7. **Instrument limit outcomes.** Emit allowed, rejected, queued, token-reserved, token-actual, and provider-429 metrics. → *Expect:* dashboards show who is hitting limits and whether reservations are accurate.
8. **Load-test the policy.** Use `k6`, `locust`, or a custom script to exceed each dimension deliberately. → *Expect:* excess traffic gets `429`, accepted traffic remains within latency and provider quota budgets.

## Decision points

- Users need bursty workflows → use token buckets with burst capacity instead of fixed windows.
- Provider 429s still occur → lower internal limits or add a shared global limiter.
- Token reservations greatly exceed actual use → refund unused reserved tokens after the response.
- Endpoint serves multiple tenants → enforce tenant limits before user limits so one tenant cannot starve others.

## Failure modes & recovery

- **F1 Non-atomic counters:** detect accepted traffic above the configured limit during load tests → move to Redis scripts or gateway-native atomic quotas.
- **F2 Identity spoofing:** detect many accounts or IPs sharing payment/user traits → add stronger auth and tenant-level limits.
- **F3 Stuck concurrency lease:** detect active leases with no worker → add TTLs and release in `finally` blocks.
- **F4 Provider throttling:** detect provider 429 despite local allow decisions → reduce headroom and retry with exponential backoff.
- **F5 Client retry storm:** detect repeated immediate retries after 429 → document `Retry-After`, add client SDK backoff, and consider temporary bans.

## Verification

Run a load test that sends at least 2x the configured request and token rate for one identity. The check passes only when accepted requests remain at or below the configured limits, rejected requests return HTTP `429` with `Retry-After`, provider 429 count is `0` or below the accepted tolerance, and no concurrency leases remain after the test.

## Variations

- `api-gateway`: easiest for request limits, weaker for model-token accounting unless the gateway can inspect payloads.
- `service-middleware`: best for token-aware limits and fallback routing.
- `queue-based`: useful for batch or long jobs where waiting is better than rejecting.

## Safety & privacy

Medium risk because weak limits can cause spend spikes and overly strict limits can deny legitimate users. Do not include raw prompts in limiter keys or logs; hash identities where possible and keep abuse investigations access-controlled.
