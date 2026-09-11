---
name: speed-up-a-slow-ci-pipeline
domain: engineering
subdomain: cicd
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

You reduce CI runtime without hiding failures, and prove the pipeline still tests the same supported paths. The end state is a faster green CI run with timing data showing where the improvement came from.

## Preconditions

- Access to the CI provider logs and repository workflow files.
- A representative branch or pull request that can run the full pipeline.
- Local dependency install and test commands are known.

## Steps

1. **Capture the current baseline.** Open the latest successful CI run and record total wall time plus the slowest jobs and steps. [BRANCH: GitHub Actions, use `gh run list --limit 5` then `gh run view <run-id> --log` | GitLab CI, use the pipeline page or `glab ci view`] → *Expect:* a written baseline such as "total 18m42s; test job 12m10s; install step 5m03s".
2. **Identify avoidable repeated work.** Look for dependency installs, builds, image pulls, and test setup repeated across jobs. → *Expect:* a short list of cacheable or parallelizable steps with durations from logs.
3. **Add dependency caching with stable keys.** [BRANCH: npm, cache `~/.npm` using a key from `hashFiles('**/package-lock.json')` | pip, cache `~/.cache/pip` keyed by `requirements*.txt` | Gradle, cache `~/.gradle/caches` and `~/.gradle/wrapper`] → *Expect:* the workflow validates and the next run prints a cache miss followed by a saved cache.
4. **Split independent checks into parallel jobs.** Put lint, unit tests, type checks, and build in separate jobs when they do not need each other's artifacts. → *Expect:* the CI graph shows jobs running at the same time and the critical path is shorter.
5. **Use targeted test sharding only when tests are independent.** [BRANCH: pytest, run `pytest --splits 4 --group $CI_NODE_INDEX` with `pytest-split` | Jest, run `jest --shard=1/4`, `2/4`, etc.] → *Expect:* each shard exits 0 and their combined test count matches the unsharded suite.
6. **Persist build artifacts instead of rebuilding them.** Upload compiled assets or packages from the build job and download them in downstream jobs. → *Expect:* downstream logs show artifact download and skip the previous rebuild step.
7. **Remove work that duplicates another required check.** Delete redundant install, lint, or test steps only after confirming another job enforces the same command. → *Expect:* CI config still contains one required execution path for each quality gate.
8. **Run the optimized pipeline twice.** Trigger CI on the same branch twice so cache warmup and steady-state time are both visible. → *Expect:* both runs pass; the second run is faster than the baseline by the target amount.

## Decision points

- Install step dominates runtime → add dependency caching before sharding tests.
- One test file dominates a shard → split that file's slow cases or isolate expensive integration setup.
- Flaky tests appear after parallelization → fix shared state or keep those tests serial.
- Paid CI concurrency is saturated → optimize caching and job contents before adding more parallel jobs.

## Failure modes & recovery

- **F1 Cache never restores:** detect repeated "cache not found" logs → verify the cache path exists and the key uses the correct lockfile path.
- **F2 Stale dependency cache:** detect missing packages or wrong binary versions → include lockfile and runtime version in the cache key, then clear the provider cache.
- **F3 Artifact mismatch:** detect downstream build or checksum failures → include commit SHA and build target in artifact names.
- **F4 Hidden coverage loss:** detect fewer tests than baseline → compare test counts and restore omitted suites before keeping the speedup.

## Verification

The optimized CI pipeline completes successfully on the target branch, and provider timing shows total wall time below the recorded baseline while required commands such as `npm test`, `pytest`, `go test ./...`, or equivalent still exit 0.

## Variations

- `GitHub Actions`: use `actions/cache` and `actions/upload-artifact`; inspect timing with `gh run view <run-id>`.
- `GitLab CI`: use `cache:key:files`, `artifacts`, and pipeline DAG `needs`.
- `CircleCI`: use `save_cache`, `restore_cache`, workspaces, and built-in test splitting.
- `monorepo`: combine path filters with package-level task runners such as Nx, Turborepo, Bazel, or Pants.

## Safety & privacy

Medium risk because CI changes can stop required checks or let broken code merge. Do not cache secrets, `.env` files, private SSH keys, or built artifacts containing credentials; keep required branch checks enabled until the replacement jobs are proven green.
