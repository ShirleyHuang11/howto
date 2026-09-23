---
name: grade-outputs-with-a-rubric
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

You grade model outputs against an explicit rubric and convert qualitative expectations into structured scores. The grading process is reproducible and can be done by humans, an LLM judge, or both.

## Preconditions

- A dataset of inputs and model outputs.
- A rubric with criteria, score ranges, and pass/fail thresholds.
- A JSON schema or spreadsheet columns for recorded grades.

## Steps

1. **Write observable criteria.** Define criteria such as correctness, completeness, grounding, format, safety, and concision with score anchors. → *Expect:* each criterion can be judged from the input, output, and references.
2. **Choose grading mode.** [BRANCH: human | LLM judge | hybrid] Decide who grades each criterion and when human adjudication is required. → *Expect:* a grading plan with reviewer or model assignment.
3. **Create structured grade fields.** Use fields like `correctness_score`, `safety_pass`, `format_errors`, and `rationale`. → *Expect:* grades validate against schema.
4. **Run a pilot.** Grade a small sample and compare results across graders. ⚠️ *Data leaves your control:* external LLM graders or contractors must receive only approved data. → *Expect:* ambiguous rubric items are revised.
5. **Grade the full set.** Execute the judge script or collect human labels with required fields. → *Expect:* one complete grade record per output.
6. **Aggregate and gate.** Compute weighted overall score and hard-fail criteria such as safety or factuality. → *Expect:* outputs pass only when both total and hard criteria meet thresholds.

## Decision points

- Criteria disagree often → split or rewrite the ambiguous criterion.
- Overall score passes but safety fails → fail the output regardless of average.
- LLM judge and humans diverge → recalibrate judge or use human labels for the decision.

## Failure modes & recovery

- **F1 Vague rubric:** detect inconsistent grades → add anchors and examples for each score level.
- **F2 Average hides severe flaw:** detect unsafe answer with high total score → add hard-fail gates.
- **F3 Invalid grade records:** detect missing fields or wrong types → validate schema before aggregation.
- **F4 Grader drift:** detect changing standards over time → keep calibration examples in every batch.

## Verification

The grading pipeline validates every grade record, reports per-criterion averages, hard-fail counts, inter-grader agreement when applicable, and final pass/fail. A run passes only if required hard criteria have zero critical failures and the weighted score meets the configured threshold.

## Variations

- `human`: slower but best for nuanced or high-impact evaluation.
- `LLM judge`: scalable after calibration against human labels.
- `hybrid`: use LLM for first pass and humans for low-confidence or high-risk cases.

## Safety & privacy

Rubric grades may include sensitive source text and model failures. Redact before external grading, keep rationales factual, and do not let a high average score override safety or privacy failures.
