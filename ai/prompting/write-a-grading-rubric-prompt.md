---
name: write-a-grading-rubric-prompt
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You write a rubric prompt that makes an LLM judge outputs consistently, with structured scores that correlate with human labels.

## Preconditions

- A task with outputs to grade and a definition of quality.
- Human-labeled calibration examples.
- A schema for judge results, such as scores, reasons, and pass/fail labels.

## Steps

1. **Define criteria independently.** Write 3-6 criteria such as correctness, completeness, groundedness, format, and safety. → *Expect:* each criterion has a clear pass/fail or numeric scale.
2. **Anchor the scale.** Describe what each score means and include at least one calibration example per boundary. → *Expect:* humans can apply the rubric without guessing.
3. **Require evidence-based grading.** Tell the judge to cite specific output spans or reference facts, not vibes. → *Expect:* judge output includes reasons tied to criteria.
4. **Use structured judge output.** Return JSON with criterion scores, overall score, and decision. → *Expect:* judge responses parse and validate.
5. **Calibrate against human labels.** Run the judge on labeled examples. ⚠️ *Data leaves your control:* if examples contain private user text and the judge is external, redact or approve first. → *Expect:* agreement statistics such as accuracy, correlation, or Cohen's kappa.
6. **Set a decision threshold.** Choose the minimum score for pass, ship, or human review. → *Expect:* threshold performance is documented on calibration data.

## Decision points

- Judge-human agreement is low → clarify criteria and add calibration anchors.
- The judge is grading its own model family → add human review or cross-model judging for critical decisions.
- Scores drive user-visible or employment/credit decisions → do not rely on an LLM judge alone.

## Failure modes & recovery

- **F1 Lenient judge:** detect high pass rate on known bad outputs → add negative anchors and stricter thresholds.
- **F2 Format failure:** detect invalid JSON → use structured output and schema validation.
- **F3 Position bias:** detect preference for first candidate → randomize candidate order and blind identifiers.
- **F4 Unsupported rationale:** detect reasons not tied to text → require quoted spans or evidence ids.

## Verification

Run `python calibrate_judge.py --rubric rubric_prompt.md --examples human_labeled.jsonl --min-kappa 0.70 --min-parse-rate 0.98`; the judge must parse at least 98% of responses and reach kappa or equivalent agreement of at least 0.70 with human labels.

## Variations

- `pairwise judge`: ask which output is better and why, then randomize order.
- `absolute score`: use a fixed rubric for regression tracking.
- `safety judge`: bias toward recall and route uncertain cases to humans.

## Safety & privacy

Medium risk when judge results affect people or production gates. Keep calibration data protected, avoid using LLM judgment as the only authority for high-impact decisions, and monitor for bias and drift.
