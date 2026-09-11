---
name: tag-a-release
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

You create and push a Git tag that points to the exact release commit, with enough metadata for release tooling and humans to identify it.

## Preconditions

- The release commit is merged and CI is green.
- You know the version string and tag naming convention, such as `v1.2.3`.
- You have permission to push tags.

## Steps

1. **Fetch and update the release branch.** Run `git fetch --tags --prune origin` and `git switch main && git pull --ff-only origin main`. → *Expect:* the local release branch matches the remote.
2. **Verify the release commit.** Run `git rev-parse HEAD` and compare it to the approved commit or CI build SHA. → *Expect:* HEAD is exactly the commit being released.
3. **Confirm the tag does not already exist.** Run `git rev-parse -q --verify refs/tags/v1.2.3`. → *Expect:* the command exits nonzero for a new tag.
4. **Create an annotated tag.** Run `git tag -a v1.2.3 -m "Release v1.2.3"`. → *Expect:* `git show v1.2.3 --no-patch` displays tag metadata and the target commit.
5. **Push the tag.** Run `git push origin v1.2.3`. → *Expect:* the remote accepts the new tag and release automation may start.
6. **Watch release checks.** [GitHub Actions | GitLab CI] run `gh run list --branch v1.2.3 --limit 5` or inspect tag pipeline status. → *Expect:* release workflow is queued, running, or successful.

## Decision points

- Lightweight tags are project policy → use `git tag v1.2.3`, but annotated tags are preferable for releases.
- Tag already exists locally but not remotely → inspect with `git show v1.2.3`; delete only if it was never published and policy allows.
- Release commit is not HEAD → tag the explicit approved SHA with `git tag -a v1.2.3 <sha> -m "Release v1.2.3"`.

## Failure modes & recovery

- **F1 Tag points to wrong commit:** detect mismatch in `git rev-list -n 1 v1.2.3` → if not pushed, delete and recreate; if pushed, follow the project's tag correction policy.
- **F2 Push denied:** detect protected tag or permission error → request release permission or have an authorized release manager push.
- **F3 Existing remote tag:** detect `already exists` rejection → inspect remote tag and do not overwrite without release-manager approval.
- **F4 Release workflow fails:** detect red tag pipeline → fix release config or code, then create a new patch tag according to policy.

## Verification

`git ls-remote --tags origin refs/tags/v1.2.3` returns the remote tag, `git rev-list -n 1 v1.2.3` matches the approved release commit SHA, and the tag-triggered CI or release workflow reports success.

## Variations

- `signed tags`: use `git tag -s v1.2.3 -m "Release v1.2.3"` when GPG or SSH signing is required.
- `GitHub release`: run `gh release create v1.2.3 --generate-notes` after pushing the tag.
- `pre-release`: use semver labels such as `v1.2.3-rc.1` and the matching release channel.

## Safety & privacy

Medium risk because tags often trigger production release automation and are treated as immutable. Verify the exact commit, version, and CI status before pushing, and do not rewrite published tags without explicit release-owner approval.
