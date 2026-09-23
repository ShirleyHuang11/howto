---
name: balance-a-training-dataset
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You adjust dataset composition so important tasks, labels, languages, and safety cases are represented intentionally. The final dataset includes distribution metrics and a rationale for sampling weights or row counts.

## Preconditions

- A cleaned dataset with category, label, language, source, and difficulty metadata.
- Target distribution based on product traffic, policy priorities, or evaluation needs.
- A way to resample, weight, or collect more data.

## Steps

1. **Define balancing dimensions.** Choose the dimensions that matter, such as label, task type, locale, refusal category, difficulty, and source. → *Expect:* every row has values for required dimensions.
2. **Measure current distribution.** Generate counts and percentages by dimension and intersections. → *Expect:* a report identifies overrepresented and underrepresented groups.
3. **Set target ranges.** Decide whether to match production traffic or intentionally upweight rare but important cases. → *Expect:* each dimension has a target or documented exemption.
4. **Downsample dominant groups.** Remove or lower weights for repetitive categories, sources, or templates. → *Expect:* no single group exceeds its target cap unless justified.
5. **Upsample carefully.** Duplicate only when trainers support weighting poorly; prefer collecting or authoring more examples. → *Expect:* oversampled rows are flagged to avoid split leakage.
6. **Recompute token and source balance.** Large examples can dominate training even if row counts look balanced. → *Expect:* token-weighted distribution is reported.
7. **Validate eval alignment.** Ensure validation and test sets reflect the release gate, not only the balanced training mix. → *Expect:* train and validation distributions are documented separately.

## Decision points

- Rare safety category is product-critical → upweight or collect more examples despite low traffic share.
- A category has low quality examples → improve or drop them rather than balancing with bad data.
- Balancing harms real traffic performance → use routing or task-specific adapters instead of one dataset.
- Upsampling creates duplicates across splits → split before or track cluster IDs correctly.

## Failure modes & recovery

- **F1 Majority-source dominance:** detect one source providing most tokens → cap or downweight that source.
- **F2 Synthetic overrepresentation:** detect synthetic rows dominating style → mix with human-reviewed real examples.
- **F3 Rare label missing from validation:** detect no examples for a required label → reserve examples before training.
- **F4 Duplicate upsampling leakage:** detect same row in multiple splits → keep duplicates inside train only and split by original ID.
- **F5 Token imbalance:** detect long categories dominating updates → balance by token count or loss weighting.

## Verification

The balancing script passes when required metadata is present, row-count and token-count distributions fall within target ranges, no duplicate or source cluster crosses splits, and the final manifest records sampling weights, removed rows, and rationale.

## Variations

- `classification`: use class weights, resampling, or thresholding based on validation metrics.
- `instruction tuning`: balance task families and safety boundaries, not only labels.
- `multilingual data`: balance by both language and task type to avoid strong languages dominating all tasks.

## Safety & privacy

Balancing can amplify harmful patterns if the source data is bad. Review upweighted groups carefully, avoid duplicating sensitive rows, and document when the training mix intentionally differs from real traffic.
