---
name: enforce-least-privilege-access
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You reduce an account, service, token, or role to the minimum permissions required and verify the intended workflow still succeeds while unauthorized actions fail.

## Preconditions

- The actor, resource, and required actions are clearly identified.
- Access to audit logs, IAM/RBAC configuration, and a safe test environment.
- Approval from the resource owner for permission changes.

## Steps

1. **Inventory current permissions.** Export the role or policy, such as `aws iam get-role-policy`, `kubectl auth can-i --list --as <subject>`, or the platform access report. → *Expect:* current grants are captured for rollback and review.
2. **Map required actions to real workflows.** List the exact read/write/admin operations the actor must perform. → *Expect:* every required permission has a business or runtime reason.
3. **Remove broad grants from a proposed policy.** Replace wildcards like `*`, admin roles, all-repository access, or cluster-wide rights with resource-scoped permissions. → *Expect:* the proposed policy is narrower than the current one.
4. **Test allowed actions.** In staging or with a dry-run identity, run the normal workflow. Example: `kubectl auth can-i get pods --namespace app --as system:serviceaccount:app:worker`. → *Expect:* required actions return yes or succeed.
5. **Test denied actions.** Try representative out-of-scope actions, such as delete, admin, or access to another namespace/project. → *Expect:* denied actions return no, 403, or access denied.
6. **Apply the least-privilege policy.** Roll out through infrastructure-as-code or the platform UI with owner review. → *Expect:* the actor has the new policy and old broad grants are removed.
7. **Monitor audit logs after rollout.** Watch denied events for the actor during a normal cycle. → *Expect:* no required workflow is blocked, and denied events are expected out-of-scope attempts.

## Decision points

- Required actions are unknown → run in audit/report mode before enforcing.
- Permission is production-admin → require explicit human approval and break-glass alternative.
- Service uses shared credentials → split credentials per service before trimming permissions.
- Denied events show legitimate work → add the narrow missing permission instead of restoring admin.

## Failure modes & recovery

- **F1 Production workflow blocked:** detect access denied in logs or failing jobs → restore the captured previous policy temporarily and add narrow permissions.
- **F2 Hidden shared account:** detect multiple services using one role → create separate roles and migrate consumers one at a time.
- **F3 Policy syntax error:** detect deploy failure or invalid policy → validate with platform policy tools before applying.
- **F4 Overbroad exception:** detect wildcard added during recovery → add an expiry and replace with resource-scoped grants.

## Verification

The normal workflow command exits 0, an out-of-scope command returns 403/access denied, and audit logs show the actor using only the approved permissions after rollout.

## Variations

- `AWS/GCP/Azure`: use IAM policy simulators and condition/resource scopes.
- `Kubernetes`: use `kubectl auth can-i` and namespace-scoped Roles instead of ClusterRoles when possible.
- `GitHub/GitLab`: prefer fine-grained tokens, protected environments, and repository-scoped access.

## Safety & privacy

Medium risk because permission reductions can break services. Keep a rollback policy snapshot, avoid shared credentials, protect audit logs, and require review for production or admin access changes.
