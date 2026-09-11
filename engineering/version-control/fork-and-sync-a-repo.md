---
name: fork-and-sync-a-repo
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

You create or use a fork, configure remotes correctly, and keep the fork synchronized with the upstream repository without overwriting your work.

## Preconditions

- You have an account on the hosting provider and permission to fork the upstream project.
- Git authentication is configured for your fork.
- You know the upstream default branch, usually `main`.

## Steps

1. **Clone your fork or add it as origin.** Run `git clone git@github.com:YOUR_USER/REPO.git` or inspect an existing clone with `git remote -v`. → *Expect:* `origin` points to your fork.
2. **Add the upstream remote.** Run `git remote add upstream git@github.com:OWNER/REPO.git`. → *Expect:* `git remote -v` shows both `origin` and `upstream`.
3. **Fetch all remotes.** Run `git fetch --prune origin` and `git fetch --prune upstream`. → *Expect:* local remote-tracking branches are current.
4. **Sync the local default branch.** Run `git switch main` and `git merge --ff-only upstream/main`. → *Expect:* local `main` fast-forwards to upstream.
5. **Push the synced branch to your fork.** Run `git push origin main`. → *Expect:* your fork's `main` matches upstream `main`.
6. **Create work branches from upstream.** Run `git switch -c feature/name upstream/main`. → *Expect:* the feature branch starts from the current upstream base.
7. **Verify remotes and divergence.** Run `git log --oneline --left-right --cherry-pick upstream/main...origin/main`. → *Expect:* no unexpected commits are listed after syncing.

## Decision points

- Your fork has commits on `main` → move them to a feature branch before syncing.
- Upstream uses `master` or another branch → substitute that branch consistently.
- Fast-forward fails → inspect divergence and avoid force-pushing until you know which commits are yours.

## Failure modes & recovery

- **F1 Origin points to upstream:** detect `origin` URL owned by the upstream org → change it with `git remote set-url origin <fork-url>`.
- **F2 Fast-forward merge fails:** detect `Not possible to fast-forward` → create a backup branch, inspect local commits, then rebase or reset only after confirmation.
- **F3 Push denied to fork:** detect auth or permission error → verify SSH key/token and fork ownership.
- **F4 PR opened from stale fork:** detect merge conflicts or old CI failures → sync from upstream, rebase the feature branch, and push with `--force-with-lease` if needed.

## Verification

`git remote -v` shows `origin` as your fork and `upstream` as the source repository, `git rev-parse origin/main` matches `git rev-parse upstream/main` after syncing, and `git log --left-right --cherry-pick upstream/main...origin/main --oneline` prints no unexpected divergence.

## Variations

- `GitHub CLI`: run `gh repo fork OWNER/REPO --clone --remote=true` to create the fork and remotes.
- `GitLab`: use the Fork button or `glab repo fork`, then add the original project as `upstream`.
- `read-only upstream`: always push feature branches to `origin` and open PRs/MRs back to upstream.

## Safety & privacy

Medium risk because syncing can overwrite branch state if done carelessly. Keep work off your fork's default branch, verify remote URLs before pushing, and use `--force-with-lease` only on branches you own.
