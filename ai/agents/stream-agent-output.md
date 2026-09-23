---
name: stream-agent-output
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent streams useful progress to the user while preserving structured state and final-answer correctness. Success means partial tokens, tool-status events, and the final result can be consumed programmatically without corrupting JSON or leaking hidden reasoning.

## Preconditions

- A model/provider SDK that supports streaming events.
- A client transport such as Server-Sent Events, WebSocket, gRPC streaming, or a CLI event iterator.
- A defined event schema for `message_delta`, `tool_start`, `tool_result`, `error`, and `final`.

## Steps

1. **Define a typed stream event protocol.** Use envelopes such as `{"type":"message_delta","text":"..."}` and `{"type":"tool_start","tool_name":"search","call_id":"..."}`. → *Expect:* every outbound event validates against one JSON Schema or typed union.
2. **Separate user-visible text from internal state.** Stream only final-channel text and safe tool progress, not hidden chain-of-thought, raw prompts, credentials, or untrusted tool payloads. → *Expect:* a stream capture contains no hidden prompt fields or secret patterns.
3. **Bridge provider events to your protocol.** [BRANCH: Anthropic | OpenAI | open model] Convert provider-specific deltas into your normalized events and buffer tool-call arguments until they parse. → *Expect:* provider streams produce the same event sequence shape in tests.
4. **Handle backpressure and disconnects.** Queue bounded events, cancel model generation on client disconnect, and emit a terminal `error` or `final` event exactly once. → *Expect:* disconnect tests close the upstream request and leave no running generation.
5. **Validate structured final output after streaming.** If the final answer must be JSON, stream progress text separately and emit the final JSON only after it parses and validates. → *Expect:* the final event contains valid JSON, even if earlier deltas were free text.
6. **Record stream telemetry.** Track time to first token, total tokens, tool latency, completion status, and cancellation reason. → *Expect:* each run has timing metrics and a terminal status.

## Decision points

- Client needs low latency UI feedback → stream text deltas and tool-status events.
- Output must be strict JSON → buffer model text until complete JSON validates, then emit one `final` event.
- User disconnects → cancel generation and tools unless the workflow is explicitly backgrounded.
- Tool payload contains PII or secrets → stream a summary or progress marker, not the raw payload.

## Failure modes & recovery

- **F1 Broken JSON from token streaming:** detect parse failures in streamed structured output → buffer and validate before emitting final JSON.
- **F2 Duplicate terminal events:** detect multiple `final` or `error` events per run → guard terminal emission with a run-state flag.
- **F3 Leaked internal prompt:** detect system prompt text or secret regex matches in stream logs → add an allowlist of event fields and redact before send.
- **F4 Orphaned model request:** detect upstream still running after client disconnect → wire cancellation tokens through provider and tool calls.

## Verification

Run an integration test that streams a tool-using agent through a fake client. The captured events must validate against the event schema, include exactly one terminal event, show time-to-first-token below your UI threshold, cancel the provider call on simulated disconnect, and produce a final payload that parses and validates when structured output is required.

## Variations

- `SSE`: simple browser support and replay-friendly text events.
- `WebSocket`: bidirectional control such as user cancellation, edits, or live tool approvals.
- `CLI`: print text deltas to stdout and write structured event logs to a sidecar file.

## Safety & privacy

Medium risk because streaming can leak intermediate or sensitive content before review. Stream only approved event fields, buffer structured or sensitive outputs until validation/redaction, stop upstream work on disconnects, and log enough telemetry to audit partial failures without storing raw private data unnecessarily.
