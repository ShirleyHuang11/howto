---
name: score-outputs-against-a-reference
domain: ai
subdomain: evals
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

You compare model outputs to trusted references using metrics appropriate to the task. The result is a reproducible score report that identifies exact, semantic, and safety failures.

## Preconditions

- A dataset with `input`, `reference`, and model `output` fields.
- Metric code for the task, such as exact match, F1, ROUGE/BERTScore, JSON validation, or an LLM judge with a rubric.
- A held-out set that was not used to tune the prompt or model.

## Steps

1. **Classify the answer type.** Decide whether each task is exact, structured, extractive, abstractive, or open-ended. → *Expect:* each row has a `metric_family` value.
2. **Normalize outputs and references.** Apply task-safe normalization such as whitespace trimming, case folding for labels, or JSON key ordering. → *Expect:* normalization is deterministic and logged.
3. **Run deterministic metrics first.** Use exact match for labels, numeric tolerance for calculations, JSON Schema for structured answers, and token F1 for extractive spans. → *Expect:* every row receives at least one non-judge score.
4. **Add semantic judging only where needed.** [BRANCH: Anthropic | OpenAI | local judge] Use a rubric and require the judge to emit JSON with `score` and `reason`. ⚠️ *Data leaves your control:* references and outputs sent to hosted judges may contain sensitive data, so redact or use local judging. → *Expect:* judge responses parse as JSON and stay within the allowed score range.
5. **Calibrate against human labels.** Compare judge or semantic metrics on a reviewed subset. → *Expect:* correlation or agreement with humans meets the documented threshold.
6. **Aggregate with confidence intervals.** Report mean score, pass rate, bootstrap confidence interval, and category breakdowns. → *Expect:* the report includes metric values plus sample counts.
7. **Save failures for review.** Export low-scoring rows with input, reference, output, and metric reasons. → *Expect:* a failure file can be opened without recomputing the eval.

## Decision points

- Exact metric is too harsh for valid paraphrases → add semantic scoring but keep exact scores visible.
- Judge-human agreement is low → revise rubric or avoid judge-based release gates.
- Numeric answers fail due to formatting → parse numbers and use tolerance rather than string match.
- High mean score hides a bad category → set per-category minimums.

## Failure modes & recovery

- **F1 Reference error:** detect a model output that is correct but marked wrong → fix the reference and rerun the full eval.
- **F2 Judge drift:** detect score changes with the same inputs after model updates → pin judge model/version and keep calibration rows.
- **F3 JSON parse failure:** detect malformed judge output → retry with constrained output and count unrepaired failures.
- **F4 Metric mismatch:** detect summaries rewarded for copying despite poor usefulness → add factuality and coverage checks.
- **F5 Data leakage:** detect examples used during prompt tuning in the held-out set → remove and rebuild the split.

## Verification

The scoring job succeeds only when all rows have parsed metric results, judge JSON validates when a judge is used, human-calibrated agreement is at least the documented threshold, and the final pass rate meets the release gate, such as `score >= 0.80` with no category below `0.70`.

## Variations

- `classification`: use exact match, macro F1, and confusion matrices.
- `summarization`: combine coverage, factuality checks, and calibrated human or judge ratings.
- `structured extraction`: validate JSON Schema and compare normalized fields individually.

## Safety & privacy

References may contain gold answers, private records, or proprietary material. Restrict access, redact before hosted judging, and track cost because judge-based scoring can multiply API spend across every eval row.
