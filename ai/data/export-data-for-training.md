---
name: export-data-for-training
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [ai/data/validate-a-data-schema, ai/data/version-a-dataset]
status: draft
last_verified: 2026-09-22
---

## Goal

You export data into a training-ready format with stable splits, validated records, provenance, and no unintended sensitive fields.

## Preconditions

- A validated source dataset and approved feature or prompt schema.
- A target training format, such as Parquet, JSONL, TFRecord, CSV, or chat fine-tuning JSONL.
- A destination with appropriate access controls.

## Steps

1. **Define the target record schema.** Specify required fields, label format, prompt/completion or messages shape, metadata, and allowed nulls. → *Expect:* a schema file or validation class exists.
2. **Freeze input version and split ids.** Use a dataset version id and deterministic split membership. → *Expect:* train, validation, and test membership will not change during export.
3. **Remove disallowed fields.** Drop raw identifiers, secrets, unneeded PII, leakage columns, and internal-only annotations. → *Expect:* exported records contain only approved fields.
4. **Serialize records in the target format.** [BRANCH: Parquet | JSONL | chat JSONL] Write one valid record per row or line. → *Expect:* output files are readable by the intended trainer.
5. **Validate every exported record.** Run JSON Schema, Pydantic, or format-specific validators. → *Expect:* invalid records are rejected with row ids and reasons.
6. **Compute export statistics.** Count records per split, label distribution, token lengths if text is used, and file checksums. → *Expect:* a manifest contains counts, distributions, and hashes.
7. **Run a loader smoke test.** Load a small batch with the actual training dataloader or API preflight tool. → *Expect:* the trainer accepts the data without parsing errors.

## Decision points

- Text examples exceed model context → truncate with rules, split examples, or choose a longer-context model.
- Export is for a third-party training API → redact sensitive data and obtain approval before upload.
- Test split is included in the export directory → mark it read-only and exclude it from training commands.
- Labels are sparse or imbalanced → preserve split-level label counts and consider stratification.

## Failure modes & recovery

- **F1 Invalid JSONL:** detect parser errors or multi-line records → write with a proper JSON serializer and validate line by line.
- **F2 Leakage column exported:** detect future or answer fields in inputs → remove the field and regenerate all splits.
- **F3 Split contamination:** detect same entity in train and test → split by entity id and re-export.
- **F4 Token length overflow:** detect examples above context limit → shorten, chunk, or filter records and log the policy.

## Verification

The export passes only if every record validates against the target schema, split counts match the manifest, checksums are written, train and test entity overlap is zero, and a trainer or API dry run loads at least one batch successfully.

## Variations

- `Parquet`: best for tabular or large-scale local training.
- `JSONL`: common for instruction, chat, and document datasets.
- `hosted fine-tuning`: use the provider's file validation tool before launching any paid job.

## Safety & privacy

Medium risk because exports often move data to new storage or training services. ⚠️ *Data leaves your control:* before uploading to a third-party API, confirm approval, redact sensitive fields, and set a small preflight budget.
