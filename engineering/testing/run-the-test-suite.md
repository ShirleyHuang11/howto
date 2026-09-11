---
name: run-the-test-suite
domain: engineering
subdomain: testing
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

Run the repository's automated tests in the intended way and produce a reliable pass/fail result.

## Preconditions

- Dependencies are installed or the repository documents how to install them.
- Required local services, such as a test database or cache, are available if the suite needs them.
- You are at the repository root.

## Steps

1. **Find the canonical test command.** Read `README`, `CONTRIBUTING`, package scripts, Makefile, or CI config. → *Expect:* one command is clearly preferred for the full or relevant suite.
2. **Install dependencies if missing.** [BRANCH: Python | Node | Go] Run `python -m pip install -r requirements-dev.txt`, `npm ci`, or `go mod download`. → *Expect:* dependency installation exits 0.
3. **Start required test services.** If documented, run `docker compose up -d postgres redis` or equivalent. → *Expect:* `docker compose ps` shows required services healthy or running.
4. **Set test environment variables.** Export only documented test values such as `DATABASE_URL=postgres://.../app_test`. → *Expect:* no production hostnames or secrets are used.
5. **Run a fast smoke test if available.** Execute a small command such as `pytest -q tests/smoke` or `npm test -- --runInBand --listTests`. → *Expect:* the runner starts successfully.
6. **Run the suite.** Use the canonical command, for example `pytest -q`, `npm test`, `go test ./...`, or `make test`. → *Expect:* the command exits 0 for a passing suite or prints actionable failures.
7. **Capture failures without hiding them.** If the suite fails, save the first failing test name, error text, and command used. → *Expect:* the next action can target the actual failure.
8. **Shut down temporary services.** Stop services started only for tests, such as `docker compose down`. → *Expect:* no test containers remain running unintentionally.

## Decision points

- Full suite is too slow for the current change → run targeted tests first, then full CI before merge.
- Tests require unavailable paid services → use documented mocks or skip only with an issue link and reviewer awareness.
- Failures reproduce in CI only → compare OS, runtime versions, environment variables, and service versions.

## Failure modes & recovery

- **F1 Missing dependency:** detect import or module-not-found errors → install dev dependencies with the repository's lockfile-aware command.
- **F2 Wrong database:** detect connection to production or shared staging → stop immediately, correct `DATABASE_URL`, and use a disposable test database.
- **F3 Port conflict:** detect `address already in use` → identify the process or configure a test port.
- **F4 Flaky failure:** detect pass on rerun without code changes → quarantine only per project policy and create a tracking issue.

## Verification

Run the canonical suite command, such as `pytest -q`, `npm test`, `go test ./...`, or `make test`; it exits 0. If CI is required, the corresponding status check is green for the same commit.

## Variations

- `pytest`: use `pytest -q` for concise output and `-k` for targeted selection.
- `Jest`: use `npm test -- --runInBand` when debugging shared-state issues.
- `Docker Compose`: run services with a test-only compose profile and tear them down afterward.

## Safety & privacy

Low risk when pointed at local or disposable resources. Never run tests against production databases, never print real secrets in logs, and clean up local containers or temporary data after the suite.
