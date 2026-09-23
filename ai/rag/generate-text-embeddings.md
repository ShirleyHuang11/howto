---
name: generate-text-embeddings
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/rag/chunk-documents-for-retrieval]
status: draft
last_verified: 2026-09-22
---

## Goal

Convert text chunks into embedding vectors with stable metadata, batching, retry handling, and validation that vectors are usable for similarity search.

## Preconditions

- Token-limited chunks with `chunk_id`, `doc_id`, and source metadata.
- An embedding model selected for the target language and domain.
- Storage for vectors and metadata, such as files, Postgres with pgvector, or a hosted vector database.

## Steps

1. **Select an embedding model.** Choose based on language support, dimensionality, cost, latency, and whether data may leave your infrastructure. → *Expect:* a model name, vector dimension, and cost estimate.
2. **Normalize input text consistently.** Trim whitespace, keep meaningful headings, and avoid lowercasing if casing matters. → *Expect:* deterministic text used for both embedding and re-embedding.
3. **Batch requests within provider limits.** [BRANCH: Anthropic | OpenAI | open model] Group chunks by token count and respect maximum batch size and rate limits. ⚠️ *Data leaves your control:* external embedding APIs receive your chunk text; redact sensitive content first. → *Expect:* embedding calls return one vector per input.
4. **Validate vector shape and numeric values.** Check dimension, finite numbers, and nonzero norm. → *Expect:* malformed vectors are rejected before storage.
5. **Persist vectors with metadata.** Store `embedding_model`, `embedding_version`, `chunk_hash`, and created timestamp with each vector. → *Expect:* vectors can be traced and safely regenerated.
6. **Retry transient failures idempotently.** Retry 429 and 5xx errors with exponential backoff, keyed by `chunk_id`. → *Expect:* duplicate retries do not create duplicate records.
7. **Run nearest-neighbor sanity checks.** Query a chunk against the index and verify close neighbors are semantically related. → *Expect:* self-match or near-duplicate appears at rank 1 when included.

## Decision points

- Text contains regulated or proprietary data → prefer local embeddings or approved private deployment.
- Model dimension changes → create a new index or column; do not mix dimensions.
- Many chunks fail token limits → revisit chunking before embedding.
- Cost estimate exceeds budget → sample, compress, or choose a cheaper embedding model.

## Failure modes & recovery

- **F1 Dimension mismatch:** detect storage insert error or vector-length check failure → recreate index for the selected model dimension.
- **F2 Rate limiting:** detect 429 responses → lower concurrency and use backoff.
- **F3 Duplicate vectors:** detect repeated `chunk_id` records → upsert by stable ID.
- **F4 Empty embeddings:** detect zero norm or NaN → reject and inspect input text.

## Verification

Run an embedding validation job. Success means every input chunk has exactly one stored vector, `vector_length == expected_dimension`, all values are finite, no vector has zero norm, and a self-query returns the same `chunk_id` at rank 1 for a random sample of indexed chunks.

## Variations

- `hosted API`: simpler scaling but text leaves your infrastructure.
- `local model`: stronger privacy, but you must manage GPU or CPU throughput and model versions.
- `multilingual corpus`: choose a multilingual embedding model and evaluate by language.

## Safety & privacy

Embeddings can leak sensitive source content and are difficult to scrub without stable deletion IDs. Redact before external calls, encrypt vector stores, record model versions, and maintain a deletion path by `doc_id` and `chunk_id`.
