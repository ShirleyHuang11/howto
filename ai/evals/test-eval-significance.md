---
name: test-eval-significance
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: [ai/evals/measure-task-accuracy]
status: draft
last_verified: 2026-09-22
---

## Goal

You determine whether an observed eval difference is likely meaningful rather than noise. The result includes effect size, uncertainty, and a decision tied to a practical threshold.

## Preconditions

- Per-example results for baseline and candidate on the same dataset.
- A chosen metric such as pass/fail, numeric score, or pairwise preference.
- A minimum practical improvement or non-inferiority margin.

## Steps

1. **Align examples.** Join baseline and candidate results by stable `id`. → *Expect:* paired rows with no missing ids.
2. **Choose the test.** Use McNemar's test for paired pass/fail, paired bootstrap for arbitrary metrics, or a binomial/sign test for pairwise wins. → *Expect:* the test matches the data shape.
3. **Compute effect size.** Report candidate minus baseline, not only a p-value. → *Expect:* a visible practical delta such as `+3.2 accuracy points`.
4. **Estimate uncertainty.** Run bootstrap confidence intervals or exact tests with `scipy` or `statsmodels`. → *Expect:* a 95% interval around the delta.
5. **Apply the decision rule.** Compare the interval to the predeclared improvement or non-inferiority margin. → *Expect:* the result is ship, no decision, or reject.

## Decision points

- Confidence interval crosses zero → treat as inconclusive unless non-inferiority was predeclared.
- Statistically significant but tiny effect → do not ship solely on p-value; consider cost and latency.
- Multiple slices tested → correct for multiple comparisons or label slice results exploratory.

## Failure modes & recovery

- **F1 Unpaired comparison:** detect different example ids → rerun on the same dataset or use an unpaired test explicitly.
- **F2 Peeking bias:** detect repeated looks until significant → predefine analysis time or use sequential testing.
- **F3 Underpowered eval:** detect very wide interval → add examples before deciding.
- **F4 Metric fishing:** detect changed primary metric after results → revert to preregistered metric.

## Verification

The analysis script outputs joined example count, effect size, 95% confidence interval, chosen test, p-value when applicable, and the predeclared decision. It fails if baseline and candidate ids do not match exactly.

## Variations

- `pass/fail`: McNemar's test is appropriate for paired binary outcomes.
- `numeric score`: paired bootstrap or permutation test is usually robust.
- `online A/B`: use experiment-level statistical methods and sample-ratio checks.

## Safety & privacy

This is low operational risk, but bad statistical decisions can ship worse systems. Preserve raw per-example results, avoid cherry-picking, and communicate uncertainty plainly.
