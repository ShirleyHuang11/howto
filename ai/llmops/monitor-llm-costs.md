---
name: monitor-llm-costs
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

You track LLM spend by model, tenant, feature, and request so cost spikes are caught before they become incidents. Alerts and budgets are enforced programmatically.

## Preconditions

- LLM calls flow through a shared wrapper, gateway, or proxy.
- Access to provider usage metadata or local token counters.
- A budget owner and limits for daily, monthly, tenant, and feature spend.

## Steps

1. **Define cost dimensions.** Tag every request with model, provider, feature, tenant, environment, route, and request id. → *Expect:* cost records can be grouped by each dimension.
2. **Capture token usage and unit prices.** Store input tokens, output tokens, cached tokens if billed differently, and price version. → *Expect:* each request has an estimated cost.
3. **Reconcile with provider billing.** Compare internal estimates to provider invoices or usage APIs daily. → *Expect:* estimate error is within an accepted tolerance.
4. **Set budgets and alerts.** Create thresholds such as 50%, 80%, 100%, and anomaly alerts for sudden cost/request changes. → *Expect:* test alerts reach owners.
5. **Enforce hard limits where needed.** Add per-tenant quotas, max tokens, concurrency limits, and expensive-model approvals. → *Expect:* requests over quota are blocked, queued, or downgraded predictably.
6. **Report unit economics.** Compute cost per successful task, cost per active user, and cost per feature. → *Expect:* dashboards show both total spend and normalized cost.
7. **Review spikes with traces.** Link cost outliers to prompt length, retries, fallback routes, or traffic changes. → *Expect:* every spike has an explainable cause or incident ticket.

## Decision points

- Spend exceeds forecast → reduce max tokens, route cheaper, cache, or throttle.
- One tenant dominates spend → enforce tenant quota or adjust pricing.
- Retry costs spike → fix upstream errors before raising budget.
- Output tokens dominate → constrain response length or summarize.
- Estimates diverge from invoice → update pricing constants and token accounting.

## Failure modes & recovery

- **F1 Missing usage metadata:** detect null token counts → estimate locally and fix wrapper instrumentation.
- **F2 Price table drift:** detect invoice mismatch → version prices and update from provider pricing.
- **F3 Unbounded retries:** detect cost per request spikes → add retry caps and circuit breakers.
- **F4 Tag cardinality explosion:** detect dashboard slowdown → restrict tags to stable ids.
- **F5 Alert fatigue:** detect repeated unactioned alerts → tune thresholds and assign owners.

## Verification

Cost monitoring is correct when a replay test emits synthetic usage records, the dashboard totals match computed expected cost, alerts fire at configured thresholds, and hard-limit tests prevent requests from exceeding tenant or daily budget.

## Variations

- `provider dashboard`: useful for invoice reconciliation but usually lacks application feature tags.
- `gateway`: centralizes token accounting and rate limits across services.
- `self-hosted`: track GPU-hours, utilization, queue time, and amortized hardware cost.
- `batch`: tag batch jobs separately because delayed billing can obscure spikes.

## Safety & privacy

Medium risk because cost logs can include user and tenant metadata. Avoid logging raw prompts by default, restrict billing dashboards, set spend caps before experiments, and require approval for new high-volume features or expensive models.
