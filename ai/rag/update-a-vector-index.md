---
name: update-a-vector-index
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: [ai/rag/set-up-a-vector-database]
status: draft
last_verified: 2026-09-22
---

## Goal

Update a vector index for added, changed, or deleted documents without creating duplicates, serving stale chunks, or breaking retrieval quality.

## Preconditions

- Stable document IDs, chunk IDs, and content hashes.
- A vector database that supports upsert and delete by ID or metadata filter.
- A backup, snapshot, or rebuild path for the current production index.

## Steps

1. **Compute document diffs.** Compare source manifests or hashes to identify added, changed, and deleted documents. → *Expect:* a change set grouped by `add`, `update`, and `delete`.
2. **Regenerate chunks for changed documents.** Use the current approved chunking config and embedding model. → *Expect:* new chunks have stable IDs or a mapping from old IDs to new IDs.
3. **Embed only changed chunks.** Batch embedding calls and validate vector dimensions and metadata. ⚠️ *Data leaves your control:* external embedding APIs receive changed chunk text. → *Expect:* vectors exist for every new or changed chunk.
4. **Upsert additions and updates.** Write new vectors and metadata using `chunk_id` as the idempotency key. → *Expect:* rerunning the job does not duplicate records.
5. **Delete removed or superseded chunks.** ⚠️ *Irreversible:* deleting production vectors can remove answers; confirm the delete filter, backup, and affected count before execution. → *Expect:* only intended stale chunk IDs are removed.
6. **Rebuild or retune indexes if needed.** For large changes, refresh ANN indexes or create a new collection and swap aliases. → *Expect:* query latency and recall remain stable.
7. **Run regression retrieval eval.** Compare updated index against baseline queries, especially changed documents. → *Expect:* no unacceptable regression before traffic uses the new index.

## Decision points

- More than a small percentage of corpus changed → build a new index and swap atomically.
- Embedding model changed → re-embed the whole corpus into a separate index.
- Delete count is unexpectedly high → stop and inspect the diff.
- Eval regresses on unchanged docs → rollback to snapshot or previous alias.

## Failure modes & recovery

- **F1 Duplicate chunks:** detect multiple rows for one `chunk_id` → enforce upsert and unique IDs.
- **F2 Stale chunks:** detect deleted source still returned → verify delete filters and tombstone handling.
- **F3 Partial update:** detect job failure mid-run → resume from manifest and idempotency keys.
- **F4 ANN degradation:** detect slower or worse retrieval after many updates → rebuild index or compact collection.

## Verification

Run an index update validation. Success means added and changed documents are retrievable, deleted chunk IDs return zero results, total record count equals previous count plus additions minus deletions, no duplicate `chunk_id`s exist, and retrieval regression metrics stay within the allowed delta.

## Variations

- `blue-green index`: build a new collection and switch an alias after eval passes.
- `pgvector`: use transactions for metadata updates and deletes where feasible.
- `streaming updates`: queue document changes and process with idempotent workers.

## Safety & privacy

This is high risk because deletion and production index swaps can break live answers, and embedding updates may send proprietary text to external APIs. Back up first, confirm affected counts, use idempotent manifests, and require review for large deletes or model-version changes.
