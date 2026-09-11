---
name: add-a-type-check-to-ci
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You add a type-checking job to CI so type errors fail before code is merged.

## Preconditions

- The project has a type checker or can adopt one without changing runtime behavior.
- CI configuration is editable for the repository.
- Dependencies install reproducibly from a lockfile or equivalent.

## Steps

1. **Find the existing build commands.** Inspect `package.json`, `pyproject.toml`, `Makefile`, and CI workflow files. → *Expect:* you know the dependency install command and current CI stages.
2. **Add or confirm the type-check script.** [TypeScript | Python] use `tsc --noEmit`, `vue-tsc --noEmit`, `mypy`, `pyright`, or the project’s existing command. → *Expect:* a local command exists such as `npm run typecheck` or `uv run mypy .`.
3. **Run the type check locally.** Execute the exact command intended for CI. → *Expect:* it exits 0 or reveals existing type debt.
4. **Handle existing type debt deliberately.** Fix small errors, narrow scope, or add a checked baseline instead of suppressing the whole project silently. → *Expect:* the command exits 0 for the chosen scope.
5. **Add CI job or step.** [GitHub Actions | GitLab CI] add the command after dependency installation and before packaging or deploy. → *Expect:* CI configuration includes a named type-check step.
6. **Cache dependencies safely.** Use the package manager’s cache keyed by lockfile hash where supported. → *Expect:* CI stays reproducible while avoiding repeated downloads.
7. **Open or update the PR and inspect CI.** Push the branch through the normal review flow. → *Expect:* the type-check job appears and reports success or a clear failure.

## Decision points

- Type checker already runs inside build → keep one authoritative command and make CI call it explicitly if visibility matters.
- Existing code has many errors → gate changed packages first and create tracked follow-up work for full coverage.
- Monorepo has multiple packages → run type checks per package or through the workspace task runner.
- Generated types are missing in CI → add generation before type checking and verify generated output is reproducible.

## Failure modes & recovery

- **F1 Missing dev dependencies in CI:** detect `command not found` for `tsc`, `mypy`, or `pyright` → install dev dependencies in CI and commit lockfile updates.
- **F2 Local passes but CI fails:** detect version mismatch → pin runtime and package manager versions.
- **F3 Type generation absent:** detect missing `.d.ts`, GraphQL, or OpenAPI types → add the codegen step before type checking.
- **F4 Job too slow:** detect CI timeout or large runtime increase → cache dependencies and split monorepo checks.

## Verification

The local type-check command, such as `npm run typecheck` or `uv run mypy .`, exits 0, and the CI run for the PR shows the named type-check job green.

## Variations

- `TypeScript`: use `tsc --noEmit`; for framework projects use the framework-aware checker such as `vue-tsc`.
- `Python`: use `mypy` or `pyright`, preferably with configuration in `pyproject.toml`.
- `GitHub Actions`: add a separate job or named step in `.github/workflows/*.yml`.
- `GitLab CI`: add a `typecheck` job in the `test` stage with the same install cache policy as tests.

## Safety & privacy

Medium risk because CI changes can block merges. Keep the first gate scoped to a command that already exits 0 locally, pin tool versions, and do not print environment secrets from diagnostic type-generation scripts.
