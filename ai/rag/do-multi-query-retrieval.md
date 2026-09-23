---
name: do-multi-query-retrieval
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You expand one user question into several retrieval-focused queries, merge the result sets, and prove recall improves without flooding the model context.

## Preconditions

- A searchable index with document ids, chunk ids, text, and metadata.
- A small labeled eval set with user queries and gold relevant chunk ids.
- You can call a query-rewriting LLM, or you have a deterministic query-expansion template.
- A retrieval script that can return top-k chunks for any query.

## Steps

1. **Define the baseline metric.** Run your current retriever against the eval set and compute recall@k with `gold_id in retrieved_ids[:k]`. → *Expect:* a baseline table such as `{"recall@5": 0.68, "mean_latency_ms": 220}`.
2. **Write a query expansion prompt.** Ask for 3-5 semantically distinct search queries, preserving entities and refusing to answer the question. [BRANCH: Anthropic | OpenAI | open model] ⚠️ *Data leaves your control:* if you send user queries to an external API, redact secrets and avoid raw PII first. → *Expect:* valid JSON like `{"queries":["..."]}` with no prose.
3. **Validate generated queries.** Parse the JSON, remove duplicates, cap length, and keep the original query as the first query. → *Expect:* each input question has `1 <= len(queries) <= 6` and every query is a non-empty string.
4. **Retrieve for every query.** Run top-k retrieval per generated query with the same filters as the original user request. → *Expect:* a list of `(query_variant, chunk_id, score)` rows for every eval item.
5. **Merge and deduplicate results.** Combine results by chunk id, keeping the best score and a count of how many variants found the chunk. → *Expect:* no duplicate chunk ids remain in the merged candidate list.
6. **Rerank the merged candidates.** Use a cross-encoder, LLM reranker, or reciprocal-rank fusion: `rrf = sum(1 / (60 + rank_i))`. → *Expect:* candidates are sorted into a final top-k list with stable tie-breaking.
7. **Measure recall and cost.** Re-run the eval and compare recall@k, latency, token use, and API cost against baseline. → *Expect:* recall@5 increases by at least 5 percentage points or you can show the trade-off is not worth shipping.
8. **Add production guards.** Cache expansions for repeated normalized queries, enforce a max number of variants, and fall back to the original query when expansion fails. → *Expect:* failed expansion still returns baseline retrieval results.

## Decision points

- Recall improves but latency is too high → reduce variants, lower per-query k, or cache expansions.
- Generated queries drift from the user's intent → tighten the prompt to preserve named entities and add a similarity check.
- Recall does not improve on the eval set → do not ship; try hybrid search or reranking first.
- Sensitive queries are common → prefer local expansion or deterministic templates.

## Failure modes & recovery

- **F1 Query drift:** detect variants that omit key entities or add unsupported facts → reject variants with low embedding similarity to the original query or missing required entities.
- **F2 Duplicate flooding:** detect repeated chunk ids dominating the final list → deduplicate before context assembly and diversify by source document.
- **F3 Cost spike:** detect token or API cost per query above budget → cache expansions and cap variants.
- **F4 Latency regression:** detect p95 retrieval latency over your SLO → parallelize retrieval calls and reduce top-k per variant.

## Verification

Programmatically pass a labeled eval: multi-query retrieval returns a gold chunk in the top 5 for at least 90% of eval queries, or improves recall@5 by at least 5 percentage points over baseline while p95 latency stays under the configured SLO and expansion JSON validates for 100% of eval inputs.

## Variations

- `hybrid-search`: run lexical and vector retrieval for each variant, then fuse all ranks.
- `local-model`: use a small local instruct model for expansion to avoid third-party query exposure.
- `reranker`: replace reciprocal-rank fusion with a cross-encoder when candidate quality matters more than latency.

## Safety & privacy

User queries may contain PII, secrets, or proprietary strategy. Redact or classify before external expansion, log only normalized query hashes where possible, cap variants and top-k to control cost, and treat retrieved text as untrusted because prompt injection can arrive through documents.
