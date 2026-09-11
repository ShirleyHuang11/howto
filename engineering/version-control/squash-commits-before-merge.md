---
name: squash-commits-before-merge
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

You combine noisy branch commits into a smaller, reviewable history before merge while preserving the final code state and passing validation.

## Preconditions

- The branch contains multiple local commits that should become one or a few commits.
- You know the correct base branch and whether the branch has been shared.
- The working tree is clean.

## Steps

1. **Fetch and identify the base.** Run `git fetch origin main`. → *Expect:* `origin/main` is current.
2. **List branch commits.** Run `git log --oneline origin/main..HEAD`. → *Expect:* only commits intended for the PR are shown.
3. **Start an interactive rebase.** Run `git rebase -i origin/main`. → *Expect:* an editor opens with branch commits in replay order.
4. **Mark commits to combine.** Keep the first relevant commit as `pick` and change later fixup commits to `squash` or `fixup`. → *Expect:* Git asks for a final message when `squash` is used, or continues automatically for `fixup`.
5. **Write the final commit message.** Keep a subject that describes the combined change and include context in the body if needed. → *Expect:* `git log --oneline origin/main..HEAD` shows the intended reduced commit count.
6. **Resolve any conflicts.** Edit files, run `git add <path>`, and `git rebase --continue`. → *Expect:* the rebase completes without unmerged files.
7. **Run validation and update the remote.** Run `pytest -q` or `npm test`; if previously pushed, ⚠️ *Irreversible:* run `git push --force-with-lease` after confirming the remote branch has no unexpected commits. → *Expect:* tests exit 0 and the remote branch reflects the squashed history.

## Decision points

- Project uses platform squash merge → local squashing may be unnecessary; clean up only commits that block review.
- Branch has collaborator commits → coordinate before rewriting history or use the hosting platform's squash merge.
- Each commit should remain independently meaningful → squash only fixups, not logical milestones.

## Failure modes & recovery

- **F1 Squashed too much:** detect lost useful commit boundaries → use `git reflog` to find the pre-rebase commit and reset locally before pushing.
- **F2 Conflict during rebase:** detect unmerged paths → resolve as in `engineering/resolve-a-merge-conflict`, stage, and continue.
- **F3 Force-with-lease rejected:** detect remote update mismatch → fetch, inspect remote commits, and coordinate before retrying.
- **F4 Final message loses issue link:** detect missing `Fixes #...` or ticket key in `git log -1 --format=%B` → amend the commit message before push.

## Verification

`git log --oneline origin/main..HEAD` shows the intended number of commits, `git diff --exit-code origin/main...HEAD -- <expected paths>` reflects the same final code changes, and the project test command exits 0.

## Variations

- `autosquash`: create commits with `git commit --fixup <sha>` and run `git rebase -i --autosquash origin/main`.
- `GitHub squash merge`: set a clean PR title/body and let the merge button create the single commit.
- `release branches`: avoid rewriting published release branch history; create a cleanup branch if needed.

## Safety & privacy

Medium risk because squashing rewrites commit IDs. Use `--force-with-lease` only on your feature branch, confirm collaborators are not depending on old SHAs, and avoid exposing private context in rewritten commit messages.
