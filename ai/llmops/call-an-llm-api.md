---
name: call-an-llm-api
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You make a single LLM API call from code, capture the response, and verify it is parseable and within budget. The call uses environment-based credentials and avoids hardcoded secrets.

## Preconditions

- An API key or local model endpoint configured as an environment variable.
- Network access to the provider or local inference server.
- A small non-sensitive test prompt.

## Steps

1. **Choose a provider branch and model.** [BRANCH: Anthropic | OpenAI | open model] Select a capable chat model such as Claude Sonnet for hosted use or a local instruction model for private testing. → *Expect:* a model id and endpoint are recorded in config.
2. **Load credentials from the environment.** Use variables such as `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or `LOCAL_LLM_BASE_URL`; never paste keys into source code. → *Expect:* the program exits with a clear error if credentials are missing.
3. **Send a minimal request.** Call the messages/chat endpoint with system instructions, user content, max tokens, and temperature. ⚠️ *Data leaves your control:* if using a hosted API, the prompt is sent to the provider; use a non-sensitive test prompt first. → *Expect:* an HTTP 200 response or a structured SDK response.
4. **Extract text and usage metadata.** Read the assistant message, input tokens, output tokens, model id, request id, and stop reason when available. → *Expect:* a log line with response text and token usage.
5. **Validate the response shape.** If you asked for JSON, parse it; otherwise assert non-empty text and acceptable finish reason. → *Expect:* the validation script passes without exceptions.
6. **Store only safe diagnostics.** Log request id, model, latency, and token counts, but not sensitive prompt content unless explicitly approved. → *Expect:* observability exists without leaking secrets.

## Decision points

- Response is malformed → add schema instructions, structured output mode, or a repair retry.
- Latency is too high → try a smaller model, lower max tokens, or streaming.
- Token usage exceeds budget → shorten prompt, retrieve fewer chunks, or cap output tokens.
- Provider returns authentication errors → rotate or reconfigure the API key.
- Data is sensitive → use an approved private endpoint or redact before calling a hosted API.

## Failure modes & recovery

- **F1 401 or 403 authentication failure:** detect provider auth error → verify environment variable, key scope, and project permissions.
- **F2 429 rate limit:** detect rate-limit status or SDK exception → back off, reduce concurrency, or request higher limits.
- **F3 Context-length error:** detect max context exceeded → count tokens before the call and truncate or summarize.
- **F4 Empty or truncated output:** detect stop reason or zero content → increase max tokens or handle refusals.
- **F5 JSON parse failure:** detect parser exception → use structured output mode or validate-and-retry once.

## Verification

The API call is correct when an automated smoke test receives a successful response, validates the expected output type, records token usage and latency, and asserts `estimated_cost <= configured_budget_per_call`.

## Variations

- `Anthropic`: use the Messages API with `system`, `messages`, `max_tokens`, and `model`.
- `OpenAI`: use the Responses or Chat Completions style supported by your SDK version.
- `open model`: use an OpenAI-compatible local server such as vLLM or Ollama when the endpoint supports it.
- `JSON task`: prefer provider structured-output features or strict schema validation.

## Safety & privacy

High risk for real data because hosted calls send prompts to a third party. Keep keys out of code, redact PII, log minimally, set per-call token limits, and review provider data-retention settings before sending customer or proprietary content.
