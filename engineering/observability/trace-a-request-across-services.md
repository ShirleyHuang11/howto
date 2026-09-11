---
name: trace-a-request-across-services
domain: engineering
subdomain: observability
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You locate and inspect one distributed trace to understand how a request moved across services and where time or errors accumulated.

## Preconditions

- Services emit traces to a backend such as Jaeger, Tempo, Honeycomb, Datadog, New Relic, or OpenSearch.
- You have a request ID, trace ID, timestamp, user-safe identifier, or endpoint from an alert or report.
- You have read access to traces and related logs.

## Steps

1. **Collect the search anchor.** Copy the trace ID, request ID, endpoint, status code, and approximate timestamp from logs, headers, or user report. → *Expect:* at least one searchable identifier or narrow time window is available.
2. **Search the trace backend.** Filter by service, operation or route, environment, and time window. → *Expect:* candidate traces appear for the affected request path.
3. **Open the most relevant trace.** Choose the trace matching the timestamp, endpoint, status, or error. → *Expect:* a span waterfall displays services, durations, parent-child relationships, and errors.
4. **Find the critical path.** Inspect the longest spans and error-marked spans. → *Expect:* the likely bottleneck or failing dependency is visible.
5. **Correlate logs.** Use trace ID or span ID to search logs for the same request. → *Expect:* logs add application-specific errors or inputs without losing trace context.
6. **Check propagation gaps.** Look for service boundaries where the trace splits or disappears. → *Expect:* any missing instrumentation or header propagation issue is identified.
7. **Record evidence.** Save the trace URL, timestamp, slow span names, errors, and related log query links. → *Expect:* another responder can reopen the same diagnostic view.

## Decision points

- Trace is sampled out → search logs by request ID or reproduce with forced sampling in a safe environment.
- Downstream service missing → inspect HTTP headers, proxies, and messaging context propagation.
- Long duration is client wait time → compare server spans with load balancer and client-side timing.
- Trace contains sensitive attributes → redact screenshots and incident notes.

## Failure modes & recovery

- **F1 No trace found:** detect empty search results → widen the time window, search by logs first, or confirm sampling rules.
- **F2 Broken trace tree:** detect separate traces for each service → fix propagation of `traceparent` or vendor headers.
- **F3 Misleading duration:** detect root span duration much larger than child spans → check queueing, retries, network time, or client disconnect behavior.
- **F4 Missing logs:** detect trace has no correlated logs → add trace ID injection into structured logging.

## Verification

The trace backend shows a specific trace for the request with service spans, timing, and error status, and a log search by the same trace ID returns related application logs for the incident window.

## Variations

- `Jaeger/Tempo`: search by trace ID when available, or by service and operation in a time window.
- `Honeycomb`: use query filters and BubbleUp-style comparisons for high-cardinality attributes.
- `Datadog/New Relic`: pivot between APM trace, logs, infrastructure, and deployment markers.
- `Async messaging`: follow producer and consumer spans linked by message context rather than strict parent-child timing.

## Safety & privacy

Low operational risk, but traces may include URLs, headers, database statements, and customer identifiers. Share trace links only with authorized responders and avoid copying sensitive attributes into tickets.
