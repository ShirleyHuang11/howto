---
name: set-up-uptime-monitoring
domain: engineering
subdomain: observability
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You create an external uptime check that verifies a service is reachable from outside its runtime environment and alerts the right owner when it fails.

## Preconditions

- The service has a stable URL and a health or lightweight synthetic endpoint.
- You have access to an uptime provider such as Pingdom, Better Stack, Datadog, Grafana Cloud, CloudWatch Synthetics, or Google Cloud Monitoring.
- Notification routes and escalation policies are known.

## Steps

1. **Choose the check endpoint.** Prefer `https://<host>/health` or a synthetic user journey that does not mutate data. → *Expect:* the endpoint returns success only when the service can serve users.
2. **Verify manually.** Run `curl -fsS -o /dev/null -w '%{http_code}\n' https://<host>/health`. → *Expect:* the command prints `200` or the expected success code.
3. **Configure the monitor.** Set URL, method, expected status, timeout, and check interval, such as every 1 minute from multiple regions. → *Expect:* the monitor validates and starts running.
4. **Add content validation if useful.** Check for a stable response string or JSON field, not a brittle full page body. → *Expect:* false positives from generic error pages are reduced.
5. **Set notification policy.** Route failures to the service owner with escalation, runbook, dashboard, and status page links. → *Expect:* alerts go to the expected channel or on-call service.
6. **Test notifications.** Use the provider's test alert feature or temporarily point a non-production check at a failing endpoint. → *Expect:* the expected recipient receives a test notification.
7. **Record ownership.** Add monitor name, URL, owner, and runbook link to service docs or infrastructure code. → *Expect:* future responders know who owns the check.

## Decision points

- Endpoint requires auth → use a dedicated low-privilege synthetic credential stored as a secret.
- Global users → run checks from multiple regions and alert on regional patterns.
- Maintenance windows → configure planned maintenance rather than disabling monitors manually.
- Mutating journey needed → create isolated test data and cleanup steps.

## Failure modes & recovery

- **F1 False outage:** detect alerts while internal metrics are healthy → check DNS, TLS, WAF, region-specific networking, and content matcher brittleness.
- **F2 No alert delivered:** detect failed test notification → fix routing, escalation policy, or integration permissions.
- **F3 Check blocked:** detect 403 from WAF or bot protection → allowlist provider ranges or use authenticated synthetic checks.
- **F4 Expired TLS:** detect certificate errors in monitor output → renew certificate and verify the chain externally.

## Verification

The uptime monitor shows passing status from at least one external location, `curl -fsS -o /dev/null -w '%{http_code}' https://<host>/health` returns the expected code, and a test notification reaches the configured route.

## Variations

- `CloudWatch Synthetics`: create a canary and alarm on failed runs.
- `Datadog Synthetics`: use API tests for endpoints and browser tests for user journeys.
- `Grafana Cloud`: use synthetic monitoring probes and Alertmanager contact points.
- `Status page`: wire uptime incidents to public status only after internal routing is correct.

## Safety & privacy

Medium risk because checks can page humans and synthetic credentials can be sensitive. Use non-mutating endpoints where possible, store credentials as secrets, and avoid exposing private URLs on public status pages.
