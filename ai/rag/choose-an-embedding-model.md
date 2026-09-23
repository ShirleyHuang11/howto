---
name: choose-an-embedding-model
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You select an embedding model based on measured retrieval quality, latency, cost, language coverage, and operational constraints rather than intuition.

## Preconditions

- A representative corpus and 50-200 labeled queries with relevant document or chunk ids.
- Candidate embedding models, including at least one hosted and one local option when privacy matters.
- A fixed chunking and retrieval pipeline for fair comparison.
- A script that computes recall@k, MRR, latency, and cost.

## Steps

1. **Define selection criteria.** Set minimum recall@k, p95 latency, max cost per 1,000 queries, dimensionality constraints, and privacy requirements. → *Expect:* a written scorecard with pass/fail thresholds.
2. **Freeze the eval set.** Keep the same chunks, labels, query filters, and train/test split for all candidates. → *Expect:* every model is evaluated on identical input files.
3. **Embed a sample with each candidate.** [BRANCH: hosted embeddings | local embeddings] ⚠️ *Data leaves your control:* hosted embedding APIs receive corpus text; redact or use approved data only. → *Expect:* vectors have documented dimensions and no failed records.
4. **Build separate indexes.** Create one vector index per model and dimension, using the same distance metric recommended for that model. → *Expect:* index metadata records model name, dimension, metric, and corpus revision.
5. **Run retrieval evaluation.** For each query, retrieve top-k and compute recall@1, recall@5, recall@10, MRR, latency, and cost. → *Expect:* a comparison table sorted by your primary metric.
6. **Test domain edge cases.** Include acronyms, code symbols, multilingual text, short queries, and long natural-language questions if your product needs them. → *Expect:* no selected model fails a required domain slice.
7. **Choose and document the winner.** Pick the lowest-risk model that passes quality and operating thresholds, not necessarily the highest-scoring model. → *Expect:* a decision record with eval results and rollback option.

## Decision points

- Hosted model wins but data cannot leave your environment → select the best local model or seek explicit data approval.
- High recall but high latency → try lower dimensions, approximate indexing, or caching.
- Poor code or table retrieval → evaluate specialized embeddings or hybrid search.
- Scores are close → prefer cheaper, simpler, better-supported operations.

## Failure modes & recovery

- **F1 Biased eval set:** detect excellent scores but poor production queries → add real anonymized queries and stratified domain slices.
- **F2 Wrong distance metric:** detect unexpectedly poor ranking → verify cosine, dot product, or L2 matches the model documentation.
- **F3 Dimension lock-in:** detect vector DB schema blocking candidates → create per-model indexes instead of mixing dimensions.
- **F4 Cost surprise:** detect monthly estimate above budget → include query volume, reindex frequency, and cache hit rates in cost modeling.

## Verification

The selected model must pass the scorecard: retrieval recall@5 meets or exceeds the threshold on the held-out eval set, p95 latency and projected monthly cost stay under budget, vector dimensions match the index schema, and required privacy constraints are satisfied.

## Variations

- `code-search`: include exact symbol queries and repository-path filters.
- `multilingual`: score each required language separately, not just aggregate recall.
- `hybrid-rag`: choose embeddings jointly with lexical retrieval and reranking because the best standalone embedder may not be best in the final stack.

## Safety & privacy

Embedding model evaluation often sends representative documents to vendors. Use approved corpora, redact PII, record vendor and retention assumptions, and do not choose a model that requires data movement your organization has not approved.
