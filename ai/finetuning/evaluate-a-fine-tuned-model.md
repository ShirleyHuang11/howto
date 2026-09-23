---
name: evaluate-a-fine-tuned-model
domain: ai
subdomain: finetuning
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

You verify that a fine-tuned model improves the target task without damaging safety, format, latency, or cost. The result is a comparison report against the base model and previous production model.

## Preconditions

- The fine-tuned model or adapter is available for inference.
- Held-out evals cover target behavior, regressions, and safety cases.
- A baseline model run with the same prompts and scoring code.

## Steps

1. **Freeze the evaluation config.** Record prompts, decoding parameters, model IDs, adapter IDs, and eval dataset hashes. → *Expect:* reruns use identical inputs and settings.
2. **Run target-task evals.** Measure accuracy, instruction adherence, reference score, or task-specific pass rate. → *Expect:* the fine-tuned model has per-category metrics.
3. **Run regression evals.** Include general helpfulness, refusal boundaries, formatting, and tasks the base model already handled. → *Expect:* any category drop is visible in the report.
4. **Run safety and privacy probes.** Test prompt injection, memorization canaries, secret extraction, and unsafe-request handling. → *Expect:* the model refuses or safely handles all required cases.
5. **Measure serving behavior.** Compare latency, throughput, context handling, and cost to baseline. → *Expect:* p50/p95 latency and cost per 1,000 requests are reported.
6. **Inspect failures.** Sample wins and losses by category and identify whether data, hyperparameters, or prompt wrapper caused them. → *Expect:* a failure analysis file links each issue to a remediation.
7. **Apply the release gate.** Require target improvement plus no unacceptable regressions. → *Expect:* CI or the eval runner returns pass/fail.

## Decision points

- Target metric improves but safety regresses → do not deploy; fix data or training.
- Fine-tune only improves cases similar to train data → expand held-out evals and check overfitting.
- Latency or cost exceeds budget → quantize, use a smaller base model, or route selectively.
- Base model beats fine-tune → keep the base model and revisit the dataset.

## Failure modes & recovery

- **F1 Eval leakage:** detect training examples in held-out eval → rebuild eval set and rerun.
- **F2 Format regression:** detect invalid JSON or missing tool calls → add format-specific eval and training examples.
- **F3 Safety regression:** detect refusal bypass or unsafe compliance → block deployment and add safety data.
- **F4 Memorization:** detect canary or training text reproduction → remove sensitive data and retrain with privacy review.
- **F5 Non-comparable runs:** detect different decoding parameters → rerun all models with identical settings.

## Verification

The model passes only if the held-out target metric improves by the required margin, all required safety probes pass, structured outputs validate, latency and cost stay under budget, and the report includes base, fine-tuned, and previous-production comparisons from the same eval config.

## Variations

- `hosted fine-tune`: use provider model IDs and batch eval APIs for comparison.
- `LoRA adapter`: evaluate both adapter-loaded and base-only paths on the same server.
- `classification fine-tune`: include calibration, confusion matrix, and threshold selection.

## Safety & privacy

Do not deploy a fine-tuned model based only on training loss. Treat memorization, unsafe compliance, and private-data leakage as blockers, and restrict access to eval artifacts that contain sensitive prompts or outputs.
