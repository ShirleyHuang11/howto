---
name: schedule-a-recurring-agent
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent runs on a schedule with bounded permissions, cost, and side effects. Success means each scheduled run is triggered once per window, produces a structured result, and respects approval gates for user-visible or irreversible actions.

## Preconditions

- A scheduler such as cron, GitHub Actions, Airflow, Temporal, Cloud Scheduler, or a queue worker.
- A stable agent entrypoint that accepts a run config and returns structured status.
- Service credentials scoped to the scheduled task.

## Steps

1. **Define the recurring job contract.** Specify schedule, timezone, input query, allowed tools, max duration, max cost, and expected output schema. → *Expect:* a versioned job config contains all scheduling and budget fields.
2. **Make runs idempotent per window.** Generate a `run_key` from job ID and scheduled window; skip or resume if that key already exists. → *Expect:* duplicate triggers do not create duplicate runs or side effects.
3. **Use least-privilege credentials.** Grant only the reads and writes needed for the scheduled task. ⚠️ *Data leaves your control:* if the recurring agent sends data to model or API providers, minimize and redact the scheduled input data. → *Expect:* the agent cannot access unrelated resources in permission tests.
4. **Gate user-visible actions.** Draft emails, tickets, posts, purchases, or deletes as pending approvals unless the user explicitly authorized automation. ⚠️ *Irreversible:* confirm the action class, target, and automation policy before enabling auto-execution. → *Expect:* unapproved side effects remain in `pending_approval`.
5. **Add monitoring and alerts.** Track start, finish, duration, cost, failures, skipped duplicate windows, and approval backlog. → *Expect:* missed or failed runs raise an alert.
6. **Evaluate scheduled outputs.** Run assertions on schema, freshness, and task-specific quality before marking the job successful. → *Expect:* bad or stale outputs fail the job rather than being published.

## Decision points

- Task only reports information → auto-send summary if privacy policy allows.
- Task changes external state → require approval or a very narrow preapproved policy.
- Scheduler fires twice for the same window → deduplicate by `run_key`.
- Run exceeds duration or cost → stop and alert rather than continuing silently.

## Failure modes & recovery

- **F1 Duplicate execution:** detect same `run_key` twice → enforce uniqueness in durable storage.
- **F2 Silent failure:** detect missing run record for a window → add scheduler heartbeat and alerts.
- **F3 Stale input data:** detect source timestamp older than threshold → fail freshness check and retry later.
- **F4 Approval backlog:** detect many pending actions → summarize for the user and pause auto-drafting if needed.

## Verification

Run scheduler tests for one normal window, one duplicate trigger, one failing tool, and one approval-gated action. The normal run must produce schema-valid output, the duplicate must skip or resume the same run key, the failure must alert with a trace link, and the approval-gated action must not execute without the configured authorization.

## Variations

- `cron or GitHub Actions`: simple periodic jobs with logs and explicit secrets.
- `Temporal or Airflow`: durable scheduling, retries, and visibility for production workflows.
- `queue-based scheduler`: useful when many tenant-specific jobs need rate limiting.

## Safety & privacy

Medium risk because recurring agents can repeatedly spend money, expose data, or take actions while unattended. Scope credentials, cap cost, deduplicate windows, review data sent to providers, and require explicit opt-in for any automated external write.
