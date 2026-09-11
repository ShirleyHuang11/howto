---
name: back-out-a-merged-pull-request
domain: engineering
subdomain: version-control
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: [engineering/run-the-test-suite]
status: draft
last_verified: 2026-09-11
---

## Goal

Safely revert a merged pull request from the target branch and prove the rollback restores a passing build without rewriting shared history.

## Preconditions

- You know the merged PR number, merge commit SHA, or squash commit SHA.
- You have permission to push a revert branch and open a pull request.
- The test suite can run locally or in CI: `engineering/run-the-test-suite`.

## Steps

1. **Identify the merge artifact.** Find the merge commit or squash commit from the PR page or release notes. → *Expect:* you have one exact SHA that represents the merged PR.
2. **Create a revert branch from the current target.** Run `git switch -c revert/pr-123 origin/main` using the correct target branch. → *Expect:* the branch starts from the current shared branch tip.
3. **Revert without rewriting history.** [BRANCH: merge commit | squash commit] For a merge commit, run `git revert -m 1 MERGE_SHA`; for a squash commit, run `git revert SQUASH_SHA`. ⚠️ *Irreversible:* reverting production-impacting code can trigger deploy or data behavior changes, so confirm the incident owner, release branch, and database compatibility first. → *Expect:* Git creates a new revert commit or stops with conflicts.
4. **Resolve conflicts conservatively.** Keep the state that removes the bad PR while preserving later unrelated changes. → *Expect:* `git status` reports no unmerged paths after `git revert --continue`.
5. **Run the impacted checks.** Execute the fastest relevant checks first, then the full required suite, for example `pytest -q`. → *Expect:* checks exit 0 or identify a remaining dependency on the reverted code.
6. **Open a revert PR.** Include the original PR link, incident or bug ID, verification command output, and any deployment notes. → *Expect:* reviewers can see exactly what is being backed out and why.
7. **Wait for CI and required review.** Do not merge until required status checks pass and the owner approves. → *Expect:* CI is green on the revert PR.
8. **Merge and monitor.** Merge using the repository's normal strategy and watch production or staging health checks if the branch deploys. → *Expect:* the target branch contains the revert commit and health checks remain green.

## Decision points

- PR introduced a database migration → verify backward compatibility before reverting application code.
- Bad PR has follow-up commits depending on it → revert the minimal set in reverse dependency order.
- Immediate production outage → follow incident rollback policy, but still prefer a revert commit over force-pushing shared history.

## Failure modes & recovery

- **F1 Wrong parent for merge revert:** detect unexpectedly huge diff after `git revert -m` → abort with `git revert --abort`, inspect parents, and retry with parent 1 for the mainline branch.
- **F2 Conflict resolution removes later fixes:** detect unrelated files or behavior changes in the revert diff → restore those hunks and rerun tests.
- **F3 Revert does not fix failing check:** detect the same CI failure after revert → identify dependent commits and revert them or apply a targeted fix.
- **F4 Deployment still unhealthy:** detect failed health checks after merge → roll back the deployed version according to the platform runbook and keep the revert PR linked to the incident.

## Verification

Run the required project checks, for example `pytest -q` or `npm test`, and confirm they exit 0 on the revert branch. The revert PR's CI status is green, and after merge the target branch contains a new revert commit instead of rewritten history.

## Variations

- `GitHub`: the PR page's Revert button creates a revert PR for simple merges and squash merges.
- `GitLab`: use the Revert button on the merge request or commit page when available.
- `Release branch`: create the revert branch from the release branch, not default branch, then cherry-pick forward if needed.

## Safety & privacy

High risk because reverting merged production code can affect users and deployments. Confirm the target branch, migration compatibility, and incident owner before merge; do not force-push shared branches; keep customer data and incident details out of public PR text.
