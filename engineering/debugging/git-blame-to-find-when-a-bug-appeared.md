---
name: git-blame-to-find-when-a-bug-appeared
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You use line history and targeted revision inspection to identify when suspicious code changed, then verify whether that change plausibly introduced the bug.

## Preconditions

- You know the file, function, route, or behavior related to the bug.
- Repository history is available locally.
- You will use blame and show commands for investigation only, without rewriting history.

## Steps

1. **Locate the suspicious code path.** Search with `rg "functionName|error message|route" .` or navigate from the failing stack trace. → *Expect:* one or more files and lines tied to the behavior.
2. **Run focused blame.** Use `git blame -L <start>,<end> -- path/to/file` on the relevant lines. → *Expect:* each line shows a commit SHA, author, and date.
3. **Inspect the blamed commit.** Run `git show --stat --patch <sha> -- path/to/file`. → *Expect:* the change explains what was modified around the suspicious lines.
4. **Follow moved or copied code.** If the file was refactored, run `git log --follow -- path/to/file` and inspect earlier names. → *Expect:* prior history is visible despite renames.
5. **Compare behavior before and after.** Check out or inspect the parent and commit in a separate worktree if needed, then run the relevant test or reproduction. → *Expect:* the parent behaves correctly and the blamed commit shows the bug, or the hypothesis is rejected.
6. **Document the finding.** Link the commit, PR, test result, and suspected mechanism in the issue or fix PR. → *Expect:* reviewers can reproduce the reasoning without rerunning the full investigation.

## Decision points

- Blame points to formatting-only commit → use `git blame -w` or inspect earlier commits.
- Code was moved → use `git log --follow` and search old symbols.
- Parent also fails → continue walking history or use `git bisect` for a stronger boundary.
- The blamed change is correct but exposed bad data → investigate callers, migrations, and config changes.

## Failure modes & recovery

- **F1 Misleading blame after reformat:** detect massive whitespace commit → rerun with `git blame -w`.
- **F2 Merge commit confusion:** detect blame lands on a merge → inspect the merged PR commits and parents.
- **F3 Incomplete reproduction:** detect behavior cannot be tested at old SHAs → use commit diff plus logs, or create a minimal regression test on current code.
- **F4 Unrelated author attribution:** detect line was only moved → avoid assigning cause until behavior is confirmed before and after.

## Verification

The relevant reproduction or test exits 0 on the known-good revision and fails on the suspect revision, or the investigation records why blame alone is insufficient and opens a follow-up bisect or test task.

## Variations

- `GitHub/GitLab UI`: use line blame and PR links for quick context, then verify locally.
- `large refactors`: combine `git blame -w`, `git log --follow`, and symbol search.
- `generated files`: blame the generator or source template instead of generated output.
- `monorepo`: restrict blame and tests to the owning package to reduce noise.

## Safety & privacy

Low risk. Treat blame as evidence, not fault assignment. Do not publish private author or incident details unnecessarily, and do not rewrite or revert history unless a separate reviewed change calls for it.

