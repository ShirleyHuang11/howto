---
name: write-an-llm-as-judge
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

You build an LLM judge that scores outputs against a rubric and returns structured, validated grades. The judge is calibrated against human labels before it is trusted.

## Preconditions

- An eval set with inputs, candidate outputs, and at least 30 human-labeled examples.
- API access to a capable judge model [BRANCH: Claude Sonnet | OpenAI | open model].
- A JSON schema for judge output, such as `{"score": 0..1, "reason": string, "errors": string[]}`.

## Steps

1. **Write the rubric.** Define 3-5 criteria with observable evidence and scoring anchors. → *Expect:* a rubric a second reviewer can apply consistently.
2. **Build a structured judge prompt.** Include task, input, reference answer if available, candidate answer, rubric, and required JSON output only. → *Expect:* judge responses parse as JSON in dry runs.
3. **Call the judge on calibration examples.** ⚠️ *Data leaves your control:* redact confidential inputs before sending them to an external judge API. → *Expect:* one JSON grade per example with no free-form trailing text.
4. **Validate and repair invalid output.** Use `jsonschema.validate()` and retry once with the validation error if parsing fails. → *Expect:* invalid JSON rate is below 2% after retry.
5. **Measure agreement with humans.** Compute Spearman correlation for scores and Cohen's kappa for pass/fail at the shipping threshold. → *Expect:* correlation and kappa are high enough for the risk level, commonly `rho >= 0.75` and `kappa >= 0.6`.
6. **Lock the judge version.** Save prompt, model id, schema, temperature, and calibration metrics. → *Expect:* future eval runs use a reproducible judge configuration.

## Decision points

- Agreement with humans is low → tighten rubric, add examples, or split one broad criterion into separate checks.
- Invalid JSON persists → use provider-native structured outputs or function/tool calling.
- Judge favors verbosity → add an explicit concision criterion and negative examples.

## Failure modes & recovery

- **F1 Position bias:** detect first candidate wins unusually often → randomize answer order and hide model names.
- **F2 Reference overfitting:** detect valid alternative answers marked wrong → revise rubric to allow equivalent evidence.
- **F3 JSON parse failure:** detect parser exceptions → enforce schema mode or retry with the exact validation error.
- **F4 Judge drift:** detect changed grades after a model update → pin model version where available and rerun calibration.

## Verification

The judge script produces valid JSON for 98% or more examples after one retry, reaches `Spearman rho >= 0.75` with human numeric scores, and reaches `Cohen kappa >= 0.6` on pass/fail labels against the calibration set.

## Variations

- `pairwise`: return `winner`, `confidence`, and `reason`, then aggregate win rates.
- `reference-free`: grade only against rubric and source context, not an answer key.
- `local model`: expect lower reliability; require a larger human calibration set.

## Safety & privacy

Do not send proprietary prompts, customer content, or source documents to a third-party judge without approval and redaction. A judge is an evaluator, not ground truth; keep human review for high-impact decisions.
