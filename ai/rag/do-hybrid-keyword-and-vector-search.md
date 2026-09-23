---
name: do-hybrid-keyword-and-vector-search
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/rag/do-semantic-search]
status: draft
last_verified: 2026-09-22
---

## Goal

Combine keyword and vector retrieval so exact identifiers, rare terms, and semantic matches are all represented in the final ranked results.

## Preconditions

- A corpus indexed for both lexical search, such as BM25, and vector search.
- Shared stable `chunk_id` values across indexes.
- A labeled query set containing semantic queries and exact-term queries.

## Steps

1. **Build or verify both indexes.** Ensure the lexical and vector indexes contain the same chunk IDs and access metadata. → *Expect:* index counts match or differences are explained.
2. **Run keyword search.** Use BM25 or a search engine for exact terms, identifiers, and quoted phrases. → *Expect:* a ranked lexical result list with scores.
3. **Run vector search.** Embed the query and retrieve semantic neighbors with the same access filters. ⚠️ *Data leaves your control:* external embedding APIs receive the query text. → *Expect:* a ranked vector result list with scores.
4. **Fuse rankings.** Use reciprocal rank fusion or normalized score fusion rather than naively adding incomparable raw scores. → *Expect:* one merged ranked list keyed by `chunk_id`.
5. **Deduplicate and preserve provenance.** Keep each chunk once while storing lexical rank, vector rank, and fusion score. → *Expect:* final results explain why each chunk was returned.
6. **Tune modality weights.** Evaluate exact-match and semantic query subsets separately and adjust fusion parameters. → *Expect:* both subsets meet recall targets.
7. **Add optional reranking.** Rerank fused candidates when precision at the top matters. → *Expect:* final top results are more relevant without losing recall.

## Decision points

- Query contains exact IDs, error codes, or names → boost keyword results.
- Query is paraphrased or conceptual → vector results may deserve more weight.
- Lexical and vector indexes disagree heavily → inspect chunk text normalization and metadata filters.
- Hybrid recall improves but top precision drops → add reranking.

## Failure modes & recovery

- **F1 Score incompatibility:** detect poor results from raw score addition → use rank-based fusion.
- **F2 Index drift:** detect chunk IDs missing from one index → rebuild or run consistency repair.
- **F3 Analyzer mismatch:** detect keyword misses for punctuation or code terms → adjust tokenization and exact fields.
- **F4 Duplicate context:** detect near-identical chunks crowding top results → deduplicate by source span.

## Verification

Run hybrid search on labeled queries split by exact-term and semantic intent. Success means fused recall@10 beats or matches the better single retriever on each subset, no result violates access filters, index chunk ID consistency is `>= 99.9%`, and p95 latency remains within budget.

## Variations

- `Elasticsearch or OpenSearch`: combine BM25 and vector retrieval with RRF or scripted rescoring.
- `Postgres`: combine full-text search with pgvector and fuse in SQL or application code.
- `hosted vector DB`: use provider hybrid search if it exposes lexical fields and fusion controls.

## Safety & privacy

Hybrid search still requires strict access filtering in both retrieval paths. Query text may leave your infrastructure for embeddings, logs can reveal sensitive exact identifiers, and rank fusion should not reintroduce chunks filtered out for authorization.
