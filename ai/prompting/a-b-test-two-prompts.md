---
name: a-b-test-two-prompts
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You compare two prompt variants with controlled traffic or offline evals and choose a winner using predefined metrics instead of subjective impressions.

## Preconditions

- Two prompt versions that differ in one meaningful way.
- A primary metric, guardrail metrics, and a minimum sample size or offline test set.
- Logging that records prompt version, model, latency, cost, and outcome.

## Steps

1. **Define the hypothesis.** State what prompt B should improve and which metric decides success. → *Expect:* a test plan with one primary metric and guardrails.
2. **Freeze both prompt versions.** Record prompt ids, hashes, model settings, and rollout allocation. → *Expect:* assignment logs can distinguish A from B.
3. **Run an offline smoke test.** Evaluate both prompts on a labeled set before exposing users. → *Expect:* neither prompt fails parse, safety, or quality thresholds.
4. **Assign traffic randomly.** [BRANCH: offline batch | online A/B] Use stable randomization by user or session when online. ⚠️ *Data leaves your control:* if live user prompts go to an external model, confirm data-processing approval first. → *Expect:* comparable sample counts and no assignment skew.
5. **Monitor guardrails during the test.** Track refusal rate, latency, cost, parse failures, and safety flags. → *Expect:* automatic stop if a guardrail breaches.
6. **Analyze with the predeclared rule.** Compute confidence intervals or a nonparametric test, then choose ship, iterate, or revert. → *Expect:* a decision record with metric values and sample size.

## Decision points

- Offline B fails a guardrail → do not run online.
- Online guardrail breach → stop B and revert traffic to A.
- Primary metric lift is inconclusive → keep A and design a larger or clearer test.

## Failure modes & recovery

- **F1 Assignment bias:** detect unequal user segments → randomize by stable id and check covariates.
- **F2 Metric gaming:** detect B improves score but worsens complaints or safety → enforce guardrail metrics.
- **F3 Underpowered test:** detect wide confidence interval → collect more samples or use offline paired eval.
- **F4 Version contamination:** detect logs missing prompt ids → fix logging before using results.

## Verification

Run `python analyze_prompt_ab.py --events ab_events.jsonl --primary success --min-n-per-arm 200 --guardrails guardrails.yaml`; the script exits 0 only if sample sizes are met, guardrails pass, and the decision rule identifies a winner or declares no ship.

## Variations

- `offline paired eval`: run both prompts on identical examples and compare per-case outcomes.
- `online experiment`: use stable assignment and user-impact guardrails.
- `human review`: blind reviewers to prompt variant and randomize output order.

## Safety & privacy

Medium risk when live users are exposed. Avoid testing unsafe variants on users, cap rollout, monitor cost and failures, and confirm privacy approval before sending production data to external APIs.
