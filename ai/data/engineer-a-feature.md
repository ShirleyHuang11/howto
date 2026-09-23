---
name: engineer-a-feature
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

You add a model feature that is available at prediction time, improves measured performance or reliability, and is reproducible in both training and serving.

## Preconditions

- A defined prediction task, label, and prediction timestamp.
- Access to raw inputs and any join tables needed to compute the feature.
- A baseline model and evaluation set.
- A feature store, pipeline code, or preprocessing module where the feature can be implemented.

## Steps

1. **State the feature hypothesis.** Describe why the feature should help and which metric or slice it should improve. → *Expect:* a testable hypothesis tied to an eval metric.
2. **Check prediction-time availability.** Confirm all source fields exist before or at the prediction timestamp and will be available in production. → *Expect:* no future or post-outcome data is required.
3. **Define the transformation.** Specify joins, windows, aggregations, encodings, default values, and data types. → *Expect:* a deterministic feature definition with input and output schema.
4. **Implement in the shared pipeline.** Add the feature where training and serving can both use the same code or feature-store definition. → *Expect:* train and online computation produce the same value for the same entity and time.
5. **Validate feature quality.** Check missingness, range, cardinality, distribution, leakage risk, and correlation with protected or sensitive attributes if relevant. → *Expect:* a feature profile and validation report.
6. **Train and compare against baseline.** Run an ablation with and without the new feature using the same data split and seed. → *Expect:* metric deltas are attributable to the feature.
7. **Test serving behavior.** Run sample online requests or batch scoring with the feature enabled. → *Expect:* no missing source fields, latency regression, or schema mismatch occurs.
8. **Document and monitor the feature.** Record owner, definition, dependencies, allowed ranges, freshness, and drift checks. → *Expect:* future changes can be audited and monitored.

## Decision points

- Feature uses future information → reject or redesign with a valid historical window.
- Feature improves average metric but hurts a key subgroup → revise or do not ship.
- Feature is expensive online → precompute it or reserve for batch scoring.
- Feature is highly correlated with sensitive attributes → review fairness and legal constraints.

## Failure modes & recovery

- **F1 Label leakage:** detect unusually large metric jump or post-outcome source fields → remove feature and rerun ablation.
- **F2 Train-serve skew:** detect different offline and online values for same key/time → share code or fix feature-store definitions.
- **F3 Missing production dependency:** detect null feature online despite training coverage → add defaults, freshness checks, or pipeline dependency alerts.
- **F4 High cardinality blowup:** detect memory or latency increase from encoding → hash, bucket, or drop rare values.
- **F5 Unstable distribution:** detect feature drift after release → add monitoring and retrain or disable if performance drops.

## Verification

Run an ablation pipeline that computes the feature for train and serving samples, asserts no future-timestamp sources are used, validates schema and ranges, confirms offline-online parity for sampled entities, and shows the target metric improves by the configured threshold without subgroup or latency regressions.

## Variations

- `tabular-aggregate`: windowed counts, rates, recency, and rolling statistics need timestamp discipline.
- `text-feature`: embeddings, language, length, or classifier scores require versioned models.
- `real-time`: use a feature store with freshness checks and fallback defaults.

## Safety & privacy

Medium risk because features can leak labels, encode sensitive attributes, or create train-serve skew. Verify timestamp availability, monitor subgroup impact, minimize sensitive joins, and document dependencies before shipping.
