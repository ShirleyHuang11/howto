---
name: add-a-regression-test-for-a-bug
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Capture a previously observed bug in an automated test so the same failure cannot return unnoticed.

## Preconditions

- The bug has a clear reproduction, observed input, or failure condition.
- Sensitive production data has been removed or replaced with synthetic equivalents.
- The relevant test layer is known: unit, integration, API, or E2E.

## Steps

1. **Summarize the bug as behavior.** Write the triggering condition and the expected correct result. → *Expect:* the test name can describe the regression in plain language.
2. **Choose the cheapest test layer.** Prefer unit or integration coverage unless only a full workflow catches the bug. → *Expect:* the test is fast enough to run routinely.
3. **Reproduce with sanitized data.** Convert the bug input into a minimal fixture or test case. → *Expect:* no real customer data or secrets appear in the test.
4. **Write the regression test.** Assert the correct behavior, not the broken behavior. → *Expect:* the test fails on the buggy version for the same reason users saw.
5. **Run the test before fixing if possible.** Execute the targeted command. → *Expect:* it fails with an assertion or error matching the bug.
6. **Apply or keep the fix.** If the fix already exists, verify the test passes against it; otherwise implement the smallest fix. → *Expect:* the regression test turns green.
7. **Run neighboring tests.** Execute the relevant suite around the changed code. → *Expect:* no related regressions appear.
8. **Link the bug context.** Mention the issue, incident, or support ticket in the PR text, not necessarily inside the test code. → *Expect:* reviewers understand why the edge case matters.

## Decision points

- Bug depends on external provider behavior → mock the provider response and add a contract test if critical.
- Bug is security-related → keep details minimal in public repositories and coordinate disclosure.
- Bug is caused by missing validation → test both the rejected bad input and accepted good input.

## Failure modes & recovery

- **F1 Test does not fail on buggy code:** detect immediate pass on the old version → tighten the input or assertion until it reproduces the bug.
- **F2 Production data leaked:** detect real names, emails, tokens, or IDs → replace with synthetic data before committing.
- **F3 Wrong test layer:** detect slow or brittle setup for a simple condition → move coverage to a lower-level test.
- **F4 Fix breaks adjacent case:** detect neighboring test failure → add another case or adjust the fix for compatibility.

## Verification

Run the targeted regression test and surrounding suite, for example `pytest tests/test_parser.py::test_handles_empty_metadata_regression -q && pytest tests/test_parser.py -q`; both commands exit 0, and the regression test fails when the fix is reverted.

## Variations

- `Bug from incident`: reference the incident ID in PR text and include only sanitized reproduction data.
- `UI bug`: assert accessible text, visible state, or screenshot snapshot only when stable.
- `API bug`: assert status code, response body, and persisted state for the edge case.

## Safety & privacy

Low risk if sanitized. Never commit customer payloads, access tokens, private URLs, or exploit details beyond what maintainers need; keep the regression focused so it does not ossify unrelated behavior.
