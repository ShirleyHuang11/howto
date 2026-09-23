---
name: deploy-an-open-model-with-vllm
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You serve an open-weight language model with vLLM behind an OpenAI-compatible API and verify that latency, throughput, and output correctness meet your release gates.

## Preconditions

- A GPU host or Kubernetes node with supported NVIDIA drivers, CUDA, and enough VRAM for the chosen model and context length.
- Permission to use the model weights under their license.
- A model repository or local checkpoint compatible with vLLM.
- A smoke-test prompt set and load-test target.

## Steps

1. **Select the model and serving shape.** Choose a model size, quantization, context length, and tensor parallel size that fit available VRAM. → *Expect:* a deployment spec with model ID, dtype or quantization, `max_model_len`, GPU count, and expected memory.
2. **Install or pull vLLM.** [BRANCH: Docker | pip | Kubernetes] For Docker, run an image matching your CUDA stack, such as `vllm/vllm-openai`, with GPU access enabled. → *Expect:* `python -m vllm.entrypoints.openai.api_server --help` or container startup succeeds.
3. **Start the OpenAI-compatible server.** Run `vllm serve <model_id> --host 0.0.0.0 --port 8000 --max-model-len <n>` and set tensor parallel flags if needed. ⚠️ *Irreversible:* deploying public endpoints can expose compute to abuse; require auth and network controls before production traffic. → *Expect:* `/health` returns success and model weights finish loading.
4. **Protect the endpoint.** Put the server behind an authenticated gateway, TLS, request limits, and network allowlists. → *Expect:* unauthenticated requests are rejected before reaching vLLM.
5. **Run a smoke test.** Call `/v1/chat/completions` with a deterministic prompt and low temperature. → *Expect:* HTTP 200, nonempty text, and usage fields or server metrics are emitted.
6. **Validate structured outputs if needed.** If callers expect JSON or tool calls, run schema validation over the generated output. → *Expect:* at least the minimum required schema-valid rate on the smoke set.
7. **Load-test realistic traffic.** Use concurrent prompts with representative input and output lengths, measuring tokens/sec, time to first token, p95 latency, GPU memory, and error rate. → *Expect:* throughput meets the target without OOM or sustained queue growth.
8. **Add operational monitors.** Export metrics and logs for GPU memory, request rate, queue time, generation tokens/sec, 5xx, and OOM events. → *Expect:* dashboards and alerts show serving health during the load test.

## Decision points

- GPU OOM at startup → reduce `max_model_len`, use quantization, lower batch settings, or choose a smaller model.
- Throughput below target → increase tensor parallelism, use a smaller model, tune batching, or add replicas.
- JSON validity below target → add constrained decoding, repair-and-validate logic, or choose a stronger instruction model.
- License prohibits your use case → stop and choose a compatible model.

## Failure modes & recovery

- **F1 Weight download failure:** detect startup errors or missing files → authenticate to the model hub or pre-stage weights locally.
- **F2 CUDA mismatch:** detect driver/runtime errors → use a vLLM image compatible with the installed driver.
- **F3 Out of memory:** detect OOM during load or long prompts → lower context length, enable quantization, or reduce concurrency.
- **F4 Unbounded public access:** detect unknown traffic or cost spikes → enforce auth, rate limits, and firewall rules immediately.
- **F5 Output incompatibility:** detect downstream schema or tool-call failures → adapt prompts and validation or reject this model for that route.

## Verification

Run a scripted deployment check that calls `/health`, sends 20 representative `/v1/chat/completions` requests, validates all required response schemas, and runs a 5-minute load test. The deployment passes only if HTTP success rate is at least `99%`, p95 latency and tokens/sec meet the configured SLO, GPU memory stays below the safety threshold, and no OOM events occur.

## Variations

- `single-gpu`: simplest; choose a model and context length that comfortably fit memory.
- `multi-gpu`: use tensor parallelism and confirm interconnect bandwidth is not the bottleneck.
- `quantized`: lowers memory and may reduce quality; rerun task evals after quantization.

## Safety & privacy

High risk because a deployed open model can leak prompts through logs, be abused for compute, or violate model-license terms. Require authentication, minimize raw prompt retention, review licenses, cap concurrency, and restrict production exposure until evals and monitors pass.
