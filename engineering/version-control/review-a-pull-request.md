---
name: review-a-pull-request
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

You review a pull request for correctness, maintainability, tests, security, and operational risk, then leave actionable feedback or approval.

## Preconditions

- You have read access to the repository and PR.
- The PR has a clear base and head branch.
- Local tooling or CI logs are available for verification.

## Steps

1. **Read the PR summary and linked issue.** Open the PR page or run `gh pr view <number> --json title,body,baseRefName,headRefName`. → *Expect:* the intended behavior, scope, and target branch are clear.
2. **Inspect changed files.** Run `gh pr diff <number> --patch` or fetch the branch and run `git diff origin/main...HEAD`. → *Expect:* you can identify risky files, public APIs, migrations, and tests.
3. **Check CI and required status.** Run `gh pr checks <number>` or the provider equivalent. → *Expect:* required checks are green or failures are explainable and not ignored.
4. **Run focused local validation when risk warrants it.** Check out the PR with `gh pr checkout <number>` and run affected tests, such as `pytest path/to/test.py -q`. → *Expect:* local reproduction exits 0 or exposes a specific failure.
5. **Review behavior before style.** Look for logic bugs, missing edge cases, broken contracts, race conditions, data loss, and inadequate tests. → *Expect:* findings are tied to concrete lines and outcomes.
6. **Leave review feedback.** Use `gh pr review <number> --comment --body-file review.md`, `--request-changes`, or `--approve`. → *Expect:* the PR shows your review state and comments.

## Decision points

- Serious bug or missing validation → request changes with a minimal reproduction or failing scenario.
- Mostly correct with small nits → comment or approve with non-blocking suggestions.
- CI red and unexplained → do not approve until the failure is fixed or proven unrelated.

## Failure modes & recovery

- **F1 Diff too large to review safely:** detect many unrelated files or mixed concerns → ask the author to split the PR or provide a review map.
- **F2 Generated files obscure logic:** detect minified or generated diffs → verify the generator command and review source inputs first.
- **F3 Local setup fails:** detect dependency or environment errors → rely on CI logs for checks you cannot run and state the local blocker.
- **F4 Stale branch:** detect conflicts or old base SHA → ask for rebase/merge from base and re-run CI before final approval.

## Verification

`gh pr view <number> --json reviewDecision,statusCheckRollup` shows your submitted review state, and required checks in `gh pr checks <number>` are passing or explicitly documented in your review.

## Variations

- `GitHub`: use review states `APPROVED`, `CHANGES_REQUESTED`, or `COMMENTED`.
- `GitLab`: use merge request discussions, approval rules, and `glab mr checkout`.
- `Security-sensitive PR`: add checks for secret exposure, authorization boundaries, audit logging, and dependency advisories.

## Safety & privacy

Medium risk because an approval can unblock production changes. Do not approve code you did not meaningfully inspect, do not paste private logs into public comments, and keep security findings in the project's approved private disclosure channel when needed.
