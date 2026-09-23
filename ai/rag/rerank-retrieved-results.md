---
name: rerank-retrieved-results
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

Improve retrieval precision by reranking an initial candidate set and verifying that relevant chunks move higher without unacceptable latency or cost.

## Preconditions

- A first-stage retriever that returns more candidates than the final context needs.
- A reranker option, such as a cross-encoder, hosted rerank API, LLM judge, or domain-specific ranker.
- Labeled queries with relevant chunk IDs.

## Steps

1. **Retrieve a broad candidate set.** Ask the vector or hybrid retriever for top 20-100 candidates, with access filters already applied. → *Expect:* candidates include IDs, text, metadata, and first-stage scores.
2. **Choose a reranker.** [cross-encoder | hosted rerank API | LLM reranker] Select based on quality, latency, cost, and privacy. → *Expect:* a reranker config with input limits and score interpretation.
3. **Score query-candidate pairs.** Send the query and candidate text to the reranker in batches. ⚠️ *Data leaves your control:* hosted rerankers receive query and candidate text. → *Expect:* each candidate has a rerank score.
4. **Sort and trim results.** Order by rerank score and keep the top `n` chunks for generation or display. → *Expect:* final results are fewer and more relevant than the initial set.
5. **Preserve traceability.** Return original score, rerank score, rank changes, and source metadata. → *Expect:* ranking changes can be audited.
6. **Evaluate ranking metrics.** Compute nDCG@k, MRR, recall@k, and latency before and after reranking. → *Expect:* the reranker improves top-rank metrics on labeled queries.
7. **Set fallback behavior.** If reranker fails or times out, use first-stage results or return a controlled error depending on product risk. → *Expect:* production does not hang or silently return empty results.

## Decision points

- First-stage recall is low → reranking cannot recover missing candidates; improve retrieval first.
- Reranker improves nDCG but hurts recall → retrieve more candidates or adjust final `n`.
- Latency exceeds budget → batch, cache, use a smaller reranker, or rerank fewer candidates.
- Documents are confidential → prefer local reranker or approved private endpoint.

## Failure modes & recovery

- **F1 Candidate omission:** detect gold chunk absent from first-stage top 100 → tune initial retriever.
- **F2 Reranker truncation:** detect candidate text cut before answer-bearing span → pass shorter chunks or highlighted snippets.
- **F3 Timeout:** detect rerank latency over SLA → add timeout and fallback to first-stage ranking.
- **F4 Score inversion:** detect worse nDCG after rerank → check sort direction and score semantics.

## Verification

Run before-and-after evaluation on labeled queries. Success means first-stage recall@candidate_k is high enough, reranked nDCG@5 or MRR improves by the target margin, p95 rerank latency remains under SLA, and no unauthorized candidate is introduced after reranking.

## Variations

- `cross-encoder`: best for quality with local control, but slower than vector search.
- `LLM judge`: flexible for complex relevance but costly and less deterministic.
- `hosted rerank`: easy to integrate; review data exposure and rate limits.

## Safety & privacy

Reranking often exposes both user queries and retrieved text to another model. Apply access filters before reranking, redact sensitive content for hosted services, cap candidate counts to control cost, and log enough metadata to audit ranking decisions.
