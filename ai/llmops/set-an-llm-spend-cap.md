---
name: set-an-llm-spend-cap
domain: ai
subdomain: llmops
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

You enforce a hard or near-hard budget for LLM usage so runaway traffic, retries, or prompt expansion cannot silently create an oversized bill.

## Preconditions

- Access to provider billing limits or project budgets.
- Application metrics that record model, input tokens, output tokens, request count, user or tenant, and route.
- Current per-model pricing or an internal price table updated by operations.
- A safe degraded mode such as cheaper routing, queuing, or rejecting noncritical requests.

## Steps

1. **Define the budget scope.** Choose caps per environment, project, tenant, user, or feature, and define the reset period. → *Expect:* a budget table with `scope`, `period`, `soft_cap`, `hard_cap`, and owner.
2. **Add token and cost accounting at the call site.** Record provider usage fields after every call and estimate cost before the call from token counts when possible. → *Expect:* each request emits cost metrics with model and route labels.
3. **Implement a preflight budget check.** Before sending a request, estimate maximum cost from input tokens and `max_tokens`; reject or downgrade if the remaining budget is insufficient. → *Expect:* over-budget requests are blocked before API spend occurs.
4. **Set provider-side caps where available.** Configure project or organization budgets in the provider console/API. ⚠️ *Irreversible:* a strict provider cap may break production traffic; confirm the degraded mode and on-call owner first. → *Expect:* provider settings show the intended monthly or daily limit.
5. **Add soft-cap alerts.** Alert at 50%, 80%, and 95% of budget with top routes, models, tenants, and recent deploys. → *Expect:* alert tests produce notifications with actionable cost attribution.
6. **Add hard-cap behavior.** At the hard cap, route only allowlisted critical tasks, use a cheaper model, or return a controlled `402/429` style application error. → *Expect:* a simulated exhausted budget triggers the configured fallback instead of calling the expensive model.
7. **Test retry containment.** Force provider 429/5xx responses and ensure retries use exponential backoff, jitter, and a maximum attempt count. → *Expect:* retry storms cannot exceed the request's cost budget.
8. **Review spend after deployment.** Compare billed provider usage to internal metrics daily until variance is understood. → *Expect:* provider invoice totals and internal cost estimates differ by less than the agreed tolerance.

## Decision points

- Internal metrics undercount provider billing → treat provider billing as source of truth and fix usage ingestion.
- Feature is noncritical and budget is exhausted → fail closed with a clear user message.
- Feature is critical and budget is exhausted → route to a cheaper model and alert an owner.
- Cost dominated by output tokens → reduce `max_tokens`, add stop conditions, or stream with early cancellation.

## Failure modes & recovery

- **F1 Missing usage fields:** detect null token counts in metrics → estimate with a tokenizer and patch provider parsing.
- **F2 Budget race condition:** detect concurrent requests exceeding cap → reserve estimated cost atomically before sending.
- **F3 Retry amplification:** detect many retries per original request → enforce retry budgets and circuit breakers.
- **F4 Price table drift:** detect invoice variance above tolerance → update model pricing and reprocess recent usage.
- **F5 Tenant abuse:** detect one scope consuming abnormal spend → throttle that scope and require manual review.

## Verification

Run an integration test with a temporary budget of `$1.00`, a mocked request estimated at `$1.20`, and a second request estimated at `$0.20`. The `$1.20` request must not call the provider, the `$0.20` request must record spend, and a simulated exhausted budget must return the configured fallback response.

## Variations

- `provider-budget`: useful as a backstop, but often too coarse for per-feature or per-tenant limits.
- `application-budget`: supports fine-grained routing decisions but must be reconciled with invoices.
- `gateway`: centralizes spend caps for many services and can enforce org-wide policy.

## Safety & privacy

Medium risk because cap mistakes can either overspend or interrupt production features. Avoid logging raw prompts in cost records, use atomic budget reservations, and require approval before raising hard caps or enabling high-cost models.
