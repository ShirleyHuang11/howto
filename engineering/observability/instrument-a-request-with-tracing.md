---
name: instrument-a-request-with-tracing
domain: engineering
subdomain: observability
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You add distributed tracing to a request path so a single request can be followed across middleware, database calls, and downstream services.

## Preconditions

- A trace backend or collector is available, such as OpenTelemetry Collector, Jaeger, Tempo, Datadog, or Honeycomb.
- You know the service name, environment, and endpoint to exercise.
- You can configure runtime environment variables or application settings.

## Steps

1. **Choose propagation and exporter settings.** Use W3C Trace Context and OTLP unless your platform requires a vendor-specific format. → *Expect:* the service has a configured endpoint such as `OTEL_EXPORTER_OTLP_ENDPOINT`.
2. **Install tracing packages.** [BRANCH: Python | Node.js | Go] Add OpenTelemetry API, SDK, instrumentation packages, and OTLP exporter. → *Expect:* dependency installation exits 0.
3. **Initialize tracing at startup.** Configure resource attributes like `service.name`, `deployment.environment`, and `service.version`. → *Expect:* the app starts and the tracer provider is initialized before request handling.
4. **Enable HTTP framework instrumentation.** Add middleware or auto-instrumentation for inbound requests. → *Expect:* each request creates a server span with route and status code attributes.
5. **Instrument important internal work.** Add spans around database calls, queue publishing, or downstream API calls where auto-instrumentation is missing. → *Expect:* nested spans show meaningful operation names and error status when failures occur.
6. **Propagate context downstream.** Ensure outgoing HTTP or messaging clients inject trace headers. → *Expect:* downstream services receive `traceparent` or equivalent headers.
7. **Run a test request.** Execute `curl -fsS -H 'traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01' http://localhost:<port>/<path>`. → *Expect:* the request succeeds and a trace appears in the backend with the same trace ID or a linked trace.

## Decision points

- Only one service is instrumented → still add inbound tracing now and plan downstream propagation next.
- Backend samples heavily → force sampling in non-production to verify instrumentation, then restore production sampling policy.
- Sensitive attributes would be useful → hash or omit private values and use logs for restricted debugging.
- Async queues involved → use messaging instrumentation and preserve context in message headers.

## Failure modes & recovery

- **F1 No traces exported:** detect empty backend after requests → verify exporter endpoint, credentials, sampling, and network egress.
- **F2 Broken trace continuity:** detect separate traces per service → fix context propagation headers in outgoing clients or proxies.
- **F3 High overhead:** detect latency or CPU increase → lower sampling, reduce span volume, and remove expensive attribute construction.
- **F4 Sensitive attributes:** detect payloads, tokens, or emails in traces → scrub attributes and rotate any exposed credentials if needed.

## Verification

A request to `/<path>` returns success, the trace backend shows a server span for the service with child spans for key work, and the trace contains `service.name`, environment, route, status code, and error status when applicable.

## Variations

- `OpenTelemetry Collector`: export OTLP to a local or sidecar collector and let it fan out to the backend.
- `Datadog/New Relic`: vendor agents may provide auto-instrumentation with environment variables plus library hooks.
- `Frontend`: propagate trace context from browser to backend while respecting sampling and privacy controls.

## Safety & privacy

Medium risk because tracing touches request handling and can expose sensitive metadata. Avoid raw bodies and secrets in attributes, keep sampling controlled, and validate overhead before broad production rollout.
