---
name: gate-a-deploy-with-manual-approval
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: high
prerequisites: [engineering/cicd/set-up-a-ci-pipeline]
status: draft
last_verified: 2026-09-11
---

## Goal

You add a manual approval gate before deployment so tests and build can run automatically, but release to the protected environment requires an authorized reviewer.

## Preconditions

- The deployment job already exists or its command is known.
- The CI provider supports protected environments, manual jobs, approvals, or deployment gates.
- The approval group and emergency process are defined.
- The target deployment has a rollback and health-check procedure.

## Steps

1. **Identify the environment that needs approval.** Choose production or another protected environment rather than every CI job. → *Expect:* only high-impact deploys are gated.
2. **Configure authorized approvers.** [GitHub Actions | GitLab CI] add required reviewers or mark the deploy job `when: manual` with protected environment permissions. → *Expect:* only approved users can release the job.
3. **Make deploy depend on green checks.** Ensure the approval gate appears after build, test, and security checks. → *Expect:* a reviewer cannot approve a deploy from a red pipeline.
4. **Display release evidence before approval.** Include artifact digest, commit SHA, changelog link, migration status, and health-check target in the CI summary or release notes. → *Expect:* approvers can review what will be deployed.
5. **Add post-approval health checks.** Run `curl -fsS "https://example.com/health"` or `kubectl rollout status deployment/app --timeout=5m`. → *Expect:* approved deploys still fail if the environment is unhealthy.
6. **Test the gate on staging or a dry-run environment.** Trigger the pipeline and verify it pauses before deployment. → *Expect:* deploy does not begin until an authorized approval is recorded.
7. **Document approval criteria.** Record who approves, what they check, and what to do when the deploy fails. → *Expect:* release operators have a repeatable checklist.
8. **Enable the gate for production.** ⚠️ *Irreversible:* a production deploy can affect live users; confirm approver list, rollback owner, and monitoring before making the gate active. → *Expect:* production releases require explicit approval.

## Decision points

- Release is low-risk staging → use automatic deploys and reserve manual gates for production.
- Migrations are included → require database owner review before approval.
- Emergency hotfix needed → use the documented bypass path and record the reason.
- Approver is also the author → decide whether separation of duties is required by policy.

## Failure modes & recovery

- **F1 Gate can be bypassed:** detect deploy job runs without approval → tighten environment protection and branch rules.
- **F2 Wrong approver group:** detect unauthorized or missing reviewers → update environment reviewers and audit permissions.
- **F3 Approval happens before artifact is built:** detect deploy rebuilds after approval → approve an immutable artifact or commit SHA.
- **F4 Manual job stuck forever:** detect no owner responds → page the release owner or cancel the pipeline according to policy.

## Verification

A pipeline targeting the protected environment pauses at the approval gate, records an authorized approval, then runs the deploy and health-check jobs to exit 0; without approval, no deployment starts.

## Variations

- `GitHub Actions`: use environments with required reviewers and deployment protection rules.
- `GitLab CI`: use manual jobs with protected environments and role restrictions.
- `CircleCI`: use approval jobs in workflows before deploy jobs.
- `cloud deploy tools`: use platform release approvals when CI delegates deployment to another system.

## Safety & privacy

High risk because this controls live releases. Keep approver groups small and role-based, expose only necessary release metadata, and never include secrets in approval summaries or logs.

