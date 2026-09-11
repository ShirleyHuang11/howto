---
name: debug-a-race-condition
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You reproduce a timing-dependent failure, identify the shared state or ordering assumption, and verify the fix under stress or race detection.

## Preconditions

- The failure is suspected to involve concurrency, async ordering, retries, or shared mutable state.
- You can run stress tests against local or staging resources.
- Logs can include timestamps, correlation IDs, and worker or thread identifiers.

## Steps

1. **Describe the invalid interleaving.** Write what two or more operations are doing and which final state is wrong. → *Expect:* the suspected shared resource is named.
2. **Make the race easier to trigger.** Add a stress test, loop, or controlled delay at safe test hooks. → *Expect:* the failure occurs more often than before.
3. **Run a race detector when available.** [Go | Rust | Java] use `go test -race ./...`, ThreadSanitizer, or JVM concurrency testing tools. → *Expect:* either a data race report or a clean detector run.
4. **Log ordering without flooding.** Add temporary structured logs with request IDs, worker IDs, and state version numbers. → *Expect:* logs reveal which operation wins or loses.
5. **Protect the shared state.** Use transactions, locks, atomic operations, idempotency keys, compare-and-swap, or queue serialization as appropriate. → *Expect:* the invalid interleaving is impossible or harmless.
6. **Verify under repeated stress.** Run the reproduction many times, such as `for i in {1..100}; do pytest -q tests/test_race.py || break; done`. → *Expect:* no failure occurs across the stress window.
7. **Remove artificial delays.** Keep deterministic tests or synchronization primitives only if they are part of the test harness. → *Expect:* production code has no debugging sleeps.

## Decision points

- Shared database row is overwritten → use transactions, row locks, optimistic locking, or idempotency keys.
- Shared in-memory map is mutated → guard it with a lock or use a concurrent data structure.
- Async UI result arrives out of order → cancel stale requests or ignore responses older than the current request token.
- Queue job runs twice → make the handler idempotent and lock around side effects.

## Failure modes & recovery

- **F1 Race disappears when logged:** detect failure vanishes with extra I/O → use lower-overhead tracing or controlled synchronization in tests.
- **F2 Lock introduces deadlock:** detect hung tests or lock timeout → enforce lock ordering and use timeouts in tests.
- **F3 Fix serializes too much:** detect unacceptable throughput drop → reduce lock scope or use optimistic concurrency.
- **F4 Race detector false confidence:** detect detector passes but bug remains → remember detectors miss distributed and database ordering races.

## Verification

The race detector command, when available, exits 0, and the focused stress command runs the previous reproduction at least 100 times without failure or inconsistent final state.

## Variations

- `Go`: use `go test -race` plus targeted stress loops.
- `JavaScript`: use fake timers, abort controllers, and request sequence IDs for async ordering races.
- `database`: use isolation levels, unique constraints, row locks, or optimistic version columns.
- `distributed systems`: prefer idempotency keys and durable state transitions over process-local locks.

## Safety & privacy

Medium risk because race testing can overload shared systems. Run stress loops locally or in staging, cap concurrency, use synthetic data, and avoid logging raw request payloads while tracing interleavings.
