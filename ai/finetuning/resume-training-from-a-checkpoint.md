---
name: resume-training-from-a-checkpoint
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You resume an interrupted training run from a valid checkpoint without corrupting model state or duplicating data. The resumed run produces continuous metrics and a new checkpoint that passes validation.

## Preconditions

- A saved checkpoint containing model weights and, ideally, optimizer, scheduler, tokenizer, and trainer state.
- The original training config, dataset version, code commit or package lock, and random seed.
- Enough disk and compute budget to continue training.

## Steps

1. **Inventory the checkpoint contents.** Inspect the checkpoint directory for weights, tokenizer files, optimizer state, scheduler state, trainer state, and metadata such as global step. → *Expect:* a checklist showing which state components are available.
2. **Verify dataset and code compatibility.** Compare dataset hashes, tokenizer version, model architecture, and training arguments against the original run. → *Expect:* hashes and config values match, or mismatches are explicitly documented.
3. **Run a load-only smoke test.** Load the checkpoint and execute one forward pass on a tiny batch without optimizer updates. → *Expect:* no missing-key errors and finite loss/logits.
4. **Resume with trainer state when available.** [BRANCH: Hugging Face Trainer | DeepSpeed | custom loop] Use `resume_from_checkpoint=/path/to/checkpoint` or the framework equivalent. ⚠️ *Irreversible:* continuing a paid run consumes compute and may overwrite output paths; back up the checkpoint and write to a new run directory first. → *Expect:* logs restart at the recorded global step, not step zero.
5. **If optimizer state is missing, resume conservatively.** Lower the learning rate, warm up briefly, and mark the run as partial-state resume. → *Expect:* loss does not spike sharply during the first validation interval.
6. **Validate immediately after resuming.** Run validation after a small number of steps and compare loss and task metrics to the last pre-interruption values. → *Expect:* metrics are within the expected noise band or improving.
7. **Save a fresh checkpoint and eval artifact.** Write a new checkpoint after successful validation and run the held-out eval. → *Expect:* a new checkpoint path and a validation report tied to the resumed run id.

## Decision points

- Architecture or tokenizer differs → do not resume; convert deliberately or restart training.
- Optimizer state is missing → resume only with lower learning rate and close monitoring.
- Loss spikes or becomes NaN after resume → stop, restore backup checkpoint, and inspect learning rate and mixed-precision state.
- Dataset order cannot be restored → treat the continuation as approximate and rely on held-out validation before using the model.
- Checkpoint came from an untrusted source → load in an isolated environment and verify file integrity first.

## Failure modes & recovery

- **F1 Step counter reset:** detect logs starting at step zero → pass the checkpoint path to the trainer and restore trainer state.
- **F2 Tokenizer mismatch:** detect shape errors or degraded validation → restore the original tokenizer files and config.
- **F3 Optimizer incompatibility:** detect load errors for optimizer groups → resume weights only with a reduced learning rate.
- **F4 Corrupt checkpoint:** detect checksum mismatch or unreadable tensors → fall back to the previous checkpoint.
- **F5 Silent data duplication:** detect repeated sample ids in resumed batches → restore sampler state or start a clean epoch and document it.

## Verification

Resume is successful when a script loads the resumed checkpoint, reports `global_step > original_checkpoint_step`, produces finite validation loss, and achieves a held-out metric no worse than the pre-resume metric by more than the declared tolerance, such as `delta_accuracy >= -0.01`.

## Variations

- `Hugging Face Trainer`: use `trainer.train(resume_from_checkpoint=checkpoint_dir)` and inspect `trainer_state.json`.
- `DeepSpeed`: restore model, optimizer, scheduler, and ZeRO partition state from the same tag.
- `LoRA`: ensure adapter weights and base model revision both match the interrupted run.
- `hosted fine-tune`: use provider-supported resume only; otherwise start a new job from the latest completed model artifact.

## Safety & privacy

High risk because compute spend and checkpoint overwrites are easy mistakes. Back up checkpoints before resuming, never load untrusted pickle-like artifacts outside an isolated environment, confirm dataset licensing and PII handling, and require review before continuing an expensive run.
