---
name: clean-a-dataset
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

You turn a raw dataset into a documented, reproducible cleaned dataset with validation checks that catch duplicates, invalid values, schema drift, and leakage before training or evaluation.

## Preconditions

- A raw dataset stored read-only or backed up.
- A schema or data contract with expected columns, types, ranges, nullable fields, and label definition.
- A processing environment such as pandas, Spark, DuckDB, or a data warehouse.
- A place to write cleaned data and a data-quality report.

## Steps

1. **Snapshot the raw input.** Record source path, row count, file hashes, extraction time, and dataset owner before modifying anything. → *Expect:* a manifest that can reproduce the raw input exactly.
2. **Load with explicit types.** Read data using declared column names, types, encodings, and timestamp parsing rules. → *Expect:* the loader fails on unexpected columns or type coercions.
3. **Profile quality issues.** Compute missingness, duplicates, invalid categories, range violations, outliers, label distribution, and train-test leakage candidates. → *Expect:* a profiling report listing counts and percentages per column.
4. **Apply deterministic cleaning rules.** Normalize text, trim whitespace, parse dates, standardize categories, remove exact duplicates, and flag impossible values according to the schema. → *Expect:* every changed field can be traced to a named rule.
5. **Handle missing values intentionally.** Drop, impute, or add missing indicators based on feature semantics, not convenience. → *Expect:* missingness after cleaning matches the schema policy.
6. **Separate rejected rows.** Write invalid or ambiguous rows to a quarantine file with rejection reasons instead of silently deleting them. → *Expect:* rejected row count plus reason distribution are available.
7. **Run validation tests.** Use Great Expectations, pandera, dbt tests, or custom assertions for schema, ranges, uniqueness, and label constraints. → *Expect:* the cleaned dataset passes all required expectations.
8. **Version the cleaned output.** Write cleaned data, manifest, cleaning code version, and report to a stable location. → *Expect:* downstream training can reference an immutable cleaned dataset version.

## Decision points

- Invalid rows are rare and clearly unusable → quarantine and continue.
- Invalid rows are common → stop and fix upstream collection or labeling.
- Cleaning changes label distribution materially → review for bias or leakage before training.
- Field meaning is ambiguous → ask the data owner instead of guessing.

## Failure modes & recovery

- **F1 Silent type coercion:** detect unexpected nulls or object types after load → enforce schema and fail on parse errors.
- **F2 Duplicate leakage:** detect same entity in multiple splits → deduplicate before splitting or split by entity/group.
- **F3 Label corruption:** detect impossible labels or changed label counts → restore raw labels and audit cleaning rules.
- **F4 Overzealous outlier removal:** detect performance drop or biased coverage → flag outliers instead of deleting until reviewed.
- **F5 Non-reproducible cleaning:** detect missing manifest or code version → rerun from raw snapshot with recorded parameters.

## Verification

Run the cleaning pipeline from the raw snapshot and assert that output row counts equal `raw_rows - quarantined_rows`, all schema validations pass, duplicate keys are `0`, required columns have allowed missingness, labels remain within allowed classes, and the output hash is stable for the same raw input and code version.

## Variations

- `pandas`: good for small to medium tabular datasets and fast iteration.
- `Spark`: use for large distributed data, but keep validation summaries materialized.
- `warehouse`: use dbt or SQL tests when the training data is assembled in a database.

## Safety & privacy

Medium risk because cleaning can silently bias models or leak private data downstream. Keep raw data immutable, quarantine rather than erase questionable rows, avoid logging sensitive fields, and require review for rules that change labels or remove protected groups disproportionately.
