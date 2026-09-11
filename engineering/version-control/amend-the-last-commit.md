---
name: amend-the-last-commit
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

You update the most recent commit to include a small correction or better message while understanding when history rewrite is safe.

## Preconditions

- The change belongs in the previous commit.
- You know whether the commit has already been pushed or reviewed.
- The working tree contains only the correction to amend, or you can stage it selectively.

## Steps

1. **Inspect the current commit.** Run `git log -1 --stat` and `git show --stat HEAD`. → *Expect:* the last commit is the one you intend to modify.
2. **Stage the correction.** Run `git add <path>` or `git add -p <path>`. → *Expect:* `git diff --cached` contains only the amendment.
3. **Amend without changing the message if appropriate.** Run `git commit --amend --no-edit`. → *Expect:* Git replaces the last commit with a new SHA containing the staged correction.
4. **Amend the message when needed.** Run `git commit --amend` and edit the subject/body. → *Expect:* `git log -1 --format=%B` shows the corrected message.
5. **Run validation.** Run focused tests such as `pytest path/to/test.py -q` or `npm test -- <pattern>`. → *Expect:* tests exit 0.
6. **Update remote only if needed.** If the old commit was pushed, ⚠️ *Irreversible:* run `git push --force-with-lease` after confirming the branch is yours and no one else added commits. → *Expect:* remote branch updates without overwriting unexpected work.

## Decision points

- Commit already merged to shared base → create a new follow-up commit instead of amending.
- Correction is unrelated → make a separate commit.
- Remote branch has new commits → fetch and inspect before any force-with-lease.

## Failure modes & recovery

- **F1 Amended wrong commit:** detect unexpected `git show HEAD` → use `git reflog` to find the previous SHA and reset or cherry-pick as needed.
- **F2 Included unrelated staged edits:** detect with `git show --stat HEAD` → amend again after resetting and staging only intended changes.
- **F3 Force-with-lease rejected:** detect stale remote error → fetch, inspect remote updates, and coordinate.
- **F4 Commit hook fails:** detect hook output → fix or restage generated changes, then rerun amend.

## Verification

`git show --stat HEAD` includes the correction, `git log -1 --format=%B` shows the intended message, and the relevant validation command exits 0.

## Variations

- `message only`: run `git commit --amend` with no staged changes.
- `author correction`: use `git commit --amend --author="Name <email@example.com>"` when policy requires it.
- `signed commits`: add `-S` or ensure commit signing remains enabled after amend.

## Safety & privacy

Medium risk if the commit was pushed because amend rewrites history. Prefer amendments before review, use `--force-with-lease` rather than `--force`, and avoid rewriting commits already merged into shared branches.
