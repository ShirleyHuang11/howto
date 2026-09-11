---
name: set-up-dependabot-updates
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min-45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You enable automated dependency update pull requests with a controlled schedule and review path. The end state is small, testable dependency updates instead of surprise bulk upgrades.

## Preconditions

- The repository uses supported package manifests such as `package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, `pom.xml`, or Dockerfiles.
- CI runs tests on dependency update pull requests.
- Maintainers know who should review dependency changes.

## Steps

1. **Inventory package ecosystems.** List each manifest path and ecosystem that needs updates. → *Expect:* a map such as "npm at `/`, pip at `/api`, docker at `/Dockerfile`".
2. **Create the Dependabot config.** Add `.github/dependabot.yml` with `version: 2`, one `updates` entry per ecosystem, directory, and schedule. → *Expect:* the YAML validates and names every intended manifest location.
3. **Set a modest cadence and PR limit.** Use weekly updates and `open-pull-requests-limit` to avoid flooding maintainers. → *Expect:* future updates arrive in small batches.
4. **Group safe updates where useful.** Group minor and patch development dependencies, but keep major or production-critical dependencies separate. → *Expect:* Dependabot will open grouped PRs according to the configured patterns.
5. **Assign reviewers and labels.** Add `reviewers`, `assignees`, or `labels` supported by Dependabot. → *Expect:* update PRs route to the responsible maintainers.
6. **Enable security updates if available.** Turn on Dependabot security updates in repository security settings. → *Expect:* vulnerable supported dependencies create security PRs even outside the normal schedule.
7. **Verify by checking dependency graph status.** Open the repository dependency graph or Dependabot page. → *Expect:* the config is recognized and no syntax errors are reported.

## Decision points

- CI is slow or flaky → fix required checks before enabling broad automated updates.
- Large monorepo → configure each manifest directory explicitly.
- Private registries are used → add registry credentials as Dependabot secrets, not normal Actions secrets.
- Critical dependency → avoid grouping and require domain-owner review.

## Failure modes & recovery

- **F1 Config ignored:** detect no Dependabot activity or a config error banner → validate `.github/dependabot.yml` indentation and ecosystem names.
- **F2 Private package auth fails:** detect PR error about registry access → add `registries` entries and Dependabot-scoped secrets.
- **F3 PR flood:** detect too many open update PRs → lower `open-pull-requests-limit`, group patch updates, or reduce cadence.
- **F4 Updates repeatedly fail tests:** detect recurring red PRs for one package → pin temporarily and open a tracked upgrade issue.

## Verification

The repository Dependabot page reports the configuration as valid, and the next scheduled run creates update PRs that execute the normal CI checks. For GitHub, the dependency graph shows Dependabot enabled for the configured ecosystems.

## Variations

- `GitHub Dependabot`: configuration lives at `.github/dependabot.yml`.
- `Renovate`: use `renovate.json` for more advanced grouping and automerge policies.
- `private registries`: credentials must be available to the dependency bot through its own secret mechanism.
- `Docker`: Dependabot can update base image tags referenced in Dockerfiles.

## Safety & privacy

Low risk when updates are PR-only and protected by CI. Do not automerge major upgrades without tests and review, keep registry credentials scoped read-only, and avoid exposing private package names in public repositories when that matters.
