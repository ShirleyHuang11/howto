---
name: set-up-an-alert-on-error-rate
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

You create an error-rate alert that fires when real user impact is likely and routes to the right responder with useful context.

## Preconditions

- Request metrics or logs include total requests and failed requests by service or route.
- You know the service owner, paging policy, and acceptable error budget.
- You can create alerts in the monitoring system.

## Steps

1. **Define the failure signal.** Use 5xx responses for server errors, or a documented application error metric for non-HTTP systems. → *Expect:* the alert measures user-impacting errors, not expected 4xx validation failures.
2. **Write the query.** For Prometheus, use `sum(rate(http_requests_total{service="<service>",status=~"5.."}[5m])) / sum(rate(http_requests_total{service="<service>"}[5m]))`. → *Expect:* the query returns a numeric error ratio.
3. **Set threshold and duration.** Choose a threshold such as `> 0.05 for 10m`, adjusted for service volume and SLO. → *Expect:* the alert avoids single-sample noise but catches sustained impact.
4. **Add a minimum traffic guard.** Add a condition like `sum(rate(http_requests_total{service="<service>"}[5m])) > 1`. → *Expect:* low-traffic periods do not page on one isolated failure.
5. **Configure routing and severity.** Send pages to the owning team for high severity and tickets or chat for lower severity. → *Expect:* the alert has owner, severity, runbook link, and dashboard link.
6. **Test the expression.** Evaluate the query over recent known incidents and normal periods. → *Expect:* it would have fired during real incidents and stayed quiet during healthy windows.
7. **Create and enable the alert.** Save the alert rule in code or the monitoring UI and deploy it. → *Expect:* the rule appears active and evaluation status is healthy.

## Decision points

- Very low traffic service → alert on absolute error count plus synthetic checks instead of percentage alone.
- Route-specific SLOs → alert on route templates only when label cardinality is controlled.
- Batch jobs → use failed job count or success freshness instead of HTTP error rate.
- No runbook exists → create a minimal runbook before enabling paging.

## Failure modes & recovery

- **F1 No data:** detect alert evaluation state `NoData` or empty query → fix metric names, labels, scrape targets, or time range.
- **F2 Too noisy:** detect repeated alerts without action needed → add traffic guard, increase duration, or move to lower severity.
- **F3 Missed incident:** detect user impact without alert → lower threshold, add route-level signal, or alert on burn rate.
- **F4 Wrong routing:** detect pages to an unrelated team → update service ownership labels and notification policy.

## Verification

The alert rule evaluates successfully in the monitoring system, its query returns a numeric value for the service, and a test notification reaches the expected channel or on-call route without exposing secrets.

## Variations

- `Prometheus/Alertmanager`: define a `PrometheusRule` with `expr`, `for`, `labels`, and `annotations`.
- `Datadog`: use a metric monitor with multi-alert by service or environment.
- `Grafana Alerting`: create the rule with contact points, notification policies, and no-data behavior.
- `SLO burn rate`: use fast and slow burn alerts tied to error budget consumption.

## Safety & privacy

Medium risk because alert changes affect on-call load and incident response. Avoid customer identifiers in notifications, route to least necessary audiences, and review paging alerts with the owning team before enabling production notifications.
