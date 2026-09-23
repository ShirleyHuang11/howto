---
name: monitor-a-training-run
domain: ai
subdomain: finetuning
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

You monitor a training or fine-tuning run with live metrics, alerts, and stop criteria. A program can detect whether the run is healthy, overfitting, stalled, or over budget.

## Preconditions

- A training job that emits metrics such as train loss, validation loss, learning rate, throughput, and cost.
- Access to logs through a provider dashboard, experiment tracker, or local files.
- A held-out validation set and budget limit.

## Steps

1. **Define health metrics and stop rules before launch.** Set thresholds for validation loss, task score, NaN loss, GPU utilization, examples/sec, and spend. → *Expect:* a config file or dashboard with numeric alert conditions.
2. **Enable structured logging.** [BRANCH: Weights & Biases | MLflow | TensorBoard | provider logs] Log run id, dataset version, model, hyperparameters, metrics, and checkpoint paths. → *Expect:* each metric event has a timestamp and global step.
3. **Track validation separately from training.** Run validation at fixed intervals and log the primary task metric, not only loss. → *Expect:* a validation curve aligned to training steps.
4. **Watch early batches closely.** Inspect the first 50-200 steps for NaNs, exploding loss, zero throughput, or tokenization errors. ⚠️ *Irreversible:* a paid training job can burn budget quickly; cancel immediately when stop rules trigger. → *Expect:* early metrics are finite and within expected ranges.
5. **Detect overfitting and checkpoint the best model.** Save checkpoints and mark the best by validation metric, not latest timestamp. → *Expect:* a best-checkpoint pointer and a validation score history.
6. **Emit alerts to the team.** Send Slack, email, or pager notifications for failed jobs, budget thresholds, NaNs, and validation regression. → *Expect:* a test alert reaches the intended channel.
7. **Write a final run report.** Export metrics, best checkpoint, cost, and pass/fail status after training ends. → *Expect:* a reproducible artifact that names the model version to promote or reject.

## Decision points

- Training loss falls but validation worsens → stop or reduce epochs; use the best validation checkpoint.
- Loss becomes NaN or infinite → stop and inspect learning rate, mixed precision, and data corruption.
- Throughput drops sharply → check data loader, storage, GPU memory, and provider incidents.
- Spend reaches the warning threshold → pause or cancel unless an owner approves continuation.
- Validation metric clears threshold early → consider early stopping to reduce overfitting and cost.

## Failure modes & recovery

- **F1 Missing validation metric:** detect logs contain only train loss → add validation and rerun before trusting the model.
- **F2 Misleading smoothed charts:** detect smoothed loss hides spikes → inspect raw metrics and alert on raw values.
- **F3 Checkpoint not saved:** detect no artifact for best step → lower save interval and verify storage permissions.
- **F4 Cost alert missing:** detect spend dashboard exceeds budget without notification → test alerts before launch.
- **F5 Data pipeline stall:** detect examples/sec near zero → restart workers, inspect storage, and resume from last checkpoint.

## Verification

Monitoring is complete when an automated check can read the run logs and confirm required fields exist for every interval, no stop rule was violated without an alert, the best checkpoint id matches the best validation metric, and total spend is below the configured budget.

## Variations

- `hosted fine-tune`: rely on provider job metrics plus your own post-training eval.
- `local GPU`: add GPU memory, utilization, temperature, and data-loader metrics.
- `distributed training`: monitor per-rank failures, gradient sync time, and checkpoint consistency.
- `LoRA`: track adapter checkpoints and base model revision together.

## Safety & privacy

Medium risk because logs can leak prompts, labels, or dataset paths and training can spend money quickly. Scrub logged examples, restrict dashboard access, set spend alerts, and require human review before promoting a checkpoint.
