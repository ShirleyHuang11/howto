---
name: stream-an-llm-completion
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: high
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You stream tokens or events from an LLM to a client while preserving final validation, cancellation, and usage accounting. The stream is responsive and still produces a complete verified result.

## Preconditions

- You can make a normal LLM API call.
- A server or notebook environment that supports server-sent events, websockets, or SDK streaming.
- A client or test harness that can consume incremental chunks.

## Steps

1. **Choose the streaming transport.** [BRANCH: SSE | websocket | SDK iterator] Select the transport your client supports and define event names such as `delta`, `error`, `done`, and `usage`. → *Expect:* a documented stream event contract.
2. **Enable streaming in the provider request.** Set the provider's streaming flag or use the streaming SDK method with the same prompt and token limits as the non-streaming call. ⚠️ *Data leaves your control:* hosted streaming sends the full prompt to the provider before chunks return. → *Expect:* the first chunk arrives before the full completion is generated.
3. **Accumulate chunks server-side.** Append text deltas or tool-call deltas into a final buffer while forwarding safe chunks to the client. → *Expect:* the reconstructed final message exactly matches the concatenated deltas.
4. **Handle cancellation and timeouts.** Abort the upstream request if the client disconnects or the request exceeds its time limit. → *Expect:* canceled streams close cleanly and stop billing as soon as the provider supports it.
5. **Validate after the final event.** Parse JSON, verify citations, or check tool-call schema only after the completion is complete. → *Expect:* the final response passes the same validator as a non-streaming call.
6. **Emit usage and trace metadata.** Send final token usage, model id, request id, finish reason, and latency in a terminal event or server log. → *Expect:* observability records exist for both success and cancellation.

## Decision points

- Client needs immediate partial text → stream text deltas but delay irreversible actions until final validation.
- Output must be strict JSON → buffer until complete, then parse; do not parse arbitrary partial chunks.
- Tool calls are streamed → reconstruct arguments exactly before executing the tool.
- Client disconnects → cancel upstream and mark the trace as aborted.
- Moderation must happen before display → pre-screen inputs and consider chunk buffering for outputs.

## Failure modes & recovery

- **F1 Broken chunk ordering:** detect invalid reconstructed output → use provider event sequence ids when available and append only ordered deltas.
- **F2 Partial JSON displayed as final:** detect client acts before `done` → gate actions on terminal event and schema validation.
- **F3 Hanging stream:** detect no chunks for the idle timeout → abort and return a retryable error.
- **F4 Lost usage accounting:** detect missing final usage event → log provider response metadata or estimate from token counters.
- **F5 Client disconnect leak:** detect upstream requests continue after disconnect → wire cancellation tokens through the server.

## Verification

Streaming is correct when an integration test receives at least one `delta` event before `done`, reconstructs the same final text as the server buffer, validates the final output schema, and confirms disconnect tests close the upstream request within the timeout.

## Variations

- `Anthropic`: handle message start, content block deltas, message delta, and message stop events.
- `OpenAI`: consume response or chat stream events and aggregate text or tool-call deltas.
- `browser`: use SSE for one-way text streams and websockets for bidirectional agent sessions.
- `terminal`: stream directly from the SDK iterator and flush stdout per chunk.

## Safety & privacy

High risk when streaming sensitive content because partial text may be shown before full validation. Avoid logging raw chunks by default, cancel on disconnect, moderate where required, and never execute streamed tool calls until the final reconstructed arguments validate.
