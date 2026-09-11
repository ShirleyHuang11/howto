---
name: write-a-failing-test-first
domain: engineering
subdomain: testing
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

Write a test that fails for the current code for the expected reason before implementing the fix or feature.

## Preconditions

- The desired behavior or bug reproduction is specific enough to assert.
- The relevant test framework runs locally.
- Existing tests are not already failing for unrelated reasons.

## Steps

1. **Run the nearby tests first.** Execute the current relevant suite, such as `pytest tests/test_parser.py -q`. → *Expect:* existing tests pass, giving a clean baseline.
2. **Write the smallest behavior test.** Add one test that describes the missing behavior or bug case. → *Expect:* the test runner discovers exactly the new test.
3. **Assert the desired final behavior.** Do not assert the current broken behavior. → *Expect:* the assertion reads like the future contract.
4. **Run only the new test.** [BRANCH: pytest | Jest] Use `pytest path/to/test.py::test_name -q` or `npm test -- path/to/test -t "name"`. → *Expect:* the new test fails.
5. **Confirm the failure reason.** Read the assertion diff or exception. → *Expect:* the failure points to the missing behavior, not syntax, import, or fixture setup.
6. **Implement the smallest code change.** Change production code only after the failure is confirmed. → *Expect:* the code addresses the asserted behavior directly.
7. **Rerun the new test.** Execute the same targeted command. → *Expect:* the test now exits 0.
8. **Run the surrounding suite.** Execute nearby tests or the project test command. → *Expect:* no regressions appear.

## Decision points

- New test fails because of setup, import, or syntax → fix the test until it fails on the intended assertion.
- Existing tests are already red → stop and establish a baseline before using red-green workflow.
- Behavior spans services → consider an integration or end-to-end test instead of forcing it into a unit test.

## Failure modes & recovery

- **F1 False red:** detect failure before reaching the assertion → correct fixture setup or imports, then rerun.
- **F2 Test passes immediately:** detect no red phase → verify the behavior already exists, tighten the assertion, or discard duplicate coverage.
- **F3 Overbroad implementation:** detect many unrelated code changes → reduce the fix to satisfy the failing test and add separate tests for new behavior.
- **F4 Regressions after green:** detect surrounding suite failure → adjust compatibility or add another focused test for the regression.

## Verification

The targeted command first fails on the intended assertion, then after the code change exits 0; the surrounding suite command, such as `pytest tests/test_parser.py -q` or `npm test -- parser`, also exits 0.

## Variations

- `TDD bug fix`: capture the reported bug as a regression test before changing code.
- `API behavior`: assert status code and response body before implementing handler logic.
- `UI component`: assert accessible text or role, not implementation state.

## Safety & privacy

Low risk because the workflow is local and reversible. Use synthetic inputs, do not copy private bug-report data into tests, and avoid weakening existing tests to make the new behavior pass.
