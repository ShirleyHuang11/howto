---
name: measure-code-coverage
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: [engineering/run-the-test-suite]
status: draft
last_verified: 2026-09-11
---

## Goal

Measure test coverage with the repository's coverage tool and use the report to identify meaningful untested behavior.

## Preconditions

- The test suite runs successfully: `engineering/run-the-test-suite`.
- The language coverage tool is installed or can be added through the project dependency manager.
- Coverage thresholds, if any, are known.

## Steps

1. **Find the existing coverage command.** Check scripts, CI, and documentation for commands such as `pytest --cov`, `npm run coverage`, or `go test -cover`. → *Expect:* you know the canonical command or confirm one must be added.
2. **Install coverage tooling if needed.** [BRANCH: Python | Node | Go] Add `pytest-cov`, use `c8` or `vitest --coverage`, or use Go's built-in coverage. → *Expect:* the coverage command is available.
3. **Run coverage locally.** Execute `pytest --cov=src --cov-report=term-missing`, `npm run coverage`, or `go test ./... -coverprofile=coverage.out`. → *Expect:* tests run and a coverage summary is printed.
4. **Inspect missing lines.** Open the terminal report or HTML output. → *Expect:* missing branches or files are visible by path and line.
5. **Ignore generated or irrelevant files deliberately.** Configure omit patterns for generated code, migrations, vendored files, or type stubs. → *Expect:* the report reflects code humans maintain.
6. **Add or adjust threshold only with team agreement.** Set realistic minimums in config or CI. → *Expect:* CI fails when coverage drops below the configured threshold.
7. **Re-run coverage after changes.** Execute the same command again. → *Expect:* report generation exits 0 and numbers are stable enough for CI.

## Decision points

- High coverage but missed bug → add targeted behavioral tests, not just line coverage.
- Low legacy coverage → introduce a baseline threshold and ratchet gradually.
- Generated code dominates report → omit it explicitly and document why.

## Failure modes & recovery

- **F1 Coverage tool cannot import app:** detect import errors only under coverage → align working directory, environment variables, and test paths.
- **F2 Threshold blocks unrelated PR:** detect broad legacy shortfall → set a baseline or diff coverage rule instead of an unrealistic global threshold.
- **F3 Missing branch coverage:** detect line coverage passes but conditions are untested → enable branch coverage where supported.
- **F4 Report includes vendored code:** detect third-party paths in report → add omit or include rules.

## Verification

Run the coverage command, for example `pytest --cov=src --cov-report=term-missing` or `npm run coverage`; it exits 0, prints a total percentage, and CI enforces the agreed threshold or uploads the report successfully.

## Variations

- `pytest`: use `pytest-cov` with `--cov-report=term-missing` and optional `--cov-fail-under`.
- `Jest or Vitest`: use `--coverage` and configure `collectCoverageFrom`.
- `Go`: use `go test ./... -coverprofile=coverage.out` and inspect with `go tool cover -html=coverage.out`.

## Safety & privacy

Low risk because coverage is diagnostic. Do not publish reports that include private source paths or secrets from generated fixtures, and avoid gaming thresholds with empty tests.
