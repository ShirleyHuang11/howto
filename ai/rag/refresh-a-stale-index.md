---
name: refresh-a-stale-index
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You update a RAG index from changed source documents without losing access controls, corrupting vectors, or degrading retrieval quality.

## Preconditions

- A current production index with recorded corpus revision, parser version, chunker version, and embedding model.
- Access to the latest approved source documents.
- A retrieval eval set and rollback path.
- Permission to update the target index.

## Steps

1. **Snapshot the current state.** Export index metadata, source manifest, active chunk ids, and retrieval metrics. → *Expect:* a rollback artifact identifies the currently served index revision.
2. **Detect changed sources.** Compare source hashes, modified timestamps, permissions, and deletion markers against the manifest. → *Expect:* a change set labeled `added`, `modified`, `deleted`, or `permission_changed`.
3. **Reprocess affected documents.** Parse, chunk, redact, and embed only changed documents unless the parser, chunker, or embedding model changed. ⚠️ *Data leaves your control:* hosted embedding calls receive changed text; confirm the data is approved for the provider. → *Expect:* new chunks validate against the same schema as the old index.
4. **Build a shadow index.** Upsert new vectors and tombstone deleted chunks in a non-serving index or namespace. → *Expect:* shadow index count matches expected active chunks.
5. **Run regression evaluation.** Compare shadow index recall@k, latency, top-query behavior, and authorization filters against production. → *Expect:* metrics are equal or better within the release tolerance.
6. **Promote the index.** ⚠️ *Irreversible:* switching production traffic can expose stale or wrong answers; confirm backups, eval pass, and authorization checks before promotion. → *Expect:* production points to the new revision and old revision remains available for rollback.
7. **Monitor after refresh.** Track zero-result queries, complaint rate, latency, and retrieval distribution drift. → *Expect:* no alert fires during the observation window.

## Decision points

- Parser, chunker, or embedding model changed → full rebuild, not incremental refresh.
- Authorization metadata changed → test permissions before promotion.
- Eval regresses → do not promote; inspect changed documents and retrieval diffs.
- Deleted documents remain retrievable → purge vectors and cached context immediately.

## Failure modes & recovery

- **F1 Orphaned stale chunks:** detect deleted source ids still returned → tombstone by source id and rebuild affected namespace.
- **F2 Permission regression:** detect restricted docs returned to unauthorized test users → roll back and fix access metadata propagation.
- **F3 Partial refresh corruption:** detect index count mismatch → rebuild shadow index from the manifest.
- **F4 Quality regression:** detect recall or MRR drop → compare top-k diffs and adjust chunking/reranking before retrying.

## Verification

Promotion is allowed only when the shadow index active chunk count equals the source manifest, deleted chunks are not retrievable, authorization tests pass for restricted documents, retrieval recall@5 is within tolerance or better than production, and rollback metadata is present.

## Variations

- `blue-green-index`: switch an alias between complete index versions.
- `namespace-refresh`: update per-tenant or per-collection namespaces independently.
- `streaming-corpus`: use queued document changes but still run periodic full reconciliation.

## Safety & privacy

Refreshing an index can expose deleted, restricted, or newly sensitive documents. Treat promotion as high risk, keep rollback artifacts, preserve access controls, avoid external embedding calls for unapproved data, and require explicit review before deleting or replacing production indexes.
