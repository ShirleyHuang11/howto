---
name: store-a-secret-in-ci
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You store a credential in the CI provider's secret manager, reference it from jobs without printing it, and verify that the job can authenticate with least privilege.

## Preconditions

- You know the exact CI project, environment, and jobs that need the secret.
- The credential has the minimum permissions required and can be rotated.
- You have permission to manage CI secrets.
- You have a non-production test credential when possible.

## Steps

1. **Define the secret scope and name.** Choose a clear name such as `STAGING_API_TOKEN` and limit it to the repository, environment, or protected branch that needs it. → *Expect:* the secret name and scope are documented.
2. **Create or retrieve a least-privilege credential.** Prefer short-lived tokens, cloud OIDC roles, or environment-specific service accounts over broad personal tokens. → *Expect:* the credential can perform only the required action.
3. **Store the secret in CI settings.** [GitHub Actions | GitLab CI] add it through repository/environment secrets or CI/CD variables with masking and protection enabled where supported. → *Expect:* the value is saved and not visible after storage.
4. **Reference the secret in the job.** Use provider syntax such as `${{ secrets.STAGING_API_TOKEN }}` or `$STAGING_API_TOKEN` only in the step that needs it. → *Expect:* the job receives the secret as an environment variable.
5. **Add a non-revealing authentication check.** Run a command such as `curl -fsS -H "Authorization: Bearer $STAGING_API_TOKEN" "https://api.example.com/health" >/dev/null`. → *Expect:* the command exits 0 without printing the token.
6. **Verify masking.** Intentionally print only a derived safe value such as token length or a fixed message, never the secret itself. → *Expect:* CI logs do not contain the credential.
7. **Record rotation and ownership.** Add the owner, purpose, creation date, and rotation process to the internal secret inventory. → *Expect:* future maintainers know how to rotate or remove it.
8. **Rotate if a live secret was exposed or copied insecurely.** ⚠️ *Irreversible:* rotating or revoking a live credential can break deployments; confirm dependent jobs and rollback path before invalidating the old secret. → *Expect:* new secret works before old credential is revoked when overlap is possible.

## Decision points

- Cloud provider supports OIDC federation → use OIDC instead of storing a long-lived cloud key.
- Secret is needed only for production deploy → scope it to the protected production environment.
- Pull requests from forks run CI → do not expose secrets to untrusted fork workflows.
- Secret must be shared across repositories → use organization/group-level secrets with narrow repository allowlists.

## Failure modes & recovery

- **F1 Secret unavailable in job:** detect empty variable or auth failure → check environment scope, protected branch rules, and variable name spelling.
- **F2 Secret printed in logs:** detect raw credential in CI output → revoke/rotate it and remove the log artifact if possible.
- **F3 Overprivileged token:** detect token can access unrelated resources → replace it with a scoped service account or role.
- **F4 Forked PR exposure risk:** detect workflow runs untrusted code with secrets → change triggers or require maintainer approval before secret-bearing jobs.

## Verification

The CI job using the secret exits 0 for a non-revealing authentication check, CI logs contain no raw secret value, and an unauthorized context such as an untrusted fork or unprotected branch cannot access the secret.

## Variations

- `GitHub Actions`: use repository, organization, or environment secrets; prefer OIDC for cloud deploys.
- `GitLab CI`: use masked, protected CI/CD variables and environment scopes.
- `CircleCI`: use project environment variables or restricted contexts.
- `Kubernetes deploys`: prefer CI-issued short-lived cloud credentials over static kubeconfig files.

## Safety & privacy

High risk because mishandled CI secrets can compromise infrastructure. Use least privilege, masking, environment protection, rotation records, and short-lived credentials where possible. Never paste secrets into repository files, pull request comments, or logs.

