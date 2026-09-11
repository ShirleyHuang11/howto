---
name: measure-request-latency-percentiles
domain: engineering
subdomain: observability
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You measure request latency percentiles, especially p95 and p99, so slow user experiences are visible instead of hidden by averages.

## Preconditions

- The service emits request duration metrics or traces.
- Route labels are bounded to templates such as `/users/:id`, not raw URLs.
- You have access to the metrics or APM query system.

## Steps

1. **Find the latency metric.** Identify histogram or distribution metrics such as `http_request_duration_seconds_bucket`. → *Expect:* the metric includes service, route, method, status, and environment labels.
2. **Check label cardinality.** Query distinct route or endpoint labels in the monitoring UI. → *Expect:* labels are bounded and do not contain user IDs or query strings.
3. **Write percentile queries.** For Prometheus histograms, use `histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{service="<service>"}[5m])) by (le, route))`. → *Expect:* the query returns p95 latency by route.
4. **Add p50, p95, and p99 panels.** Display median and tail latency on the same dashboard or adjacent panels. → *Expect:* tail behavior is visible separately from typical requests.
5. **Filter failed or irrelevant traffic when needed.** Exclude health checks and optionally separate 5xx responses. → *Expect:* latency reflects the intended user journey.
6. **Validate against a synthetic request.** Run `curl -w 'time_total=%{time_total}\n' -o /dev/null -s https://<host>/<path>`. → *Expect:* observed latency is plausible relative to dashboard values.
7. **Document thresholds.** Record expected p95 and p99 targets or SLO thresholds. → *Expect:* responders can tell normal latency from degraded latency.

## Decision points

- Only averages exist → add histogram or distribution instrumentation before claiming percentiles.
- Histograms are client-side aggregated → ensure buckets are appropriate for service latency ranges.
- Very low traffic route → use longer windows or avoid interpreting sparse percentiles.
- Vendor APM available → compare trace-derived percentiles with metric-derived percentiles.

## Failure modes & recovery

- **F1 Bad histogram query:** detect p95 values lower than p50 or always zero → aggregate by `le` correctly and use `rate()` over bucket counters.
- **F2 Missing slow requests:** detect traces show slow calls but dashboard does not → verify instrumentation coverage and route filtering.
- **F3 Cardinality explosion:** detect route labels with raw IDs → normalize routes in middleware and drop bad labels.
- **F4 Unit confusion:** detect seconds shown as milliseconds or vice versa → set panel units and convert consistently.

## Verification

The metrics backend returns non-empty p50, p95, and p99 latency values for the service over the last hour, and a manual `curl -w '%{time_total}'` sample is within a plausible range of the displayed request duration distribution.

## Variations

- `Prometheus`: use `histogram_quantile()` over `_bucket` series.
- `OpenTelemetry`: export explicit bucket histograms or exponential histograms depending on backend support.
- `Datadog/New Relic`: use distribution metrics or APM latency percentiles from the vendor UI.
- `Logs only`: compute approximate percentiles from structured duration fields as a temporary bridge.

## Safety & privacy

Low operational risk. Avoid high-cardinality route labels and do not put raw URLs, query strings, customer IDs, or request bodies into metric dimensions.
