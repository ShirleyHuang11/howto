---
name: add-observability-to-an-llm-app
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You instrument an LLM application so operators can trace requests, explain failures, measure quality proxies, and control cost. Observability covers prompts, retrieval, tools, model calls, validation, and user-visible outcomes.

## Preconditions

- An LLM app with a request path you can modify.
- A tracing or logging backend such as OpenTelemetry, LangSmith, Arize/Phoenix, Honeycomb, Datadog, or self-hosted logs.
- A privacy policy for what content may be captured.

## Steps

1. **Define the trace schema.** Include request id, tenant, feature, model, route, prompt version, retrieval ids, tool calls, validation result, latency, token usage, cost, and final status. → *Expect:* a required-field schema for every trace.
2. **Instrument the request lifecycle.** Create spans for input handling, retrieval, prompt assembly, LLM call, streaming, tool execution, validation, and response delivery. → *Expect:* one trace shows the full path of a request.
3. **Capture safe content selectively.** Store redacted prompts, retrieved chunk ids, and completions only when policy allows. ⚠️ *Data leaves your control:* third-party observability tools may receive prompt or output content; redact or disable content capture first. → *Expect:* sensitive canaries are absent or redacted in traces.
4. **Record quality signals.** Log schema validity, citation support, judge score, user feedback, refusal reason, and fallback use. → *Expect:* dashboards can separate technical success from answer quality.
5. **Add alerts and SLOs.** Alert on error rate, p95 latency, cost spikes, validation failures, retrieval misses, and provider failures. → *Expect:* test alerts reach owners with a trace link.
6. **Build debugging views.** Query traces by user-safe request id, model, route, error type, and eval failure. → *Expect:* an engineer can diagnose a bad answer without raw database access.
7. **Sample traces for evals.** Export reviewed, redacted examples into an eval dataset with provenance. → *Expect:* sampled eval records include trace ids and review status.

## Decision points

- Content is sensitive → capture metadata and hashes rather than raw prompts.
- Failures are mostly retrieval misses → add retrieval metrics and chunk ids to traces.
- Failures are malformed outputs → log validator errors and prompt/schema versions.
- Cost spikes appear → inspect token usage, retries, and fallback spans.
- Observability backend is external → confirm data-processing terms and disable raw content unless approved.

## Failure modes & recovery

- **F1 Trace fragmentation:** detect no shared request id across spans → propagate trace context through async jobs and streams.
- **F2 Sensitive content leak:** detect canary in observability backend → purge, rotate secrets if needed, and strengthen redaction.
- **F3 Missing cost data:** detect traces without token usage → add usage extraction or local token estimates.
- **F4 Quality blind spot:** detect all traces marked success despite bad answers → add validation and feedback fields.
- **F5 High-cardinality overload:** detect backend cost or query failures → limit tag cardinality and move raw ids to attributes.

## Verification

Observability is complete when an integration test sends successful, failing, retried, and validation-failing requests, then queries the backend to confirm every trace has required fields, sensitive canaries are redacted, alerts fire for injected failures, and cost totals match token usage estimates.

## Variations

- `OpenTelemetry`: portable spans and metrics across vendors.
- `LLM-specific observability`: adds prompt/version/eval views with less custom work.
- `self-hosted`: preferred for sensitive content but still needs access controls.
- `agent app`: trace each tool call, tool result validation, and planner step separately.

## Safety & privacy

Medium risk because observability can become a second copy of sensitive conversations. Minimize raw content, redact before export, restrict trace access, set retention, audit reads, and require review before using traces as training or eval data.
