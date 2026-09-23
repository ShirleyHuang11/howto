---
name: validate-a-data-schema
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You enforce a machine-checkable schema so bad or drifted data is caught before training, indexing, or inference.

## Preconditions

- A representative dataset sample and the expected column names, types, ranges, and nullability.
- A validation library such as Pandera, Great Expectations, Pydantic, or PyArrow.
- A place in CI or the pipeline where validation can fail the run.

## Steps

1. **Declare the contract.** Write required columns, data types, allowed categories, range bounds, uniqueness keys, and nullable fields. → *Expect:* a schema file or Python schema object exists.
2. **Validate a known-good sample.** Run the validator against a small accepted dataset. → *Expect:* validation passes and emits no unexpected warnings.
3. **Add negative checks.** Create tiny rows with a missing required column, wrong type, duplicate key, and out-of-range value. → *Expect:* each bad example fails with a clear error.
4. **Run validation on full inputs.** Execute `python scripts/validate_schema.py --input data/incoming.parquet`. → *Expect:* the command exits `0` only when all schema checks pass.
5. **Store validation output.** Save row count, schema version, validation timestamp, and failure summary in pipeline logs. → *Expect:* each dataset load has an auditable validation record.
6. **Gate downstream jobs.** Make training, embedding, or feature generation depend on validation success. → *Expect:* downstream work does not start when validation exits nonzero.

## Decision points

- Data is row-oriented API input → use Pydantic or JSON Schema.
- Data is tabular training data → use Pandera, Great Expectations, or PyArrow schemas.
- Schema changes are intentional → bump a schema version and add a migration or compatibility note.
- Validation failures affect production → quarantine the batch and alert the owning team.

## Failure modes & recovery

- **F1 Type ambiguity:** detect strings in numeric columns after CSV load → parse with explicit dtypes and reject unparseable rows.
- **F2 Null explosion:** detect null rate above the schema threshold → quarantine the batch and inspect upstream extraction.
- **F3 Category drift:** detect unseen enum values → decide whether to map to unknown, update the schema, or reject the data.
- **F4 Validator too slow:** detect validation exceeding the pipeline budget → validate partitions in parallel or use typed columnar formats.

## Verification

The validation command must pass on the approved fixture and fail on at least four bad fixtures: missing column, wrong type, duplicate key, and out-of-range value. CI passes only when the validator returns the expected exit codes for all fixtures.

## Variations

- `Pandera`: define dataframe schemas directly in Python and run them in tests.
- `Great Expectations`: create expectation suites with HTML validation reports.
- `JSON Schema/Pydantic`: validate structured API payloads and LLM outputs.

## Safety & privacy

Low risk when run locally, but validation logs may include sample values. Redact PII from error reports before sending logs to external observability tools.
