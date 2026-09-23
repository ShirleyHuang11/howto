---
name: set-up-a-model-router
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: medium
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You route LLM requests to the cheapest or fastest model that meets quality and safety requirements. Routing decisions are observable, testable, and reversible.

## Preconditions

- Multiple candidate models or endpoints approved for the data involved.
- An eval set labeled by task type, difficulty, and required capabilities.
- Centralized request metadata such as task name, tenant, latency budget, and data sensitivity.

## Steps

1. **Define routing inputs and policies.** List allowed features such as task type, prompt length, user tier, sensitivity, latency budget, and required tools. → *Expect:* a policy schema that excludes raw sensitive prompt text where possible.
2. **Benchmark candidate models.** Run each model on the same eval set and capture quality, schema validity, latency, and cost. → *Expect:* a model scorecard per task segment.
3. **Create initial routing rules.** [BRANCH: rules | classifier | bandit] Start with transparent rules such as `strict_json -> reliable_model`, `long_context -> long_context_model`, and `low_risk_summary -> cheap_model`. → *Expect:* every route has an explicit reason.
4. **Add fallback and escalation.** Route failed validation, low confidence, or sensitive tasks to a stronger model or human review. ⚠️ *Data leaves your control:* cross-provider routes may send the same prompt to multiple vendors; approve this before enabling. → *Expect:* fallback paths are listed and logged.
5. **Implement budget and rate-limit guards.** Enforce per-tenant cost ceilings, provider rate limits, and model availability checks. → *Expect:* router rejects or queues requests instead of exceeding limits.
6. **Shadow-test before serving users.** Compare router choices to a default strong model on recent traffic or synthetic prompts without changing user-visible output. → *Expect:* router savings and quality deltas are measured.
7. **Roll out with monitoring.** Enable for a small traffic percentage and track route distribution, quality proxies, validation failures, latency, and cost. → *Expect:* a dashboard shows each route and rollback switch.

## Decision points

- Cheap route fails validation often → escalate that segment to a stronger model.
- Prompt contains restricted data → route only to approved endpoints.
- Latency budget is tight → prefer faster models or streaming if quality holds.
- Cost budget is exceeded → tighten cheap-model eligibility or add caching.
- Model outage occurs → fail over only to models approved for the same data class.

## Failure modes & recovery

- **F1 Silent quality regression:** detect task score drop in routed traffic → roll back route and rerun eval.
- **F2 Policy bypass:** detect restricted tenant routed to unapproved provider → disable route and audit.
- **F3 Router oscillation:** detect repeated model retries → add max fallback depth and terminal failure.
- **F4 Cost spike:** detect expensive model route dominates traffic → inspect rules and add budget guard.
- **F5 Biased difficulty classifier:** detect hard cases sent to weak model → retrain classifier or use conservative rules.

## Verification

The router is ready when automated tests cover every policy branch, replay eval traffic through the router, and show selected routes meet per-segment quality thresholds while reducing expected cost or latency against the baseline. Restricted-data tests must prove unapproved providers are never selected.

## Variations

- `rules`: easiest to audit and best first step for production.
- `classifier`: useful when request metadata predicts difficulty; requires drift monitoring.
- `bandit`: use only with strong guardrails and online quality signals.
- `gateway`: implement routing in an LLM gateway so app teams share policy.

## Safety & privacy

Medium risk because routing can expose data to unintended providers and hide quality regressions. Maintain provider allowlists by data class, log route reasons, cap fallback depth, and require human review before adding new providers or online-learning policies.
