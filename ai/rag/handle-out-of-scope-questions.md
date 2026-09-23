---
name: handle-out-of-scope-questions
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

You detect when a user question is not answerable from your knowledge base and return a safe abstention instead of a hallucinated answer.

## Preconditions

- A RAG pipeline with retrieval scores, source metadata, and answer generation.
- An eval set containing in-scope and out-of-scope questions.
- A classifier, retrieval threshold, or answerability judge.
- A product-approved fallback message.

## Steps

1. **Define scope explicitly.** List topics, document collections, time range, and user intents your system is allowed to answer. → *Expect:* a written policy that can label eval questions as in scope or out of scope.
2. **Create an answerability eval set.** Include near-miss questions, stale-date questions, unsupported comparisons, and malicious requests. → *Expect:* balanced labeled examples with `answerable: true|false`.
3. **Collect retrieval signals.** Record top score, score gap, number of distinct sources, and whether a trusted source type appears. → *Expect:* a feature row for every eval question.
4. **Choose an abstention gate.** [BRANCH: score threshold | classifier | LLM judge] Combine retrieval thresholds with a source-only answerability check for ambiguous cases. ⚠️ *Data leaves your control:* if a hosted judge sees user queries or snippets, redact PII first. → *Expect:* every question receives `answerable`, `not_answerable`, or `needs_review`.
5. **Force grounded generation only after the gate.** If not answerable, skip answer generation and return the approved fallback. → *Expect:* out-of-scope questions never reach free-form answer generation.
6. **Tune thresholds.** Optimize for high abstention precision while keeping false refusals acceptable for your product. → *Expect:* a threshold report with false-positive and false-negative rates.
7. **Log abstentions for review.** Store query hash, decision reason, and source ids without unnecessary raw PII. → *Expect:* review dashboards show common gaps in the knowledge base.

## Decision points

- False answers are more harmful than refusals → raise the answerability threshold.
- Users complain about false refusals → add source coverage or clarify supported scope.
- Retrieval scores are poorly calibrated across indexes → route by index first and tune thresholds per index.
- Missing documents cause repeated abstentions → prioritize ingestion rather than weakening the gate.

## Failure modes & recovery

- **F1 Confident hallucination:** detect generated answers when no source supports them → block generation unless answerability passes.
- **F2 Over-refusal:** detect answerable eval questions rejected → lower thresholds or add reranking before gating.
- **F3 Stale knowledge:** detect questions requiring newer facts than indexed documents → expose source dates and abstain on outdated evidence.
- **F4 Prompt injection bypass:** detect user asks model to ignore scope rules → enforce scope checks outside the answer prompt.

## Verification

On the held-out answerability set, the gate must achieve the configured minimum out-of-scope detection recall, such as 0.95, while in-scope false refusal rate stays below the product threshold, and no out-of-scope eval item proceeds to answer generation.

## Variations

- `support-bot`: return a ticket escalation path for unsupported account-specific questions.
- `enterprise-search`: show top related documents even when refusing to synthesize an answer.
- `regulated-domain`: route `needs_review` questions to a human instead of answering.

## Safety & privacy

Abstention is a safety feature. Keep scope checks outside user-controllable prompts, avoid logging raw sensitive queries, do not answer from model memory when evidence is missing, and review threshold changes because they can silently increase hallucination risk.
