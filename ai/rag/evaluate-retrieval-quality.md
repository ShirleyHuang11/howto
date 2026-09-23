---
name: evaluate-retrieval-quality
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

Measure retrieval quality with labeled queries and ranking metrics so changes to chunking, embeddings, indexing, or reranking can be accepted or rejected objectively.

## Preconditions

- A retrieval system that returns ranked chunk IDs and metadata.
- A labeled evaluation set mapping queries to relevant chunk IDs, documents, or source spans.
- A script or notebook that can compute recall@k, MRR, nDCG, and latency.

## Steps

1. **Build a representative query set.** Include common questions, rare edge cases, exact identifiers, paraphrases, and no-answer queries. → *Expect:* an eval file with query IDs and labels.
2. **Define relevance granularity.** Decide whether a relevant hit is a chunk, document, page, or span, and map labels accordingly. → *Expect:* scoring code knows how to match retrieved IDs to gold labels.
3. **Run retrieval deterministically.** Use fixed index version, embedding model, filters, and top `k` for every query. → *Expect:* a result file with ranked IDs, scores, and latency.
4. **Compute ranking metrics.** Calculate recall@k, precision@k, MRR, nDCG@k, and no-answer false-positive rate. → *Expect:* metrics are reported overall and by query slice.
5. **Inspect failures by slice.** Group misses by document type, language, query length, and exact-vs-semantic intent. → *Expect:* the likely failure cause is visible.
6. **Compare against a baseline.** Run the previous production configuration or a saved baseline on the same eval set. → *Expect:* deltas show whether the change improved retrieval.
7. **Set launch gates.** Require minimum recall and latency thresholds before using retrieval for RAG answers. → *Expect:* a machine-readable pass/fail report.

## Decision points

- Labels are incomplete → use pooled judging or sample manual review before trusting precision.
- Recall@k is high but answer quality is low → inspect reranking, context assembly, and generation.
- No-answer false positives are high → add score thresholds or abstention logic.
- New config improves average but hurts a critical slice → do not ship until the slice is addressed.

## Failure modes & recovery

- **F1 Leaky eval set:** detect queries copied from training prompts or tuning data → create a held-out set.
- **F2 Wrong gold granularity:** detect relevant document but different chunk counted wrong → adjust matching rules intentionally.
- **F3 Flaky index version:** detect metrics changing without code changes → pin index and model versions.
- **F4 Incomplete labels:** detect many apparently relevant unlabelled hits → expand labels using pooled results.

## Verification

The evaluation job must produce a pass/fail artifact. Success means all queries have scored results, recall@k and nDCG@k meet configured thresholds, p95 latency is under SLA, no-answer false-positive rate is below threshold, and the candidate configuration does not regress critical slices versus baseline.

## Variations

- `RAG QA`: label answer-bearing chunks and score recall@context_k.
- `search product`: include click or human relevance grades and optimize nDCG.
- `multitenant corpus`: evaluate with access filters and tenant-specific query sets.

## Safety & privacy

Eval queries and labels may contain real user needs or confidential document references. Store them securely, scrub PII where possible, and avoid sending sensitive eval data to external judge models without approval.
