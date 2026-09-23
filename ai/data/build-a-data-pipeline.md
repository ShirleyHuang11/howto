---
name: build-a-data-pipeline
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: [ai/data/validate-a-data-schema, ai/data/version-a-dataset]
status: draft
last_verified: 2026-09-22
---

## Goal

You build a repeatable data pipeline that extracts, validates, transforms, versions, and publishes data for AI training, evaluation, or retrieval.

## Preconditions

- Access to source data and permission to process it.
- A workflow runner such as cron, Airflow, Dagster, Prefect, GitHub Actions, or a managed pipeline service.
- Schema validation and dataset versioning choices, such as `ai/data/validate-a-data-schema` and `ai/data/version-a-dataset`.

## Steps

1. **Define inputs, outputs, and ownership.** Write source tables or files, expected output artifacts, refresh cadence, and responsible owner. → *Expect:* a short pipeline contract with owners and SLAs.
2. **Implement extract as an idempotent step.** Read from snapshot ids, time windows, or incremental watermarks without modifying the source. → *Expect:* rerunning extract for the same window produces the same raw artifact.
3. **Validate raw data before transformation.** Run schema, row-count, null-rate, and freshness checks. → *Expect:* invalid input stops the pipeline before derived data is written.
4. **Transform with deterministic code.** Normalize types, join reference data, deduplicate, and create features in versioned scripts. → *Expect:* transformation logs row counts in and out for every stage.
5. **Write outputs atomically.** Write to a temporary path, validate, then promote or swap into the final location. → *Expect:* consumers never read half-written data.
6. **Version and publish the artifact.** Save checksums, schema hash, data version id, and run metadata. → *Expect:* a downstream training job can pin exactly this pipeline output.
7. **Add monitoring and alerts.** Track freshness, volume, validation failures, runtime, and cost. → *Expect:* pipeline failure or unusual drift sends an alert to the owner.

## Decision points

- Data must update in near real time → use streaming or micro-batch orchestration with stronger idempotency.
- Data is used for model evaluation → prefer immutable snapshots and manual approval before replacing it.
- Source is unreliable → add quarantine storage and upstream quality reports.
- Pipeline cost grows unexpectedly → add partition pruning, incremental processing, or sampling for development runs.

## Failure modes & recovery

- **F1 Partial output:** detect missing partitions or failed write after consumers started reading → write atomically and roll back to the previous version.
- **F2 Duplicate rows:** detect key uniqueness validation failure → fix incremental watermark logic and deduplicate by stable primary key.
- **F3 Schema drift:** detect new or changed columns → pause downstream jobs and update schema or transformation code intentionally.
- **F4 Stale data:** detect freshness SLA breach → alert owner, fall back to last known good version, and mark output stale.

## Verification

A dry run and a production-sized run must both complete with passing schema checks, matching expected row-count ranges, no duplicate primary keys, a recorded dataset version id, and an atomic output path that downstream code can read successfully.

## Variations

- `Airflow`: model steps as DAG tasks with retries and sensors.
- `Dagster/Prefect`: use typed assets or flows with built-in metadata.
- `warehouse-native`: schedule SQL transformations with dbt or managed warehouse jobs.

## Safety & privacy

Medium risk because pipelines can multiply sensitive data. Minimize copied fields, enforce access controls on intermediate outputs, avoid logging raw records, and require review before changing retention or publishing destinations.
