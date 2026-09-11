---
name: open-a-pull-request
domain: engineering
subdomain: version-control
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You open a pull request from a feature branch to the correct base branch with enough context, tests, and metadata for reviewers and CI to evaluate it.

## Preconditions

- The feature branch is pushed to a remote.
- Local commits are intentional and the relevant tests pass.
- You know the target base branch and required reviewers or labels.

## Steps

1. **Confirm branch and upstream.** Run `git status --short --branch` and `git rev-parse --abbrev-ref --symbolic-full-name @{u}`. → *Expect:* the current branch tracks the intended remote branch.
2. **Compare against the target base.** Run `git fetch origin main` and `git diff --stat origin/main...HEAD`. → *Expect:* the diff contains only the intended files.
3. **Run validation before opening.** [pytest | Jest] run `pytest -q` or `npm test`. → *Expect:* the suite exits 0 or known unrelated failures are documented.
4. **Push the latest commits.** Run `git push`. → *Expect:* the remote branch is up to date.
5. **Create the pull request.** [GitHub Actions | GitLab CI] run `gh pr create --base main --head feature/descriptive-name --title "Clear title" --body-file pr-body.md` or use the GitLab merge request UI. → *Expect:* the host returns a PR/MR URL.
6. **Fill required metadata.** Add reviewers, labels, linked issue, release note, and test evidence. → *Expect:* the PR page shows required fields populated.
7. **Wait for initial checks.** Run `gh pr checks --watch` or inspect the CI page. → *Expect:* required status checks are pending, running, or green; red checks are visible with links.

## Decision points

- PR includes unrelated files → split or amend before requesting review.
- CI is red on first run → fix or document if the failure is unrelated and reproducible on base.
- Target branch is release-specific → set the PR base to that branch and mention any backport plan.

## Failure modes & recovery

- **F1 Wrong base branch:** detect unexpected diff size or PR target → edit the PR base in the UI or close and recreate against the correct branch.
- **F2 Missing remote branch:** detect `head ref not found` → run `git push -u origin <branch>` and retry.
- **F3 CI fails:** detect red checks in `gh pr checks` → open failing logs, fix the branch, push, and wait for rerun.
- **F4 Template incomplete:** detect unchecked required boxes or bot comments → update the PR body with exact test and rollout information.

## Verification

`gh pr view --json url,baseRefName,headRefName,mergeStateStatus,statusCheckRollup` shows the intended base/head and a PR URL, and `gh pr checks` reports all required checks passing before merge readiness.

## Variations

- `GitHub`: `gh pr create`, `gh pr view`, and `gh pr checks` provide scriptable verification.
- `GitLab`: use `glab mr create`, `glab mr view`, and pipeline status from `glab ci status`.
- `Bitbucket/Azure DevOps`: use the web UI or provider CLI, but still verify base/head and CI status programmatically when possible.

## Safety & privacy

Medium risk because a PR can trigger CI, preview deployments, and reviewer workflows. Do not include secrets in the branch, commits, screenshots, or PR body; request reviewers only after validation evidence is present.
