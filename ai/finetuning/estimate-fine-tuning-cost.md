---
name: estimate-fine-tuning-cost
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You estimate fine-tuning and inference cost before launching a job. The estimate includes training tokens, epochs, validation, storage, evaluation, and expected serving volume.

## Preconditions

- Training and validation files in the format required by the target provider or framework.
- Current pricing for the selected provider, GPU rental, or internal cluster chargeback.
- Expected production request volume and average input/output lengths.

## Steps

1. **Count training and validation tokens.** Use the target tokenizer when possible, such as `tiktoken`, a provider tokenizer, or the model's Hugging Face tokenizer. → *Expect:* `train_tokens`, `valid_tokens`, and token-count percentiles.
2. **Estimate billable training tokens.** Compute `train_tokens * epochs` plus any validation or minimum-job charges documented by the provider. → *Expect:* a numeric billable-token estimate.
3. **Add experiment overhead.** Include dry runs, failed runs, data generation, teacher labeling, and at least one repeated training attempt. → *Expect:* a high estimate with a multiplier such as `1.5x` or `2x`.
4. **Estimate post-training eval cost.** Count eval prompts and expected completions for every candidate model. ⚠️ *Data leaves your control:* hosted eval calls send prompts and labels to a third party; redact sensitive examples first. → *Expect:* eval cost is included separately from training cost.
5. **Estimate serving cost.** Multiply expected monthly traffic by average input/output tokens and fine-tuned model pricing or GPU serving costs. → *Expect:* monthly cost at p50 and p95 request sizes.
6. **Set a hard budget gate.** Define a maximum spend for labeling, training, eval, and serving before any paid job starts. → *Expect:* a budget number and an owner who can approve exceptions.
7. **Record assumptions with pricing date.** Store provider, region, model, pricing URL or table copy, token counts, epochs, and date. → *Expect:* a reproducible cost worksheet.

## Decision points

- Training estimate exceeds budget → reduce dataset size, lower epochs, use LoRA, or improve prompting/RAG instead.
- Serving dominates training cost → consider a smaller model, caching, routing, or distillation.
- Eval cost is large → sample strategically but preserve critical strata.
- Pricing is unclear or changes often → add a contingency multiplier and require approval before launch.
- Sensitive data is required for hosted training → include security/legal review before cost approval.

## Failure modes & recovery

- **F1 Wrong tokenizer:** detect token counts far from provider usage after a small dry run → switch to the provider-compatible tokenizer.
- **F2 Ignored output tokens:** detect serving bills exceed estimates → include generated tokens and retries in the model.
- **F3 Failed-run blind spot:** detect one failure consumes most budget → add retry overhead and use small smoke jobs.
- **F4 Minimum charge surprise:** detect provider bills a minimum job size → include documented minimums before launch.
- **F5 Evaluation omitted:** detect no cost line for held-out evals → add eval and judge-model costs to the worksheet.

## Verification

The estimate is valid when a script reads the dataset, computes token counts with the selected tokenizer, applies the recorded pricing constants, and prints total training, eval, and monthly serving estimates. The job must not launch unless `estimated_total <= approved_budget`.

## Variations

- `hosted API`: use provider training-token, validation-token, and inference prices.
- `self-hosted GPU`: estimate GPU-hours, storage, engineer time, and utilization instead of token billing.
- `distillation`: include teacher-labeling cost as a separate line item.
- `batch workload`: use batch discounts only if the workload can tolerate provider batch latency.

## Safety & privacy

Low direct operational risk because this is an estimate, but the next step may spend money or expose data. Keep pricing assumptions dated, avoid uploading sensitive files just to count tokens, and require review before any paid fine-tune starts.
