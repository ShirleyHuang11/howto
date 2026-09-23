---
name: evaluate-a-rag-system
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/evals/build-an-eval-set, ai/evals/measure-hallucination-rate]
status: draft
last_verified: 2026-09-22
---

## Goal

You evaluate a retrieval-augmented generation system across retrieval quality, answer correctness, citation support, latency, and cost. The result shows whether failures come from retrieval or generation.

## Preconditions

- A RAG app with logged retrieved chunk ids and final answers.
- An eval set with queries, gold document or chunk ids, and answer labels or rubric.
- Access to the vector index and retrieval configuration.

## Steps

1. **Measure retrieval recall.** For each query, check whether gold chunks appear in top `k`. → *Expect:* metrics such as `recall@3`, `recall@10`, and MRR.
2. **Measure context precision.** Count retrieved chunks that are relevant versus distracting. → *Expect:* a precision table by retriever, reranker, and category.
3. **Generate answers with logged context.** Run the RAG pipeline and store query, retrieved ids, answer, citations, tokens, and latency. ⚠️ *Data leaves your control:* external LLM calls receive retrieved context, so redact or restrict sensitive corpora. → *Expect:* complete traces for every eval query.
4. **Grade answer correctness.** Use exact checks where possible and a calibrated judge for open answers. → *Expect:* each answer has a correctness score and failure reason.
5. **Verify citation support.** Check that cited chunks actually support the claims they are attached to. → *Expect:* unsupported or missing citations are counted.
6. **Break down failures.** Label each failure as retrieval miss, bad context selection, generation error, or citation error. → *Expect:* remediation points to the right subsystem.

## Decision points

- Low recall@k → improve chunking, embedding model, metadata filters, or hybrid retrieval.
- High recall but low answer accuracy → improve prompt, reranking, or answer synthesis.
- Good answers but bad citations → enforce citation-span validation before returning.

## Failure modes & recovery

- **F1 Index drift:** detect eval gold ids missing from index → rebuild or update gold ids with provenance.
- **F2 Metadata filter bug:** detect relevant chunks excluded by filters → test filter logic separately.
- **F3 Context stuffing:** detect too many irrelevant chunks → add reranker or reduce top-k.
- **F4 Hallucinated citation:** detect cited chunk does not support claim → fail answer and tune citation prompt.

## Verification

The RAG eval reports `recall@k`, MRR, answer accuracy, citation support rate, unsupported claim rate, p95 latency, and cost. The system passes only if retrieval and answer gates both pass, for example `recall@5 >= 0.9`, `answer_accuracy >= 0.8`, and `citation_support >= 0.95`.

## Variations

- `hybrid search`: report dense, sparse, and combined retrieval metrics separately.
- `hosted vector DB`: include index namespace and metadata filter version.
- `agentic RAG`: score query rewriting and multi-step retrieval traces too.

## Safety & privacy

Retrieved context may contain proprietary or user data. Enforce document permissions before retrieval, redact sensitive snippets in logs, and never let retrieved text override system instructions.
