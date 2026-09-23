---
name: merge-a-lora-adapter
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/finetuning/fine-tune-with-lora]
status: draft
last_verified: 2026-09-22
---

## Goal

You merge a LoRA adapter into its base model when the serving stack requires merged weights. The merged artifact loads, matches adapter behavior, and preserves the original base and adapter files.

## Preconditions

- Base model checkpoint and matching LoRA adapter.
- Enough disk and memory to materialize merged weights.
- Permission to create and store a derivative model under the base model license.

## Steps

1. **Confirm base-adapter compatibility.** Check adapter config `base_model_name_or_path`, tokenizer, and revision. → *Expect:* base model ID exactly matches the adapter metadata.
2. **Back up original artifacts.** Keep the base model and adapter unchanged. → *Expect:* checksums for base and adapter are recorded before merging.
3. **Load and merge in the framework.** [BRANCH: PEFT] Use `PeftModel.from_pretrained(base, adapter).merge_and_unload()` and save with safe serialization. → *Expect:* merged weights and config are written to a new directory.
4. **Save tokenizer and chat template.** Copy the tokenizer files needed by inference. → *Expect:* the merged directory can be loaded without referring to the adapter directory.
5. **Run equivalence prompts.** Compare base+adapter output to merged-model output with deterministic decoding. → *Expect:* outputs or logits match within a small tolerance.
6. **Run the held-out smoke eval.** Check the merged artifact, not the adapter path. → *Expect:* metrics match the adapter-loaded model within tolerance.
7. **Package metadata.** Record merge command, library versions, source checksums, and license notes. → *Expect:* artifact provenance is complete.

## Decision points

- Outputs differ materially after merge → inspect dtype, quantization, and adapter/base mismatch.
- Base license restricts derivatives → do not distribute merged weights.
- Serving stack supports adapters directly → skip merging to preserve flexibility.
- Disk or memory is insufficient → merge on a larger machine or serve adapters unmerged.

## Failure modes & recovery

- **F1 Wrong base model:** detect shape mismatch or bad outputs → reload the exact base revision from adapter config.
- **F2 Quantization merge issue:** detect errors merging into quantized weights → merge in higher precision, then quantize the merged model.
- **F3 Missing tokenizer:** detect serving failure due to tokenizer files → copy tokenizer and chat template into artifact.
- **F4 License violation:** detect derivative distribution not permitted → keep internal only or choose another base.
- **F5 Behavior drift:** detect eval drop after merge → compare logits and rerun merge with consistent dtype.

## Verification

The merged model passes when it loads without the adapter directory, deterministic test prompts match base+adapter behavior within tolerance, held-out smoke eval metrics are unchanged within the documented margin, and checksums plus provenance for source artifacts are recorded.

## Variations

- `PEFT`: use `merge_and_unload()` for standard Hugging Face LoRA adapters.
- `multi-adapter serving`: do not merge; load adapters dynamically by request.
- `quantized deployment`: merge first in supported precision, then quantize and re-evaluate.

## Safety & privacy

Merged weights can make an internal adapter easier to redistribute accidentally. Check model licenses, do not overwrite the original base or adapter, and avoid publishing merged artifacts trained on confidential data.
