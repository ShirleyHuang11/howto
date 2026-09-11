---
name: debug-a-failing-ci-job
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You identify why a CI job failed, reproduce or isolate the cause locally when possible, and verify the corrected job passes.

## Preconditions

- You can view the CI run logs and workflow configuration.
- The branch, commit SHA, and failing job name are known.
- Required secrets remain in CI and are not copied into local logs.

## Steps

1. **Open the failing job log.** Find the first command that exits nonzero, not just the final cleanup failure. → *Expect:* one failing step and exit code are identified.
2. **Record the environment.** Note runner OS, language version, package manager version, cache status, and commit SHA. → *Expect:* local reproduction can match the CI environment closely.
3. **Classify the failure.** Decide whether it is test failure, lint/type failure, dependency install, missing secret, timeout, infrastructure outage, or deploy gate. → *Expect:* the next action fits the failure type.
4. **Reproduce the exact command locally.** Run the command from the failing step, such as `npm ci && npm test` or `pytest -q`. → *Expect:* it either fails locally with the same message or reveals a CI-only difference.
5. **Inspect recent changes and config.** Read the workflow file and changed package, lock, or test files relevant to the failing command. → *Expect:* a likely cause is tied to code or environment.
6. **Apply the smallest fix.** Update code, tests, lockfiles, CI setup, or environment assumptions as appropriate. → *Expect:* the failing command exits 0 locally or the CI-only configuration is corrected.
7. **Re-run CI.** Push through the normal workflow or manually rerun the job if no code change is needed. → *Expect:* the previously failing job reports green.

## Decision points

- Failure is from missing secret on forked PR → skip or mock the secret-required job for untrusted forks.
- Failure is dependency resolution → regenerate lockfile with the project package manager and runtime version.
- Failure is flaky test → reproduce with repeats, quarantine only with owner and issue, and keep a fix path.
- Failure is external service outage → retry once after confirming status, then add resilience if it recurs.

## Failure modes & recovery

- **F1 Chasing the last error:** detect cleanup or artifact upload failure after earlier red step → scroll to the first nonzero command.
- **F2 Cache poisoning:** detect failures resolved by clearing cache → tighten cache keys around lockfiles and runtime versions.
- **F3 Local environment mismatch:** detect local pass but CI fail → run in the same container or match OS and runtime versions.
- **F4 Secret printed in logs:** detect credential-like values in output → revoke exposed secret and mask output.
- **F5 Flaky test hidden by rerun:** detect rerun passes without code change → repeat and file an owner-tracked flake fix.

## Verification

The exact command from the failing CI step exits 0 locally when reproducible, and the CI provider shows the previously failing job green for the same branch or replacement commit.

## Variations

- `GitHub Actions`: inspect the failed step, annotations, runner image, and cache keys in `.github/workflows`.
- `GitLab CI`: inspect job trace, artifacts, `needs`, and runner tags.
- `CircleCI/Buildkite`: compare executor images, environment variables, and workspace artifact restoration.
- `deploy job`: verify the deployment target and approvals separately because a green build does not imply a safe deploy.

## Safety & privacy

Medium risk because CI often has deployment credentials and shared branch gates. Do not print secrets, be cautious rerunning deploy jobs, and avoid weakening required checks just to turn the dashboard green.
