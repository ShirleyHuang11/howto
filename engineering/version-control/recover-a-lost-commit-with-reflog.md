---
name: recover-a-lost-commit-with-reflog
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

You recover a commit that disappeared from branch history after reset, rebase, amend, or branch deletion by finding it in the reflog and restoring it safely.

## Preconditions

- The repository still has the local reflog that may reference the lost commit.
- You know roughly when or how the commit was lost.
- The current working tree is clean or safely stashed.

## Steps

1. **Stop making history changes.** Avoid garbage collection and new resets until recovery is complete. → *Expect:* the lost commit remains likely reachable in local reflog data.
2. **Inspect the reflog.** Run `git reflog --date=iso`. → *Expect:* recent HEAD positions, resets, rebases, and commits are listed with SHAs.
3. **Find the candidate commit.** Run `git show --stat <sha>` for likely entries. → *Expect:* the desired lost changes appear in the commit.
4. **Create a recovery branch.** Run `git switch -c recovery/lost-commit <sha>`. → *Expect:* `git branch --show-current` prints the recovery branch and points at the recovered commit.
5. **Compare with the intended base.** Run `git diff --stat origin/main...HEAD` or the relevant base. → *Expect:* the recovered changes are visible and understandable.
6. **Move or merge the recovery as needed.** Cherry-pick the commit onto the real branch with `git cherry-pick <sha>` or open a PR from the recovery branch. → *Expect:* the intended branch contains the recovered change.
7. **Run validation.** Run affected tests such as `pytest -q` or `npm test`. → *Expect:* the recovered state passes checks.

## Decision points

- Commit exists only on another clone or remote → fetch that source and recover from its refs instead of local reflog.
- Recovered commit includes unwanted follow-up work → cherry-pick individual commits or use `git restore -p` to split.
- Reflog lacks the commit → search with `git fsck --lost-found` and inspect dangling commits.

## Failure modes & recovery

- **F1 Candidate SHA is wrong:** detect unrelated `git show` output → keep searching reflog entries before creating a permanent branch.
- **F2 Reflog expired:** detect no useful entries → check other clones, remote branches, CI checkout logs, or backups.
- **F3 Dirty tree blocks switch:** detect Git refusing to switch → stash or commit current work before creating the recovery branch.
- **F4 Recovered commit fails tests:** detect validation failure → identify missing dependent commits from reflog and recover them too.

## Verification

`git branch --contains <recovered-sha>` lists a named branch such as `recovery/lost-commit`, `git show --stat <recovered-sha>` shows the expected files, and the relevant test command exits 0 after applying it where needed.

## Variations

- `lost branch`: run `git reflog show --all` to search refs beyond HEAD.
- `lost stash`: run `git stash list` and `git stash show -p stash@{n}` before using reflog.
- `remote recovery`: use hosting provider branch and PR refs, such as `git fetch origin pull/123/head:recovery/pr-123` on GitHub.

## Safety & privacy

Medium risk because recovery often happens after mistaken history edits. Create a new recovery branch before moving existing branches, avoid garbage collection, and do not force-push recovered history until the correct state is reviewed.
