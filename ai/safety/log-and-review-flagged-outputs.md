---
name: log-and-review-flagged-outputs
domain: ai
subdomain: safety
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Capture flagged LLM outputs for audit and human review without leaking sensitive data, then measure review throughput, agreement, and remediation.

## Preconditions

- A moderation or policy layer that emits categories, confidence, and action.
- Secure logging/storage with role-based access and retention limits.
- A reviewer workflow with labels, escalation paths, and appeal handling.

## Steps

1. **Define what gets logged.** Include request id, policy category, model version, prompt/output hashes, redacted snippets, and action. → *Expect:* the log schema excludes unnecessary raw secrets by default.
2. **Redact before persistence.** Run PII/secret scrubbing on prompts and outputs before writing review records. ⚠️ *Data leaves your control:* if logs go to a third-party observability tool, scrub and contractually approve the transfer first. → *Expect:* stored records contain placeholders for blocked sensitive fields.
3. **Create the review queue.** Route high-severity or uncertain cases to human review with priority and SLA. → *Expect:* flagged records appear in a queue with status `open`.
4. **Record reviewer decisions.** Capture label, rationale, policy version, and required remediation. → *Expect:* each reviewed item transitions to `confirmed`, `dismissed`, or `escalated`.
5. **Measure quality and throughput.** Track queue age, reviewer agreement, false positives, false negatives from appeals, and category trends. → *Expect:* dashboard metrics update from the review table.
6. **Feed fixes back into evals.** Convert confirmed misses and representative false positives into regression tests. → *Expect:* new test cases reference review ids and policy versions.

## Decision points

- Logs contain unsanitized PII → stop export, purge where possible, and fix scrubber before resuming.
- Queue SLA is missed → sample lower-risk categories or add reviewer capacity.
- Reviewer disagreement is high → clarify policy and add calibration rounds.

## Failure modes & recovery

- **F1 Sensitive log leak:** detect raw credentials or PII in logs → revoke exposed secrets, purge logs if possible, and add pre-log tests.
- **F2 Missing provenance:** detect flagged output without model/policy version → block deployment until logging middleware is complete.
- **F3 Review backlog:** detect queue age above SLA → adjust thresholds or staffing and prioritize high severity.
- **F4 Feedback not applied:** detect repeated failure category → add regression tests and assign owner.

## Verification

A synthetic flagged-output test writes a review record with required provenance, redaction tests find zero raw PII/secret fixtures in stored logs, queue metrics report open/closed counts, and at least one reviewed failure is automatically exported into the regression test set.

## Variations

- `internal review tool`: best for sensitive data; requires access controls and audit logs.
- `third-party observability`: convenient dashboards; scrub before export and verify retention.
- `regulated workflow`: add dual review, immutable audit trails, and formal escalation.

## Safety & privacy

This is high risk because logs can concentrate sensitive prompts, model errors, and user data. Minimize raw text, encrypt records, restrict reviewer access, set retention limits, and document when data is exported to external systems.
