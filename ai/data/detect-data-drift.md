---
name: detect-data-drift
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You detect when production or new-batch data diverges from training data and trigger review before model quality silently degrades.

## Preconditions

- A reference dataset such as training data or a recent trusted production window.
- New data batches or production feature logs with the same schema.
- Drift tests appropriate to numeric, categorical, text, embedding, and label features.
- Alerting or reporting infrastructure.

## Steps

1. **Define the reference window.** Choose the baseline data, feature schema, and time period that represent expected input distribution. → *Expect:* a versioned reference profile with row counts and feature summaries.
2. **Collect comparable current data.** Use the same feature generation code and exclude fields unavailable at inference. → *Expect:* current data matches the reference schema or fails fast.
3. **Compute feature-level drift metrics.** Use PSI, KS test, Wasserstein distance, chi-square, categorical frequency deltas, embedding distance, or text length/token distributions as appropriate. → *Expect:* each monitored feature has a drift score and threshold.
4. **Monitor label and outcome drift when labels arrive.** Compare delayed labels, conversion rates, or human review outcomes to the reference. → *Expect:* target drift is tracked separately from input drift.
5. **Segment by important groups.** Compute drift by tenant, geography, language, device, source, or subgroup where relevant. → *Expect:* localized drift is visible even if global drift is small.
6. **Set alert thresholds and severity.** Combine statistical thresholds with minimum sample sizes and business impact. → *Expect:* alerts avoid tiny-sample noise but catch meaningful shifts.
7. **Create a drift report.** Include top drifting features, plots or tables, sample counts, model performance if labels exist, and recommended action. → *Expect:* reviewers can see what changed and where.
8. **Automate the check.** Run drift detection on a schedule or per batch and block retraining/deployment when drift exceeds severe thresholds. → *Expect:* a failed drift gate creates an alert or pipeline failure.

## Decision points

- Drift is high but labels are stable → monitor closely and consider feature normalization updates.
- Drift is high and performance drops → retrain, recalibrate, or roll back depending on severity.
- Drift is localized to one segment → route or retrain for that segment rather than global changes.
- Schema drift occurs → stop downstream scoring until the feature pipeline is fixed.

## Failure modes & recovery

- **F1 False alarm from small samples:** detect high drift with low counts → enforce minimum sample sizes or widen the window.
- **F2 Missed conditional drift:** detect stable global metrics but subgroup complaints → add segment-level drift checks.
- **F3 Feature pipeline bug:** detect many features drifting simultaneously or impossible values → inspect upstream data generation first.
- **F4 Delayed label blindness:** detect input drift without outcome monitoring → add delayed label joins and proxy metrics.
- **F5 Reference staleness:** detect repeated benign drift alerts → update the reference only after quality review.

## Verification

Run the drift job on a controlled dataset where one numeric feature, one categorical feature, and one schema field are intentionally shifted. The check passes only when the shifted features exceed thresholds, unchanged features remain below thresholds, schema mismatch is reported, and the job emits an alert or failed gate with the expected feature names.

## Variations

- `tabular`: PSI, KS, chi-square, and missingness changes are common.
- `text`: monitor language, length, topic embeddings, toxicity, and token distribution.
- `embeddings`: compare centroid distance, nearest-neighbor overlap, and cluster proportions.

## Safety & privacy

Medium risk because drift monitoring often uses production data. Aggregate metrics where possible, avoid storing raw sensitive examples in reports, control access to segment-level findings, and review retraining decisions before replacing production models.
