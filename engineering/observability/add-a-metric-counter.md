---
name: add-a-metric-counter
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

You add a counter metric that records how often a specific event happens and can be queried reliably in monitoring.

## Preconditions

- The service already exposes or exports metrics through Prometheus, OpenTelemetry, StatsD, or a vendor SDK.
- You know the event to count and the dimensions needed for useful debugging.
- You can run the service locally or in a test environment.

## Steps

1. **Define the metric contract.** Choose a name, help text, and labels, for example `checkout_attempts_total{status,method}`. → *Expect:* the metric is a monotonic counter with bounded labels.
2. **Add the counter to code.** [BRANCH: Prometheus | OpenTelemetry] Register a Prometheus `CounterVec` or an OpenTelemetry `LongCounter`. → *Expect:* the application starts without duplicate metric registration errors.
3. **Increment at the event point.** Add `counter.inc()` or `counter.add(1, attributes)` after the event outcome is known. → *Expect:* each real event increments exactly once.
4. **Avoid high-cardinality labels.** Keep labels to bounded values like status, route template, or provider. → *Expect:* no user IDs, emails, raw URLs, or request IDs appear as metric labels.
5. **Add a test.** Exercise success and failure paths and assert the counter changes or the instrumentation wrapper is called. → *Expect:* the new test fails before instrumentation and passes after it.
6. **Inspect local metrics.** Run `curl -fsS http://localhost:<port>/metrics | grep -E '^checkout_attempts_total'`. → *Expect:* the counter appears with expected label sets and numeric values.
7. **Deploy and query.** Query `sum(rate(checkout_attempts_total[5m])) by (status)` in the metrics UI. → *Expect:* the query returns a time series after events occur.

## Decision points

- Event can happen more than once per request → define whether each attempt or each request is counted.
- Labels may grow without bound → move detail into logs or traces instead of labels.
- Counter needs latency too → add a histogram separately rather than encoding duration into labels.
- Background jobs → ensure worker metrics are scraped or exported separately from web pods.

## Failure modes & recovery

- **F1 Duplicate registration:** detect startup error about an already registered collector → register once at module initialization or reuse an existing registry.
- **F2 Missing metric:** detect no line in `/metrics` → confirm endpoint exposure, scrape config, and that the code path ran.
- **F3 Cardinality spike:** detect many label values or monitoring cost alerts → remove unbounded labels and restart affected exporters.
- **F4 Double counting:** detect counts roughly twice expected volume → audit retries, middleware, and both success/failure instrumentation paths.

## Verification

After triggering the event once locally, `curl -fsS http://localhost:<port>/metrics | grep -E '^checkout_attempts_total\{.*\} 1$|^checkout_attempts_total 1$'` exits 0, and the unit or integration test for the instrumented path exits 0.

## Variations

- `Prometheus`: expose `_total` counters on `/metrics` and use `rate()` or `increase()` in queries.
- `OpenTelemetry`: export counters through OTLP and confirm the collector forwards them to the backend.
- `StatsD`: emit increment packets and verify aggregation naming in the vendor backend.

## Safety & privacy

Low operational risk, but metric labels can leak private data or overload monitoring. Keep label sets bounded, never use raw user input as labels, and document the metric owner and intended query.
