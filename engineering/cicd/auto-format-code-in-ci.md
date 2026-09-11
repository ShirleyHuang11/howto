---
name: auto-format-code-in-ci
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You make CI enforce code formatting and, when desired, automatically propose formatting changes. The end state is a reproducible formatter check that fails on unformatted code or opens a safe formatting update.

## Preconditions

- The project already has or can adopt a deterministic formatter.
- CI can install dependencies and run repository scripts.
- Auto-commit permissions are approved if CI will write back to branches.

## Steps

1. **Choose one formatter per language surface.** Use standard tools such as `prettier`, `black`, `ruff format`, `gofmt`, `rustfmt`, or `terraform fmt`. → *Expect:* a formatter command exists and produces deterministic output locally.
2. **Add a check-mode script.** [BRANCH: npm, add `format:check` as `prettier --check .` | Python, use `black --check .` or `ruff format --check .` | Go, use `test -z "$(gofmt -l .)"`] → *Expect:* the script exits 0 on formatted code and nonzero when files need formatting.
3. **Run the formatter locally once.** Execute the write-mode command, such as `npm run format`, `black .`, or `gofmt -w .`. → *Expect:* any formatting diff is visible in the working tree.
4. **Add the CI check.** Insert a workflow step that runs the check-mode script after dependency installation. → *Expect:* CI fails with clear formatter output when code is unformatted.
5. **Optionally add an auto-format bot workflow.** For trusted branches, run the write-mode formatter and commit changes with a bot token. → *Expect:* CI creates a commit or PR containing only formatting changes.
6. **Protect against unsafe write events.** Disable auto-commit on untrusted fork pull requests and use read-only tokens for check-only jobs. → *Expect:* fork PRs run checks without receiving write credentials.
7. **Verify with an intentionally unformatted file.** Create a temporary branch with bad formatting and run CI. → *Expect:* the formatter check fails or the bot proposes a formatting-only patch.

## Decision points

- Repository accepts bot commits → use auto-format only on trusted branches.
- Fork PRs are common → prefer fail-only checks and let contributors run the formatter locally.
- Multiple formatters overlap → define file ownership so two tools do not rewrite the same files.
- Generated files are committed → exclude them or format them as part of generation.

## Failure modes & recovery

- **F1 Formatter versions differ:** detect local and CI disagreeing → pin formatter versions in lockfiles or tool config.
- **F2 Bot changes non-format files:** detect semantic diffs in auto-commit → restrict the command and review the diff before enabling write-back.
- **F3 Fork PR permission failure:** detect token or push denied errors → skip auto-commit for fork events.
- **F4 Endless format loop:** detect bot commits repeatedly changing the same files → ensure all jobs use the same formatter version and line-ending settings.

## Verification

The CI formatter job exits 0 on formatted code and exits nonzero on a branch with an intentional formatting violation, or the approved bot workflow opens a formatting-only change that then makes the check pass.

## Variations

- `Prettier`: use `prettier --check .` in CI and `prettier --write .` locally.
- `Python`: `ruff format --check .` is fast; `black --check .` remains common.
- `Go`: `gofmt -l` should print no files; combine with `go test ./...`.
- `Rust`: `cargo fmt -- --check` enforces `rustfmt`.

## Safety & privacy

Medium risk if CI writes to branches or has broad tokens. Keep auto-format write access limited to trusted branches, never expose bot tokens to forked code, and ensure formatting commits do not include generated secrets or local environment files.
