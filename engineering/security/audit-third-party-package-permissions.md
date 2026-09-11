---
name: audit-third-party-package-permissions
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [engineering/scan-dependencies-for-vulnerabilities]
status: draft
last_verified: 2026-09-11
---

## Goal

You review third-party packages for excessive permissions, risky install scripts, and supply-chain signals before adding or keeping them in the project.

## Preconditions

- The package name, version, registry, and intended use are known.
- Dependency manifests and lockfiles are available.
- The project has an approved package manager and registry policy.

## Steps

1. **Inspect package metadata.** Run `npm view <pkg> version repository scripts dependencies`, `pip index versions <pkg>`, or inspect the registry page. → *Expect:* maintainer, repository, license, release cadence, and dependency count are visible.
2. **Check install-time behavior.** For npm, inspect `preinstall`, `install`, and `postinstall` scripts with `npm view <pkg> scripts`; for other ecosystems, inspect build hooks and native extensions. → *Expect:* no unexpected network, shell, or binary execution is hidden.
3. **Review requested runtime permissions.** For browser extensions, mobile SDKs, GitHub Apps, or cloud integrations, list requested scopes and compare them to required functionality. → *Expect:* permissions are minimal and justified.
4. **Audit transitive dependencies.** Run `npm ls <pkg>`, `pipdeptree -p <pkg>`, or `cargo tree -i <crate>`. → *Expect:* the package's dependency tree is understood.
5. **Run vulnerability and malware-oriented scans.** Use `osv-scanner`, `npm audit`, `pip-audit`, or an internal supply-chain scanner. → *Expect:* no unresolved high-risk findings block adoption.
6. **Test in a sandbox.** Install with restricted credentials and no production secrets, such as `npm ci --ignore-scripts` first, then explicitly allow scripts only if reviewed. → *Expect:* installation behavior matches expectations.
7. **Document the decision.** Record version, purpose, permissions, risks, and owner in the PR or dependency review record. → *Expect:* reviewers can approve or reject based on evidence.

## Decision points

- Package is new, low-download, or recently transferred → require stronger review or avoid it.
- Install scripts are unnecessary → install with scripts disabled or choose another package.
- Permissions exceed need → request a narrower integration or reject the package.
- Maintainer activity stopped and package is security-sensitive → prefer a maintained alternative.

## Failure modes & recovery

- **F1 Typosquatting:** detect similar package names or unexpected repository → remove package and install the verified canonical package.
- **F2 Malicious install script:** detect unexpected network/file activity → revoke any exposed tokens and rebuild from a clean environment.
- **F3 License conflict:** detect incompatible license → replace the package or get legal approval.
- **F4 Hidden permission expansion:** detect new scopes after upgrade → pin, roll back, and review release notes before retrying.

## Verification

The dependency review record lists package purpose, version, permissions/scopes, install scripts, vulnerability scan result, and an approve/reject decision; scanner commands exit 0 or have documented exceptions.

## Variations

- `npm`: inspect lifecycle scripts and consider `npm ci --ignore-scripts` in CI where feasible.
- `GitHub Apps/OAuth`: review exact scopes and repository access before installation.
- `Container images`: audit image provenance, digest pinning, and Linux capabilities.

## Safety & privacy

Medium risk because third-party code may execute during install or runtime. Use least-privilege tokens, sandbox package evaluation, avoid giving packages production credentials, and pin versions or digests where appropriate.
