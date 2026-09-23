---
name: prepare-a-fine-tuning-dataset
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You turn raw examples into a clean, documented fine-tuning dataset that matches the target task and trainer format. The finished dataset passes schema, privacy, deduplication, and split checks.

## Preconditions

- Source examples with permission to use them for model training.
- A target behavior definition and evaluation set.
- Local tooling for JSONL validation, PII scanning, and token counting.

## Steps

1. **Define the target behavior.** Write the task, input distribution, refusal rules, output style, and examples that should not be changed by fine-tuning. → *Expect:* a dataset spec with accepted and rejected example types.
2. **Collect candidate examples.** Pull examples from approved logs, synthetic generation, or human-authored cases. → *Expect:* every row has source provenance and license or consent metadata.
3. **Remove sensitive data.** Run PII and secret scanners, then redact or drop unsafe rows. → *Expect:* scanners report zero high-confidence secrets and only approved PII categories remain.
4. **Normalize labels and outputs.** Ensure outputs demonstrate the desired answer, not explanations of the label unless the product needs reasoning text. → *Expect:* fields are consistently named and every row has nonempty input and target output.
5. **Deduplicate and filter low quality.** Remove exact duplicates, near duplicates, broken markup, and rows with contradictory labels. → *Expect:* duplicate rate falls below the documented threshold.
6. **Count tokens.** Use the tokenizer for the intended base model and flag rows above the trainer limit. → *Expect:* `max_tokens_per_example` is below the model and provider limit.
7. **Write train/validation/test splits.** Split by user, document, or prompt family to prevent leakage. → *Expect:* no grouping key appears in more than one split.

## Decision points

- Dataset includes customer or proprietary data → treat as high review risk and confirm training rights before upload.
- Validation performance is worse than base model → dataset likely teaches wrong behavior; pause tuning.
- Token lengths exceed limits → summarize inputs, chunk tasks, or choose a longer-context base model.
- Examples mix incompatible styles → split into separate fine-tunes or add explicit task tags.

## Failure modes & recovery

- **F1 Training without rights:** detect missing license or consent metadata → remove rows until provenance is complete.
- **F2 PII leakage:** detect emails, names, credentials, or account IDs → redact, rescan, and audit the source pipeline.
- **F3 Duplicate leakage:** detect near-identical rows across splits → regroup and resplit before training.
- **F4 Label contradiction:** detect same input with different targets → adjudicate or drop all conflicting rows.
- **F5 Token overflow:** detect examples above limit → truncate only when semantics remain valid, otherwise drop.

## Verification

Run a dataset validator that checks JSONL parsing, required fields, source metadata, zero high-confidence secrets, no duplicate group IDs across splits, `max_tokens <= trainer_limit`, and at least the minimum planned row count for train and validation.

## Variations

- `chat fine-tuning`: format rows as role-based messages after cleaning.
- `classification`: keep compact labels and class balance reports.
- `tool-use tuning`: validate tool-call JSON and tool result transcripts before training.

## Safety & privacy

Fine-tuning can memorize sensitive or copyrighted material. Use only data you are allowed to train on, remove secrets and unnecessary PII, document retention rules, and require review before uploading private data to any hosted trainer.
