---
name: rate-limit-to-prevent-abuse
domain: ai
subdomain: safety
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

Add rate limits that prevent abusive or runaway LLM usage while preserving normal user workflows and enforcing predictable cost ceilings.

## Preconditions

- User, organization, API key, or IP identity available at request time.
- A shared counter store such as Redis, a gateway rate limiter, or provider-side quota controls.
- Usage metrics for requests, tokens, tool calls, and cost.

## Steps

1. **Choose limit dimensions.** Limit by user/org/API key/IP and by requests, input tokens, output tokens, tool calls, and spend. → *Expect:* a quota table with windows and burst allowances.
2. **Implement atomic counters.** Use Redis `INCR`/Lua, gateway policies, or a token bucket library so concurrent requests cannot bypass limits. → *Expect:* simultaneous requests update one consistent counter.
3. **Apply limits before expensive work.** Estimate tokens and cost before model calls, then reserve quota. → *Expect:* requests over quota receive a structured `429` without calling the model.
4. **Reconcile actual usage.** After completion, update counters with actual tokens and cost. → *Expect:* usage records match provider billing within an allowed tolerance.
5. **Add abuse-specific throttles.** Lower limits for unauthenticated users, repeated policy violations, or suspicious automation. → *Expect:* abusive traffic is throttled faster than normal traffic.
6. **Load-test the limiter.** Simulate bursts, parallel requests, and reset windows. → *Expect:* allowed/blocked counts match the configured limits.

## Decision points

- Users hit limits during legitimate batch work → add approved higher quotas or async batch workflows.
- Provider bills exceed internal counters → reconcile token accounting and reserve larger safety margins.
- Attackers rotate IPs → rate-limit authenticated identities and add behavior-based abuse signals.

## Failure modes & recovery

- **F1 Race-condition bypass:** detect more successful requests than quota under concurrency → move to atomic server-side counters.
- **F2 Cost runaway:** detect actual spend above budget → add pre-call token/cost reservation and hard org caps.
- **F3 Bad reset logic:** detect limits not resetting or resetting early → test fixed and rolling windows around boundaries.
- **F4 Shared IP unfairness:** detect many users blocked behind NAT → prefer account-level limits for authenticated traffic.

## Verification

Concurrency tests prove no identity can exceed configured request or token quotas, over-limit requests return `429` before model invocation, and daily cost counters stay within 5% of provider billing on a sampled reconciliation report.

## Variations

- `Redis token bucket`: flexible and fast for app-level limits.
- `API gateway`: centralizes enforcement across services.
- `provider quota`: useful backstop but still add application-level user/org limits.

## Safety & privacy

Rate limiting protects cost and platform safety but can become a denial-of-service vector if identity is weak. Store minimal identifiers, hash IPs where possible, disclose fair-use limits, and provide review paths for legitimate high-volume users.
