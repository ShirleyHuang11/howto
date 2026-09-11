---
name: split-a-large-change-into-prs
domain: engineering
subdomain: version-control
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

Break a large working change into a sequence of reviewable pull requests that can be tested and merged independently.

## Preconditions

- The working tree contains or can reproduce the large change.
- The target branch is known and current enough for review.
- The project test command is known, such as `pytest -q`, `npm test`, or `go test ./...`.

## Steps

1. **Map the dependency order.** List the smallest logical slices: mechanical rename, shared API, migration, implementation, callers, cleanup. → *Expect:* every slice has a clear reason and at most one depends on the previous slice.
2. **Create the first branch from the target branch.** Run `git switch -c split/01-foundation origin/main` or the repository's target branch. → *Expect:* `git branch --show-current` prints the first split branch.
3. **Stage only the first logical slice.** Use `git add -p` and direct path staging for files that belong in PR 1. → *Expect:* `git diff --cached --stat` shows only the intended slice.
4. **Run focused checks.** Execute the relevant test or build command, for example `pytest -q tests/unit`. → *Expect:* the command exits 0 for the staged behavior.
5. **Commit the first slice.** Create a commit with a message that describes the isolated change. → *Expect:* the branch has one reviewable commit or a small coherent set.
6. **Create the next branch on top of the previous branch.** Run `git switch -c split/02-implementation`. → *Expect:* the second branch includes the first slice plus new staged work.
7. **Repeat for each dependent slice.** Stage, test, commit, and branch for each layer. → *Expect:* each branch can be opened as a stacked PR with a clear base branch.
8. **Open PRs with correct bases.** [BRANCH: GitHub | GitLab] Set PR 2's base to PR 1's branch, PR 3's base to PR 2, and so on. → *Expect:* each PR diff shows only its own slice.
9. **Rebase or retarget after merges.** When PR 1 merges, rebase PR 2 onto the target branch or update its base as the hosting platform recommends. → *Expect:* the remaining PR diff still contains only its slice and tests still pass.

## Decision points

- Large mechanical change plus behavior change → split mechanical-only first so reviewers can ignore noise later.
- Database migration required → put migration and compatibility code before destructive cleanup.
- Shared API unstable → keep downstream PRs draft until the foundation PR settles.

## Failure modes & recovery

- **F1 PR diff includes previous slices:** detect repeated files or commits in the PR view → change the PR base to the prior branch or rebase onto the merged target.
- **F2 Partial slice fails tests:** detect red tests after staging → include the missing compatibility shim or shrink the slice further.
- **F3 Merge conflict between stacked branches:** detect conflict during rebase → resolve in the lowest affected branch, then replay higher branches.
- **F4 Review comments require foundation changes:** detect comments on PR 1 that affect later PRs → update PR 1 first, then rebase downstream branches.

## Verification

For each PR branch, run the project's check command, such as `pytest -q` or `npm test`, and confirm it exits 0. In the hosting UI, each PR diff contains only its intended slice and its CI status check is green.

## Variations

- `Graphite or ghstack`: use the stack tool to create and restack dependent PRs automatically.
- `GitHub`: set each stacked PR's base branch manually or with `gh pr edit --base`.
- `GitLab`: use merge request dependencies and update target branches as earlier MRs merge.

## Safety & privacy

Medium risk because rebasing stacked branches can disrupt collaborators if branches are shared. Communicate branch ownership, avoid force-updating branches others are using without notice, and never mix secrets or unrelated cleanup into a split PR.
