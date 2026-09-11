---
name: reproduce-a-bug-reliably
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You turn an intermittent or reported bug into a repeatable local, test, or staging reproduction that can verify a fix.

## Preconditions

- You have a bug report, failing CI job, log sample, or user-visible symptom.
- The relevant code version and environment are known or can be inferred.
- Any production data needed for understanding is replaced with sanitized fixtures.

## Steps

1. **Write the observed symptom precisely.** Include input, expected behavior, actual behavior, timestamps, browser or runtime versions, and request IDs. → *Expect:* the report is specific enough to test.
2. **Match the code version.** Confirm the commit, release tag, container image, or package version that showed the bug. → *Expect:* your checkout or environment matches the failing version.
3. **Minimize the trigger.** Remove unrelated user actions, data, and services until the smallest sequence still fails. → *Expect:* a compact reproduction sequence remains.
4. **Create controlled input data.** Use fixtures, factories, mock API responses, or a sanitized database row. → *Expect:* the bug no longer depends on a live customer account.
5. **Automate the reproduction.** Add a failing test, script, or curl command such as `curl -i -X POST localhost:3000/api/orders -d @fixtures/bad-order.json`. → *Expect:* one command reproduces the failure.
6. **Run it repeatedly.** Execute the reproduction at least three times, clearing state between runs. → *Expect:* the failure appears consistently or with a measured probability.
7. **Capture the failure artifact.** Save stack trace, logs, screenshots, or response bodies needed for the fix. → *Expect:* the next engineer can see the same failure without asking for context.

## Decision points

- Bug depends on time → freeze the clock or test at the boundary time.
- Bug depends on concurrency → create a stress script or controlled barrier to align competing operations.
- Bug appears only in production → reproduce in staging with sanitized data and the same feature flags.
- Reproduction is still flaky → record frequency and keep reducing nondeterminism before fixing.

## Failure modes & recovery

- **F1 Cannot match production config:** detect behavior differs locally → export non-secret feature flags and runtime settings from the failing environment.
- **F2 Missing data shape:** detect fixture passes but production fails → compare schemas and sanitized payload fields.
- **F3 Race disappears under debugger:** detect bug vanishes when slowed down → use logging, barriers, or stress loops instead of breakpoints.
- **F4 Test pollutes state:** detect later runs fail differently → reset database, queues, caches, and temp files between attempts.

## Verification

A single documented command or test, such as `pytest -q tests/regression/test_issue_123.py`, fails on the known-bad code and exits 0 after the fix, using sanitized deterministic inputs.

## Variations

- `web app`: use Playwright or Cypress to encode the user journey and assert the failing UI state.
- `API`: use a checked-in fixture payload and assert HTTP status plus response body.
- `background job`: enqueue a synthetic job with fixed inputs and run one worker in foreground.
- `concurrency`: use stress loops plus race detectors such as `go test -race` where available.

## Safety & privacy

Medium risk because reproductions often start from production reports. Do not copy raw customer data into tests, keep access tokens out of fixtures, and run destructive reproductions only against disposable local or staging resources.
