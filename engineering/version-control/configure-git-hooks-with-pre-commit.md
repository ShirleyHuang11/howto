---
name: configure-git-hooks-with-pre-commit
domain: engineering
subdomain: version-control
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Install and pin `pre-commit` hooks so local commits run the same lightweight checks that the project expects in CI.

## Preconditions

- You are in the repository root and can edit project configuration.
- Python is available for `pre-commit`, or the repository already uses a package-manager wrapper.
- The repository has agreed lint, format, or secret-scan tools to run before commits.

## Steps

1. **Install the pre-commit runner.** Use the project's package manager, for example `python -m pip install pre-commit` or `brew install pre-commit`. → *Expect:* `pre-commit --version` prints a version and exits 0.
2. **Create the hook configuration.** Add `.pre-commit-config.yaml` with pinned hook repositories and revisions, for example `pre-commit sample-config > .pre-commit-config.yaml` and then edit the hooks. → *Expect:* the file contains explicit `repo`, `rev`, and `hooks` entries.
3. **Pin hook versions intentionally.** Run `pre-commit autoupdate` only when you are ready to accept newer hook versions, then review the diff. → *Expect:* each hook uses a concrete tag or commit, not `main` or `master`.
4. **Install the local Git hook.** Run `pre-commit install`. → *Expect:* `.git/hooks/pre-commit` exists and mentions `pre-commit`.
5. **Run the hooks across the repository.** Execute `pre-commit run --all-files`. → *Expect:* either all hooks pass or hooks modify files and ask you to rerun.
6. **Commit generated fixes after review.** If formatters changed files, inspect the edits and rerun `pre-commit run --all-files`. → *Expect:* the second run exits 0 with no unexpected file changes.
7. **Mirror the check in CI.** Add a CI job such as `pre-commit run --all-files --show-diff-on-failure`. → *Expect:* pull requests fail when the same hooks fail outside the developer machine.

## Decision points

- Repository already has a hook manager → add `pre-commit` only if it does not duplicate or fight the existing system.
- Hook is slow or needs services → keep it out of `pre-commit`; run it in CI or a manual check instead.
- Hook changes many legacy files → either accept a dedicated formatting PR or narrow the hook with `files:` and schedule a cleanup.

## Failure modes & recovery

- **F1 Missing executable:** detect `pre-commit: command not found` → install through the repo's standard package manager and re-run `pre-commit --version`.
- **F2 Hook modifies files repeatedly:** detect the same files changing on every run → check formatter versions and line-ending settings, then pin compatible versions.
- **F3 Private hook repository denied:** detect authentication or 404 errors while installing hooks → use an accessible mirror or configure credentials with least privilege.
- **F4 CI passes locally but fails remotely:** detect different hook output in CI → compare runtime versions and cache keys; install the same `pre-commit` version in CI.

## Verification

Run `pre-commit validate-config && pre-commit run --all-files --show-diff-on-failure`; both commands exit 0, and the CI job that invokes `pre-commit run --all-files --show-diff-on-failure` is green on the PR.

## Variations

- `Python`: install with `python -m pip install pre-commit` or a locked tool such as `uv tool install pre-commit`.
- `Node`: call `pre-commit` from CI separately from `npm test`; do not hide hook failures inside lifecycle scripts.
- `Monorepo`: use `files:` and `exclude:` patterns so hooks only scan relevant paths.

## Safety & privacy

Medium risk because hooks can block commits and CI for the team. Do not add hooks that upload source code or secrets to third-party services without review, pin every hook revision, and treat secret-scanning findings as sensitive.
