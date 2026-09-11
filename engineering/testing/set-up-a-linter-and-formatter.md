---
name: set-up-a-linter-and-formatter
domain: engineering
subdomain: testing
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

You add consistent linting and formatting commands that developers and CI can run with the same result.

## Preconditions

- The project language, package manager, and CI system are known.
- Existing style choices are understood enough to avoid a disruptive whole-repo rewrite unless approved.
- You can run the test suite after formatting changes.

## Steps

1. **Inventory current tooling.** Check package files such as `pyproject.toml`, `package.json`, `go.mod`, or `.prettierrc`. → *Expect:* you know whether a linter or formatter already exists.
2. **Choose standard tools for the stack.** [Python | JavaScript | Go] use Ruff/Black or Ruff format, ESLint/Prettier, or `gofmt`/`go vet`. → *Expect:* the selected tools are common and actively maintained for the language.
3. **Add minimal configuration.** Configure line length, target runtime, ignored generated paths, and import rules only where needed. → *Expect:* config files are small and match the project’s style.
4. **Add scripts.** Create commands such as `lint`, `format`, and `format:check` in the native task runner. → *Expect:* contributors can run one documented command locally.
5. **Run format in check mode first.** Use `ruff format --check .`, `prettier --check .`, or `gofmt -l .`. → *Expect:* the command reports files needing formatting without changing them.
6. **Apply formatting intentionally.** Run the formatter only if the resulting diff is acceptable for the task. → *Expect:* changed files are mechanical and easy to review.
7. **Wire CI to check only.** Add `npm run lint && npm run format:check` or equivalent to CI, not auto-formatting. → *Expect:* CI fails when code violates style and passes when clean.
8. **Run tests after tooling changes.** Execute the normal test command. → *Expect:* formatting and lint configuration did not break behavior.

## Decision points

- Repository already has tooling → extend existing config rather than replacing it.
- Large existing formatting drift → separate mechanical formatting from functional changes.
- Formatter and linter disagree → disable overlapping lint rules and let the formatter own whitespace.
- Generated files are flagged → exclude generated directories rather than editing generated output manually.

## Failure modes & recovery

- **F1 Whole-repo noisy diff:** detect hundreds of unrelated formatted files → split into a dedicated formatting change or narrow tool scope.
- **F2 Tool version drift:** detect different local and CI results → pin versions in lockfiles and use the same package manager command.
- **F3 Linter blocks legacy code:** detect many pre-existing violations → set a baseline, limit to changed files, or stage rule adoption.
- **F4 Formatter changes semantics:** detect failing tests after formatting → inspect language-sensitive constructs and update tool config or code.

## Verification

The configured commands, for example `npm run lint`, `npm run format:check`, and the project test command, all exit 0 locally and in CI.

## Variations

- `Python`: use Ruff for linting and formatting or pair Ruff with Black; configure in `pyproject.toml`.
- `JavaScript/TypeScript`: use ESLint for code quality and Prettier for formatting; avoid duplicate formatting rules in ESLint.
- `Go`: `gofmt` is canonical; pair with `go vet` and optional `golangci-lint`.
- `Rust`: use `cargo fmt --check` and `cargo clippy -- -D warnings` when the project enforces warnings.

## Safety & privacy

Medium risk because CI and broad formatter runs can block shared branches. Keep config minimal, pin tool versions, exclude vendored or generated files, and avoid uploading proprietary source to hosted lint services unless approved.
