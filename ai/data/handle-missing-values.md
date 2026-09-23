---
name: handle-missing-values
domain: ai
subdomain: data
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

You treat missing values in a dataset with explicit, testable rules so model training is stable and missingness does not create hidden leakage or bias.

## Preconditions

- A dataset with a known schema and label column if supervised learning is used.
- Column-level meaning for null, blank, zero, unknown, not applicable, and not collected.
- A train/validation/test split plan or grouped split key.
- A modeling pipeline that can include imputers and missingness indicators.

## Steps

1. **Profile missingness by column and split candidate.** Compute null, blank, sentinel, and invalid-code rates, plus missingness by label and key groups. → *Expect:* a table of missing rates and correlations with the label.
2. **Define missing-value semantics.** Distinguish true unknown, not applicable, measurement failure, redacted, and structurally absent values. → *Expect:* each nullable column has a documented missingness meaning.
3. **Choose per-column handling.** [BRANCH: drop | impute | indicator | model-native missing] Use median/most-frequent imputation for simple baselines, domain values for known semantics, or model-native missing handling when supported. → *Expect:* a handling plan for every column with missing values.
4. **Fit imputers only on training data.** Split first, then fit imputation statistics on train and apply them to validation/test. → *Expect:* validation and test data do not influence imputation values.
5. **Add missingness indicators where informative.** Create boolean flags for columns whose missingness carries signal or risk. → *Expect:* feature matrix includes named indicators such as `income__is_missing`.
6. **Reject columns or rows when justified.** Drop columns with excessive missingness or rows missing required labels, and record thresholds. → *Expect:* dropped data counts are documented and reproducible.
7. **Validate post-imputation data.** Assert no unsupported nulls remain, imputed values are in valid ranges, and categorical unknowns are allowed categories. → *Expect:* the model pipeline receives valid numeric/categorical inputs.
8. **Evaluate impact.** Compare baseline performance, calibration, and subgroup metrics with and without the missingness strategy. → *Expect:* chosen handling improves or preserves target metrics without unacceptable subgroup harm.

## Decision points

- Missingness strongly predicts the label → add indicators and review for leakage.
- Test missingness differs from train → investigate data drift before trusting metrics.
- A column is mostly missing and not essential → drop it and document the loss.
- Missing label values exist → exclude from supervised training unless a labeling process can recover them.

## Failure modes & recovery

- **F1 Leakage through imputation:** detect validation statistics used in fit → refit imputers inside the train-only pipeline.
- **F2 Sentinel treated as real value:** detect values like `-999` or `"unknown"` in numeric summaries → normalize sentinels to missing before imputation.
- **F3 Biased row dropping:** detect dropped rows concentrated in a subgroup → use imputation or collect data rather than deleting.
- **F4 Invalid categorical unknown:** detect serving-time category errors → include an explicit unknown category in the encoder.
- **F5 Train-serve mismatch:** detect production nulls not seen in training → keep imputation and validation in the serving pipeline.

## Verification

Run the preprocessing pipeline on train, validation, and test splits and assert that imputation statistics are fit only on train, unsupported null count is `0`, valid ranges still hold, dropped-row counts match the manifest, and model metrics plus subgroup metrics meet the configured thresholds.

## Variations

- `tree-models`: some implementations handle missing values natively; still validate missingness and serving behavior.
- `linear-models`: usually require explicit imputation and often benefit from missingness indicators.
- `deep-learning`: use learned embeddings or mask tensors for structured missingness where appropriate.

## Safety & privacy

Medium risk because missingness can encode access, socioeconomic status, device behavior, or redaction. Do not erase these patterns blindly; measure subgroup impact, avoid leakage from future data, and document every missing-value assumption.
