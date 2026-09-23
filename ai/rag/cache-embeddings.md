---
name: cache-embeddings
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You avoid recomputing embeddings for unchanged text while guaranteeing stale vectors are invalidated when the model, preprocessing, or source text changes.

## Preconditions

- An embedding model selected for your retrieval task.
- A chunking pipeline that emits stable chunk ids and text.
- A cache store such as SQLite, Postgres, object storage, or your vector DB metadata.
- A way to run a small retrieval regression test.

## Steps

1. **Define the cache key.** Hash normalized text together with embedding model id, model version, dimensions, preprocessing version, and chunker version. → *Expect:* identical inputs produce the same key and any relevant pipeline change produces a new key.
2. **Create the cache table.** Store `cache_key`, `embedding`, `model`, `dims`, `text_sha256`, `created_at`, and optional `source_id`. → *Expect:* a unique constraint prevents duplicate embeddings for the same key.
3. **Normalize text deterministically.** Apply the same Unicode normalization, whitespace handling, and metadata inclusion every time. → *Expect:* a unit test shows equivalent whitespace variants map as intended.
4. **Look up before calling the API.** Batch chunks into cache hits and misses, then embed only misses. [BRANCH: hosted embedding API | local embedding model] ⚠️ *Data leaves your control:* hosted embedding calls send chunk text externally; redact secrets and confirm data policy first. → *Expect:* repeated indexing run makes zero embedding API calls for unchanged chunks.
5. **Validate vector shape before insert.** Check the returned vector length and numeric values before saving. → *Expect:* every stored vector has the expected dimension and no NaN or infinite values.
6. **Write through to the vector index.** Upsert cached and newly computed vectors with source metadata. → *Expect:* vector DB row count equals the number of active chunks.
7. **Measure savings and correctness.** Log hit rate, miss count, embedding cost, and retrieval regression results. → *Expect:* cache hit rate rises on the second run and recall metrics match the uncached pipeline.

## Decision points

- Model id or dimensions change → invalidate by key version and re-embed all chunks.
- Chunker changes → treat as a new preprocessing version even if source documents did not change.
- Cache hit rate is low → inspect unstable metadata or non-deterministic chunk ids.
- Sensitive corpus → use local embeddings or encrypt the cache at rest.

## Failure modes & recovery

- **F1 Stale vectors:** detect retrieval returning old content after document edits → include text hash and source revision in the key, then rebuild affected chunks.
- **F2 Dimension mismatch:** detect vector DB rejecting upserts → verify model dimensions before insertion and use a separate index per dimension.
- **F3 Cache poisoning:** detect vectors stored for the wrong text hash → recompute keys, delete bad rows, and restore from source chunks.
- **F4 Unbounded cache growth:** detect storage growth beyond budget → expire embeddings for deleted source revisions after confirming they are not referenced.

## Verification

Run the indexing pipeline twice on the same corpus. The second run must make zero embedding calls for unchanged chunks, every cached vector must match the expected dimension and text hash, and retrieval recall@k must equal the first run within floating-point tie tolerance.

## Variations

- `sqlite`: simple local cache for development and small corpora.
- `postgres`: central cache with row locks for parallel indexers.
- `vector-db-metadata`: store text hash and embedding model metadata alongside vectors when a separate cache is unnecessary.

## Safety & privacy

Embeddings can leak semantic information about source text and may be regulated when derived from PII. Encrypt caches containing sensitive material, restrict access, avoid sending confidential chunks to hosted embedding APIs without approval, and cap batch sizes to control spend.
