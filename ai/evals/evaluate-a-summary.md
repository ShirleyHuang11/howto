---
name: evaluate-a-summary
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/evals/write-an-llm-as-judge]
status: draft
last_verified: 2026-09-22
---

## Goal

You evaluate generated summaries for factual consistency, coverage, concision, and format. The result identifies whether summaries are useful without introducing unsupported claims.

## Preconditions

- Source documents and generated summaries.
- A rubric or reference summaries for the task.
- A claim support checker or calibrated LLM judge.

## Steps

1. **Define summary requirements.** Specify max length, audience, required sections, and disallowed content. → *Expect:* a checklist the scorer can enforce.
2. **Check format deterministically.** Validate length, required headings, JSON fields, or bullet count before semantic judging. → *Expect:* format violations are caught without an LLM judge.
3. **Measure factual consistency.** Extract claims from the summary and verify each against the source. ⚠️ *Data leaves your control:* redact confidential source documents before external judge calls. → *Expect:* unsupported claims are listed with source evidence status.
4. **Score coverage.** Compare against key points from a reference summary or source-derived checklist. → *Expect:* each required point is marked present or missing.
5. **Score concision and usefulness.** Use a rubric or human review for redundancy, clarity, and audience fit. → *Expect:* a numeric score and reason per summary.
6. **Aggregate by document type.** Report factuality, coverage, and format pass rates by category. → *Expect:* weaknesses are visible for long, technical, or noisy documents.

## Decision points

- Factuality below threshold → block release even if users prefer the style.
- Coverage low but factuality high → adjust prompt or extraction plan to include required points.
- Long-document failures cluster → improve chunking or map-reduce summarization.

## Failure modes & recovery

- **F1 Unsupported claim:** detect claim not entailed by source → require citations or stricter synthesis prompt.
- **F2 Missing key point:** detect absent required fact → add key-point checklist to prompt and scorer.
- **F3 Overlong summary:** detect token or word limit exceeded → enforce max tokens and post-generation length check.
- **F4 Source truncation:** detect source length exceeds context → chunk and evaluate coverage per chunk.

## Verification

The evaluator reports deterministic format pass rate, unsupported-claim rate, key-point recall, and overall rubric score. A summary model passes only if `unsupported_claim_rate <= 0.03`, `key_point_recall >= 0.85`, and format pass rate is at least 0.95 on the held-out set.

## Variations

- `meeting summary`: include action item accuracy and owner/date extraction.
- `medical/legal`: require domain expert review and stricter factuality thresholds.
- `structured summary`: validate JSON schema before semantic scoring.

## Safety & privacy

Summaries can leak or distort sensitive source material. Preserve access controls, avoid sending confidential documents to external APIs without approval, and prioritize factual consistency over fluency.
