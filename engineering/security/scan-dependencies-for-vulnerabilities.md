---
name: scan-dependencies-for-vulnerabilities
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 25min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You scan project dependencies for known vulnerabilities, produce a reproducible report, and decide which findings require patches.

## Preconditions

- Dependency manifests and lockfiles are present.
- The project can install dependencies in a clean environment.
- Network access to package registries or a configured internal mirror.

## Steps

1. **Install from the lockfile.** [BRANCH: npm, run `npm ci` | Python, run `pip install -r requirements.txt` or the project installer | Ruby, run `bundle install` | Java, run the build tool dependency resolve step] → *Expect:* dependencies install without modifying lockfiles.
2. **Run the ecosystem scanner.** [BRANCH: npm, `npm audit --audit-level=moderate` | Python, `pip-audit -r requirements.txt` | Ruby, `bundle audit check --update` | Java, `mvn org.owasp:dependency-check-maven:check`] → *Expect:* a vulnerability report or clean exit is produced.
3. **Run a multi-ecosystem scanner if available.** Use `osv-scanner --lockfile package-lock.json --lockfile requirements.txt` or `trivy fs .`. → *Expect:* findings include advisory IDs, affected versions, and fixed versions.
4. **Triage reachability and severity.** Mark each finding as direct/transitive, runtime/dev-only, reachable/unreachable, and fixed/no-fix. → *Expect:* a prioritized list with owners and patch path.
5. **Fail CI on agreed thresholds.** Add or verify a CI job that exits nonzero for high/critical runtime vulnerabilities. → *Expect:* future vulnerable dependency additions are blocked.
6. **Record accepted exceptions.** Use the scanner's ignore format with advisory ID, reason, owner, and expiry date. → *Expect:* ignored findings are explicit and time-bound.
7. **Create patch tasks for actionable findings.** Link each high-priority finding to `engineering/patch-a-vulnerable-dependency`. → *Expect:* every actionable advisory has an upgrade or mitigation task.

## Decision points

- Scanner exits nonzero with fixable high severity → patch before merge.
- Vulnerability is dev-only and not shipped → document lower priority but keep an expiry.
- No fixed version exists → apply vendor mitigation, disable affected feature, or monitor advisory updates.
- Lockfile missing → create one before relying on scan results.

## Failure modes & recovery

- **F1 Registry unavailable:** detect network or 5xx errors → retry against the internal mirror or rerun when the advisory source is available.
- **F2 False positive package path:** detect scanner matching unused packages → document reachability evidence and add a scoped ignore.
- **F3 Lockfile drift:** detect install modifies lockfile → restore dependency resolution and commit lockfile changes only in the patch PR.
- **F4 CI noise:** detect too many low-risk failures → tune thresholds while keeping high/critical runtime findings blocking.

## Verification

The chosen scanner command exits 0 or produces only documented time-bound exceptions, and CI contains a dependency vulnerability scan job that fails on the agreed severity threshold.

## Variations

- `npm`: `npm audit` is built in; `osv-scanner` provides cross-ecosystem advisory matching.
- `Python`: `pip-audit` checks installed or requirements-based dependencies.
- `Containers`: use `trivy image <image>` or `grype <image>` for OS packages plus app dependencies.

## Safety & privacy

Medium risk because scan output may reveal private package names and versions. Keep reports in restricted issue trackers, avoid uploading proprietary dependency graphs to unapproved services, and use time-limited exceptions.
