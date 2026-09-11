---
name: set-up-a-ci-pipeline
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You add a CI pipeline that installs dependencies, runs the project checks on every pull request or merge request, and reports a clear pass/fail status.

## Preconditions

- The project has a known package manager and test command.
- You can edit CI configuration and access the repository's CI service.
- Required secrets are already available or can be added through the CI secret store.
- The default branch protection policy allows adding a new non-required check first.

## Steps

1. **Identify the canonical local checks.** Run the existing commands, such as `npm ci && npm test`, `pip install -r requirements.txt && pytest -q`, or `go test ./...`. → *Expect:* a known command set and current local result.
2. **Choose the CI trigger.** [GitHub Actions | GitLab CI] configure pull request and default-branch pushes. → *Expect:* CI runs for proposed changes and mainline updates.
3. **Create the pipeline file.** Add `.github/workflows/ci.yml` or `.gitlab-ci.yml` with checkout, runtime setup, dependency install, and test steps. → *Expect:* the CI service recognizes the configuration.
4. **Pin the runtime version.** Use `.nvmrc`, `.python-version`, `go.mod`, Docker image tags, or setup action versions. → *Expect:* CI and local runs use the same major runtime.
5. **Use clean dependency installation.** Run lockfile-respecting installs such as `npm ci`, `pnpm install --frozen-lockfile`, `pip install -r requirements.txt`, or `bundle install`. → *Expect:* dependency resolution is reproducible.
6. **Open a test pull request.** Push a branch with the CI config. → *Expect:* a CI run starts automatically and displays logs.
7. **Fix CI-only failures.** Adjust missing system packages, environment variables, cache paths, or test assumptions. → *Expect:* the CI job exits 0.
8. **Document the check name.** Record the final status-check name for branch protection or contributor docs. → *Expect:* maintainers know which check must stay green.

## Decision points

- Tests require services → add CI service containers or compose setup before the test step.
- Tests require secrets → use CI secret storage and skip forked PR access unless explicitly safe.
- Pipeline is slow → add dependency caching after the pipeline is correct.
- Multiple languages exist → split jobs per runtime or use a matrix.

## Failure modes & recovery

- **F1 Missing lockfile:** detect install resolves different versions in CI → add or regenerate the lockfile before relying on CI.
- **F2 CI cannot access secrets:** detect empty env vars or `401` in logs → add secrets through CI settings and mask outputs.
- **F3 Test depends on local state:** detect missing files, timezone, or database errors → make setup explicit in the pipeline.
- **F4 Workflow not triggered:** detect no run on PR → verify file path, branch, event trigger, and repository Actions/CI settings.

## Verification

The CI run for the pull request completes successfully with exit 0 for dependency installation and test steps, and the repository shows a green status check for the configured pipeline.

## Variations

- `GitHub Actions`: use `.github/workflows/ci.yml`, `actions/checkout`, and runtime setup actions.
- `GitLab CI`: use `.gitlab-ci.yml`, stages, cache keys, and project CI/CD variables.
- `CircleCI`: use `.circleci/config.yml` with jobs and workflows.
- `Docker`: build and test inside the same image used by developers or deployment.

## Safety & privacy

Medium risk because CI changes can block shared branches or expose logs. Keep secrets in the CI secret manager, avoid printing environment variables, and introduce required checks only after the new pipeline is stable.

