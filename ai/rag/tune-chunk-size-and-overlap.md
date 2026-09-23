---
name: tune-chunk-size-and-overlap
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: [ai/rag/chunk-documents-for-retrieval, ai/rag/evaluate-retrieval-quality]
status: draft
last_verified: 2026-09-22
---

## Goal

Select chunk size and overlap by measuring retrieval quality, context fit, duplication, latency, and cost across candidate configurations.

## Preconditions

- A representative corpus and labeled retrieval query set.
- A tokenizer for the embedding and generation models.
- An automated pipeline that can rebuild chunks and indexes for several configurations.

## Steps

1. **Choose candidate configurations.** Test several token sizes, such as 256, 512, and 1,024, with overlaps such as 0%, 10%, and 20%. → *Expect:* a grid of chunking configs.
2. **Rebuild chunks for each config.** Preserve identical source metadata and stable config labels. → *Expect:* each config produces a separate chunk table or index namespace.
3. **Embed and index each config.** Use the same embedding model and vector DB settings to isolate chunking effects. → *Expect:* comparable indexes exist for every config.
4. **Run retrieval evaluation.** Compute recall@k, MRR, nDCG, latency, and number of retrieved tokens. → *Expect:* metrics table by config.
5. **Measure duplication.** Calculate near-duplicate rate and repeated source-span coverage caused by overlap. → *Expect:* overlap tradeoffs are visible.
6. **Test context assembly.** Pack top chunks into the generation context and check whether answer-bearing evidence fits. → *Expect:* selected chunks fit within model context and answer budget.
7. **Pick the smallest config that meets quality.** Prefer lower cost and less duplication when metrics are tied. → *Expect:* one config is selected with evidence.

## Decision points

- Recall improves with larger chunks but precision drops → add reranking or use smaller chunks with heading context.
- Overlap improves recall marginally but doubles storage → reduce overlap.
- Long documents need different settings than FAQs → use corpus-specific chunking profiles.
- Context window overflows → reduce chunk size or limit retrieved chunks.

## Failure modes & recovery

- **F1 Comparing changed variables:** detect different embedding models or filters across configs → rerun with controlled settings.
- **F2 Duplicate dominance:** detect repeated near-identical chunks in top results → lower overlap or deduplicate at retrieval time.
- **F3 Lost context:** detect small chunks missing definitions or headings → prepend section path or increase size.
- **F4 Eval overfit:** detect config tuned to tiny query set → validate on held-out queries.

## Verification

Run a grid evaluation. Success means the chosen configuration meets recall@k and nDCG thresholds on held-out queries, has duplicate rate below the configured limit, keeps p95 retrieval latency within SLA, and assembled context stays under the generation model's token budget for at least `99%` of eval queries.

## Variations

- `technical docs`: include headings in every chunk and test smaller chunks.
- `legal or policy`: larger chunks may preserve clauses and exceptions.
- `FAQ`: short answer-sized chunks often work best with little or no overlap.

## Safety & privacy

Tuning is usually local, but rebuilding indexes can expose data to embedding providers and increase storage of sensitive text. Use sampled corpora where possible, isolate test indexes, and delete obsolete indexes after validation.
