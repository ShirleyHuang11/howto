---
name: log-agent-traces
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent writes structured traces that make runs debuggable, evaluable, and auditable without leaking unnecessary private data. Success means every model turn, tool call, retry, and stop reason can be joined by `trace_id`.

## Preconditions

- An agent runtime with hooks around model calls, tool calls, and run lifecycle events.
- A telemetry sink such as OpenTelemetry, LangSmith, Arize/Phoenix, Weights & Biases, or a database table.
- A redaction policy for secrets, PII, prompts, tool arguments, and tool results.

## Steps

1. **Define the trace schema.** Include `trace_id`, `run_id`, `span_id`, `parent_span_id`, `event_type`, timestamps, model, token counts, cost, tool name, status, and sanitized metadata. → *Expect:* a sample trace validates against the schema.
2. **Instrument model calls.** Record model name, input/output token counts, latency, stop reason, and structured-output validation status. ⚠️ *Data leaves your control:* if prompts are sent to a third-party tracing service, redact or disable prompt capture first. → *Expect:* each model call creates one span with token and latency fields.
3. **Instrument tool calls.** Log tool name, argument hash or redacted arguments, result status, error type, retry count, and duration. → *Expect:* each tool call creates a child span under the agent step.
4. **Capture agent decisions and terminal state.** Log selected next action, guardrail outcomes, approval pauses, and final stop reason. → *Expect:* the trace timeline explains why the run stopped.
5. **Add sampling and retention controls.** Keep full traces for test and incident runs; sample production success traces; shorten retention for sensitive workloads. → *Expect:* trace volume stays within storage budget and sensitive fields respect retention policy.
6. **Link traces to evaluations.** Store `eval_case_id` and `dataset_version` when running evals. → *Expect:* failed eval cases open directly to the corresponding agent trace.

## Decision points

- Workload contains PII or proprietary data → log hashes, categories, and metrics instead of raw content.
- You need debugging for a failing eval → enable full trace capture for that run class.
- Trace sink is external SaaS → complete a data-processing and retention review before sending prompts or tool payloads.
- Cost grows with trace volume → sample successful runs but keep failures and approval events.

## Failure modes & recovery

- **F1 Missing child spans:** detect tool events without parent IDs → propagate context through async tasks and workers.
- **F2 Secret leakage:** detect API-key regex matches in traces → block export, rotate exposed credentials, and add redaction tests.
- **F3 Unjoinable evals:** detect failed cases without `eval_case_id` → require eval metadata in the run constructor.
- **F4 Trace overload:** detect storage or ingestion throttling → lower sample rate and aggregate large payloads.

## Verification

Run a traced fixture containing two model calls, one successful tool, one failed retried tool, and a final stop reason. Query the telemetry sink by `trace_id`; the result must have a connected parent-child span tree, sanitized payloads with no secret-pattern matches, token/cost fields on model spans, retry metadata on the failed tool span, and the expected terminal stop reason.

## Variations

- `OpenTelemetry`: export spans to your existing observability backend with semantic attributes for LLM and tool calls.
- `LangSmith or Phoenix`: use built-in LLM trace viewers and eval linking.
- `self-hosted database`: store normalized trace tables when data cannot leave your infrastructure.

## Safety & privacy

Medium risk because traces can contain prompts, user data, tool outputs, and credentials. Redact before export, minimize raw payload retention, restrict trace viewer access, and treat external observability systems as third parties that may receive sensitive data.
