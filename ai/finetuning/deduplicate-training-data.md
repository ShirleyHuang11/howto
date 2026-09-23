---
name: deduplicate-training-data
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You remove exact and near-duplicate training examples so the model does not overfit repeated content or leak across splits. The output dataset has documented duplicate clusters and retained representatives.

## Preconditions

- A dataset with stable row IDs and text fields to compare.
- A normalization script and optional embedding or MinHash tooling.
- A policy for which row to keep when duplicates conflict.

## Steps

1. **Choose fields for comparison.** Compare prompts, completions, source document IDs, and rendered chat text as appropriate. → *Expect:* the dedupe script has explicit field names.
2. **Normalize text.** Lowercase where safe, trim whitespace, canonicalize JSON, and remove volatile IDs only if they are not semantically important. → *Expect:* normalized hashes are reproducible.
3. **Remove exact duplicates.** Hash normalized rows and keep one representative per identical hash. → *Expect:* the report lists exact duplicate clusters and retained IDs.
4. **Find near duplicates.** Use MinHash, SimHash, or embeddings with a threshold such as cosine similarity above 0.95. → *Expect:* candidate duplicate clusters are produced for review.
5. **Resolve conflicting duplicates.** If near-identical prompts have different targets, adjudicate or drop the cluster. → *Expect:* no retained duplicate cluster has contradictory labels.
6. **Dedupe before splitting.** Assign duplicate cluster IDs and split by cluster to prevent leakage. → *Expect:* no cluster ID appears in multiple splits.
7. **Save an audit manifest.** Store removed row IDs, reason, representative ID, and script version. → *Expect:* deduplication can be reproduced or reversed from raw data.

## Decision points

- Similar text has different correct answers due to context → keep both only if the context difference is explicit.
- Dataset is small → prefer reviewing near duplicates manually before dropping many rows.
- Repetition reflects production frequency → downweight rather than fully remove if frequency is an important signal.
- Exact duplicate appears in train and validation → rebuild splits after dedupe.

## Failure modes & recovery

- **F1 Over-aggressive dedupe:** detect distinct examples clustered together → raise threshold or include more context fields.
- **F2 Missed template duplicates:** detect many examples differing only by names or IDs → normalize placeholders and rerun.
- **F3 Split leakage:** detect cluster IDs across splits → split by cluster and regenerate files.
- **F4 Label conflict:** detect same prompt with different target → adjudicate with a reviewer or drop.
- **F5 Lost provenance:** detect removed rows without source metadata → rebuild manifest from raw IDs before proceeding.

## Verification

The dedupe job passes when exact duplicate hashes are unique in the retained set, near-duplicate clusters above the threshold are resolved, no cluster crosses split boundaries, and the audit manifest accounts for every removed row with a reason and representative ID.

## Variations

- `large corpus`: use MinHash/LSH for scalable candidate generation.
- `chat data`: compare rendered conversations and final assistant targets separately.
- `code data`: normalize formatting carefully but avoid removing semantically meaningful identifiers.

## Safety & privacy

Deduplication is low risk, but duplicate reports can expose sensitive text. Store manifests in the same protected location as the source dataset and avoid exporting raw private examples in review spreadsheets.
