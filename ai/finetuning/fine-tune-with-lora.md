---
name: fine-tune-with-lora
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 4h
risk: medium
prerequisites: [ai/finetuning/format-chat-fine-tuning-data]
status: draft
last_verified: 2026-09-22
---

## Goal

You train a parameter-efficient LoRA adapter for a local or open-weight model and save an adapter that improves a held-out metric. The run is reproducible from config, dataset hashes, and evaluation output.

## Preconditions

- An open-weight base model license that permits your use case.
- Formatted train and validation data.
- A GPU environment with PyTorch, Transformers, PEFT, TRL or Axolotl, and enough VRAM for the chosen quantization.

## Steps

1. **Choose the base checkpoint and precision.** [BRANCH: LoRA | QLoRA] Use full or 8-bit loading for LoRA, and 4-bit NF4 for QLoRA when VRAM is tight. → *Expect:* a model loads and a single validation prompt runs before training.
2. **Write the training config.** Set `lora_r`, `lora_alpha`, target modules, learning rate, batch size, gradient accumulation, max sequence length, and eval cadence. → *Expect:* the config file is checked into the run directory and resolves without unknown keys.
3. **Tokenize with the model chat template.** Render conversations exactly as inference will see them. → *Expect:* tokenized examples have labels masked for prompt tokens when using supervised fine-tuning.
4. **Launch a small smoke run.** Train for 10-50 steps on a subset before the full run. → *Expect:* loss decreases or stays finite, no CUDA OOM occurs, and an adapter checkpoint is written.
5. **Run the full training job.** Save checkpoints and evaluation metrics at fixed intervals. → *Expect:* training completes with final adapter files such as `adapter_config.json` and `adapter_model.safetensors`.
6. **Evaluate against the base model.** Run the same held-out eval for base and LoRA-adapted model. → *Expect:* the adapter improves the target metric without safety or format regressions.
7. **Package the adapter.** Save config, dataset hashes, base model ID, training command, and eval report. → *Expect:* another machine can load the adapter with the same base model.

## Decision points

- Smoke run OOMs → reduce sequence length, batch size, or switch to QLoRA.
- Validation loss worsens while training loss drops → stop early and inspect overfitting.
- Adapter improves style but hurts factuality → reduce epochs or improve data quality.
- License forbids commercial use → choose another base model before training.

## Failure modes & recovery

- **F1 CUDA OOM:** detect allocator errors → lower batch size, enable gradient checkpointing, or quantize.
- **F2 NaN loss:** detect non-finite loss → lower learning rate, inspect bad rows, and disable unstable precision settings.
- **F3 Chat template mismatch:** detect good eval during training but bad inference → use the same tokenizer template at train and serve time.
- **F4 Overfit adapter:** detect validation loss rising and memorized outputs → stop earlier and add more diverse data.
- **F5 Broken checkpoint:** detect missing adapter files → resume from previous checkpoint and verify save permissions.

## Verification

The adapter directory loads with the declared base model, a smoke inference returns a valid response, validation loss is finite, and the held-out eval improves the target metric by the documented threshold, such as `instruction_pass_rate >= base + 0.03`, with no category regression above the allowed limit.

## Variations

- `Axolotl`: define LoRA and dataset settings in YAML and run `axolotl train config.yml`.
- `TRL SFTTrainer`: use Python config and PEFT objects directly.
- `multi-adapter serving`: keep adapters separate and route by task instead of merging immediately.

## Safety & privacy

Training can encode private data into weights or adapters. Use approved datasets only, keep base model license records, monitor GPU spend, and do not publish adapters trained on confidential data without review.
