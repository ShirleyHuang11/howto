---
name: bisect-a-performance-regression
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h-3h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You identify the first commit that introduced a measurable performance regression and produce a repeatable benchmark proving the before/after difference.

## Preconditions

- The repository history is available locally, and the working tree changes needed for benchmarking are saved outside the files under test.
- You have a deterministic performance command with a clear pass/fail threshold.
- Dependencies can be installed for historical commits, or the project has lockfiles/containers to recreate them.
- You will not rewrite shared history while investigating.

## Steps

1. **Define the performance predicate.** Choose a command that exits 0 for good performance and nonzero for bad performance, such as `./scripts/bench-search --max-ms 250`. → *Expect:* a single command with a documented threshold and stable exit code.
2. **Warm and measure the current commit.** Run the benchmark at least three times, for example `for i in 1 2 3; do ./scripts/bench-search --json; done`. → *Expect:* current results are consistently worse than the threshold.
3. **Find a known good revision.** Use a release tag, deployment SHA, or date range and run the same benchmark there. → *Expect:* the older revision passes the threshold.
4. **Create a bisect script.** Write or select a script that installs dependencies if needed, runs the benchmark, and exits `0` for good, `1` for bad, or `125` for untestable commits. → *Expect:* the script behaves correctly on the known good and known bad revisions.
5. **Run the bisect.** Execute `git bisect start`, `git bisect bad HEAD`, `git bisect good <known-good-sha>`, then `git bisect run ./scripts/bisect-performance.sh`. → *Expect:* the tool reports the first bad commit SHA.
6. **Confirm the boundary manually.** Run the benchmark on the parent of the first bad commit and on the first bad commit. → *Expect:* the parent passes and the reported commit fails under the same threshold.
7. **Record the cause and fix path.** Inspect the reported commit, identify the changed code path, and file or implement the remediation. → *Expect:* an issue, PR, or patch references the first bad commit and includes the benchmark output.
8. **Exit bisect state.** Run `git bisect reset`. → *Expect:* the repository returns to the original branch or commit.

## Decision points

- Benchmark varies by more than 10 percent between repeated runs → stabilize CPU governor, isolate external services, increase samples, or benchmark in a container.
- Historical commits cannot install dependencies → use `git bisect skip` or make the bisect script exit `125`.
- Regression appears only in production data → use a scrubbed snapshot or synthetic workload that reproduces the same query shape.
- First bad commit is a merge commit → test relevant parents and inspect merged PR commits before assigning cause.

## Failure modes & recovery

- **F1 Dirty working tree blocks checkout:** detect checkout errors during bisect → save local edits outside the repo or use a separate clone.
- **F2 Benchmark flakes:** detect alternating good and bad verdicts for one SHA → increase runs, use median/p95, and make the script inconclusive until stable.
- **F3 Dependency drift changes results:** detect lockfile installs pulling new packages → use lockfile-enforced installs such as `npm ci`, `bundle install --deployment`, or `pip-tools` constraints.
- **F4 Bisect lands on infrastructure-only commit:** detect no code path change related to performance → verify config, dependency, schema, and runtime environment changes in that commit.

## Verification

`git bisect run ./scripts/bisect-performance.sh` reports a first bad commit, and manual benchmark runs show `<first-bad>^` exits 0 while `<first-bad>` exits nonzero under the documented threshold.

## Variations

- `web frontend`: use Lighthouse CI, Playwright trace timings, or bundle-size thresholds.
- `database`: use `EXPLAIN (ANALYZE, BUFFERS)` on a scrubbed snapshot and fail when duration or rows scanned exceeds the budget.
- `service latency`: use `wrk`, `vegeta`, or `k6` against a local or staging instance with fixed seed data.
- `monorepo`: restrict setup and benchmark commands to the affected package to keep bisect fast.

## Safety & privacy

Medium risk because bisect repeatedly checks out old code and may run old scripts. Use disposable local services, scrubbed data, and isolated credentials. Do not run historical migration or deploy scripts against shared environments during a bisect.

