---
name: parse-messy-csv-data
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: [ai/data/validate-a-data-schema]
status: draft
last_verified: 2026-09-22
---

## Goal

You turn an inconsistent CSV export into a typed, validated dataset while preserving enough diagnostics to fix upstream issues.

## Preconditions

- The source CSV file and any known encoding, delimiter, quote, escape, and header conventions.
- Python with `pandas`, `pyarrow`, or `duckdb`.
- An expected schema or a profiling target, such as `ai/data/validate-a-data-schema`.

## Steps

1. **Inspect raw bytes and shape.** Run `file`, `head`, and a small binary read to detect encoding, delimiter, BOM, and malformed lines. → *Expect:* identified encoding and delimiter candidates.
2. **Load with explicit parser options.** Use `pd.read_csv(path, encoding="utf-8-sig", sep=",", quotechar='"', on_bad_lines="warn", dtype=str)`. → *Expect:* a dataframe loads without silently coercing important fields.
3. **Capture rejected rows.** Re-run with a parser or precheck that writes malformed line numbers and raw content to a quarantine file. → *Expect:* every skipped or bad row is auditable.
4. **Normalize headers and whitespace.** Strip whitespace, standardize names, remove duplicate columns, and normalize obvious null tokens. → *Expect:* columns match the expected naming convention.
5. **Cast types deliberately.** Convert dates, numbers, booleans, and categories with explicit error handling. → *Expect:* type conversion reports invalid values instead of silently replacing them.
6. **Validate the cleaned data.** Run schema checks for required columns, type constraints, uniqueness, and null limits. → *Expect:* validation passes or produces a specific failure report.
7. **Write a typed output format.** Save cleaned data as Parquet plus a parsing report. → *Expect:* downstream code reads typed columns without repeating CSV cleanup.

## Decision points

- Encoding is uncertain → test `utf-8-sig`, `latin-1`, and declared export settings, then record the chosen encoding.
- Bad rows are numerous → stop and request a corrected export rather than guessing.
- Numeric fields contain locale-specific commas or currency → parse with explicit locale and symbol removal.
- CSV is too large for memory → use DuckDB, Polars lazy scan, or chunked pandas reads.

## Failure modes & recovery

- **F1 Shifted columns:** detect rows with unexpected field counts → inspect quoting and delimiter settings, then quarantine bad lines.
- **F2 Silent type corruption:** detect ids losing leading zeros or large integers changing → load as strings first and cast only approved columns.
- **F3 Date ambiguity:** detect mixed day/month parsing → require an explicit date format and reject ambiguous rows.
- **F4 Duplicate headers:** detect repeated column names → rename with a deterministic rule or reject until upstream fixes the export.

## Verification

The parser passes only if row counts equal valid rows plus quarantined rows, schema validation succeeds on the cleaned output, no required column is missing, and a round-trip Parquet read preserves declared column types.

## Variations

- `pandas`: practical for small and medium files with explicit `dtype` and parser options.
- `DuckDB`: robust for large local CSVs and direct Parquet export.
- `Polars`: fast lazy scanning and strict schema overrides.

## Safety & privacy

Low risk, but CSV parsing reports can expose raw sensitive rows. Store quarantine files with the same access controls as the source and avoid pasting raw customer data into external tools.
