---
name: run-a-pairwise-comparison
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/evals/build-an-eval-set]
status: draft
last_verified: 2026-09-22
---

## Goal

You compare two model, prompt, or system versions on the same examples and estimate which one users would prefer. The comparison is randomized, blinded, and statistically summarized.

## Preconditions

- A fixed eval dataset and two runnable variants, `A` and `B`.
- A pairwise rubric or human review form.
- Storage for both outputs and judge decisions.

## Steps

1. **Generate both outputs.** Run each variant on every example with fixed decoding settings. ⚠️ *Data leaves your control:* confirm the dataset is approved for both providers. → *Expect:* paired outputs exist for every example id.
2. **Blind and randomize order.** Create comparison rows with `left` and `right` randomly assigned and without model names. → *Expect:* reviewers or judges cannot infer which side is the candidate.
3. **Judge each pair.** Use humans or an LLM judge to return `left`, `right`, or `tie` with a rubric-grounded reason. → *Expect:* one validated decision per pair.
4. **Unblind decisions.** Map left/right back to A/B and count wins, losses, and ties. → *Expect:* a win-rate table for A versus B.
5. **Estimate uncertainty.** Bootstrap examples or run a binomial test ignoring ties. → *Expect:* a confidence interval and p-value or posterior probability.
6. **Inspect disagreements.** Review pairs where the new variant loses badly or the judge reason mentions safety, factuality, or tool misuse. → *Expect:* a failure list, not just a headline win rate.

## Decision points

- New version wins overall but loses safety slice → do not ship until the slice is fixed.
- Many ties → use cost, latency, and reliability as deciding metrics.
- Judge preference conflicts with human labels → trust calibrated human review and recalibrate the judge.

## Failure modes & recovery

- **F1 Order bias:** detect left side wins too often across unrelated runs → randomize position and test with swapped pairs.
- **F2 Style bias:** detect verbose answers always win → add task-success and concision criteria.
- **F3 Missing paired outputs:** detect ids present for only one variant → rerun missing calls before analysis.
- **F4 Non-independent examples:** detect many near-duplicates → cluster and bootstrap by cluster.

## Verification

`compare.py` produces a CSV with one decision per example, zero unparsed judge outputs, a win-rate summary, and a bootstrap 95% confidence interval. A candidate ships only if its lower confidence bound exceeds the configured margin or the team accepts a documented tradeoff.

## Variations

- `human review`: use two reviewers per pair and adjudicate disagreements.
- `llm judge`: validate JSON decisions and calibrate against a human-labeled subset.
- `multi-model`: run a tournament or Bradley-Terry model instead of only A/B.

## Safety & privacy

Pairwise outputs may contain user data twice, once from each variant. Redact inputs, hide model/provider names from reviewers, and review any safety regressions before acting on aggregate preference.
