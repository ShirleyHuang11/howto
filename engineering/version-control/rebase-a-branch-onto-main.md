---
name: rebase-a-branch-onto-main
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

You replay a feature branch on top of the latest `main` so the branch has a linear history and includes current base changes.

## Preconditions

- The current branch is a feature branch, not `main`.
- Work is committed or safely stashed.
- You understand the team's policy on rebasing shared branches.

## Steps

1. **Confirm the current branch and cleanliness.** Run `git status --short --branch`. → *Expect:* you are on the feature branch and uncommitted work is absent or intentionally stashed.
2. **Fetch the latest base.** Run `git fetch --prune origin`. → *Expect:* `origin/main` is current.
3. **Review commits to be replayed.** Run `git log --oneline origin/main..HEAD`. → *Expect:* only your branch commits are listed.
4. **Start the rebase.** Run `git rebase origin/main`. → *Expect:* Git replays commits or stops at a named conflict.
5. **Resolve conflicts if they occur.** Edit conflicted files, run `git add <path>`, then `git rebase --continue`. → *Expect:* rebase progresses until Git reports success.
6. **Run validation.** Run `pytest -q`, `npm test`, or the repository's standard check. → *Expect:* validation exits 0 on the rebased branch.
7. **Update the remote branch if already pushed.** ⚠️ *Irreversible:* run `git push --force-with-lease` only after confirming no one else's commits are on the remote branch. → *Expect:* the remote branch updates only if its previous value matches your local expectation.

## Decision points

- Branch is shared by multiple authors → prefer merging `origin/main` or coordinate before force-with-lease.
- Rebase produces many confusing conflicts → abort with `git rebase --abort` and consider merging or asking for help.
- Remote changed since fetch → `--force-with-lease` rejects; fetch and inspect before retrying.

## Failure modes & recovery

- **F1 Rebased wrong branch:** detect `git branch --show-current` or unexpected commits → abort if in progress, or use `git reflog` to reset back before pushing.
- **F2 Conflict resolution dropped changes:** detect failing tests or diff anomalies → inspect `git range-diff origin/main@{1} HEAD@{1} origin/main HEAD` and repair.
- **F3 Force-with-lease rejected:** detect `stale info` rejection → fetch, inspect `git log --oneline HEAD..origin/<branch>`, and coordinate with the remote author.
- **F4 Hooks fail during rebase:** detect hook output after `rebase --continue` → fix the files, stage them, and continue.

## Verification

`git merge-base --is-ancestor origin/main HEAD` exits 0, `git status --short --branch` shows no rebase in progress, and the repository test command exits 0.

## Variations

- `upstream remote`: use `git fetch upstream` and `git rebase upstream/main` in fork-based projects.
- `interactive cleanup`: use `git rebase -i origin/main` when you also need to reorder, squash, or edit commits.
- `protected branches`: do not rebase or force-push protected shared branches; open a new branch instead.

## Safety & privacy

Medium risk because rebasing rewrites commit IDs and force-pushing can overwrite remote work. Use `--force-with-lease`, never plain `--force`, and coordinate with collaborators before rewriting a shared branch.
