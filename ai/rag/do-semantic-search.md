---
name: do-semantic-search
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/rag/generate-text-embeddings, ai/rag/set-up-a-vector-database]
status: draft
last_verified: 2026-09-22
---

## Goal

Embed a user query, retrieve semantically similar chunks, and return ranked results with scores and metadata suitable for RAG or search UI use.

## Preconditions

- A populated vector index with chunk text or retrievable text pointers.
- The same embedding model or compatible query embedding model used for the indexed corpus.
- A test set of queries with expected relevant chunks if quality matters.

## Steps

1. **Normalize the query.** Strip accidental whitespace, preserve user intent, and reject empty or extremely long queries. → *Expect:* a validated query string under the embedding token limit.
2. **Embed the query.** [BRANCH: hosted embeddings | local embeddings] Use the same embedding family and preprocessing used for documents. ⚠️ *Data leaves your control:* an external embedding API receives the query text. → *Expect:* one finite vector with the expected dimension.
3. **Run nearest-neighbor search.** Query the vector DB for top `k`, using the configured metric and any required tenant or access filters. → *Expect:* ranked results with chunk IDs, similarity scores, and metadata.
4. **Apply score and metadata filters.** Remove results below a minimum score or outside the user's authorization scope. → *Expect:* only eligible chunks remain.
5. **Return source metadata.** Include title, section, page, URI, and score so downstream systems can cite or inspect results. → *Expect:* every result is traceable to a source.
6. **Log retrieval traces.** Record query hash, model version, filters, top IDs, scores, and latency without storing raw sensitive queries unnecessarily. → *Expect:* retrieval behavior can be debugged.
7. **Evaluate recall.** Run labeled queries and compute recall@k and mean reciprocal rank. → *Expect:* retrieval quality is quantified before use in answers.

## Decision points

- Query asks for exact identifier or code → semantic search may need keyword or hybrid search.
- Top scores are all low → return no-answer context or broaden query, not random chunks.
- User has access filters → apply them before returning or generating with results.
- Recall@k is below threshold → revisit chunking, embeddings, or add reranking.

## Failure modes & recovery

- **F1 Embedding mismatch:** detect dimension or quality mismatch → re-embed query with the indexed model version.
- **F2 Authorization leak:** detect results from another tenant → enforce filters in database query, not after display only.
- **F3 Low-relevance results:** detect low recall or low scores → tune chunking or add hybrid search.
- **F4 Query too long:** detect embedding token-limit error → summarize or truncate with clear rules.

## Verification

Run semantic search on a labeled query set. Success means query vectors have the expected dimension, access filters exclude forbidden chunks in tests, p95 retrieval latency meets target, and recall@5 or recall@10 meets the configured threshold, such as `>= 0.85`.

## Variations

- `question answering`: retrieve more candidates, then rerank or compress before generation.
- `search UI`: expose titles, snippets, and scores rather than only chunk text.
- `local embeddings`: avoid external query exposure but benchmark latency carefully.

## Safety & privacy

Queries may contain personal or confidential information, and retrieved chunks may expose data across access boundaries. Apply authorization filters at query time, minimize logs, and treat low-confidence retrieval as no-answer rather than fabricating context.
