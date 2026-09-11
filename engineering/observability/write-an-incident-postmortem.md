---
name: write-an-incident-postmortem
domain: engineering
subdomain: observability
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h-2h
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You produce a blameless incident postmortem that records impact, timeline, root causes, contributing factors, and concrete follow-up work.

## Preconditions

- The incident is mitigated or stable enough that responders can shift to documentation.
- You have access to alerts, dashboards, logs, deployment history, chat notes, and ticket links.
- The organization has a postmortem template or review process.

## Steps

1. **Open the template.** Create a postmortem doc from the standard template with incident ID, title, date, severity, owners, and status. → *Expect:* a draft exists in the shared incident location.
2. **Record customer impact.** Summarize affected users, duration, symptoms, data loss if any, and business impact. → *Expect:* impact is specific and measurable where data allows.
3. **Build the timeline.** Add detection, escalation, mitigation, recovery, and relevant deploy/configuration events with timestamps and timezone. → *Expect:* readers can follow what happened in chronological order.
4. **Add evidence links.** Link dashboards, alert pages, log queries, traces, deploys, PRs, and rollback commands. → *Expect:* every major claim has a reproducible source.
5. **Analyze causes blamelessly.** Separate trigger, root cause, and contributing factors without naming individuals as causes. → *Expect:* the analysis explains system conditions and decision points.
6. **List what went well and poorly.** Capture detection, response, tooling, communication, and recovery observations. → *Expect:* the team can preserve strengths and improve weaknesses.
7. **Create action items.** Write owner, priority, due date, and success criterion for each follow-up. → *Expect:* action items are trackable tickets, not vague intentions.
8. **Review and publish.** Share with responders and service owners, resolve factual corrections, and mark the postmortem final. → *Expect:* the final document is discoverable and action items are assigned.

## Decision points

- Impact is uncertain → state the uncertainty and add a follow-up to improve measurement.
- Legal or customer communication needed → coordinate with incident command, support, legal, or communications before publishing broadly.
- Human error appears central → analyze system safeguards, tooling, review, and training rather than blaming the person.
- Action items are too broad → split them into smaller tickets with programmatic completion checks.

## Failure modes & recovery

- **F1 Missing timeline data:** detect unknown timestamps or conflicting accounts → reconcile from alert history, deploy logs, and chat exports, noting uncertainty.
- **F2 Blameful language:** detect phrases centered on personal fault → rewrite around system behavior and missing safeguards.
- **F3 Unowned actions:** detect action items without owners or dates → assign owners before final review.
- **F4 Stale postmortem:** detect draft not reviewed after several days → schedule a review meeting and link unresolved questions.

## Verification

The postmortem document contains impact, timeline, root cause, contributing factors, evidence links, and action items with owners and due dates, and every action item exists as a trackable ticket or issue.

## Variations

- `SEV process`: include severity, incident commander, communications lead, and review sign-off.
- `Regulated environments`: include audit evidence, data exposure assessment, and approval history.
- `Small teams`: keep the document lightweight but still include timeline, impact, cause, and actions.

## Safety & privacy

Low operational risk, but postmortems may include customer impact and sensitive infrastructure details. Redact personal data, restrict drafts appropriately, and coordinate external-facing statements through the approved process.
