---
name: stage-and-commit-selectively
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

You stage only the files and hunks that belong together, then create a focused commit that can be reviewed, reverted, or cherry-picked cleanly.

## Preconditions

- The repository has uncommitted changes.
- The working tree may contain unrelated edits that must not be included.
- Tests or formatting commands for the affected area are available.

## Steps

1. **Inspect all changed paths.** Run `git status --short` and `git diff --stat`. → *Expect:* every modified, added, deleted, and untracked file is visible.
2. **Review the unstaged diff.** Run `git diff -- <path>` for each candidate file. → *Expect:* you can identify which lines belong in this commit.
3. **Stage whole files that are entirely relevant.** Run `git add <path>`. → *Expect:* `git diff --cached --name-only` includes only intended files.
4. **Stage partial hunks where needed.** Run `git add -p <path>` and accept only relevant hunks. → *Expect:* `git diff --cached` contains the target change while unrelated edits remain unstaged.
5. **Verify staged content, not just filenames.** Run `git diff --cached --check` and `git diff --cached`. → *Expect:* no whitespace errors and no accidental debug code, secrets, or unrelated edits.
6. **Run focused validation.** [pytest | Jest] run `pytest path/to/test.py -q` or `npm test -- --runInBand path/to/test`. → *Expect:* the relevant tests exit 0.
7. **Commit the staged change.** Run `git commit -m "Describe focused change"`. → *Expect:* the commit succeeds and unstaged unrelated work remains in the working tree.

## Decision points

- File contains generated and source changes → regenerate cleanly or stage only the source plus required generated artifact.
- Lockfile changed unexpectedly → inspect package manager output; include it only if dependency resolution actually changed.
- Test requires unstaged edits to pass → the commit may be incomplete; stage the missing dependency or split the work differently.

## Failure modes & recovery

- **F1 Accidental unrelated hunk staged:** detect with `git diff --cached` → unstage interactively using `git restore --staged -p <path>` and restage correctly.
- **F2 Whitespace error:** detect `git diff --cached --check` failure → edit or format the affected line, then stage the fix.
- **F3 Untracked file omitted:** detect tests failing because a new module is missing → run `git status --short`, stage the required file, and rerun validation.
- **F4 Hook modifies files:** detect a pre-commit hook changing files after commit attempt → inspect `git diff`, stage hook changes if appropriate, and retry.

## Verification

`git show --stat --oneline HEAD` lists only the intended files, `git diff --cached --exit-code` exits 0 after the commit, and the focused test command exits 0.

## Variations

- `GUI clients`: use the client's per-file and per-hunk staging view, then verify with `git diff --cached` in a terminal.
- `binary files`: stage intentionally with `git add <file>` and verify size/type with `file <file>` or project tooling.
- `large refactors`: split mechanical formatting, behavior changes, and tests into separate commits when possible.

## Safety & privacy

Low risk when local. The main risk is accidentally committing unrelated work or sensitive local files, so inspect staged diffs and keep secrets ignored before creating the commit.
