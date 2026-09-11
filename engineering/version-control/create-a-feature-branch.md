---
name: create-a-feature-branch
domain: engineering
subdomain: version-control
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You create a new branch from the current integration branch so work can proceed independently and be reviewed before merge.

## Preconditions

- The repository has a clean or intentionally understood working tree.
- You know the base branch, usually `main`, `master`, `develop`, or a release branch.
- You have permission to push a new branch if remote collaboration is needed.

## Steps

1. **Check current state.** Run `git status --short --branch`. → *Expect:* Git shows the current branch and whether local changes exist.
2. **Fetch the latest remote refs.** Run `git fetch --prune origin`. → *Expect:* remote branch references are updated without errors.
3. **Switch to the base branch.** Run `git switch main`. → *Expect:* `git branch --show-current` prints `main`.
4. **Update the base branch.** Run `git pull --ff-only origin main`. → *Expect:* the branch fast-forwards or reports it is already up to date.
5. **Create and switch to the feature branch.** Run `git switch -c feature/descriptive-name`. → *Expect:* `git branch --show-current` prints the new branch name.
6. **Push the branch when collaboration or CI is needed.** Run `git push -u origin feature/descriptive-name`. → *Expect:* the remote branch is created and upstream tracking is set.

## Decision points

- Local changes exist before switching → commit them, stash them, or create the branch from the current point if they belong to the new work.
- Base branch is not `main` → substitute the team's integration branch and verify with the repository's contribution guide.
- Branch name policy exists → include ticket ID or type prefix, such as `abc-123/add-login-rate-limit`.

## Failure modes & recovery

- **F1 Base branch behind remote:** detect `git pull --ff-only` failure → inspect local commits, then rebase or merge according to team policy.
- **F2 Branch already exists:** detect `fatal: a branch named ... already exists` → switch to it with `git switch <branch>` or choose a unique name.
- **F3 Push permission denied:** detect `403`, `permission denied`, or protected namespace errors → push to a fork or request access.
- **F4 Uncommitted changes block switch:** detect checkout conflict warnings → stash or commit the changes, then retry.

## Verification

`git status --short --branch` shows the new branch, and `git rev-parse --abbrev-ref --symbolic-full-name @{u}` prints `origin/feature/descriptive-name` if the branch was pushed.

## Variations

- `Git worktree`: use `git worktree add ../repo-feature -b feature/descriptive-name origin/main` to keep multiple branches checked out.
- `fork workflow`: add `upstream`, fetch it, branch from `upstream/main`, and push to `origin`.
- `trunk-based teams`: keep branches short-lived and push early so CI runs quickly.

## Safety & privacy

Low risk. Avoid branching from stale or wrong bases, avoid putting secrets in branch names, and do not push experimental work to protected or shared release branches unless the team expects it.
