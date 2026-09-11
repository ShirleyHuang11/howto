---
name: set-up-rate-limiting-to-stop-abuse
domain: engineering
subdomain: security
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

You add rate limiting to abusive or expensive endpoints so legitimate users continue working while excessive traffic is throttled with clear, testable responses.

## Preconditions

- The endpoint, identity key, and abuse pattern are known.
- Access to app middleware, API gateway, CDN, or load balancer configuration.
- Metrics for normal request rates by user, IP, token, or tenant.

## Steps

1. **Choose the limiting key and scope.** Use authenticated user ID, API key, tenant ID, or IP fallback; avoid IP-only limits for logged-in users behind NAT. → *Expect:* each request maps to a stable rate-limit bucket.
2. **Set an initial threshold from traffic data.** Query request counts over a normal week and pick a threshold above legitimate p95/p99 usage. → *Expect:* the limit targets abuse, not normal traffic.
3. **Implement the limiter at the right layer.** [BRANCH: app, use middleware with Redis/token bucket | API gateway/CDN, configure route-level limits | Nginx, use `limit_req_zone`] → *Expect:* excessive requests receive 429 responses.
4. **Return useful rate-limit responses.** Include HTTP 429 and, where supported, `Retry-After` plus rate-limit headers. → *Expect:* clients can back off programmatically.
5. **Add tests for allowed and blocked traffic.** Simulate requests up to and beyond the threshold using the same identity key. → *Expect:* requests under the limit succeed and over-limit requests return 429.
6. **Deploy in observe or soft-limit mode first if available.** Monitor would-block metrics before enforcing. → *Expect:* expected abusive traffic is identified without surprising legitimate users.
7. **Enable enforcement and monitor.** Track 429 rate, latency, login success, signup conversion, and support tickets. → *Expect:* abuse drops and legitimate success metrics remain stable.

## Decision points

- Endpoint is login/password reset → combine rate limits with account lockout protections and CAPTCHA/risk checks where appropriate.
- Limit state must span many instances → use shared storage such as Redis, gateway state, or CDN edge limiting.
- High-value API customers need bursts → use token bucket burst capacity and per-plan quotas.
- Abuse changes identity keys → layer limits by user, token, IP, and route.

## Failure modes & recovery

- **F1 Legitimate users throttled:** detect 429 spikes for known customers → raise thresholds or add scoped allowlists with expiry.
- **F2 Limit bypassed:** detect abuse across many IPs or tokens → add tenant/user/device-level limits and fraud controls.
- **F3 Redis dependency failure:** detect limiter errors causing 500s → choose fail-open or fail-closed per endpoint risk and alert on store outage.
- **F4 Missing client backoff:** detect retry storms after 429 → add `Retry-After` and communicate API client guidance.

## Verification

An automated test or script sends `N` requests under the threshold and receives 2xx, then sends one more request and receives HTTP 429 with the expected rate-limit headers.

## Variations

- `Express`: use `express-rate-limit` with Redis store for multi-instance deployments.
- `Django/Rails`: use framework middleware or a maintained throttling package backed by cache/Redis.
- `Cloudflare/AWS API Gateway`: configure route rules at the edge for cheap pre-app enforcement.

## Safety & privacy

Medium risk because bad limits can deny service to legitimate users. Avoid logging full request bodies, protect user identifiers in metrics, and review allowlists so they do not become permanent bypasses.
