---
name: initialize-a-git-repository
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

You create a new Git repository in an existing project directory, make the first commit, and optionally connect it to a remote so future changes are trackable and shareable.

## Preconditions

- Git is installed: `git --version` exits 0.
- The project directory contains only files that should be considered for version control, or a `.gitignore` plan exists.
- You know whether the default branch should be `main`, `master`, or a team-specific branch name.

## Steps

1. **Enter the project root.** Run `pwd` and inspect the expected project files with `ls`. → *Expect:* the working directory is the project root, not a parent directory or home folder.
2. **Initialize Git with the intended default branch.** Run `git init -b main`. → *Expect:* Git prints that it initialized an empty repository and `.git/` exists.
3. **Add an ignore file before staging generated files.** Create or update `.gitignore` for dependency directories, build output, local environment files, and editor metadata; for example include `node_modules/`, `dist/`, `.env`, and `.DS_Store` when applicable. → *Expect:* `git status --ignored -s` shows generated files as ignored rather than staged.
4. **Stage only source and required project files.** Run `git add .`, then inspect with `git status --short`. → *Expect:* intended source, config, lockfiles, and docs are staged; secrets and build artifacts are absent.
5. **Create the first commit.** Run `git commit -m "Initial commit"`. → *Expect:* Git creates a root commit and reports the number of files changed.
6. **Connect a remote if one exists.** Run `git remote add origin git@github.com:OWNER/REPO.git` or the equivalent HTTPS URL. → *Expect:* `git remote -v` shows `origin` for fetch and push.
7. **Push the default branch when ready.** Run `git push -u origin main`. → *Expect:* the push exits 0 and sets `main` to track `origin/main`.

## Decision points

- Repository already has `.git/` → do not reinitialize; inspect `git status` and continue from the existing repository state.
- Generated files appear in `git status --short` → update `.gitignore`, then run `git restore --staged <path>` before committing.
- Remote branch already exists → fetch first with `git fetch origin` and reconcile histories before pushing.

## Failure modes & recovery

- **F1 Wrong directory initialized:** detect `.git/` in the wrong path or unexpected files in `git status` → remove only that mistaken `.git/` directory after confirming it is not an existing repository, then initialize in the correct root.
- **F2 Missing identity:** detect `Author identity unknown` → set `git config user.name` and `git config user.email`, preferably at repo scope for automation.
- **F3 Push rejected:** detect `non-fast-forward` or existing remote history → run `git fetch origin`, inspect `git log --oneline --graph --all`, then merge or rebase intentionally.
- **F4 Secret staged:** detect `.env`, key files, or credentials in `git diff --cached --name-only` → unstage with `git restore --staged <path>`, add ignore rules, and rotate exposed credentials if they were committed.

## Verification

`git rev-parse --is-inside-work-tree` prints `true`, `git log --oneline -1` shows `Initial commit`, and, if a remote was configured, `git ls-remote --heads origin main` exits 0 and returns the pushed branch SHA.

## Variations

- `GitHub/GitLab`: create the empty remote repository in the web UI or with `gh repo create` / `glab repo create` before `git remote add origin`.
- `default branch`: use `git init -b trunk` or another team standard when the repository does not use `main`.
- `monorepo`: initialize only at the monorepo root; do not create nested repositories unless submodules are explicitly intended.

## Safety & privacy

Low risk when local, but the first push can publish secrets or generated artifacts. Review staged filenames and `.gitignore` before committing, never commit private keys or `.env` files, and use a least-privilege deploy key or personal token for automation.
