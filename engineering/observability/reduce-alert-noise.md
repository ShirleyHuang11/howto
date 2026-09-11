---
name: reduce-alert-noise
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

You reduce noisy alerts without hiding real incidents, so paging signals are actionable and backed by tested alert rules.

## Preconditions

- Access to the alerting system, runbooks, recent incident history, and notification routing.
- A staging or preview path for alert-rule changes when the tool supports it.
- Agreement on which alerts are paging versus ticket-only.

## Steps

1. **Export the current alert set.** [BRANCH: Prometheus/Alertmanager, run `amtool config routes show` and keep alert rule files from the repo | Grafana, export alert rules from the UI/API | Datadog, export monitors with `datadog-ci monitors pull`] → *Expect:* a reviewable snapshot of current alert names, thresholds, routes, and owners.
2. **Measure noisy alerts from real history.** Query the last 14-30 days of alert events and group by alert name, service, and receiver. Example: `curl -s "$ALERT_API/events?from=$FROM&to=$TO" | jq '.events[] | .alert' | sort | uniq -c | sort -nr`. → *Expect:* a ranked list of the alerts that fire most often.
3. **Classify each noisy alert.** Mark it as duplicate, flaky input, wrong threshold, missing `for` duration, wrong severity, or genuinely urgent. → *Expect:* every candidate has a cause and proposed disposition.
4. **Change only one noise pattern at a time.** Add `for:` windows, widen thresholds from SLO data, route low-impact alerts to tickets, or group by stable labels. Example Prometheus change: `for: 10m` and `severity: ticket` for non-page symptoms. → *Expect:* a small diff that explains why the alert will page less.
5. **Preview or unit-test the rules.** [BRANCH: Prometheus, run `promtool check rules alerts.yml` and `promtool test rules alert-tests.yml` | Grafana, use rule preview | Datadog, validate monitor JSON before applying] → *Expect:* alert syntax validates and test cases still fire for real failure examples.
6. **Deploy the alert change during staffed hours.** Apply through the normal CI/config pipeline and watch the alerting UI. → *Expect:* the new rule version is active and no alert engine errors appear.
7. **Compare post-change alert volume.** After one normal traffic cycle, rerun the history query for the modified alerts. → *Expect:* reduced pages for the target alerts while synthetic or known-bad scenarios still alert.

## Decision points

- Alert has no owner → do not silence permanently; assign ownership or remove only after stakeholder review.
- Alert catches customer-impacting outages → prefer tuning `for`, grouping, or burn-rate logic over disabling it.
- Noise comes from missing telemetry labels → fix instrumentation before changing thresholds.
- Alert is purely informational → route to ticket/dashboard, not paging.

## Failure modes & recovery

- **F1 Masked outage:** detect an incident with no matching page → revert the alert diff and add a regression test for that scenario.
- **F2 Invalid rule deploy:** detect CI failure or alert engine parse errors → roll back to the exported snapshot and fix syntax locally.
- **F3 Notification black hole:** detect no notifications after route changes → send a test alert and restore the previous receiver route.
- **F4 Flapping continues:** detect repeated resolve/fire cycles → add hysteresis, a longer `for`, or fix the unstable metric source.

## Verification

`promtool check rules alerts.yml` exits 0, alert-rule tests exit 0, and the alert history query shows the target paging alert count decreased without removing the expected synthetic failure alert.

## Variations

- `Prometheus/Alertmanager`: use rule files, `promtool`, `amtool`, route grouping, and inhibition rules.
- `Grafana Alerting`: use rule preview, contact point test notifications, and provisioning files when available.
- `Datadog`: use monitor audit history, composite monitors, notification renotify settings, and monitor JSON validation.

## Safety & privacy

Medium risk because alert changes can hide production incidents. Keep an export of the old rules, avoid permanent silences as a substitute for fixes, do not paste incident data with secrets into tickets, and require review before disabling or downgrading a paging alert.
