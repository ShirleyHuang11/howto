---
name: build-a-basic-rag-pipeline
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/rag/chunk-documents-for-retrieval, ai/rag/generate-text-embeddings, ai/rag/do-semantic-search]
status: draft
last_verified: 2026-09-22
---

## Goal

Build a basic retrieval-augmented generation pipeline that retrieves source chunks, answers only from those chunks, and verifies citations and answer quality.

## Preconditions

- A chunked and embedded corpus with a working semantic search endpoint.
- An LLM API client or local chat model.
- A labeled question set with expected sources or answers for evaluation.

## Steps

1. **Define the request contract.** Accept a user question, tenant or access context, and optional metadata filters. → *Expect:* invalid or unauthorized requests are rejected before retrieval.
2. **Retrieve candidate chunks.** Run semantic search with top `k` and access filters, then optionally rerank. → *Expect:* a ranked context list with source IDs and scores.
3. **Build the generation prompt.** Delimit retrieved chunks, include source IDs, and instruct the model to answer only from provided context. → *Expect:* prompt contains no untrusted instructions outside the context delimiter.
4. **Generate the answer.** [BRANCH: Anthropic | OpenAI | open model] Ask for an answer plus citations to source IDs. ⚠️ *Data leaves your control:* retrieved chunks and the user question are sent to the model provider unless using a local model. → *Expect:* a response with answer text and cited chunk IDs.
5. **Validate citations.** Check that cited IDs exist in the retrieved context and that every factual sentence has at least one citation. → *Expect:* unsupported citations are rejected.
6. **Handle insufficient context.** If retrieval scores are too low or no chunk supports the question, return a grounded no-answer response. → *Expect:* the system refuses rather than hallucinating.
7. **Evaluate end to end.** Score retrieval recall, answer correctness, citation validity, latency, and cost. → *Expect:* a report with launch thresholds.

## Decision points

- Retrieval recall is low → fix retrieval before prompt tuning.
- Answer correct but citations invalid → improve citation validation and prompt format.
- Context contains conflicting sources → answer with the conflict and cite both, or route to review.
- Cost or latency is too high → reduce `k`, use reranking, cache, or choose a smaller model.

## Failure modes & recovery

- **F1 Hallucinated answer:** detect claims absent from retrieved chunks → reject and regenerate with stricter grounding.
- **F2 Citation fabrication:** detect cited IDs not in context → fail validation and retry once.
- **F3 Prompt injection in documents:** detect chunks instructing the model to ignore rules → wrap chunks as untrusted data and keep system rules separate.
- **F4 Stale index:** detect answer cites outdated content → refresh changed documents and include freshness metadata.

## Verification

Run the RAG pipeline on an evaluation set. Success means retrieval recall@k meets threshold, `100%` of cited source IDs are present in retrieved context, unsupported-claim rate is below the configured limit, no-answer cases are correctly refused, and p95 latency plus cost per query stay within budget.

## Variations

- `enterprise search`: enforce tenant and document ACL filters at retrieval time.
- `customer support`: add escalation when confidence is low or policy content is missing.
- `local model`: keep data in your environment but evaluate answer quality separately.

## Safety & privacy

RAG sends user questions and retrieved internal text to the generator unless fully local. Redact sensitive data where possible, apply authorization before generation, defend against prompt injection in retrieved text, and require review before using answers for high-impact decisions.
