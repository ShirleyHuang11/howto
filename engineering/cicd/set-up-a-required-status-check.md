---
name: set-up-a-required-status-check
domain: engineering
subdomain: cicd
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: [engineering/cicd/set-up-a-ci-pipeline]
status: draft
last_verified: 2026-09-11
---

## Goal

You make a known-good CI check required before merging to a protected branch, so changes cannot land while the check is failing or missing.

## Preconditions

- The CI check has run successfully at least once on the target branch or a pull request.
- You have repository admin or maintainer permissions.
- The team agrees which branch and check names should be required.
- Emergency bypass and administrator policies are understood.

## Steps

1. **Confirm the exact check name.** Open a recent pull request or commit status page and copy the CI job name exactly. → *Expect:* a check name such as `ci / test (node 22)` is known.
2. **Open branch protection settings.** [GitHub | GitLab] navigate to repository settings for branch rules or protected branches. → *Expect:* the target branch rule is visible.
3. **Select the target branch pattern.** Choose `main`, `master`, `release/*`, or the team's protected branch pattern. → *Expect:* the rule applies to the intended branch only.
4. **Require status checks before merge.** Enable the status-check requirement and select the exact CI check. → *Expect:* the selected check appears in the required checks list.
5. **Configure stale-review and admin behavior intentionally.** Choose whether administrators are included and whether branches must be up to date before merge. → *Expect:* the rule matches team policy and does not surprise maintainers.
6. **Test with a pull request.** Open a PR with a passing CI run and another throwaway PR or commit that fails CI. → *Expect:* the passing PR is mergeable and the failing PR is blocked.
7. **Document the requirement.** Update contributor docs or team notes with the required check and recovery owner. → *Expect:* contributors know which check blocks merges.

## Decision points

- Check name is not listed → run the workflow on the branch first or verify app permissions.
- Multiple matrix jobs exist → require each supported matrix check or a single aggregate check.
- The check is flaky → fix flakiness before making it required.
- Hotfix branches need different rules → create separate branch patterns with narrower checks.

## Failure modes & recovery

- **F1 Required check never appears:** detect PR blocked with "expected" status → confirm the selected name exactly matches the CI-reported context.
- **F2 Flaky CI blocks everyone:** detect repeated red checks unrelated to changes → temporarily unrequire the check only with maintainer approval and file a fix.
- **F3 Wrong branch protected:** detect merges still bypass checks → adjust the branch pattern and verify the actual default branch.
- **F4 Admin bypass surprise:** detect admins can merge red PRs unexpectedly → enable admin enforcement if policy requires it.

## Verification

A pull request targeting the protected branch cannot be merged while the required CI check is failing or pending, and becomes mergeable when that exact check reports success.

## Variations

- `GitHub`: use Rulesets or Branch protection rules under repository Settings.
- `GitLab`: use Protected branches and Merge request approval/status check settings available for the project tier.
- `Bitbucket`: configure branch restrictions and required successful builds.
- `monorepo`: require an aggregate status if individual package jobs are dynamically generated.

## Safety & privacy

Medium risk because required checks can block all merges. Enable only stable checks, document an emergency path, and restrict admin changes to maintainers. Do not weaken branch protection to work around unrelated CI failures without team approval.

