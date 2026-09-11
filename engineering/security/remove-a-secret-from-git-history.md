---
name: remove-a-secret-from-git-history
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: high
prerequisites: [engineering/rotate-a-leaked-api-key]
status: draft
last_verified: 2026-09-11
---

## Goal

You purge a committed secret from repository history after rotating it, then verify the secret is no longer present in reachable commits.

## Preconditions

- The exposed secret has already been revoked or rotated.
- Repository owners approve history rewriting and downstream coordination.
- All collaborators and automation consumers can be notified to reclone or reset.

## Steps

1. **Confirm the secret is no longer valid.** Verify provider revocation from `engineering/rotate-a-leaked-api-key`. → *Expect:* using the old secret returns 401/403 or the provider shows it disabled.
2. **Create a fresh mirror clone for rewriting.** Use an isolated working copy: `git clone --mirror <repo-url> repo.git` and work only in that clone. → *Expect:* a bare mirror clone exists for history rewrite work.
3. **Choose a history rewrite tool.** Prefer `git filter-repo` or BFG Repo-Cleaner over manual filter-branch. → *Expect:* the tool is installed and version output works.
4. **Rewrite the secret out of history.** Example with replacements: create `replacements.txt` containing the exact secret replaced by `***REMOVED***`, then run `git filter-repo --replace-text replacements.txt`. → *Expect:* rewrite completes and reports changed refs.
5. **Scan the rewritten repository.** Run `gitleaks detect --source repo.git --redact` or `trufflehog git file://$PWD/repo.git --only-verified`. → *Expect:* the removed secret is not detected.
6. **Coordinate the force push.** ⚠️ *Irreversible:* rewriting published history disrupts every clone and open branch; confirm owner approval, rotation completion, and collaborator notice first. Push rewritten refs with the chosen tool's recommended force command. → *Expect:* remote refs now point to rewritten history.
7. **Invalidate caches and forks where possible.** Ask hosting support or use platform tools to clear cached views; notify fork owners if applicable. → *Expect:* obvious hosted references to the secret are removed or access-restricted.
8. **Tell collaborators how to recover.** Provide exact reset/reclone instructions and warn not to merge old branches. → *Expect:* active developers move to the rewritten history.

## Decision points

- Secret is still valid → rotate/revoke first; history cleanup is not sufficient.
- Repository is public or forked → assume exposure is permanent and focus on revocation plus cleanup.
- Rewrite would disrupt release branches → schedule a maintenance window and tag replacement releases.
- Only latest commit is affected and unpushed → amend locally instead of rewriting shared history.

## Failure modes & recovery

- **F1 Secret still detected:** detect scanner finding after rewrite → add all variants to replacements and rerun from a fresh mirror.
- **F2 Collaborator pushes old history:** detect rejected or resurrected commits → block old refs, ask them to reclone/reset, and rescan.
- **F3 CI uses old commit:** detect builds pulling missing refs → update branch references, caches, and deployment pins.
- **F4 Hosted cache still shows secret:** detect web UI/search result contains secret → request cache purge from the hosting provider.

## Verification

The leaked credential is revoked, `gitleaks detect --source repo.git --redact` or equivalent exits 0 on the rewritten mirror, and the remote default branch no longer contains the secret when scanned from a fresh clone.

## Variations

- `git filter-repo`: preferred for precise rewrites and modern Git workflows.
- `BFG Repo-Cleaner`: useful for removing large files or replacing known secret strings quickly.
- `GitHub/GitLab`: coordinate protected-branch settings, pull requests, forks, and hosted cache purges.

## Safety & privacy

High risk because published history rewrites are disruptive and do not make a leaked secret safe again. Rotate first, minimize who sees the secret, warn collaborators, and never paste the secret into public commands or issues.
