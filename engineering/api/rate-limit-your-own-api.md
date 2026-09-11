---
name: rate-limit-your-own-api
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You protect an API endpoint with enforceable rate limits that return standard responses, work across instances, and can be verified under load.

## Preconditions

- The endpoint, user identity, and abuse scenario are known.
- A shared store such as Redis is available for multi-instance deployments, or the service is explicitly single-instance.
- You can run a local or staging load test.

## Steps

1. **Choose the limit dimension.** Limit by authenticated user, API key, tenant, IP address, or a combination. → *Expect:* the limiter key matches the abuse risk without punishing unrelated users.
2. **Select an algorithm.** Use token bucket or sliding window for production APIs; fixed window is acceptable for simple internal tools. → *Expect:* bursts and sustained rates are described numerically.
3. **Implement the limiter before expensive work.** Place middleware before database queries or downstream API calls. → *Expect:* rejected requests consume minimal CPU and no unnecessary downstream capacity.
4. **Use an atomic shared backend.** With Redis, use a library or Lua script that updates counters and expiry atomically. → *Expect:* concurrent requests cannot bypass the limit.
5. **Return standard headers.** Send HTTP `429` with `Retry-After` and, where appropriate, `RateLimit-Limit`, `RateLimit-Remaining`, and `RateLimit-Reset`. → *Expect:* clients can back off programmatically.
6. **Add allowlist and observability carefully.** Add metrics for allowed and blocked requests, plus narrowly scoped exemptions for health checks or trusted internal callers. → *Expect:* dashboards show limiter behavior without hiding real abuse.
7. **Load test the rule.** Run `hey -n 20 -c 5 http://localhost:3000/api/limited` or an equivalent. → *Expect:* requests above the configured budget return 429.

## Decision points

- Service runs on multiple instances → use Redis or another shared atomic store, not per-process memory.
- Endpoint handles login attempts → limit by account and IP, and avoid revealing whether an account exists.
- Paid tiers differ → include tenant or plan in the policy lookup.

## Failure modes & recovery

- **F1 Everyone blocked:** detect widespread 429s immediately after release → disable or loosen the rule through configuration and inspect key construction.
- **F2 Limit bypass:** detect too many successful concurrent requests → move from in-memory counters to atomic shared operations.
- **F3 Redis outage:** detect limiter backend errors → choose fail-open for availability or fail-closed for high-risk endpoints and alert either way.
- **F4 NAT unfairness:** detect many legitimate users behind one IP being blocked → prefer authenticated user or tenant keys where possible.

## Verification

Run an automated limiter test, for example `npm test -- rate-limit` or `pytest tests/test_rate_limit.py -q`, and a local burst command such as `hey -n 20 -c 5 "$URL"`; tests exit 0 and the burst produces HTTP 429 responses after the configured allowance.

## Variations

- `Express/Fastify`: use Redis-backed middleware such as `rate-limiter-flexible`.
- `Django/DRF`: use throttling classes with cache or Redis backing.
- `API gateway`: configure limits in Kong, Envoy, NGINX, Cloudflare, or AWS API Gateway and keep app-level tests for critical endpoints.

## Safety & privacy

Medium risk because bad limits can cause an outage or weaken abuse protection. Roll out in staging first, keep emergency configuration rollback available, avoid logging raw API keys, and review exemptions carefully.
