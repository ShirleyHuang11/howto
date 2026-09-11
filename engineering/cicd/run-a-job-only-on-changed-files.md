---
name: run-a-job-only-on-changed-files
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You make a CI job run only when relevant files change, while preserving required checks for protected branches. The end state is faster CI that still blocks unsafe changes.

## Preconditions

- The repository has clear ownership boundaries such as `frontend/`, `backend/`, `docs/`, or service directories.
- Required branch protection behavior is understood.
- You can trigger CI on a test branch or pull request.

## Steps

1. **Map jobs to file paths.** List which directories, lockfiles, and shared config files should trigger each job. → *Expect:* a path map such as "frontend tests: `frontend/**`, `package-lock.json`, `.github/workflows/ci.yml`".
2. **Add path filtering at the workflow or job level.** [BRANCH: GitHub Actions, use `on.pull_request.paths` for whole workflows or `dorny/paths-filter` for jobs | GitLab CI, use `rules:changes`] → *Expect:* CI config validates with the new path rules.
3. **Include shared and workflow files.** Add files that affect the job indirectly, such as lockfiles, Dockerfiles, base images, and CI config. → *Expect:* editing shared config triggers the relevant job.
4. **Preserve a required check result.** If branch protection requires a check, create a lightweight skip job with the same required status or keep a wrapper workflow that always reports success when the heavy job is not needed. → *Expect:* pull requests with unrelated changes are not stuck waiting for a skipped required check.
5. **Test a relevant change.** Modify or open a PR touching a target file path. → *Expect:* the job runs and exits according to its real test command.
6. **Test an unrelated change.** Modify a file outside the filter, such as docs when testing backend filters. → *Expect:* the heavy job is skipped and the required status is satisfied by the wrapper or skip result.
7. **Document the filter ownership.** Add a brief comment near the path list explaining why lockfiles and shared files are included. → *Expect:* future maintainers can update the filter safely.

## Decision points

- Job is required by branch protection → use an always-running wrapper or provider-supported skipped-success behavior.
- Shared library changes affect many services → trigger all dependent service jobs.
- Path ownership is unclear → run the job by default until ownership is explicit.
- Monorepo has a build graph tool → use the graph tool's affected command instead of hand-maintained path lists.

## Failure modes & recovery

- **F1 Required check stuck pending:** detect PR blocked with a skipped workflow → add a wrapper status or update branch protection to require the always-present check.
- **F2 Job skipped when it should run:** detect changed shared code with no test job → add the shared path or dependency graph edge to the filter.
- **F3 Job runs too often:** detect path filters matching generated files or docs → tighten globs and test with a changed-files tool.
- **F4 Forked PR lacks permissions:** detect path-filter action failing on fork events → use provider-native path rules or read-only token settings.

## Verification

Two CI runs prove the behavior: a PR touching a matched path runs the target job and exits 0, while a PR touching only unmatched paths skips the heavy job and still reports all required checks as passing.

## Variations

- `GitHub Actions`: `paths` filters work at trigger time; job-level filtering needs an action or custom `git diff`.
- `GitLab CI`: `rules:changes` can be combined with `if` conditions for branches and merge requests.
- `Bazel/Nx/Turborepo/Pants`: run affected targets from the dependency graph for safer monorepo filtering.
- `docs-only`: use path filters to run spelling, link, or docs builds instead of application tests.

## Safety & privacy

Medium risk because an incorrect filter can skip tests for code that needs them. Include shared files, keep conservative defaults, and avoid exposing changed file lists from private paths into public notifications.
