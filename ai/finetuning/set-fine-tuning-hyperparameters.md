---
name: set-fine-tuning-hyperparameters
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/finetuning/choose-a-base-model]
status: draft
last_verified: 2026-09-22
---

## Goal

You choose fine-tuning hyperparameters that are stable, cost-aware, and matched to dataset size. The result is a config with explicit defaults, sweep bounds, and early-stop criteria.

## Preconditions

- A selected base model and formatted train/validation data.
- A target eval metric and maximum training budget.
- Knowledge of the training method, such as hosted SFT, LoRA, QLoRA, full fine-tune, or DPO.

## Steps

1. **Start from conservative defaults.** Use low learning rates for full fine-tunes, moderate rates for LoRA, and 1-3 epochs for most instruction datasets. → *Expect:* a first-run config that is unlikely to destroy base behavior.
2. **Set effective batch size.** Choose per-device batch size and gradient accumulation to reach a stable effective batch without OOM. → *Expect:* a smoke run logs the intended effective batch size.
3. **Set sequence length from data.** Use p95 token length when possible and cap outliers rather than blindly using max context. → *Expect:* token report shows the retained percentage and truncation rate.
4. **Configure evaluation cadence.** Evaluate often enough to catch overfitting and save the best checkpoint by validation metric. → *Expect:* training logs include validation metrics at planned intervals.
5. **Bound the sweep.** Try a small grid over learning rate, epochs, LoRA rank, and weight decay before larger runs. → *Expect:* each run has a unique config hash and budget estimate.
6. **Add early stopping.** Stop when validation metric fails to improve for a set patience or safety regressions appear. → *Expect:* runs can terminate before the maximum epoch count.
7. **Record final hyperparameters.** Save the winning config with dataset hash, base model ID, and eval report. → *Expect:* the selected config is reproducible from the run directory.

## Decision points

- Validation loss rises early → lower learning rate or reduce epochs.
- Training loss does not move → increase learning rate slightly, inspect labels, or unfreeze/target more modules.
- OOM during smoke test → reduce batch size, sequence length, or precision.
- Fine-tuned model forgets general behavior → reduce update strength or use more mixed data.

## Failure modes & recovery

- **F1 Too high learning rate:** detect loss spikes or NaNs → lower by 2-10x and resume from base.
- **F2 Undertraining:** detect no validation improvement and flat loss → increase steps or LoRA capacity after checking data quality.
- **F3 Overfitting:** detect training loss down while validation metric worsens → stop earlier, add data, or regularize.
- **F4 Truncation damage:** detect missing answer fields after token cap → adjust packing or shorten inputs.
- **F5 Untracked sweep:** detect run folders without configs → require config hashes before launching.

## Verification

A smoke run completes without OOM or NaN, the full config records effective batch size and token limits, validation metrics are logged at least twice, and the selected run beats the baseline eval threshold while staying inside the declared cost and time budget.

## Variations

- `LoRA/QLoRA`: tune rank, alpha, target modules, dropout, and quantization settings.
- `full fine-tune`: use smaller learning rates and stronger checkpointing.
- `hosted fine-tuning`: use provider-supported knobs and rely on validation files plus post-training evals.

## Safety & privacy

Hyperparameter sweeps can spend money quickly. Cap the number of runs, use small smoke tests first, and avoid uploading sensitive datasets to hosted trainers without the same review required for the final run.
