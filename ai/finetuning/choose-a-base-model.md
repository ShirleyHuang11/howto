---
name: choose-a-base-model
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

You select a base model that fits the task, license, context length, serving budget, and fine-tuning method. The decision is backed by a small benchmark rather than popularity alone.

## Preconditions

- A task description, expected languages, latency target, and quality threshold.
- Candidate hosted or open-weight models with documented licenses.
- A small representative eval set and serving-cost estimate.

## Steps

1. **List hard constraints.** Record context length, modality, tool-use needs, deployment environment, latency, privacy, and license requirements. → *Expect:* candidates that violate hard constraints are removed.
2. **Shortlist candidate models.** [BRANCH: hosted fine-tune | open model] Include at least one strong hosted model and one open-weight model when privacy or cost matters. → *Expect:* a table with model ID, context length, license, fine-tuning support, and estimated cost.
3. **Run baseline inference.** Evaluate candidates without fine-tuning on 50-200 representative examples. ⚠️ *Data leaves your control:* hosted candidates receive eval prompts, so redact sensitive fields first. → *Expect:* each candidate has quality, latency, and cost metrics.
4. **Check tokenizer and format fit.** Verify the model handles your languages, chat template, special tokens, and structured output needs. → *Expect:* sample outputs parse in the required format.
5. **Estimate fine-tuning feasibility.** Confirm trainer support, GPU memory, parameter-efficient method, and maximum example length. → *Expect:* each candidate has a feasible or rejected training path.
6. **Pick the smallest model that clears the bar.** Prefer lower latency and cost when quality is within the acceptable margin. → *Expect:* a written decision with runner-up and rejection reasons.
7. **Freeze the model identifier.** Record exact provider model ID or open-weight checkpoint revision. → *Expect:* training config uses an immutable model reference where possible.

## Decision points

- Data cannot leave your environment → choose an open-weight model and local training/serving.
- Prompt-only baseline already meets the target → skip fine-tuning and improve prompts or evals instead.
- Small model fails on reasoning-heavy cases → test a larger candidate before tuning.
- License terms are unclear → stop until legal or policy review resolves them.

## Failure modes & recovery

- **F1 License mismatch:** detect noncommercial or restricted terms for a commercial product → choose a permissive model or hosted option with suitable terms.
- **F2 Context mismatch:** detect eval inputs exceed model context → select longer context or redesign the task.
- **F3 Benchmark contamination:** detect public benchmark overlap with training data → use private representative evals.
- **F4 Hidden serving cost:** detect acceptable training cost but excessive inference cost → benchmark throughput and quantization options.
- **F5 Unsupported trainer:** detect no fine-tuning path for the model/provider → switch candidate or serving stack.

## Verification

The chosen base model must satisfy every hard constraint, pass the baseline eval or be the best feasible candidate by documented metrics, have an approved license, load successfully in the intended trainer or provider, and produce outputs that validate against the target format on smoke prompts.

## Variations

- `hosted provider`: prioritize data policy, fine-tuning limits, and production SLA.
- `open model`: prioritize license, checkpoint quality, tokenizer fit, and GPU serving cost.
- `edge deployment`: prioritize quantization support, memory footprint, and latency on target hardware.

## Safety & privacy

Model choice determines where data goes and what terms bind the product. Review licenses, hosted data retention, export controls, and privacy constraints before moving beyond evaluation.
