---
name: bisect-to-find-a-regression
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

You use `git bisect` to identify the first commit that introduced a regression, using a repeatable test command whenever possible.

## Preconditions

- You can name one known bad revision and one known good revision.
- The regression has a deterministic command, script, or manual check.
- The working tree is clean.

## Steps

1. **Define the failure predicate.** Write a command that exits nonzero when the bug is present, such as `pytest tests/test_login.py::test_refresh -q`. → *Expect:* the command distinguishes good from bad revisions.
2. **Confirm endpoints.** Run the test on the current bad revision and known good revision if practical. → *Expect:* bad fails and good passes.
3. **Start bisect.** Run `git bisect start`. → *Expect:* Git enters bisect mode.
4. **Mark revisions.** Run `git bisect bad HEAD` and `git bisect good <known-good-sha>`. → *Expect:* Git checks out a midpoint commit.
5. **Automate the search.** Run `git bisect run ./scripts/regression-check.sh` or the direct test command if setup is stable. → *Expect:* Git tests midpoints and prints the first bad commit.
6. **Inspect the result.** Run `git show --stat <first-bad-sha>` and `git show <first-bad-sha>`. → *Expect:* the suspected change plausibly explains the regression.
7. **Exit bisect mode.** Run `git bisect reset`. → *Expect:* Git returns to the branch where bisect started.

## Decision points

- Test is flaky → run it multiple times in the bisect script and return exit code 125 for inconclusive setup failures.
- Some commits do not build → skip with `git bisect skip` or make the script return 125.
- Regression depends on database or services → reset fixtures inside the script so each commit is tested consistently.

## Failure modes & recovery

- **F1 Bad/good endpoints reversed:** detect impossible result or known good failing → run `git bisect reset`, verify endpoints, and restart.
- **F2 Dirty tree blocks checkout:** detect checkout errors → commit, stash, or clean local work before bisecting.
- **F3 Inconclusive commits dominate:** detect many skipped commits → choose closer endpoints or create a more robust test script.
- **F4 Generated artifacts stale:** detect build failures unrelated to source → include install/build regeneration in the bisect script.

## Verification

`git bisect run <command>` exits after printing `<sha> is the first bad commit`, `git show --stat <sha>` shows the candidate change, and rerunning the failure predicate on the first bad and its parent gives fail/pass respectively.

## Variations

- `manual bisect`: run the check by hand at each midpoint, then mark `git bisect good` or `git bisect bad`.
- `monorepo`: limit build cost with focused tests and package filters, such as `pnpm --filter api test`.
- `performance regression`: script a benchmark threshold and keep noise low with repeated runs.

## Safety & privacy

Low risk because bisect checks out historical code locally. Avoid running old migrations or scripts against production services, and isolate credentials and test databases from real environments.
