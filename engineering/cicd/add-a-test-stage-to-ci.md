---
name: add-a-test-stage-to-ci
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

You add a dedicated CI test stage that runs the project's automated tests after dependencies are installed and fails the pipeline when tests fail.

## Preconditions

- A CI pipeline already exists and runs on pull requests or merge requests.
- The test command is known and passes locally or has documented expected failures.
- Required test services, fixtures, and environment variables are available in CI.

## Steps

1. **Run the test command locally.** Execute the exact intended command, such as `pytest -q`, `npm test`, `go test ./...`, or `bundle exec rspec`. → *Expect:* the local result and runtime requirements are known.
2. **Add a test stage or job.** [GitHub Actions | GitLab CI] create a `test` job after install/build, or add `stage: test` in GitLab. → *Expect:* the CI graph shows a distinct test step.
3. **Install test dependencies.** Include lockfile-based dependency installation and any system packages needed by tests. → *Expect:* the job reaches the test command without missing dependency errors.
4. **Configure test environment variables.** Set safe defaults or CI secrets for test-only services. → *Expect:* tests do not depend on a developer's local `.env`.
5. **Publish test reports when supported.** Emit JUnit XML or coverage artifacts, for example `pytest --junitxml=reports/pytest.xml`. → *Expect:* CI displays test failures in its UI or stores the report artifact.
6. **Make failures fail the job.** Ensure the test command is not hidden behind `|| true` and shell scripts use `set -euo pipefail` where appropriate. → *Expect:* any failing test makes the CI job red.
7. **Push and observe a run.** Open or update a PR/MR with the CI change. → *Expect:* the new test stage runs and reports pass/fail status.

## Decision points

- Tests need a database → add service containers and migrations before the test command.
- Tests are too slow for every PR → split unit tests into required CI and schedule longer integration tests separately.
- Flaky tests fail the first CI run → quarantine only with an issue and owner; do not ignore the entire test command.
- Coverage is required → add coverage thresholds after the test stage is stable.

## Failure modes & recovery

- **F1 Test command exits 0 despite failures:** detect failed assertions in logs with green job → remove wrappers that swallow exit codes.
- **F2 Missing service readiness:** detect connection refused to database or cache → add health checks or wait scripts before tests.
- **F3 Report path not found:** detect CI artifact upload warning → create the report directory and verify the test runner output path.
- **F4 CI-only timezone or locale failure:** detect date/string mismatch → set `TZ=UTC` and stable locale variables for tests.

## Verification

A CI run shows a separate test stage that exits 0 when tests pass and exits nonzero when a deliberately failing test is pushed to a throwaway branch.

## Variations

- `pytest`: use `pytest -q --junitxml=reports/pytest.xml`.
- `Jest/Vitest`: use `npm test -- --ci` and a JUnit reporter if the CI UI supports it.
- `Go`: use `go test ./...` and optionally `gotestsum --junitfile`.
- `GitLab`: declare `stages: [test]` or add the job to an existing stage list.

## Safety & privacy

Medium risk because a broken test stage can block all contributors. Avoid exposing test secrets in logs, use isolated test databases, and make the check required only after it has passed reliably.

