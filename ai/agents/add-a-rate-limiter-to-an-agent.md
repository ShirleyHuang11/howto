---
name: add-a-rate-limiter-to-an-agent
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent respects model, tool, API, and budget limits under normal and concurrent load. Success means rate-limited operations queue, back off, or fail with typed errors instead of causing provider throttling or runaway spend.

## Preconditions

- Known limits for model requests, tokens per minute, tool calls, external APIs, and cost budgets.
- A centralized agent controller or middleware through which model and tool calls pass.
- Metrics for request count, token count, latency, queue depth, and cost.

## Steps

1. **Inventory limit dimensions.** Record per-provider RPM, TPM, concurrency, daily quota, external API limits, and per-user cost budgets. → *Expect:* a config file contains numeric limits for each resource.
2. **Add a centralized limiter.** Use token bucket, leaky bucket, or semaphore controls before model and tool calls. → *Expect:* concurrent calls acquire permits before execution.
3. **Reserve estimated tokens and cost before calls.** Estimate prompt plus output tokens and reject or queue requests that would exceed budget. → *Expect:* no call starts when the remaining budget is insufficient.
4. **Handle provider rate-limit responses.** On `429`, respect `Retry-After`, reduce concurrency, and return a typed retryable error if the queue deadline expires. → *Expect:* test `429` responses cause backoff rather than immediate retry storms.
5. **Set per-user and per-run caps.** Prevent one user or runaway agent from consuming the shared quota. → *Expect:* a single run stops with `budget_exceeded` while other users can continue.
6. **Expose metrics and alerts.** Track allowed, queued, rejected, retried, and budget-stopped calls. → *Expect:* dashboards or logs show limiter decisions by resource and user.

## Decision points

- Latency-sensitive request and permits unavailable → fail fast with a retryable error.
- Background task and permits unavailable → queue until deadline.
- Provider returns repeated `429` → lower concurrency and increase backoff.
- User budget exceeded → stop the agent and ask for approval before continuing paid work.

## Failure modes & recovery

- **F1 Retry storm:** detect many immediate retries after `429` → centralize retries and honor backoff.
- **F2 Token budget underestimate:** detect actual tokens above reservation → increase safety margin and reconcile after usage reports.
- **F3 Starvation:** detect one queue class never runs → add fairness by user, tenant, or priority.
- **F4 Distributed oversubscription:** detect multiple workers exceeding shared limit → use a shared limiter store such as Redis.

## Verification

Run a load test with concurrent agent runs. Requests must never exceed configured RPM, TPM, concurrency, or per-user cost limits; simulated `429` responses must back off according to policy; excess requests must queue or fail with typed limiter errors; and metrics must report allowed, queued, rejected, and budget-stopped counts.

## Variations

- `single process`: in-memory buckets are acceptable for local tools and tests.
- `distributed workers`: use Redis or a managed rate-limit service for shared counters.
- `multi-provider`: route to fallback providers only if policy, data residency, and eval quality allow it.

## Safety & privacy

Medium risk from cost overruns and denial of service. Reserve budget before work starts, isolate users and tenants, avoid logging raw prompts in limiter metrics, and require approval before exceeding configured spend caps.
