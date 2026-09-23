---
name: measure-hallucination-rate
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/evals/build-an-eval-set]
status: draft
last_verified: 2026-09-22
---

## Goal

You estimate how often model outputs contain unsupported claims relative to trusted context or references. The final report includes a hallucination rate and examples of unsupported statements.

## Preconditions

- A dataset with inputs, model outputs, and authoritative source context or references.
- A claim extractor or judge prompt that can label claims as supported, unsupported, or not applicable.
- A policy for what counts as hallucination in your product.

## Steps

1. **Define support rules.** State that a claim is supported only if the provided context directly entails it. → *Expect:* reviewers and judge prompts use the same definition.
2. **Generate or load outputs.** Run the app with fixed settings and save outputs with source document ids. ⚠️ *Data leaves your control:* redact private context before external model calls. → *Expect:* every example has output text and retrieved context.
3. **Extract factual claims.** Use a deterministic sentence splitter plus an LLM claim extractor or manual spot check. → *Expect:* a list of atomic claims for each answer.
4. **Check claims against context.** Ask a judge model to return JSON labels per claim with cited supporting span ids, or use NLI for narrow domains. → *Expect:* each claim has `supported`, `unsupported`, or `irrelevant`.
5. **Compute hallucination rate.** Calculate examples with any unsupported claim and unsupported claims divided by total factual claims. → *Expect:* a rate table by category and retrieval source.
6. **Review severe cases.** Inspect unsupported claims that mention numbers, dates, legal/medical advice, or user-specific facts. → *Expect:* a prioritized failure list for mitigation.

## Decision points

- Unsupported rate high but retrieval recall low → fix retrieval before prompt wording.
- Unsupported rate high despite good context → require citations, abstention, or stricter answer synthesis.
- Judge disagreement high → add human adjudication and improve claim granularity.

## Failure modes & recovery

- **F1 Claim extraction misses facts:** detect long answers with few claims → sample manually and adjust extractor prompt.
- **F2 Context not included:** detect empty or wrong source ids → fix retrieval logging before scoring.
- **F3 Judge overcalls hallucination:** detect paraphrases marked unsupported → include entailment examples in rubric.
- **F4 Citation laundering:** detect citations to irrelevant spans → require span-level support, not document-level citation.

## Verification

The script emits `hallucination_examples_rate`, `unsupported_claim_rate`, and per-category rates, with valid JSON labels for at least 98% of claims. Shipping passes only if the configured threshold is met, such as `unsupported_claim_rate <= 0.05` on the held-out set.

## Variations

- `rag`: require every factual answer sentence to cite a retrieved span.
- `summarization`: compare claims against the source document only.
- `open-domain`: use trusted references and human review for high-impact samples.

## Safety & privacy

Hallucinations can cause real user harm. Apply stricter thresholds for medical, legal, financial, or user-account claims, and do not expose confidential context to external judges without approval.
