---
name: set-up-a-gitignore
domain: engineering
subdomain: version-control
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

You create or update `.gitignore` so Git tracks source and required lockfiles while excluding secrets, local state, dependencies, and generated artifacts.

## Preconditions

- The repository language, build tools, and deployment artifacts are known.
- You can distinguish source files from generated output.
- No secrets or local-only files should already be staged.

## Steps

1. **Inspect current repository state.** Run `git status --short --ignored`. → *Expect:* tracked, untracked, and ignored files are visible.
2. **Identify tool-specific ignore patterns.** Check frameworks and package managers, then add entries such as `node_modules/`, `.venv/`, `dist/`, `build/`, `.env`, `.DS_Store`, and coverage output where applicable. → *Expect:* `.gitignore` covers local and generated artifacts without hiding source.
3. **Preserve files that must be tracked.** Add negation rules if needed, such as `!.env.example` or `!dist/manifest.json` for required artifacts. → *Expect:* templates and required generated files remain visible to Git.
4. **Unstage files newly ignored.** If generated or secret files are staged, run `git restore --staged <path>`. → *Expect:* ignored files are not in `git diff --cached --name-only`.
5. **Remove already tracked generated files only by deliberate change.** Run `git rm --cached <path>` for files that should stop being tracked while remaining locally. → *Expect:* the file is scheduled for removal from the repository but still exists on disk.
6. **Check ignore behavior.** Run `git check-ignore -v <path>` for representative files. → *Expect:* Git prints the matching `.gitignore` rule for files that should be ignored.
7. **Validate staged result.** Run `git diff --cached -- .gitignore` and `git status --short --ignored`. → *Expect:* `.gitignore` contains only intentional patterns and ignored files are marked `!!`.

## Decision points

- File contains a real secret and was already committed → stop and follow a history cleanup and secret rotation procedure.
- Generated file is required by deployment → track it or document the build step; do not ignore it blindly.
- Pattern hides too much → replace broad globs with narrower directory-specific rules.

## Failure modes & recovery

- **F1 Source file accidentally ignored:** detect missing file from `git status` and matching `git check-ignore -v` output → narrow or remove the ignore pattern.
- **F2 Secret already tracked:** detect `.env` or key file in `git ls-files` → remove from tracking with `git rm --cached`, rotate the secret, and use the project's history-removal policy if published.
- **F3 Required lockfile ignored:** detect package lock absent from status → add a negation rule or remove the broad pattern.
- **F4 Ignore rule not applying:** detect file still untracked normally → fix path anchoring, trailing slash, or parent `.gitignore` precedence.

## Verification

`git check-ignore -v <ignored-path>` prints the intended rule, `git check-ignore -q <tracked-template>` exits nonzero for files that should remain trackable, and `git diff --cached --name-only` excludes secrets and generated artifacts.

## Variations

- `Node.js`: usually ignore `node_modules/`, build output, coverage, and `.env*` except `.env.example`; usually track lockfiles.
- `Python`: ignore `.venv/`, `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, build artifacts, and local `.env`.
- `Docker`: keep `.dockerignore` separate; `.gitignore` controls Git history, not build context alone.

## Safety & privacy

Low risk when done before the first commit, higher if secrets were already tracked. Never rely on `.gitignore` to protect committed secrets; rotate exposed credentials and remove them from history through the approved process.
