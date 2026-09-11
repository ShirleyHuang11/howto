---
name: search-logs-to-diagnose-an-incident
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

You use logs to narrow an incident to affected services, time ranges, errors, and likely causes while preserving evidence.

## Preconditions

- Logs are available in a centralized system such as CloudWatch Logs, Datadog, Grafana Loki, Splunk, OpenSearch, or BigQuery.
- You know the incident start time, affected service, alert, request ID, trace ID, user-safe identifier, or endpoint.
- You have read access to production logs.

## Steps

1. **Set a bounded time window.** Start with the alert window, for example 15 minutes before and after first detection. → *Expect:* searches run against a focused period instead of all retention.
2. **Filter by service and environment.** Query `service:<service> env:prod` or equivalent labels. → *Expect:* results belong to the affected production service.
3. **Search for error severity.** Query `level:error OR level:fatal OR status:[500 TO 599]`. → *Expect:* recent failures and stack traces appear.
4. **Group repeated failures.** Aggregate by message, exception type, route, host, pod, or version. → *Expect:* the dominant error pattern is visible.
5. **Correlate with deployments.** Filter or facet by `version`, `build_sha`, or pod image, and compare before and after deploy time. → *Expect:* errors can be tied to or separated from a release.
6. **Follow one request.** Search by `request_id` or `trace_id` from a failed log line. → *Expect:* the request timeline shows upstream and downstream context.
7. **Save evidence.** Capture query URLs, timestamps, counts, and representative redacted log lines in the incident notes. → *Expect:* responders can reproduce the investigation without raw secret exposure.

## Decision points

- No structured fields → search text first, then add structured logging as a follow-up.
- One pod or host dominates → inspect container events, node health, and recent restarts.
- Errors correlate with a dependency → check dependency dashboards and timeouts next.
- Logs contain PII → redact before sharing outside the least-privilege responder group.

## Failure modes & recovery

- **F1 Missing logs:** detect gaps or no results for a known request → check ingestion pipeline, service labels, sampling, and retention.
- **F2 Too many matches:** detect millions of results → add service, route, version, host, or exact exception filters.
- **F3 Clock skew:** detect timestamps out of order across services → compare ingestion time and event time, then use trace IDs if available.
- **F4 Redaction needed:** detect tokens, emails, or payloads in logs → redact incident notes and file a logging hygiene follow-up.

## Verification

A saved query or documented log search returns the same dominant error pattern for the incident window, including count, affected service, time range, and at least one redacted representative event.

## Variations

- `Loki`: query labels first, then pipe filters, for example `{service="api",env="prod"} |= "error"`.
- `CloudWatch Logs Insights`: use `fields @timestamp, @message | filter level="error" | sort @timestamp desc | limit 50`.
- `Splunk`: use indexed fields such as `index=prod service=<service> status>=500`.
- `Datadog`: facet by service, env, version, and trace ID.

## Safety & privacy

Low operational risk, but high privacy sensitivity. Search with least-privilege access, do not paste raw customer data into public tickets, and preserve timestamps and query links so conclusions remain auditable.
