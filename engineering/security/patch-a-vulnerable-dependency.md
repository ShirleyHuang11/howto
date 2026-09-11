---
name: patch-a-vulnerable-dependency
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [engineering/scan-dependencies-for-vulnerabilities]
status: draft
last_verified: 2026-09-11
---

## Goal

You upgrade or mitigate a vulnerable dependency, keep lockfiles consistent, and verify the advisory no longer applies.

## Preconditions

- Advisory ID, affected package, vulnerable version range, and fixed version are known.
- The dependency scan and test suite can run locally or in CI.
- A rollback path exists if the upgrade breaks runtime behavior.

## Steps

1. **Confirm the vulnerable path.** Run the scanner and dependency tree command, such as `npm ls <package>`, `pipdeptree -r -p <package>`, or `mvn dependency:tree`. → *Expect:* the vulnerable direct or transitive dependency path is identified.
2. **Choose the smallest safe upgrade.** Prefer the first fixed patch/minor version that satisfies compatibility; read release notes for breaking changes. → *Expect:* a target version and compatibility notes are documented.
3. **Update the manifest and lockfile together.** [BRANCH: npm, `npm install <package>@<fixed-version>` | Python, update constraints then regenerate lockfile | Ruby, `bundle update <gem>` | Maven/Gradle, update version property] → *Expect:* only expected dependency files change.
4. **Run targeted tests.** Execute tests for code paths that use the package, plus the package manager's audit command. → *Expect:* functional tests pass and the advisory is gone.
5. **Run the full project verification.** Use the normal test/build command, such as `npm test`, `pytest -q`, `mvn test`, or CI. → *Expect:* the full suite exits 0.
6. **If no fixed version exists, apply mitigation.** Disable the vulnerable feature, add input constraints, vendor a patch only with review, or isolate the service. → *Expect:* exploitability is reduced and a follow-up upgrade task exists.
7. **Document the security impact.** Note advisory ID, old version, new version or mitigation, and scanner proof. → *Expect:* reviewers can verify the patch closes the finding.

## Decision points

- Upgrade is breaking → add compatibility fixes and broaden tests before merging.
- Vulnerability is transitive → update the parent package or use an overrides/resolutions mechanism with caution.
- Package is unmaintained → replace it with a maintained alternative instead of pinning forever.
- Patch touches production-critical library → deploy behind normal canary/rollback process.

## Failure modes & recovery

- **F1 Lockfile inconsistent:** detect install or CI failure → regenerate the lockfile with the project package manager version.
- **F2 Override hides duplicate vulnerable copy:** detect scanner still finds another path → inspect full dependency tree and update all parents.
- **F3 Runtime regression:** detect failing targeted tests or smoke tests → read changelog, adapt code, or choose the next compatible fixed version.
- **F4 No fixed version:** detect advisory has no patched release → implement documented mitigation and add monitoring for new releases.

## Verification

The vulnerability scanner no longer reports the advisory for the project, the dependency tree shows a fixed version, and the full test/build command exits 0.

## Variations

- `npm`: use `overrides` only when updating the parent package is not possible.
- `pip-tools/Poetry`: regenerate lockfiles with the same tool used by the project.
- `Containers`: patch both application packages and base image packages, then rebuild and rescan the image.

## Safety & privacy

Medium risk because dependency upgrades can break builds or runtime behavior. Keep changes narrow, do not publish exploit details beyond the advisory, and avoid permanent ignores for fixable vulnerabilities.
