---
name: write-a-changelog-entry
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

You add a clear changelog entry that tells users or operators what changed, why it matters, and whether any action is required.

## Preconditions

- The change being documented is merged, ready for PR, or associated with a release.
- The repository has a changelog convention, release note file, or changeset system.
- You know whether the audience is end users, developers, or operators.

## Steps

1. **Find the changelog convention.** Inspect `CHANGELOG.md`, `.changeset/`, `docs/releases/`, or contributing docs. → *Expect:* the expected location and format are known.
2. **Classify the change.** Choose a category such as Added, Changed, Deprecated, Removed, Fixed, Security, or Breaking. → *Expect:* the entry lands under the correct heading.
3. **Write user-facing impact.** Describe the observable behavior, not internal implementation details. → *Expect:* a reader can tell whether the release affects them.
4. **Call out action items.** Include migration steps, config changes, feature flags, or rollback notes when required. → *Expect:* operators know exactly what to do before or after deploy.
5. **Link the source of truth.** Reference the PR, issue, or ticket using the project convention. → *Expect:* maintainers can trace the change.
6. **Run changelog validation.** [Changesets | Markdown] run `npx changeset status --since=origin/main` or `markdownlint CHANGELOG.md`. → *Expect:* formatting and release tooling pass.
7. **Review the rendered diff.** Run `git diff -- CHANGELOG.md .changeset`. → *Expect:* only the intended changelog or changeset files changed.

## Decision points

- Project uses generated changelogs → add a changeset or release fragment, not manual `CHANGELOG.md` edits.
- Breaking change → include migration instructions and versioning impact.
- Internal-only refactor → omit from user changelog unless it affects operators or downstream developers.

## Failure modes & recovery

- **F1 Entry too implementation-focused:** detect language about private classes or refactors only → rewrite around user-visible behavior.
- **F2 Wrong release section:** detect entry under an already released version → move it to `Unreleased` or the current changeset.
- **F3 Missing migration note:** detect config/API/schema change without instructions → add exact commands or compatibility guidance.
- **F4 Release tooling fails:** detect changeset or lint errors → fix frontmatter, package name, semver bump, or Markdown formatting.

## Verification

`git diff --check -- CHANGELOG.md .changeset` exits 0, and the repository's changelog command such as `npx changeset status --since=origin/main` or `markdownlint CHANGELOG.md` exits 0.

## Variations

- `Keep a Changelog`: group entries under Added, Changed, Deprecated, Removed, Fixed, and Security.
- `Changesets`: create one file in `.changeset/` with package bump metadata and prose.
- `Monorepo`: mention affected package names and use the release tool's package selector.

## Safety & privacy

Low risk, but changelogs are public-facing in many projects. Do not disclose embargoed vulnerabilities, customer names, internal incident links, or private roadmap details unless the release process explicitly approves them.
