---
name: set-up-a-deploy-on-merge
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: high
prerequisites: [engineering/cicd/set-up-a-ci-pipeline]
status: draft
last_verified: 2026-09-11
---

## Goal

You configure CI/CD to deploy automatically after a change merges to the chosen branch, with tests, secrets, environment targeting, and post-deploy verification in place.

## Preconditions

- The normal CI pipeline is green and required before merge.
- Deployment credentials are available through the CI secret store with least privilege.
- The target environment, deploy command, rollback path, and health check are known.
- The team has approved automatic deploys for the branch and environment.

## Steps

1. **Define the deploy trigger and target.** Choose the branch and environment, such as pushes to `main` deploying to staging or production. → *Expect:* a written mapping from branch to environment.
2. **Confirm the deploy command manually in a safe environment.** Run the equivalent staging deploy command from CI documentation, not against production first. → *Expect:* the command completes and updates the intended environment.
3. **Store deploy credentials in CI secrets.** Add tokens or cloud role configuration through the provider UI or CLI. → *Expect:* secrets are available to the deploy job and masked in logs.
4. **Add a deploy job after tests.** [GitHub Actions | GitLab CI] make the job depend on successful test/build jobs and run only on the merge branch. → *Expect:* deploy does not run for unmerged pull requests.
5. **Pin artifact or image identity.** Deploy the artifact, image digest, or commit SHA built by CI. → *Expect:* the deployed version can be traced to the exact source commit.
6. **Add post-deploy health verification.** Run `curl -fsS "https://example.com/health"` or provider-specific health checks after deploy. → *Expect:* the job fails if the service is not healthy.
7. **Test with a non-production merge.** Merge a harmless change to the configured staging branch or environment. → *Expect:* tests pass, deploy runs once, and health check succeeds.
8. **Enable production only after approval.** ⚠️ *Irreversible:* automatic production deploys affect live users; confirm branch protection, rollback, monitoring, and on-call coverage before enabling. → *Expect:* production deploys happen only from the approved branch with green prerequisites.

## Decision points

- Deploy requires human judgment → add manual approval instead of fully automatic production deploy.
- Builds and deploys happen in separate jobs → pass immutable artifacts, not a rebuilt source tree.
- Health check is shallow → add smoke tests for the critical user path before marking deploy successful.
- Multiple environments exist → use CI environment protections and separate credentials for each.

## Failure modes & recovery

- **F1 Deploy runs on pull requests:** detect environment changes from unmerged branches → restrict triggers and require protected environments.
- **F2 Wrong artifact deployed:** detect version endpoint differs from commit SHA → deploy immutable artifact digest from the build job.
- **F3 Health check fails after deploy:** detect non-2xx or timeout → trigger rollback, stop further rollout, and inspect deploy logs.
- **F4 Secret printed in logs:** detect token text or credential JSON in output → revoke/rotate secret and mask variables correctly.

## Verification

After a merge to the configured branch, CI shows tests green, exactly one deploy job for the target environment exits 0, and `curl -fsS "https://example.com/health"` returns success with the deployed version matching the merge commit SHA or artifact digest.

## Variations

- `GitHub Actions`: use branch filters, `needs`, environments, and OIDC cloud credentials where available.
- `GitLab CI`: use `only`/`rules`, environments, protected variables, and deployment approvals.
- `Kubernetes`: deploy image digests with `kubectl rollout status deployment/app --timeout=5m`.
- `PaaS`: use provider CLIs and verify release IDs through the platform API.

## Safety & privacy

High risk for production deploys. Use least-privilege credentials, protected branches, immutable artifacts, health checks, rollback automation, and explicit approval before enabling automatic live deploys. Never expose deployment tokens in logs.

