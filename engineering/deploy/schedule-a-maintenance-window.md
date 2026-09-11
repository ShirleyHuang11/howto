---
name: schedule-a-maintenance-window
domain: engineering
subdomain: deploy
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

You schedule planned maintenance with a clear time window, owner, customer communication, rollback plan, and programmatic checks for starting and ending the work.

## Preconditions

- The maintenance task, expected user impact, and rollback path are known.
- Access to the status page, calendar, incident channel, and deployment or operations console.
- Stakeholders for affected services have reviewed the timing.
- Monitoring dashboards and health checks exist for the affected system.

## Steps

1. **Define the exact scope and impact.** Write the service name, user-visible effect, start time, end time, and rollback trigger. → *Expect:* a concise maintenance plan with no ambiguous systems.
2. **Choose a low-traffic window.** Check traffic and business calendars; avoid launches, billing runs, and regional peak hours. → *Expect:* the selected window has lower expected impact and stakeholder approval.
3. **Create the calendar event and incident channel.** Add owners, reviewers, and links to the runbook and dashboards. → *Expect:* participants have an invite and a single coordination channel.
4. **Publish customer notice if users are affected.** Update the status page or send approved customer communications. → *Expect:* the notice displays start/end times, affected service, and expected impact.
5. **Prepare the preflight checklist.** Include backup status, current deploy version, rollback command, and health check command such as `curl -fsS https://app.example.com/healthz`. → *Expect:* every checklist item has an owner and pass/fail criterion.
6. **Run pre-maintenance verification.** Execute health checks and confirm monitoring is green before starting. → *Expect:* baseline health is normal, or the window is paused before adding more risk.
7. **Announce start of work.** Post in the coordination channel and mark the status page as under maintenance at the scheduled time. → *Expect:* all participants know the window is active.
8. **Announce completion or rollback.** After work, run verification and update the status page to operational or rollback status. → *Expect:* the final state is visible to users and stakeholders.

## Decision points

- Maintenance can cause data loss or downtime → require explicit approval from service owner and incident commander.
- Preconditions fail before the window → postpone rather than starting from a degraded baseline.
- Work exceeds the window → roll back or publish an extension before the posted end time.
- Customer impact differs from the notice → update the status page immediately with corrected impact.

## Failure modes & recovery

- **F1 Missing approver:** detect no service owner or reviewer in the event → reschedule or block until accountable owners are present.
- **F2 Bad baseline:** detect health checks failing before work starts → cancel the window and treat the baseline issue separately.
- **F3 Communication drift:** detect status page and internal channel disagree → update the public status first, then sync internal notes.
- **F4 Rollback unclear:** detect no tested rollback command → do not start high-risk work until rollback is rehearsed or a backup exists.

## Verification

The calendar event, status page notice, runbook link, rollback plan, and health check command exist before the window; after completion, `curl -fsS -o /dev/null -w '%{http_code}\n' https://app.example.com/healthz` returns `200` and the status page is back to operational.

## Variations

- `Statuspage`: schedule maintenance with affected components and automatic reminder notifications.
- `GitHub deployments`: link the planned deployment or environment change in the calendar event.
- `Internal-only maintenance`: use an internal status page or Slack announcement but keep the same owner and rollback structure.

## Safety & privacy

Medium risk because maintenance coordinates changes that may affect users. Do not publish internal hostnames, secrets, or vulnerability details in public notices; state user impact plainly and keep rollback authority explicit.
