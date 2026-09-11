---
name: write-a-good-commit-message
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

You write a commit message that accurately summarizes the change, explains the reason when needed, and remains useful in logs, reviews, and release notes.

## Preconditions

- The intended changes are staged or visible in the working tree.
- You can inspect the diff and any linked issue, ticket, or incident.
- The project's commit style is known, such as Conventional Commits, imperative summaries, or ticket prefixes.

## Steps

1. **Inspect the staged change.** Run `git diff --cached --stat` and `git diff --cached`. → *Expect:* you understand the files, behavior changes, and test impact.
2. **Confirm the commit has one coherent purpose.** If unrelated changes are staged, run `git restore --staged <path>` and split them. → *Expect:* the staged diff can be described by one concise subject.
3. **Write an imperative subject line.** Use a short command-style summary such as `fix auth token refresh` or `Add invoice export validation`. → *Expect:* the first line is specific, under roughly 50-72 characters when practical, and does not end with a period.
4. **Add a body when context matters.** Run `git commit` or `git commit -m "subject" -m "body"` and explain why, tradeoffs, migrations, or operational notes. → *Expect:* reviewers can tell why the change exists without opening every linked artifact.
5. **Reference external work items when useful.** Include `Refs #123`, `Fixes #123`, or the team's ticket key in the body or footer. → *Expect:* repository hosting can link the commit to the relevant issue.
6. **Check the final message.** Run `git log -1 --format=%B`. → *Expect:* the subject and body render cleanly with no accidental template text or private notes.

## Decision points

- Diff is mechanical or generated → say what generator or command produced it.
- Commit fixes a production incident → include impact and validation evidence in the body.
- Project uses Conventional Commits → format as `type(scope): summary`, such as `fix(api): reject expired tokens`.

## Failure modes & recovery

- **F1 Message too vague:** detect subjects like `update`, `fix stuff`, or `changes` → rewrite with `git commit --amend` before pushing.
- **F2 Multiple concerns in one commit:** detect unrelated files or multiple behaviors → reset the commit locally with `git reset --soft HEAD~1`, split staging, and recommit.
- **F3 Secret or sensitive note in message:** detect credentials, customer names, or internal incident details → amend before push; if pushed publicly, follow the project's secret-removal process.
- **F4 Commit hook rejects format:** detect commitlint or hook errors → update the subject to match the project's configured pattern and retry.

## Verification

`git log -1 --format=%s` prints a specific imperative subject, and `git log -1 --format=%B` contains any required context, issue reference, or Conventional Commit prefix without hook failures.

## Variations

- `Conventional Commits`: use `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `build:`, or `chore:` prefixes according to project policy.
- `squash merge`: write the PR title and body with the same care, because the squash commit message may be generated from them.
- `regulated systems`: include ticket IDs and validation notes required by audit policy.

## Safety & privacy

Low risk, but commit messages are durable and often replicated. Do not include secrets, private customer data, unreleased security details, or emotional commentary; put sensitive operational details in the approved incident system instead.
