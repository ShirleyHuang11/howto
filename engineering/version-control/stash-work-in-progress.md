---
name: stash-work-in-progress
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

You temporarily save uncommitted work, switch context safely, and later reapply the stash without losing track of what it contains.

## Preconditions

- The repository has uncommitted changes that are not ready to commit.
- You need to switch branches, pull changes, or test another state.
- You understand whether untracked files should be included.

## Steps

1. **Inspect current changes.** Run `git status --short` and `git diff --stat`. → *Expect:* you know which tracked and untracked files are present.
2. **Create a named stash.** Run `git stash push -m "wip: describe reason"` for tracked changes, or `git stash push -u -m "wip: describe reason"` to include untracked files. → *Expect:* Git reports `Saved working directory and index state`.
3. **Verify the stash exists.** Run `git stash list --date=local`. → *Expect:* the newest stash has the message you provided.
4. **Confirm the working tree is clean enough.** Run `git status --short`. → *Expect:* stashed tracked changes are gone; ignored files may remain.
5. **Do the context-switching work.** Switch branches, pull, or run the urgent task. → *Expect:* the temporary task can proceed without the previous WIP blocking it.
6. **Preview before applying.** Run `git stash show -p stash@{0}`. → *Expect:* the patch matches the WIP you want to restore.
7. **Reapply and remove the stash when ready.** Run `git stash pop stash@{0}`. → *Expect:* changes return to the working tree and the stash is dropped if applied cleanly.

## Decision points

- WIP should be durable or shared → make a draft commit or branch instead of a stash.
- Untracked files matter → use `git stash push -u`; ignored files require `-a` and extra caution.
- Applying onto a changed branch conflicts → resolve like a merge conflict, then continue with normal staging.

## Failure modes & recovery

- **F1 Stash omitted untracked files:** detect missing new files after stash → check whether they remained in the working tree; if removed separately, recover from backups or editor history.
- **F2 Stash pop conflicts:** detect conflict markers and unmerged paths → resolve conflicts, stage files, and continue; the stash is usually kept until a clean pop.
- **F3 Applied wrong stash:** detect unexpected changes → use `git stash list`, reverse or restore the working tree, then apply the correct stash.
- **F4 Stash dropped accidentally:** detect missing stash after pop → inspect `git fsck --lost-found` or reflog promptly before garbage collection.

## Verification

After stashing, `git stash list --format=%gd:%s` shows the named stash and `git status --short` no longer shows those WIP changes; after restoring, `git diff --stat` shows the expected WIP and `git stash list` no longer includes the popped entry.

## Variations

- `keep staged`: use `git stash push --keep-index -m "wip"` to stash unstaged changes while preserving the index.
- `branch from stash`: use `git stash branch wip/recover stash@{n}` to restore onto the original base.
- `ignored files`: use `git stash push -a` only when ignored local artifacts are safe to stash.

## Safety & privacy

Low risk, but stashes are local, easy to forget, and can include secrets or generated data. Name stashes clearly, avoid stashing large private artifacts, and convert important WIP into commits before long-lived context switches.
