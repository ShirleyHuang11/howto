---
name: measure-task-accuracy
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [ai/evals/build-an-eval-set]
status: draft
last_verified: 2026-09-22
---

## Goal

You measure how often an LLM application completes its intended task correctly on a labeled eval set. The result is a reproducible score with confidence intervals and failing examples.

## Preconditions

- A versioned eval set with machine-checkable labels.
- A runnable app endpoint, CLI, or function such as `answer(input)`.
- A scorer for the task: exact match, semantic judge, schema check, or custom predicate.

## Steps

1. **Choose the scoring predicate.** Use the strictest valid scorer: exact match for deterministic labels, JSON schema plus field checks for extraction, judge rubric for open-ended answers. → *Expect:* `score(example, output)` returns pass/fail or a numeric score.
2. **Run the model at fixed settings.** Set model, prompt version, temperature, top-p, and tool configuration. ⚠️ *Data leaves your control:* confirm eval inputs are approved for the provider if calling an external API. → *Expect:* one output is saved for every eval example.
3. **Grade each output.** Execute `python run_eval.py --dataset eval.jsonl --out results.jsonl`. → *Expect:* result rows contain `id`, `passed`, `score`, `latency_ms`, and failure reason.
4. **Compute aggregate accuracy.** Report mean pass rate and Wilson confidence interval. → *Expect:* a summary such as `accuracy=0.86, 95% CI [0.80,0.91]`.
5. **Inspect failures by category.** Group by `category` and sort examples by severe or repeated failures. → *Expect:* a table showing which task slices are below threshold.

## Decision points

- Accuracy below threshold → do not ship; improve prompt, retrieval, tools, or model and rerun.
- Wide confidence interval → add more labeled examples before comparing versions.
- One category fails badly → gate on per-category thresholds, not only overall accuracy.

## Failure modes & recovery

- **F1 Flaky outputs:** detect accuracy changes across identical reruns → lower temperature or average multiple trials.
- **F2 Bad labels:** detect obviously correct outputs marked wrong → fix labels and bump dataset version.
- **F3 Scorer mismatch:** detect scorer rewards invalid behavior → add schema and safety checks before semantic scoring.
- **F4 Missing outputs:** detect fewer result rows than examples → retry failed calls and fail the run if any remain missing.

## Verification

The eval runner exits 0, writes exactly one result per dataset id, reports overall accuracy with a 95% confidence interval, and enforces the configured gate, for example `accuracy >= 0.85` and every critical category `>= 0.80`.

## Variations

- `classification`: use macro-F1 and confusion matrix in addition to accuracy.
- `extraction`: require valid JSON and field-level precision/recall.
- `agent task`: score final state plus required tool calls, not just final text.

## Safety & privacy

Accuracy evals can spend real API budget and expose eval data to providers. Use rate limits, budgets, redaction, and separate non-production credentials where possible.
