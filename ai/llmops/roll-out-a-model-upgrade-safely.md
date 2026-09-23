---
name: roll-out-a-model-upgrade-safely
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You replace or add a newer LLM version without surprising users: offline evals pass, canary traffic is monitored, and rollback is a one-command operation.

## Preconditions

- A current production model route and a candidate model route behind configuration or a feature flag.
- A held-out eval set with expected outputs, judge rubrics, latency budgets, and cost budgets.
- Metrics for quality, refusal rate, tool-call validity, latency, error rate, and spend.
- A rollback path that can restore the previous model without redeploying code.

## Steps

1. **Freeze the current baseline.** Record model ID, prompt version, tool schemas, decoding parameters, context policy, and current eval scores. → *Expect:* a baseline artifact with exact production configuration and metrics.
2. **Run the candidate on the held-out eval set.** [BRANCH: Anthropic | OpenAI | open model] Execute the same prompts and tool schemas against the new model with temperature and max-token settings explicitly pinned. → *Expect:* a scored candidate report with quality, JSON validity, tool success, latency, and cost per task.
3. **Compare against release gates.** Require candidate quality to meet or exceed baseline within the agreed margin and require no critical safety regression. → *Expect:* a pass/fail table for every gate, not just an average score.
4. **Replay production traces after redaction.** Use recent representative requests with PII removed and compare output shape, refusal behavior, citations, and tool calls. ⚠️ *Data leaves your control:* redact or synthesize traces before sending them to any third-party candidate model. → *Expect:* trace replay produces no schema breakages or severe behavior changes.
5. **Create a canary route.** Add a feature flag such as `MODEL_ROUTE=candidate` for 1% of low-risk traffic or internal users. → *Expect:* requests are labeled with model route, prompt version, and experiment ID in metrics.
6. **Launch the canary.** ⚠️ *Irreversible:* user-visible responses may change; confirm rollback ownership and alert thresholds before enabling external traffic. → *Expect:* canary traffic reaches the candidate and dashboards separate candidate from baseline.
7. **Ramp gradually.** Move from 1% to 5%, 25%, 50%, and 100% only if quality, error, latency, and cost gates hold for each window. → *Expect:* each ramp step has a timestamped decision record and metric snapshot.
8. **Keep rollback live through stabilization.** Retain the previous model route until the candidate has passed the full stabilization window. → *Expect:* a tested rollback command restores baseline behavior in a staging smoke test.

## Decision points

- Offline eval below threshold → do not canary; fix prompts, tools, or choose another model.
- Candidate improves quality but doubles cost → require product approval or add routing only for high-value tasks.
- Canary error rate or schema failures exceed budget → rollback immediately and inspect traces.
- Safety refusal rate changes materially → review examples before expanding traffic.

## Failure modes & recovery

- **F1 Hidden prompt incompatibility:** detect via JSON parse failures or invalid tool calls → update prompts/tool schemas and rerun offline evals.
- **F2 Latency regression:** detect p95 above SLO during replay or canary → lower max tokens, use streaming, route long tasks differently, or reject the upgrade.
- **F3 Cost spike:** detect spend per successful task above budget → cap traffic, lower token limits, or restrict the candidate to selected intents.
- **F4 Safety regression:** detect judge failures, policy classifier alerts, or user reports → rollback and add those cases to the held-out eval set.
- **F5 Provider incident during rollout:** detect elevated 5xx/429 on candidate only → fail over to baseline and pause ramp.

## Verification

The upgrade is successful only when the candidate passes all offline release gates, canary metrics for the stabilization window stay within configured thresholds, and an automated rollback smoke test confirms the old model route can be restored with `MODEL_ROUTE=baseline` and returns HTTP 200 with valid output.

## Variations

- `Anthropic`: compare exact dated model aliases when available and watch tool-use formatting changes.
- `OpenAI`: pin model snapshots where supported and monitor structured-output validation separately.
- `open-model`: benchmark serving throughput and memory headroom in addition to generation quality.

## Safety & privacy

High risk because rollout changes user-facing behavior and can increase spend quickly. Redact production traces, ramp slowly, alert on cost and quality, and require human approval before sending regulated data to a new external provider or enabling 100% traffic.
