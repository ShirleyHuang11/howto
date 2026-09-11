---
name: resolve-a-merge-conflict
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

You resolve merge conflicts by preserving the intended behavior from both sides, regenerate derived files when necessary, and finish with a clean working tree and passing checks.

## Preconditions

- A merge, rebase, cherry-pick, or pull has stopped with conflicts.
- You know the base branch and the purpose of both sets of changes.
- Relevant tests or build commands are available.

## Steps

1. **Identify conflicted files.** Run `git status --short` and `git diff --name-only --diff-filter=U`. → *Expect:* all unmerged paths are listed.
2. **Inspect each conflict in context.** Open files and search for `<<<<<<<`, `=======`, and `>>>>>>>`. → *Expect:* every conflict marker maps to a real choice between versions.
3. **Resolve source files deliberately.** Edit each file to keep the correct combined behavior and remove conflict markers. → *Expect:* no conflict marker remains in source files.
4. **Regenerate derived artifacts.** For lockfiles, generated code, snapshots, or schema files, run the project command such as `npm install --package-lock-only`, `bundle install`, or `make generate`. → *Expect:* derived files match the resolved source and dependency state.
5. **Stage resolved files.** Run `git add <resolved-paths>`. → *Expect:* `git diff --name-only --diff-filter=U` prints nothing.
6. **Continue the interrupted operation.** [merge | rebase | cherry-pick] run `git merge --continue`, `git rebase --continue`, or `git cherry-pick --continue`. → *Expect:* Git advances or stops only on the next conflict.
7. **Run validation.** Run the focused tests and then the normal suite command, such as `pytest -q` or `npm test`. → *Expect:* tests exit 0.

## Decision points

- Conflict is in a lockfile → resolve package manifests first, then regenerate the lockfile instead of hand-editing it.
- Conflict repeats during rebase → resolve each commit's conflict, stage, and continue until rebase completes.
- Correct resolution is unclear → stop and ask the code owner; guessing can silently drop behavior.

## Failure modes & recovery

- **F1 Conflict markers committed:** detect `grep -R '<<<<<<<\\|>>>>>>>' .` or failed linters → remove markers, stage fixes, and amend or continue.
- **F2 Lost one side's behavior:** detect failing tests or missing code paths → compare with `git show :2:<file>` and `git show :3:<file>`, then restore the missing logic.
- **F3 Rebase continue fails due editor or hooks:** detect hook/test failure → fix the reported issue, stage changes, and rerun `git rebase --continue`.
- **F4 Wrong conflict strategy used:** detect suspicious mass deletion or `ours/theirs` misuse → abort with `git merge --abort` or `git rebase --abort` if still in progress, then redo carefully.

## Verification

`git diff --name-only --diff-filter=U` prints nothing, `grep -R '<<<<<<<\\|=======' --exclude-dir=.git .` finds no conflict markers, and the project test command exits 0.

## Variations

- `merge`: finish with `git merge --continue` or a merge commit.
- `rebase`: finish with repeated `git rebase --continue` until the branch is replayed.
- `binary conflicts`: choose one side with `git checkout --ours <file>` or `git checkout --theirs <file>` only after confirming the correct binary artifact.

## Safety & privacy

Medium risk because conflict resolution can remove another person's work while appearing successful. Review both sides, run tests, and avoid using blanket `ours` or `theirs` strategies on shared code without owner confirmation.
