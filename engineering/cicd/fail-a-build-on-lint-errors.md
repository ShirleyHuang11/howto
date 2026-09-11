---
name: fail-a-build-on-lint-errors
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [engineering/cicd/set-up-a-ci-pipeline]
status: draft
last_verified: 2026-09-11
---

## Goal

You add linting to CI so style, syntax, and static-analysis violations fail the build before code is merged.

## Preconditions

- A linter is configured locally or the team has selected one.
- The repository has a CI pipeline that runs on pull requests or merge requests.
- Existing lint violations are either fixed first or intentionally baselined.

## Steps

1. **Run the linter locally.** Execute the project command, such as `npm run lint`, `ruff check .`, `flake8`, `golangci-lint run`, or `bundle exec rubocop`. → *Expect:* local lint output and exit status are known.
2. **Fix or baseline current violations.** Repair issues that should fail CI, or configure a documented ignore list for legacy code. → *Expect:* the linter exits 0 locally on the intended scope.
3. **Add a CI lint job.** [GitHub Actions | GitLab CI] add a job or stage that installs dependencies and runs the same lint command. → *Expect:* CI has a visible lint step.
4. **Ensure nonzero exit codes fail the build.** Remove `|| true`, warning-only wrappers, or permissive flags. → *Expect:* lint violations mark the job failed.
5. **Cache dependencies only if already safe.** Reuse existing cache configuration without changing lint semantics. → *Expect:* lint performance improves without hiding install failures.
6. **Test a deliberate violation on a throwaway branch.** Add a temporary lint error and push. → *Expect:* the CI lint job fails with the linter's diagnostic.
7. **Remove the deliberate violation and rerun.** → *Expect:* the lint job returns green.

## Decision points

- Existing code has many violations → create a scoped baseline and require lint only on changed files until cleanup is scheduled.
- Linter overlaps formatter → run formatter checks separately or before lint to reduce noise.
- Generated files fail lint → exclude generated output and lint the source generator or templates.
- Lint is slow → use cache, changed-file linting, or a faster linter, but keep full lint on scheduled CI.

## Failure modes & recovery

- **F1 CI command differs from local command:** detect local pass and CI fail for different rule sets → centralize the command in package scripts or Makefile.
- **F2 Lint warnings do not fail:** detect warnings in logs with green job → enable strict flags such as `--max-warnings=0` for ESLint when intended.
- **F3 Generated files create noise:** detect violations in build artifacts → update ignore patterns and verify source files are still covered.
- **F4 Linter version drift:** detect new failures without code changes → pin linter versions in the lockfile or tool config.

## Verification

The CI lint job exits nonzero for a deliberate lint violation and exits 0 after the violation is removed, while the normal pull request shows a green lint status.

## Variations

- `ESLint`: use `eslint . --max-warnings=0` when warnings must block merges.
- `Python`: use `ruff check .` for fast linting or project-standard tools like `flake8` and `mypy`.
- `Go`: use `go vet ./...` and optionally `golangci-lint run`.
- `pre-commit`: run `pre-commit run --all-files` in CI to match developer hooks.

## Safety & privacy

Medium risk because a new lint gate can block contributors. Fix or baseline existing issues before requiring the check, keep tool versions pinned, and do not upload source code to third-party lint services unless approved.

