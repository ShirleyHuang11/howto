---
name: split-a-training-and-validation-set
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You split examples into train, validation, and optional test sets without leakage. The final manifests prove that related examples do not cross split boundaries.

## Preconditions

- A cleaned dataset with stable row IDs.
- Grouping keys such as user ID, document ID, conversation ID, prompt family, or source file.
- Target split proportions, commonly 80/10/10 or 90/10 when data is small.

## Steps

1. **Choose the leakage boundary.** Split by the largest related unit, not by individual row, such as document or user. → *Expect:* every row has a nonempty `group_id`.
2. **Stratify important labels.** Preserve class, language, difficulty, and safety-category distributions where possible. → *Expect:* a distribution table shows each split is within the allowed tolerance.
3. **Assign groups deterministically.** Hash `group_id` with a fixed seed or use a saved manifest. → *Expect:* rerunning the script produces the same split assignment.
4. **Write separate files.** Save `train.jsonl`, `validation.jsonl`, and `test.jsonl` or the provider-specific names. → *Expect:* row counts match the manifest.
5. **Check for leakage.** Assert that no `group_id`, exact input hash, or near-duplicate cluster appears in multiple splits. → *Expect:* leakage check returns zero overlaps.
6. **Keep test set untouched.** Use validation for hyperparameter choices and reserve test for final reporting. → *Expect:* run logs show no training or tuning step used test labels.
7. **Version the split metadata.** Save split seed, script version, dataset hash, and counts. → *Expect:* a manifest can reproduce the split.

## Decision points

- Dataset is very small → use cross-validation or a larger validation share, but keep a final untouched test if shipping.
- Stratification conflicts with leakage boundaries → prioritize leakage prevention over perfect class proportions.
- Near duplicates span splits → cluster first, then split by cluster ID.
- New data arrives after tuning → assign it deterministically or create a new split version.

## Failure modes & recovery

- **F1 Row-level leakage:** detect same user or document in multiple splits → resplit by group key.
- **F2 Class imbalance:** detect rare labels missing from validation → stratify groups or collect more examples.
- **F3 Non-reproducible split:** detect different counts on rerun → fix random seed and save manifests.
- **F4 Test contamination:** detect test examples used during prompt tuning → retire that test set and create a new one.
- **F5 Duplicate content:** detect high similarity across splits → deduplicate or split by cluster.

## Verification

Run a split validator that confirms all rows are assigned exactly once, no group IDs or input hashes overlap across splits, label distributions are within the documented tolerance, and split manifests include dataset hash, seed, counts, and script version.

## Variations

- `classification`: stratify by label and group.
- `conversation data`: split by conversation or account, not message.
- `document RAG tuning`: split by source document to avoid memorized passages in validation.

## Safety & privacy

Splitting is low risk, but manifests can contain user or document identifiers. Store hashed or internal IDs when possible and do not publish split files containing private metadata.
