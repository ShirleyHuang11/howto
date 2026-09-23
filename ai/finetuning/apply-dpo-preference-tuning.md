---
name: apply-dpo-preference-tuning
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 4h
risk: medium
prerequisites: [ai/evals/build-a-preference-dataset]
status: draft
last_verified: 2026-09-22
---

## Goal

You use Direct Preference Optimization to tune a model toward chosen responses over rejected responses. The finished adapter or model improves preference win rate without harming safety or task accuracy.

## Preconditions

- A validated preference dataset with `prompt`, `chosen`, and `rejected` fields.
- A base or supervised fine-tuned model suitable for the preference task.
- A DPO-capable trainer such as TRL, Axolotl, or another supported stack.

## Steps

1. **Validate preference pairs.** Confirm chosen and rejected responses differ, labels are resolved, and prompt IDs do not leak across splits. → *Expect:* dataset validator reports zero invalid pairs.
2. **Choose the starting model.** [BRANCH: base model | SFT model] Prefer an SFT model when the task requires a specific format. → *Expect:* starting model passes a basic format and safety smoke eval.
3. **Set DPO parameters.** Configure beta, learning rate, batch size, max prompt length, max response length, and LoRA settings if using adapters. → *Expect:* config resolves and logs all hyperparameters.
4. **Run a smoke training job.** Train on a tiny subset for a few steps. → *Expect:* DPO loss is finite and a checkpoint is written.
5. **Run full training with validation.** Save checkpoints and evaluate preference accuracy or rewards on held-out pairs. → *Expect:* validation preference accuracy improves over the starting model.
6. **Evaluate downstream behavior.** Compare target task score, instruction following, refusal behavior, and verbosity against the starting model. → *Expect:* preference tuning does not break required behavior.
7. **Select the checkpoint.** Choose by held-out preference win rate plus regression gates, not final training loss alone. → *Expect:* selected checkpoint has a reproducible eval report.

## Decision points

- Chosen/rejected data encodes unsafe preferences → fix the dataset before training.
- DPO improves preference score but hurts correctness → lower beta, mix SFT data, or stop.
- Reward margin saturates early → use earlier checkpoint to avoid over-optimization.
- Preference data mostly covers style → do not expect factuality gains; add correctness labels.

## Failure modes & recovery

- **F1 Reversed labels:** detect model learns worse responses → sample pairs and repair labeling pipeline.
- **F2 Over-optimization:** detect verbose, evasive, or reward-hacking outputs → reduce beta or training steps.
- **F3 Length bias:** detect chosen responses are always longer → length-normalize data or add balanced pairs.
- **F4 OOM:** detect training memory errors → reduce sequence lengths or use QLoRA.
- **F5 Safety regression:** detect higher unsafe compliance → block release and add safety preference pairs.

## Verification

The DPO run passes when preference validation accuracy or win rate improves over the starting model on held-out pairs, downstream task metrics do not regress beyond the allowed threshold, safety evals pass, and the selected checkpoint loads for inference with the recorded config.

## Variations

- `TRL DPOTrainer`: use Hugging Face datasets with `prompt`, `chosen`, and `rejected` columns.
- `Axolotl DPO`: configure preference datasets and LoRA settings in YAML.
- `IPO/KTO variants`: use alternative preference objectives when pairwise DPO data is weak or unavailable.

## Safety & privacy

Preference tuning can amplify reviewer bias and unsafe shortcuts. Audit preference criteria, protect sensitive prompts, track annotator agreement, and avoid optimizing only against a judge model without human calibration.
