---
name: set-a-log-retention-policy
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

You set a log retention period that meets debugging, compliance, privacy, and cost requirements without keeping logs indefinitely.

## Preconditions

- You know the log storage backend, log groups or indexes, and environments affected.
- Compliance, security, and incident-response retention requirements are known.
- You have permission to update retention policy for the log store.

## Steps

1. **Inventory current retention.** [BRANCH: CloudWatch | Datadog | Loki] Run `aws logs describe-log-groups --log-group-name-prefix <prefix> --query 'logGroups[].{name:logGroupName,retention:retentionInDays}'` or inspect equivalent backend settings. → *Expect:* current retention periods are visible.
2. **Classify log sensitivity.** Identify production, security, audit, application, access, and debug logs. → *Expect:* each log class has a retention need and data sensitivity level.
3. **Choose retention values.** Pick periods such as 7 days for debug logs, 30-90 days for application logs, and longer only where required. → *Expect:* values satisfy policy and reduce unnecessary storage.
4. **Get required approval.** For production, audit, or security logs, confirm with the owning team before shortening retention. → *Expect:* approval is recorded in a ticket or change request.
5. **Apply the retention policy.** For CloudWatch, run `aws logs put-retention-policy --log-group-name <name> --retention-in-days <days>`. → *Expect:* the command exits 0.
6. **Verify the setting.** Run `aws logs describe-log-groups --log-group-name-prefix <name> --query 'logGroups[0].retentionInDays'`. → *Expect:* the configured number of days is returned.
7. **Document exceptions.** Record any log group with longer or shorter retention and the reason. → *Expect:* future reviewers can explain deviations.

## Decision points

- Shortening production retention → confirm compliance and incident-response needs first.
- Logs contain PII → prefer shorter retention and stricter access controls.
- Audit logs → follow legal or regulatory retention requirements, which may be longer than application logs.
- Backend uses index lifecycle policies → update lifecycle templates rather than individual indexes.

## Failure modes & recovery

- **F1 Permission denied:** detect IAM or role errors → request least-privilege permission to manage retention for the specific log groups.
- **F2 Wrong log group:** detect setting applied to an unintended prefix → restore the prior retention and tighten selection filters.
- **F3 Compliance conflict:** detect required retention exceeds proposed value → keep the longer requirement and document it.
- **F4 Cost unchanged:** detect storage still rising → check archived tiers, duplicate sinks, and indexes outside the updated policy.

## Verification

The backend reports the expected retention value for every targeted log group or index, for example `aws logs describe-log-groups --log-group-name-prefix <name> --query 'logGroups[].retentionInDays'` returns `<days>` for each target.

## Variations

- `AWS CloudWatch Logs`: use `put-retention-policy` per log group.
- `Datadog`: configure retention by index and routing filters.
- `Grafana Loki`: configure per-tenant or per-stream retention in limits and compactor settings.
- `Elasticsearch/OpenSearch`: use Index Lifecycle Management policies.

## Safety & privacy

Medium risk because shortening retention can delete forensic evidence and lengthening retention can increase privacy exposure. Get approval before changing production, audit, or security logs, and avoid retaining sensitive logs longer than policy requires.
