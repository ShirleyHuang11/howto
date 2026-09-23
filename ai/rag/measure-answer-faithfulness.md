---
name: measure-answer-faithfulness
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

You measure whether generated answers are supported by retrieved evidence and block regressions before deployment.

## Preconditions

- A set of question, retrieved-context, answer triples from your RAG system.
- Gold labels or a reviewed sample for calibration.
- A faithfulness evaluator: entailment model, LLM-as-judge rubric, or claim-level checker.
- Stored source ids and answer citations.

## Steps

1. **Define faithfulness.** Write a rubric that marks an answer faithful only when all factual claims are supported by the provided context. → *Expect:* a binary or numeric score definition reviewers can apply consistently.
2. **Split answers into claims.** Use deterministic sentence splitting or an LLM claim extractor that outputs JSON claims. [BRANCH: rule-based | LLM extractor] → *Expect:* each answer has a list of atomic factual claims.
3. **Check each claim against evidence.** Run entailment or a judge prompt that sees only the claim and retrieved context. ⚠️ *Data leaves your control:* external judges receive answers and source text; redact sensitive data or use a local judge. → *Expect:* each claim is labeled `supported`, `unsupported`, or `not_enough_info`.
4. **Aggregate to an answer score.** Compute `faithfulness = supported_claims / total_factual_claims` and mark answers with any critical unsupported claim as failing. → *Expect:* one numeric score and one pass/fail label per answer.
5. **Calibrate the evaluator.** Compare judge labels with human labels on a sample and adjust prompts or thresholds. → *Expect:* evaluator agreement reaches your target, such as Cohen's kappa >= 0.6 or judge accuracy >= 0.85.
6. **Add regression gates.** Run the evaluator in CI or pre-release evals and fail when mean faithfulness or unsupported-claim rate regresses. → *Expect:* a machine-readable report blocks bad builds.
7. **Inspect failures.** Group unsupported claims by missing retrieval, answer hallucination, stale index, and bad citation. → *Expect:* each failure has a fix owner in retrieval, generation, or data.

## Decision points

- Low faithfulness with relevant evidence present → tighten answer prompt or add claim-level regeneration.
- Low faithfulness because evidence is missing → fix retrieval, chunking, or routing.
- Judge disagrees with humans → improve calibration or use human review for critical domains.
- Faithfulness high but usefulness low → add separate answer-quality and completeness metrics.

## Failure modes & recovery

- **F1 Judge leniency:** detect unsupported claims marked supported → add adversarial examples and require quoted evidence spans.
- **F2 Claim extraction misses hedges:** detect complex sentences scored incorrectly → split into atomic claims and preserve negation.
- **F3 Context contamination:** detect evaluator using outside knowledge → use prompts that forbid external knowledge and test impossible claims.
- **F4 Metric gaming:** detect answers becoming vague to pass faithfulness → pair faithfulness with completeness and answer relevance scores.

## Verification

The eval pipeline must output valid JSON per answer, achieve the calibrated judge agreement target on a human-labeled sample, and report mean faithfulness above the release threshold with unsupported critical claims below the allowed maximum.

## Variations

- `entailment-model`: faster and cheaper for short claims with clear evidence.
- `llm-judge`: better for nuanced business text but needs calibration and cost controls.
- `citation-aware`: score only claims against their cited sources, not the whole retrieved context.

## Safety & privacy

Faithfulness evals may process production questions, answers, and source text. Sample and redact logs carefully, avoid sending sensitive documents to third-party judges without approval, and treat evaluator outputs as risk signals rather than absolute truth in high-impact domains.
