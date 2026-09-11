---
name: undo-uncommitted-changes
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

You discard, unstage, or selectively restore uncommitted work without accidentally deleting changes that should be kept.

## Preconditions

- The changes to undo have not been committed.
- You have inspected the diff and know which files or hunks are disposable.
- Any valuable work has been committed, stashed, or copied into a patch.

## Steps

1. **Inventory the working tree.** Run `git status --short` and `git diff --stat`. → *Expect:* modified, staged, deleted, and untracked files are visible.
2. **Save a patch when uncertain.** Run `git diff > /tmp/wip.patch` and `git diff --cached > /tmp/staged.patch` if any discarded work might be needed later. → *Expect:* patch files exist outside the repository.
3. **Unstage files without deleting edits.** Run `git restore --staged <path>` or `git restore --staged .`. → *Expect:* changes move from staged to unstaged in `git status --short`.
4. **Discard tracked file edits selectively.** Run `git restore <path>` or `git restore -p <path>`. → *Expect:* selected tracked file changes disappear from `git diff`.
5. **Remove untracked files only after inspection.** Run `git clean -nd` first, then ⚠️ *Irreversible:* run `git clean -fd <path>` only for files confirmed disposable. → *Expect:* previewed untracked files are removed.
6. **Verify the final state.** Run `git status --short`. → *Expect:* only intended remaining changes are listed, or the working tree is clean.

## Decision points

- You may need the work later → use `git stash push -u -m "reason"` instead of discarding.
- Only some hunks should be removed → use `git restore -p` and verify each prompt.
- Untracked files include local data or secrets → do not clean them until backed up or confirmed disposable.

## Failure modes & recovery

- **F1 Deleted untracked file:** detect missing file after `git clean` → recover from backup, editor local history, or filesystem snapshot; Git cannot restore files it never tracked.
- **F2 Discarded needed tracked edits:** detect missing changes after `git restore` → reapply from `/tmp/wip.patch`, stash, editor history, or saved patch.
- **F3 Unstaged but not discarded:** detect files still modified after `git restore --staged` → run `git restore <path>` if the edits should also be removed.
- **F4 Clean command too broad:** detect preview includes valuable files → stop and clean specific paths rather than `git clean -fd`.

## Verification

`git status --short` shows exactly the intended remaining files, and `git diff --exit-code` plus `git diff --cached --exit-code` exit 0 when the goal is a fully clean working tree.

## Variations

- `older Git`: use `git checkout -- <path>` instead of `git restore <path>`.
- `ignored files`: preview with `git clean -ndX` for ignored files or `git clean -ndx` for all untracked and ignored files before removal.
- `IDE`: use source-control discard actions only after checking the terminal diff.

## Safety & privacy

Medium risk because `git clean` permanently removes untracked files. Preview destructive cleanup, prefer stashing when unsure, and never remove local secrets, databases, or generated evidence without confirmation.
