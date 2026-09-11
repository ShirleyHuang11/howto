---
name: cherry-pick-a-commit
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

You copy one specific commit from another branch into the current branch while preserving reviewability and verifying the result.

## Preconditions

- The source commit SHA is known and reachable locally or from a remote.
- The destination branch is checked out and clean.
- You understand whether the commit has dependencies on earlier commits.

## Steps

1. **Fetch the source branch.** Run `git fetch --prune origin`. → *Expect:* the source commit is available locally.
2. **Inspect the source commit.** Run `git show --stat <sha>` and `git show <sha>`. → *Expect:* the commit contains only the change you intend to copy.
3. **Confirm destination branch.** Run `git status --short --branch`. → *Expect:* you are on the target branch with no uncommitted changes.
4. **Apply the commit.** Run `git cherry-pick -x <sha>` for public backports so the new message records the source SHA. → *Expect:* Git creates a new commit or stops for conflicts.
5. **Resolve conflicts if needed.** Edit files, run `git add <path>`, then `git cherry-pick --continue`. → *Expect:* the cherry-pick completes and no unmerged files remain.
6. **Run validation.** Run affected tests and the branch's required checks, such as `pytest -q`. → *Expect:* tests exit 0 on the destination branch.
7. **Push or open a review.** Run `git push` or create a PR from the destination branch. → *Expect:* remote CI starts for the cherry-picked commit.

## Decision points

- Commit depends on earlier commits → cherry-pick the dependency range or create a targeted patch.
- Backport to release branch → keep `-x` so auditors can trace the original commit.
- Conflict changes behavior → ask the owner or add a focused test before pushing.

## Failure modes & recovery

- **F1 Empty cherry-pick:** detect `previous cherry-pick is now empty` → run `git cherry-pick --skip` if the change already exists, or inspect why the patch disappeared.
- **F2 Missing dependency:** detect compile/test failures after cherry-pick → inspect the original branch history and cherry-pick prerequisite commits.
- **F3 Conflict unresolved:** detect unmerged files → resolve, stage, and continue; use `git cherry-pick --abort` if the chosen commit is wrong.
- **F4 Wrong destination branch:** detect incorrect branch in `git status --branch` → abort if in progress or revert the new commit before switching.

## Verification

`git log -1 --format=%B` includes the cherry-picked commit message and source SHA when `-x` was used, `git diff --name-only --diff-filter=U` prints nothing, and the destination branch's test command exits 0.

## Variations

- `commit range`: use `git cherry-pick <oldest>^..<newest>` for consecutive commits.
- `no commit`: use `git cherry-pick -n <sha>` to stage changes for manual adjustment before committing.
- `patch file`: use `git format-patch -1 <sha>` and `git am` when moving across repositories.

## Safety & privacy

Medium risk because copied commits can miss dependencies or change stable branches. Verify the target branch, source SHA, and tests before pushing, and avoid cherry-picking secrets or environment-specific changes into broader branches.
