---
name: build-a-monitoring-dashboard
domain: engineering
subdomain: observability
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You build a dashboard that shows service health, traffic, errors, latency, saturation, and recent changes in a form responders can use during incidents.

## Preconditions

- Metrics, logs, or traces are already flowing to a monitoring backend.
- You know the service name, environment labels, and owner.
- You have permission to create or edit dashboards.

## Steps

1. **Define the audience and use case.** Decide whether the dashboard is for on-call triage, release validation, capacity planning, or executive reporting. → *Expect:* panel choices match a concrete operational use.
2. **Add service selectors.** Create variables for environment, service, region, and cluster where supported. → *Expect:* viewers can filter without editing queries.
3. **Create traffic panels.** Add request rate or job throughput, for example `sum(rate(http_requests_total{service="$service",env="$env"}[5m]))`. → *Expect:* the dashboard shows current load and trends.
4. **Create error panels.** Add 5xx rate and error ratio panels. → *Expect:* spikes in failed requests are visible and comparable to traffic.
5. **Create latency panels.** Add p50, p95, and p99 latency from histograms or vendor percentiles. → *Expect:* tail latency is visible separately from median latency.
6. **Create saturation panels.** Add CPU, memory, queue depth, connection pool, or dependency usage panels. → *Expect:* resource pressure can be correlated with errors and latency.
7. **Add deploy and alert context.** Overlay deployment markers, link active alerts, and add a runbook link. → *Expect:* responders can connect symptoms to recent changes.
8. **Save and share.** Store dashboard JSON as code where possible or save in the monitoring UI with ownership metadata. → *Expect:* the dashboard has a stable URL and owner.

## Decision points

- Metrics are missing → add instrumentation before building placeholder panels.
- Labels differ by service → use dashboard variables and documented label conventions.
- Too many panels → keep the first screen to the golden signals and move deep dives lower.
- Public display needed → remove sensitive panels and use a read-only view.

## Failure modes & recovery

- **F1 Empty panels:** detect `No data` across normal time ranges → correct metric names, labels, environment selectors, or scrape status.
- **F2 Slow dashboard:** detect panels timing out → reduce cardinality, widen query intervals, or pre-aggregate metrics.
- **F3 Misleading units:** detect latency shown as raw seconds or milliseconds inconsistently → set panel units explicitly.
- **F4 Broken links:** detect runbook, alert, or trace links returning 404 → update URLs and ownership metadata.

## Verification

The saved dashboard URL loads successfully, core panels show non-empty data for the selected service over the last hour, and at least one traffic, error, latency, and saturation panel has a valid query result.

## Variations

- `Grafana`: store dashboard JSON in Git and provision it or import through the UI.
- `Datadog`: use dashboard widgets and template variables.
- `CloudWatch`: build metric math widgets and alarms together for AWS-native services.
- `Kibana/OpenSearch`: build dashboards around log-derived fields when metrics are unavailable.

## Safety & privacy

Low operational risk, but dashboards can expose internal URLs, customer identifiers, and business-sensitive traffic. Share with the smallest necessary audience and avoid panels that display raw logs or PII by default.
