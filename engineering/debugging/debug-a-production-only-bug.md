---
name: debug-a-production-only-bug
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You diagnose a bug that appears only in production without exposing sensitive data or making uncontrolled live changes, then verify the fix in a lower environment or with a guarded production check.

## Preconditions

- You have read-only access to production logs, metrics, traces, deployed version metadata, and feature-flag state.
- You know the incident window, affected user segment, endpoint, job, or workflow.
- You have an approved path for any production change, rollback, or feature-flag adjustment.
- Sensitive data handling rules are clear before inspecting production evidence.

## Steps

1. **Define the symptom and blast radius.** Record exact errors, timestamps, request IDs, affected versions, regions, tenants, and user-facing impact. → *Expect:* a bounded investigation target rather than a vague production issue.
2. **Compare production to staging.** Check deployed SHA, config, env vars, feature flags, schema version, traffic shape, and dependency versions. → *Expect:* a short list of production-only differences.
3. **Collect read-only evidence.** Query logs and traces by request ID or error signature, for example `kubectl logs deploy/api --since=30m | rg 'request_id=abc123|NullPointer'` only if policy permits. → *Expect:* correlated log, metric, or trace evidence without dumping unrelated user data.
4. **Reproduce with safe inputs.** Use a scrubbed payload, test tenant, or staging data snapshot to run the failing path locally or in staging. → *Expect:* a deterministic reproduction outside real user traffic, or a documented reason it cannot be reproduced.
5. **Add temporary observability behind a guard.** If evidence is insufficient, add structured logging or metrics that redact secrets and sample narrowly. → *Expect:* new telemetry identifies the branch, state, or dependency causing the bug.
6. **Mitigate before deep fixes when impact is active.** [BRANCH: feature flag | rollback | traffic shift] use the lowest-risk approved mitigation. ⚠️ *Irreversible:* production rollback, data repair, or config changes can affect live users; confirm owner approval, current version, and rollback plan first. → *Expect:* error rate or user impact decreases in production telemetry.
7. **Implement the durable fix.** Patch the production-only assumption, add a regression test using the captured safe case, and update config or migration code if needed. → *Expect:* tests fail before the fix and pass after it.
8. **Verify after release.** Watch dashboards, logs, and traces for the original signature after the fix or mitigation. → *Expect:* the signature stops or returns to the accepted baseline.

## Decision points

- Production and staging differ by config or flags → test the production config in staging before code changes.
- Only one tenant or region is affected → focus on data shape, regional dependency, cache, or rollout cohort.
- Active user impact is severe → prioritize mitigation or rollback over root-cause completeness.
- Evidence requires customer data access → escalate through the approved privacy and support workflow.

## Failure modes & recovery

- **F1 Cannot reproduce outside production:** detect staging and local passes → add narrow, redacted telemetry or create a scrubbed fixture from the failing shape.
- **F2 Mitigation worsens impact:** detect rising error rate or latency after flag/rollback → revert the mitigation using the pre-approved rollback plan.
- **F3 Missing deploy metadata:** detect unknown SHA or image tag → query CI, container registry digest, or release dashboard before comparing code.
- **F4 Logs contain sensitive data:** detect tokens, emails, or payload dumps → restrict the artifact, redact it, and follow incident policy for exposure.

## Verification

The regression test exits 0, for example `pytest -q tests/test_production_bug.py` or `npm test -- production-bug`, and production monitoring shows the original error signature at zero or accepted baseline for the agreed observation window.

## Variations

- `Kubernetes`: use read-only `kubectl logs`, `kubectl describe`, and deployment image digests; avoid exec into prod containers unless approved.
- `serverless`: compare function versions, aliases, environment variables, and cold-start metrics.
- `feature flags`: inspect targeting rules, percentage rollout, prerequisites, and flag evaluation logs.
- `database-backed bug`: compare schema version, query plan, data cardinality, and replica lag.

## Safety & privacy

High risk because production systems and user data may be involved. Prefer read-only investigation, redact all evidence, use test tenants, get explicit approval before live changes, and document every production action with timestamp and operator.

