---
name: join-two-datasets
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/data/validate-a-data-schema]
status: draft
last_verified: 2026-09-22
---

## Goal

You join two datasets without accidental row duplication, data leakage, or key mismatch, and you verify the joined output quantitatively.

## Preconditions

- Two datasets with documented join keys and expected relationship: one-to-one, one-to-many, or many-to-one.
- Python, SQL, DuckDB, Spark, or another join-capable tool.
- Schema and uniqueness expectations for both inputs.

## Steps

1. **Validate join keys.** Check null rates, type consistency, trimming/case normalization, and uniqueness with `groupby(key).size()`. → *Expect:* a key quality report for both datasets.
2. **Declare the join relationship.** Decide whether the join should be `one_to_one`, `many_to_one`, `one_to_many`, or `many_to_many`. → *Expect:* an explicit relationship used by the join command or test.
3. **Run the join with validation.** In pandas, use `left.merge(right, on=key, how="left", validate="many_to_one", indicator=True)`. → *Expect:* the command fails if the declared relationship is violated.
4. **Measure match coverage.** Count `_merge` values or SQL matched/unmatched rows. → *Expect:* match, left-only, and right-only rates are visible.
5. **Check row-count expansion.** Compare input and output row counts and duplicate key counts. → *Expect:* row count changes match the declared relationship.
6. **Audit feature leakage.** Remove columns from the right dataset that would not be available at prediction time. → *Expect:* joined features respect the model's serving timestamp and availability.
7. **Write the joined dataset and report.** Save output plus join keys, relationship, row counts, and coverage metrics. → *Expect:* downstream users can reproduce and inspect the join.

## Decision points

- Coverage is lower than expected → normalize keys, inspect unmatched samples, or obtain a better crosswalk.
- Join is many-to-many → aggregate first or document why row multiplication is intended.
- Right-side data is generated after the label time → exclude it to prevent leakage.
- Keys contain PII → hash or tokenize keys before sharing joined outputs.

## Failure modes & recovery

- **F1 Row explosion:** detect output rows far above input rows → inspect duplicate keys and aggregate or deduplicate before joining.
- **F2 Low match rate:** detect high left-only count → standardize key format and compare unmatched examples.
- **F3 Type mismatch:** detect numeric ids on one side and strings on the other → cast to canonical strings before joining.
- **F4 Time leakage:** detect future attributes joined into training examples → perform an as-of join constrained by event timestamp.

## Verification

The join passes only if declared relationship validation succeeds, row-count expansion is within the expected bound, unmatched rate is below the configured threshold, and a leakage check confirms all joined feature timestamps are at or before the prediction timestamp.

## Variations

- `pandas`: use `merge(..., validate=..., indicator=True)` for local joins.
- `SQL`: use pre-join uniqueness queries and post-join coverage counts.
- `Spark`: use broadcast joins for small dimension tables and inspect skewed keys.

## Safety & privacy

Medium risk because joining can re-identify records or create sensitive profiles. Minimize joined fields, protect keys, and review whether the combined dataset has stricter access requirements than either input alone.
