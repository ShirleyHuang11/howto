---
name: debug-a-deadlock
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

You identify the resources involved in a deadlock, fix the lock ordering or transaction behavior, and verify the system no longer hangs.

## Preconditions

- You can reproduce or observe the hang in a safe environment.
- Thread, goroutine, database lock, or transaction diagnostics are available.
- You know any timeout or cancellation behavior expected by the service.

## Steps

1. **Confirm it is a deadlock or hang.** Observe requests, tests, or jobs stop making progress while CPU is low or workers wait. → *Expect:* the symptom is blocked progress, not slow computation.
2. **Capture waiting stacks.** [Go | JVM | Python] dump goroutines, thread stacks, or async task stacks; for databases, inspect lock views. → *Expect:* stack traces show where each worker is waiting.
3. **Identify the lock cycle.** Map each participant to the lock, row, mutex, channel, or future it holds and the one it wants. → *Expect:* a cycle or blocking dependency is visible.
4. **Reproduce with a focused test.** Create two transactions, threads, or workers that acquire resources in the problematic order. → *Expect:* the test hangs or times out on the bad code.
5. **Break the cycle.** Enforce a consistent lock order, shorten transactions, use `SELECT ... FOR UPDATE` consistently, add timeouts, or remove nested locks. → *Expect:* no participant waits forever.
6. **Add timeout assertions.** Make tests fail quickly with explicit timeouts rather than hanging CI. → *Expect:* a regression produces a clear timeout failure.
7. **Run concurrency verification.** Execute the focused test repeatedly and inspect database lock metrics if applicable. → *Expect:* no deadlocks or lock timeout errors occur.

## Decision points

- Deadlock is inside database transactions → inspect lock graphs and reorder queries consistently.
- Deadlock is in process mutexes → enforce global lock ordering and avoid callbacks while holding locks.
- Async code awaits while holding a lock → release before await or use a scoped async lock carefully.
- Only production shows it → capture diagnostics during incident response and reproduce in staging with synthetic load.

## Failure modes & recovery

- **F1 CI hangs indefinitely:** detect no output until job timeout → add per-test timeout and stack dump on timeout.
- **F2 Database deadlock retries hide the bug:** detect intermittent `deadlock detected` with successful retry → keep retry but fix lock order to reduce errors.
- **F3 Added timeout causes partial writes:** detect cancellation after some side effects → make the operation transactional or compensating.
- **F4 Incomplete lock graph:** detect stacks show waits but not owners → enable database lock diagnostics or runtime blocking profile.

## Verification

The focused deadlock reproduction test completes within its timeout and exits 0 for repeated runs, and database logs or runtime diagnostics show no new deadlock reports during the verification window.

## Variations

- `Postgres`: inspect `pg_stat_activity` and `pg_locks`; deadlocks appear as `deadlock detected`.
- `MySQL/InnoDB`: inspect `SHOW ENGINE INNODB STATUS` and lock wait timeout messages.
- `Go`: use goroutine dumps and mutex/block profiles.
- `JVM`: use `jstack`, thread dumps, and deadlock detection from management tools.

## Safety & privacy

Medium risk because deadlock debugging often touches transactions and concurrency controls. Use staging or local fixtures, keep lock-diagnostic output restricted, and avoid changing isolation levels in production without review.
