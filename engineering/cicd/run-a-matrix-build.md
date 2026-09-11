---
name: run-a-matrix-build
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [engineering/cicd/set-up-a-ci-pipeline]
status: draft
last_verified: 2026-09-11
---

## Goal

You configure CI to run the same checks across multiple supported versions, operating systems, packages, or configurations and report each combination separately.

## Preconditions

- A single CI job already passes for one configuration.
- The supported version or platform list is known.
- The test suite can run independently for each matrix entry.

## Steps

1. **Choose meaningful matrix axes.** Select versions or environments that match support policy, such as `node: [20, 22]`, `python: ["3.11", "3.12"]`, or `os: [ubuntu-latest, macos-latest]`. → *Expect:* a small matrix with real coverage value.
2. **Convert the existing job to a matrix.** [GitHub Actions | GitLab CI] parameterize runtime setup and job names from matrix variables. → *Expect:* CI expands one job into multiple visible jobs.
3. **Keep installation deterministic per entry.** Use the same lockfile-respecting install command in every matrix cell. → *Expect:* each entry installs dependencies without sharing unsafe state.
4. **Add allowed experimental entries only when needed.** Mark unreleased or non-required versions as allowed failures if the CI system supports it. → *Expect:* stable supported entries still control overall pass/fail.
5. **Control concurrency and cost.** Limit matrix size, split slow jobs, or use fail-fast intentionally. → *Expect:* CI duration and runner use stay within project limits.
6. **Push and inspect all entries.** Open or update a PR/MR and watch the matrix. → *Expect:* every configured combination runs and has a separate status.
7. **Fix environment-specific failures.** Patch version assumptions, OS path handling, or dependency constraints. → *Expect:* all required matrix entries exit 0.

## Decision points

- One axis is unsupported but useful for preview → allow failure or run it on a schedule instead of requiring it.
- Matrix becomes too large → test primary versions on PRs and full matrix nightly.
- OS-specific tests fail → inspect path separators, shell differences, file permissions, and installed system packages.
- Dependency lockfile cannot support multiple runtimes → use compatible dependency constraints or separate lockfiles if the ecosystem expects them.

## Failure modes & recovery

- **F1 Matrix variable not substituted:** detect jobs all use the same runtime → fix variable syntax for the CI provider.
- **F2 Fail-fast hides failures:** detect later jobs cancelled after first failure → disable fail-fast while stabilizing the matrix.
- **F3 Unsupported runtime in dependency:** detect install resolver errors on one version → update support policy or dependency constraints.
- **F4 Runner shortage:** detect queued jobs timing out → reduce matrix size or move full coverage to scheduled CI.

## Verification

The CI run displays one job per matrix combination, all required combinations finish with exit 0, and the check names include the matrix values so failures are attributable.

## Variations

- `GitHub Actions`: use `strategy.matrix`, `fail-fast`, and `include` or `exclude`.
- `GitLab CI`: use `parallel:matrix` and variables in job definitions.
- `tox/nox`: drive Python version matrices inside one CI provider job definition.
- `monorepo`: use matrix entries for packages or workspaces touched by the change.

## Safety & privacy

Medium risk because matrices can multiply CI cost and block merges. Keep required entries aligned with support policy, avoid exposing secrets to unnecessary jobs, and review runner minutes before broadening coverage.

