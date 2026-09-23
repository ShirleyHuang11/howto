---
name: detect-outliers
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [ai/data/compute-summary-statistics]
status: draft
last_verified: 2026-09-22
---

## Goal

You identify unusual records or values, distinguish data errors from valid rare cases, and decide how they should affect training or evaluation.

## Preconditions

- A dataset with typed numeric, categorical, timestamp, or embedding features.
- Baseline summary statistics, such as `ai/data/compute-summary-statistics`.
- A review path for records that may be valid but unusual.

## Steps

1. **Define what counts as an outlier.** Choose column-level bounds, robust z-score, IQR, isolation forest, or nearest-neighbor distance depending on feature type. → *Expect:* a documented rule for each checked feature group.
2. **Compute univariate flags.** For numeric columns, calculate percentiles, IQR fences, and impossible domain bounds. → *Expect:* each numeric column has an outlier count and examples.
3. **Compute multivariate flags if needed.** Use `IsolationForest`, robust covariance, or embedding-neighbor distance on scaled features. → *Expect:* records receive an anomaly score.
4. **Segment the analysis.** Compare outlier rates by source, date, label, or customer segment. → *Expect:* spikes point to possible pipeline or source issues.
5. **Review sampled outliers.** Inspect examples and label each as error, valid rare case, fraud/abuse candidate, or unknown. → *Expect:* treatment rules are based on observed cases, not automatic deletion.
6. **Apply a reversible treatment.** [BRANCH: cap | remove | keep with flag | quarantine] Store flags and transformations separately from raw data. → *Expect:* the original values remain recoverable.
7. **Measure model impact.** Train or evaluate with and without the proposed treatment. → *Expect:* metrics show whether the treatment helps without hiding important rare cases.

## Decision points

- Outliers are data-entry or sensor errors → quarantine or correct with provenance.
- Outliers are valid rare target cases → keep them and consider sample weighting or segment metrics.
- Outlier rate jumps by source or date → investigate upstream data drift before modeling.
- Treatment changes evaluation results materially → document the decision and rerun held-out tests.

## Failure modes & recovery

- **F1 Deleting important rare cases:** detect performance drop on rare segments → restore flagged records and use robust models or segment-aware metrics.
- **F2 Scale-sensitive detector:** detect one high-variance feature dominating scores → standardize or use robust scaling before multivariate detection.
- **F3 Threshold overfit:** detect threshold tuned to make validation look better → set thresholds from training data or domain rules before final evaluation.
- **F4 Hidden pipeline error:** detect a sudden cluster of outliers from one batch → stop downstream jobs and inspect extraction or parsing changes.

## Verification

The outlier report passes only if it includes per-feature flag counts, anomaly-score thresholds, sampled review labels, treatment rules, and a before/after metric comparison. Automated checks must confirm that raw values are preserved and treated rows are traceable by id.

## Variations

- `tabular numeric`: use robust z-scores, IQR, and domain bounds.
- `high-dimensional embeddings`: use nearest-neighbor distance or density-based methods.
- `time series`: use rolling baselines and seasonal decomposition before flagging anomalies.

## Safety & privacy

Medium risk because outliers can represent vulnerable people, fraud, medical events, or abuse. Do not automatically delete unusual records from safety-critical tasks, and avoid exposing raw outlier examples outside approved systems.
