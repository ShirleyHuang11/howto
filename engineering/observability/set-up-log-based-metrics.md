---
name: set-up-log-based-metrics
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

You turn structured log events into low-cardinality metrics that can power dashboards and alerts without overloading the logging or metrics backend.

## Preconditions

- Logs are centralized and include structured fields such as service, environment, level, route, status, or event name.
- Access to the log platform and metrics/alerting configuration.
- A clear metric question, such as error count, payment failures, or job retries.

## Steps

1. **Define the metric from a log query.** Write the exact log filter, such as `service:api env:prod level:error` or `{service="api"} |= "payment_failed"`. → *Expect:* the query returns only events that should increment the metric.
2. **Check sample events and fields.** Inspect recent matching logs for stable fields and sensitive data. → *Expect:* required labels exist and no secret/customer payload fields are needed.
3. **Choose low-cardinality labels.** Use labels like `service`, `env`, `status_class`, or `error_type`; avoid request ID, user ID, email, raw URL, or stack trace labels. → *Expect:* estimated time-series count is bounded.
4. **Create the log-based metric.** [BRANCH: Cloud Logging, create a logs-based counter metric | Datadog, create a log facet/metric | Grafana Loki, use recording rules | Splunk, save a scheduled search to metrics] → *Expect:* the platform accepts the metric definition.
5. **Backtest the query window.** Compare the metric count to the raw log query for the same interval. → *Expect:* counts match or the difference is explained by ingestion delay/sampling.
6. **Add dashboard and alert usage.** Plot the metric and create an alert only after normal baseline is visible. → *Expect:* the graph is populated and thresholds are based on real rates.
7. **Monitor cardinality and cost.** Inspect series count, ingestion volume, and alert noise after one traffic cycle. → *Expect:* metric volume remains within platform limits and budget.

## Decision points

- Logs are unstructured → add structured logging before building the metric.
- Metric needs per-user labels → use logs/search for investigation, not metrics labels.
- Ingestion delay is high → do not use the metric for tight real-time paging.
- Query matches noisy debug logs → tighten the filter or raise log level quality first.

## Failure modes & recovery

- **F1 Cardinality explosion:** detect too many series or high cost → remove high-cardinality labels and recreate the metric.
- **F2 Metric undercounts:** detect raw logs exceed metric count → check ingestion delay, sampling, and filter mismatch.
- **F3 Sensitive label exposure:** detect PII/secrets in labels → delete/recreate metric without that label and review retention.
- **F4 Alert flaps:** detect frequent short alerts → add rolling windows, burn-rate logic, or threshold tuning.

## Verification

For a fixed interval, the log query count and log-based metric count match within expected ingestion delay, the dashboard shows current data, and any alert query evaluates successfully in the platform.

## Variations

- `Google Cloud Logging`: use counter or distribution logs-based metrics and monitor label cardinality.
- `Datadog`: generate metrics from indexed logs and watch custom metric count.
- `Loki/Grafana`: prefer recording rules from LogQL aggregations and avoid dynamic labels.

## Safety & privacy

Medium risk because logs often contain sensitive data and high-cardinality labels can create large costs. Never use raw user identifiers as metric labels, keep retention appropriate, and review filters before alerting.
