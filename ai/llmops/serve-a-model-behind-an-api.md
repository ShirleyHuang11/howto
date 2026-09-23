---
name: serve-a-model-behind-an-api
domain: ai
subdomain: llmops
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

You expose a model through a stable API contract with authentication, validation, observability, and automated tests that prove clients receive valid responses.

## Preconditions

- A working model invocation function or provider client.
- An API framework such as FastAPI, Express, Flask, or a managed gateway.
- A deployment target and secrets manager for API keys.
- Example requests and expected response schemas.

## Steps

1. **Define the API contract.** Specify request fields, response schema, error schema, timeouts, and streaming behavior if any. → *Expect:* an OpenAPI spec or typed contract checked into the service.
2. **Validate inputs before model calls.** Reject oversized prompts, unsupported parameters, missing auth, and invalid JSON with `4xx` errors. → *Expect:* malformed requests fail without spending model tokens.
3. **Wrap the model call.** Put model invocation behind a service function that accepts validated input and returns typed output plus usage metadata. [BRANCH: provider API | vLLM | local inference] → *Expect:* the API handler does not contain provider-specific parsing logic.
4. **Add authentication and authorization.** Require API keys, OAuth, or signed internal service identity before inference. → *Expect:* unauthenticated requests return `401` or `403`.
5. **Set timeouts, retries, and cancellation.** Use bounded retries for transient provider errors and cancel work when clients disconnect. → *Expect:* hung model calls do not hold workers indefinitely.
6. **Add response validation.** Validate the model output or postprocessed result against the public response schema before returning it. → *Expect:* invalid model output becomes a controlled `5xx` or repair path, not malformed client data.
7. **Instrument the endpoint.** Log request ID, route, model, latency, token usage, status, and error class without raw sensitive content. → *Expect:* one trace connects API admission, model call, and response.
8. **Deploy behind a gateway.** ⚠️ *Irreversible:* exposing the endpoint can create spend and privacy risk; confirm auth, rate limits, and rollback before production traffic. → *Expect:* the public or internal endpoint returns HTTP 200 for a smoke test and rejects unauthorized calls.

## Decision points

- Clients need partial output quickly → use server-sent events or WebSocket streaming.
- Output must be machine-actionable → enforce JSON schema validation and retry once with a repair prompt.
- Provider latency exceeds API timeout → queue the job or return an async task ID.
- Endpoint handles user data → add PII redaction and data retention controls before deployment.

## Failure modes & recovery

- **F1 Invalid request reaches model:** detect model calls for requests that later return `4xx` → move validation before invocation.
- **F2 Malformed model response:** detect schema validation failures → add structured output mode, constrained decoding, or a repair step.
- **F3 Timeout leak:** detect workers stuck after client disconnects → propagate cancellation and enforce server-side deadlines.
- **F4 Unauthorized access:** detect missing auth in access logs → block at gateway and rotate exposed keys.
- **F5 Missing cost attribution:** detect token usage without tenant or route labels → require metadata before admission.

## Verification

Run contract tests that submit valid, invalid, unauthorized, oversized, and timeout-triggering requests. The API passes only when valid requests return HTTP 200 with schema-valid JSON, invalid requests return expected `4xx` without model calls, unauthorized requests return `401/403`, and traces include request ID, model, latency, and usage metadata.

## Variations

- `FastAPI`: use Pydantic models for request and response validation.
- `managed-gateway`: offload auth, TLS, and coarse rate limits while keeping token-aware checks in the service.
- `serverless`: simple to operate but test cold starts and maximum execution duration.

## Safety & privacy

Medium risk because an API can expose data and generate spend. Enforce auth, validate before spending tokens, avoid raw prompt logs, cap request sizes, and require review before making the endpoint public.
