---
name: compute-summary-statistics
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You compute reliable summary statistics that describe dataset size, missingness, distributions, and label balance before modeling or evaluation.

## Preconditions

- A dataset in CSV, Parquet, database, or dataframe form.
- Python with `pandas`, `polars`, DuckDB, or a warehouse SQL interface.
- A list of important columns, labels, and grouping dimensions.

## Steps

1. **Load data with explicit types.** Read the dataset using declared dtypes or schema. → *Expect:* columns have expected types rather than accidental parser guesses.
2. **Count rows, columns, and duplicate keys.** Compute `len(df)`, `df.shape[1]`, and duplicates for primary keys. → *Expect:* basic size and uniqueness metrics are recorded.
3. **Measure missingness.** Run `df.isna().mean().sort_values(ascending=False)`. → *Expect:* null rates are available for every column.
4. **Summarize numeric columns.** Compute count, mean, standard deviation, quantiles, min, and max. → *Expect:* impossible ranges or extreme values are visible.
5. **Summarize categorical columns.** Compute top values, cardinality, rare-value counts, and label balance. → *Expect:* dominant categories and rare classes are identified.
6. **Group by critical segments.** Compare metrics across source, date, language, geography, or label. → *Expect:* segment-level differences are measurable.
7. **Save a profile artifact.** Write statistics to JSON, Markdown, or an HTML report. → *Expect:* a reproducible profile can be compared across dataset versions.

## Decision points

- Dataset is larger than memory → use DuckDB, Polars lazy scans, Spark, or warehouse SQL.
- Heavy-tailed numeric columns → report robust statistics such as median and percentiles.
- Label balance is skewed → follow an imbalance-handling workflow before training.
- Summary includes sensitive small groups → suppress or bucket groups below a privacy threshold.

## Failure modes & recovery

- **F1 Wrong type inference:** detect numeric stats missing for numeric-looking strings → reload with explicit schema and parse errors.
- **F2 Misleading average:** detect extreme skew or outliers → report median, percentiles, and clipped views.
- **F3 Hidden duplicates:** detect duplicate ids after counting rows → deduplicate or explain repeated entities.
- **F4 Privacy leak in counts:** detect tiny groups in report → suppress counts below the minimum group size.

## Verification

The statistics job passes only if it emits machine-readable row count, column count, null rates for all columns, numeric quantiles for numeric columns, cardinality for categorical columns, and duplicate-key count, with no missing required metrics.

## Variations

- `pandas-profiling/ydata-profiling`: quick exploratory HTML reports for local data.
- `DuckDB`: fast SQL summaries over local Parquet and CSV files.
- `warehouse SQL`: compute summaries near large production tables.

## Safety & privacy

Low risk if reports stay internal. Summary statistics can still reveal sensitive small cohorts, so suppress tiny groups and avoid exporting raw examples in profile reports.
