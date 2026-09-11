---
name: set-up-branch-protection-rules
domain: engineering
subdomain: cicd
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min-45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You configure branch protection so important branches cannot receive unreviewed or untested changes. The protected branch requires current CI checks and blocks direct pushes according to the team's policy.

## Preconditions

- Admin access to the repository or project settings.
- CI already reports named status checks on pull or merge requests.
- The default branch name and release branches are known.

## Steps

1. **Identify branches to protect.** Choose exact names or patterns such as `main`, `release/*`, or `production`. → *Expect:* a short list of protected targets and the reason each matters.
2. **Open branch protection settings.** [BRANCH: GitHub, go to Settings > Branches > Branch protection rules | GitLab, go to Settings > Repository > Protected branches and Merge request approvals] → *Expect:* the page shows branch rules for the repository.
3. **Require pull or merge requests.** Enable PR/MR before merge, require at least one approval, and dismiss stale approvals if the platform supports it. → *Expect:* direct merge without review is blocked for non-admin users.
4. **Require current CI checks.** Select the required check names that must pass before merge, and require branches to be up to date if that matches team practice. → *Expect:* PRs with failing or missing checks cannot merge.
5. **Restrict bypasses and force pushes.** Disable force pushes and deletions; allow admin bypass only if the organization explicitly needs it. ⚠️ *Irreversible:* branch deletion or force-push can lose shared work, so confirm the bypass policy with repository owners before enabling any exception. → *Expect:* settings show force pushes and branch deletion are blocked.
6. **Save the rule and test it.** Open a small PR or use an existing one with a failing check. → *Expect:* the merge button is disabled until review and required checks pass.
7. **Verify direct push behavior with a safe account or dry run.** Use provider UI or a non-admin token if available; do not push a real change to `main` just to test. → *Expect:* the provider reports direct pushes are disallowed for protected branches.

## Decision points

- Small solo repo → one approval may be enough, but still require CI before merge.
- Regulated or production-critical repo → require code owners, signed commits, linear history, and no admin bypass.
- CI check names change often → require stable wrapper checks rather than matrix leaf jobs.
- Release branches need hotfixes → define a separate protection rule with explicit release-owner approval.

## Failure modes & recovery

- **F1 Required check never appears:** detect PR blocked by a missing status → update the required check name or restore the CI workflow that emits it.
- **F2 Admins accidentally bypass rules:** detect merges without checks → disable admin bypass or require audit review.
- **F3 Merge queue conflicts:** detect repeated stale-branch failures → enable merge queue or auto-update branches.
- **F4 Emergency hotfix blocked:** detect urgent fix unable to merge → use documented break-glass permissions and record the follow-up review.

## Verification

A pull or merge request targeting the protected branch cannot merge until the selected CI checks are green and the required approval count is met; the repository settings show force pushes and branch deletion disabled for that branch.

## Variations

- `GitHub`: branch protection and rulesets can both enforce status checks, code owners, deployments, and signed commits.
- `GitLab`: protected branches combine allowed push/merge roles with approval rules and pipeline requirements.
- `Bitbucket`: branch permissions can block deletion, rewriting history, and direct pushes.
- `monorepo`: require stable aggregate checks per area rather than every matrix job.

## Safety & privacy

Medium risk because overstrict rules can block delivery and loose rules can permit unsafe changes. Restrict bypass permissions, keep rule ownership documented, and avoid weakening production branch settings without explicit maintainer approval.
