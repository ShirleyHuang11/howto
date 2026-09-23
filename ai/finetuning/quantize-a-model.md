---
name: quantize-a-model
domain: ai
subdomain: finetuning
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You reduce a model's memory and serving cost through quantization while preserving required quality. The result is a quantized artifact with measured accuracy, latency, and compatibility.

## Preconditions

- A base or fine-tuned model with permission to modify and serve.
- A representative calibration or evaluation set.
- Quantization tooling such as bitsandbytes, GPTQ, AWQ, GGUF/llama.cpp, or vendor-specific exporters.

## Steps

1. **Choose a quantization target.** [BRANCH: 8-bit | 4-bit NF4 | GPTQ | AWQ | GGUF] Match format to the serving engine and hardware. → *Expect:* the chosen method is supported by your inference stack.
2. **Prepare calibration data.** Use representative prompts and formats, not random unrelated text. → *Expect:* calibration rows pass the same tokenizer/template as production.
3. **Run baseline eval and benchmark.** Measure quality, p50/p95 latency, tokens per second, and memory before quantization. → *Expect:* a baseline report exists for comparison.
4. **Quantize the artifact.** Run the tool command, such as an AWQ/GPTQ exporter or `llama.cpp` conversion for GGUF. → *Expect:* a quantized model file or directory is produced with metadata.
5. **Load in the target server.** Start the intended runtime, not just a Python notebook. → *Expect:* health check succeeds and a smoke prompt returns valid text or JSON.
6. **Rerun evals and benchmarks.** Compare quantized results to the baseline. → *Expect:* quality drop, latency gain, and memory reduction are quantified.
7. **Record compatibility constraints.** Note GPU type, runtime version, max context, and unsupported features. → *Expect:* deployment docs include exact artifact and runtime versions.

## Decision points

- Quality drop exceeds tolerance → use higher bit width, better calibration data, or no quantization.
- Serving runtime cannot load artifact → export in a supported format.
- Latency worsens despite memory savings → benchmark a different kernel or quantization method.
- Long-context behavior degrades → evaluate with long prompts before production.

## Failure modes & recovery

- **F1 Artifact load failure:** detect runtime errors loading weights → regenerate with a compatible format and version.
- **F2 Accuracy collapse:** detect eval score below threshold → increase precision or improve calibration set.
- **F3 Tokenizer mismatch:** detect garbled outputs → package the correct tokenizer and chat template.
- **F4 Unsupported hardware:** detect missing kernels or slow CPU fallback → choose a runtime matched to the hardware.
- **F5 Hidden safety regression:** detect refusal or format eval drops → treat as a blocking quality regression.

## Verification

The quantized model passes only when it loads in the target serving runtime, produces valid smoke outputs, memory usage falls by the documented amount, p95 latency or throughput meets target, and held-out eval score drops no more than the allowed tolerance, such as `<= 2 percentage points`.

## Variations

- `bitsandbytes`: simple 8-bit or 4-bit loading for Python inference and QLoRA.
- `AWQ/GPTQ`: static quantized artifacts optimized for GPU serving.
- `GGUF`: llama.cpp-compatible artifacts for CPU, Apple silicon, or lightweight edge deployment.

## Safety & privacy

Quantization is usually reversible if you keep the original model, but deploying a lower-quality model can affect users. Keep the unquantized artifact, rerun safety evals, and avoid publishing models whose license or data provenance does not allow redistribution.
