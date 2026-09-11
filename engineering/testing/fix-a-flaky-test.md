---
name: fix-a-flaky-test
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [engineering/run-the-test-suite]
status: draft
last_verified: 2026-09-11
---

## Goal

Make an intermittently failing test deterministic by identifying the unstable dependency and replacing it with explicit synchronization, isolation, or controlled data.

## Preconditions

- You have a flaky test name, CI failure, or reproduction command.
- The suite can run locally or in CI: `engineering/run-the-test-suite`.
- You can inspect recent failures and logs.

## Steps

1. **Collect failure evidence.** Record the failing test name, error text, seed, timing, environment, and recent changes. → *Expect:* you know how the flaky failure presents.
2. **Reproduce with repetition.** Run a loop such as `for i in $(seq 1 50); do pytest tests/test_x.py::test_y -q || break; done`. → *Expect:* either the failure reproduces or local evidence suggests a CI-only condition.
3. **Classify the flake source.** Look for time, random order, shared state, network, filesystem, concurrency, or resource limits. → *Expect:* one instability category is most likely.
4. **Replace guesswork with control.** Use fake clocks, fixed random seeds, unique temp paths, transactions, explicit waits, or mocked external calls. → *Expect:* the test no longer relies on timing or inherited state.
5. **Remove arbitrary sleeps.** Replace `sleep` with waiting for a condition with a bounded timeout. → *Expect:* the test is faster or equally fast and more reliable.
6. **Run the repeated command again.** Execute the same loop or framework retry-free repetition. → *Expect:* all repetitions pass without retries.
7. **Run neighboring tests in varied order if supported.** Use random-order plugins or run the package suite. → *Expect:* the test passes with surrounding tests too.
8. **Document the cause in the change.** Mention the root cause and deterministic fix in the PR. → *Expect:* reviewers can tell the flake was actually fixed, not hidden.

## Decision points

- Failure cannot be reproduced locally → add temporary diagnostic logging in CI or inspect artifacts before changing behavior.
- Test only passes with retries → keep investigating; retries hide flakes and should not be the fix.
- Root cause is product race → fix production synchronization and keep the test as coverage.

## Failure modes & recovery

- **F1 Flake masked by retry:** detect test marked with retry but no deterministic fix → remove or reduce retry after fixing root cause.
- **F2 Order dependency remains:** detect pass alone but fail in suite → isolate global state and reset singletons or database rows.
- **F3 Timeout increased only:** detect a larger timeout with same race → add condition-based waiting or explicit synchronization.
- **F4 CI resource issue:** detect OOMKilled, browser crash, or worker timeout → reduce parallelism or right-size CI resources.

## Verification

Run the formerly flaky test in a repetition loop without framework retries, such as `for i in $(seq 1 50); do pytest tests/test_x.py::test_y -q || exit 1; done`; the loop exits 0, and the relevant CI job passes without retry-only success.

## Variations

- `pytest`: use `pytest-randomly`, fixed seeds, and `tmp_path` fixtures.
- `Jest`: use fake timers, `--runInBand` for diagnosis, and cleanup in `afterEach`.
- `Playwright`: use locator assertions and traces instead of fixed sleeps.

## Safety & privacy

Medium risk because changing tests can hide real defects. Do not delete assertions or add broad skips without owner approval, keep diagnostic logs free of secrets, and prefer fixing product races over weakening tests.
