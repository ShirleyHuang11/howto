---
name: speed-up-a-slow-test-suite
domain: engineering
subdomain: testing
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

You reduce test suite runtime while preserving coverage and determinism, and prove the improvement with before-and-after timing.

## Preconditions

- The full suite currently runs locally or in CI.
- You can profile test durations without changing production code paths.
- You know the normal CI command, such as `pytest`, `npm test`, `go test ./...`, or `bundle exec rspec`.

## Steps

1. **Capture a baseline.** Run `time pytest -q` or the project’s normal test command and save total duration and failing tests, if any. → *Expect:* a baseline wall-clock time and exit status.
2. **List slow tests.** [pytest | RSpec | Jest] use `pytest --durations=25`, `bundle exec rspec --profile 25`, or `jest --runInBand --logHeapUsage`. → *Expect:* the slowest files or examples are ranked by duration.
3. **Separate setup cost from assertion cost.** Inspect top offenders for database migrations, network calls, sleeps, browser startup, huge fixtures, or repeated app boot. → *Expect:* each slow test has a suspected cause.
4. **Remove unnecessary waiting and I/O.** Replace fixed sleeps with polling timeouts, mock external APIs at the boundary, reuse expensive read-only fixtures, or use in-memory stores where valid. → *Expect:* the target tests still assert the same behavior with less wall time.
5. **Enable safe parallelism where supported.** Try `pytest -n auto`, `go test -parallel`, or CI matrix splitting only after data isolation is in place. → *Expect:* parallel runs exit 0 without worker collisions.
6. **Run the impacted tests repeatedly.** Execute the slow files three times, such as `pytest -q tests/test_checkout.py --count=3` if the repeat plugin exists or with a shell loop locally. → *Expect:* no flakes appear.
7. **Re-run the full suite and compare.** Run the same command used for the baseline. → *Expect:* the suite exits 0 and total runtime is lower by a measured amount.

## Decision points

- Slow time is concentrated in a few integration tests → optimize setup or split them from unit tests.
- Runtime is spread evenly across many isolated tests → parallel execution likely helps more than micro-optimizing.
- Tests hit real network services → replace with contract fixtures or local fakes unless the suite is explicitly end-to-end.
- Optimization removes coverage → keep the slower test or move it to a smaller scheduled suite with clear ownership.

## Failure modes & recovery

- **F1 New flakiness:** detect intermittent failures after timing changes → restore deterministic waits or isolate shared resources.
- **F2 Parallel database collision:** detect duplicate keys or changed row counts under workers → use per-worker databases or transaction isolation.
- **F3 Mock hides real behavior:** detect production bug no longer caught → add one contract or integration test at the boundary.
- **F4 CI slower than local:** detect local improvement but CI regression → check CPU limits, cache paths, and runner parallelism overhead.
- **F5 Memory pressure:** detect `OOMKilled` or heap errors after parallelism → lower worker count and profile memory.

## Verification

The original full-suite command exits 0 after the change, and a repeated timing command such as `/usr/bin/time -p pytest -q` shows a lower wall-clock time than the recorded baseline on the same machine or CI runner class.

## Variations

- `pytest`: use `--durations`, `pytest-xdist`, fixture scopes, and per-worker databases.
- `Jest`: use `--runInBand` to profile serially, tune `--maxWorkers`, and avoid global setup that rebuilds state per file.
- `Go`: use `go test -json ./...` with tooling such as `gotestsum`; cache pure tests and isolate tests using `t.Parallel()`.
- `CI`: split by historical timing when the CI provider supports test balancing.

## Safety & privacy

Medium risk because speeding tests can accidentally weaken coverage or create shared-state flakes. Keep a baseline, preserve at least one realistic integration path, and do not replace security or payment boundary tests with mocks unless a contract test remains.
