---
name: revert-a-bad-commit
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

You safely undo a committed change by creating a new revert commit, preserving published history and making the rollback auditable.

## Preconditions

- The bad commit SHA or merge commit is known.
- The working tree is clean.
- You know whether the target commit is already published or deployed.

## Steps

1. **Identify the exact commit.** Run `git log --oneline --decorate` or inspect the PR/CI history. → *Expect:* the bad commit SHA and scope are known.
2. **Inspect the commit before reverting.** Run `git show --stat <sha>` and `git show <sha>`. → *Expect:* you confirm it is the change to undo.
3. **Create the revert commit.** Run `git revert <sha>` for a normal commit. → *Expect:* Git creates a new commit that applies the inverse patch or stops for conflicts.
4. **Handle merge commits explicitly.** If reverting a merge commit, run `git revert -m 1 <merge-sha>` after confirming parent 1 is the mainline branch. → *Expect:* Git reverts the merged changes relative to the chosen mainline.
5. **Resolve conflicts if needed.** Edit conflicted files, run `git add <path>`, then `git revert --continue`. → *Expect:* revert completes and no unmerged files remain.
6. **Run validation.** Run the tests or health checks that exposed the regression, such as `pytest -q` or `npm test`. → *Expect:* validation exits 0 and the regressed behavior is gone.
7. **Push or open a PR.** Run `git push` or open a revert PR depending on branch policy. → *Expect:* CI runs on the revert commit.

## Decision points

- Commit is not published and local only → `git reset` may be acceptable, but use revert for shared history.
- Reverting a merge commit → confirm the mainline parent with `git show --pretty=raw <merge-sha>`.
- Revert removes follow-up fixes too → create a targeted fix instead of reverting the whole commit.

## Failure modes & recovery

- **F1 Wrong commit reverted:** detect unexpected diff in `git show --stat HEAD` → run `git revert HEAD` to undo the revert, then revert the correct commit.
- **F2 Merge revert blocks future re-merge:** detect need to reintroduce reverted branch later → revert the revert commit or cherry-pick corrected commits.
- **F3 Conflict resolution incomplete:** detect unmerged paths or failed tests → inspect both sides and continue after resolving.
- **F4 CI still red:** detect same failing check after revert → identify dependent commits or environmental changes and revert/fix them too.

## Verification

`git show --name-status HEAD` shows a `Revert "<original subject>"` commit, `git diff --name-only --diff-filter=U` prints nothing, and the regression test or full suite exits 0.

## Variations

- `GitHub UI`: use the PR's Revert button for merged PRs, then verify the generated branch and CI.
- `hotfix branch`: create the revert on a release branch and later merge/cherry-pick it back to main.
- `multiple commits`: use `git revert <oldest>^..<newest>` after confirming the range.

## Safety & privacy

Medium risk because a revert can remove necessary follow-up work or trigger deployment. Prefer revert over history rewrite for published commits, verify the exact SHA, and use normal review for production-impacting rollbacks.
