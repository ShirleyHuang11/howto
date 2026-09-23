---
name: stream-tokens-to-a-frontend
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You stream model output to a frontend with low perceived latency while preserving cancellation, error handling, moderation, and final response validation.

## Preconditions

- A backend that can call the model with streaming enabled.
- A frontend capable of Server-Sent Events, `fetch` readable streams, or WebSockets.
- A response protocol for chunks, final metadata, and errors.
- A policy for handling unsafe partial output.

## Steps

1. **Choose the transport.** Use Server-Sent Events for simple one-way token streams, WebSockets for bidirectional sessions, or `fetch` streams for modern browser clients. → *Expect:* the frontend and backend agree on one chunk protocol.
2. **Define stream events.** Emit `message_start`, `delta`, `message_stop`, `usage`, and `error` events or an equivalent typed format. → *Expect:* the frontend can distinguish partial text from final metadata.
3. **Enable provider streaming.** [BRANCH: Anthropic | OpenAI | vLLM] Call the model with streaming enabled and convert provider chunks into your internal event format. → *Expect:* first token arrives before full completion.
4. **Handle cancellation.** Propagate browser aborts or socket closes to the provider request and stop billing where supported. → *Expect:* closing the client connection cancels backend generation.
5. **Buffer for safety checks when needed.** For high-risk content, hold a short buffer or stream only after moderation passes. → *Expect:* disallowed content is blocked or replaced before user display.
6. **Validate the final response.** If the route expects JSON or citations, validate after `message_stop` and send a final success or repair/error event. → *Expect:* the frontend knows whether the final answer is trustworthy.
7. **Add reconnect and timeout behavior.** Include request IDs, heartbeat comments, server deadlines, and client retry rules. → *Expect:* network stalls produce clear error states, not stuck spinners.
8. **Measure streaming latency.** Track time to first byte, time to first token, tokens/sec, completion time, cancellations, and stream errors. → *Expect:* dashboards show streaming health separately from non-streaming calls.

## Decision points

- Output must be valid JSON only → avoid token-by-token display or stream a separate progress channel until final validation.
- Content needs strict moderation → buffer and classify before displaying chunks.
- Client networks are unreliable → use SSE with request IDs and resumable state where possible.
- Provider does not support cancellation → keep server-side deadlines and avoid long max-token limits.

## Failure modes & recovery

- **F1 Broken chunk framing:** detect frontend parse errors → use newline-delimited JSON or SSE framing tests.
- **F2 Partial unsafe output:** detect moderation alert after chunks shown → add pre-moderation, buffering, or route-level no-stream policy.
- **F3 Cancellation leak:** detect provider calls continuing after client disconnect → wire abort signals through every async layer.
- **F4 Stuck stream:** detect no chunks and no terminal event before timeout → send heartbeat and enforce server deadlines.
- **F5 Final validation failure:** detect invalid JSON after streamed text → send a final error/repair event and avoid committing the result.

## Verification

Run an end-to-end test that opens a stream, asserts the first chunk arrives within the target latency, receives at least one `delta` and one terminal event, cancels a second stream and confirms backend cancellation, and validates final output or error events against the stream schema.

## Variations

- `SSE`: simple browser support and easy proxying for one-way streams.
- `WebSocket`: useful for interactive agents and client messages during generation.
- `fetch-stream`: flexible in modern browsers but requires careful decoding and abort handling.

## Safety & privacy

Medium risk because partial output may reach users before full validation or moderation. Avoid streaming high-risk structured actions, propagate cancellation, keep raw stream logs disabled or redacted, and make final validation status explicit to the frontend.
