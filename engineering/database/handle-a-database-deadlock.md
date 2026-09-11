---
name: handle-a-database-deadlock
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You diagnose a database deadlock, make the application tolerate safe retries, and reduce the lock-order pattern that caused it.

## Preconditions

- Deadlock errors or logs identify the affected queries or transactions.
- You can inspect database lock activity and application logs.
- The affected operation is understood well enough to decide whether retry is safe.
- A test or staging environment can reproduce or simulate concurrent operations.

## Steps

1. **Capture the deadlock evidence.** Collect error text, transaction IDs, SQL statements, and timestamps from database and app logs. → *Expect:* the conflicting statements and affected code path are identified.
2. **Inspect current locks if the issue is ongoing.** [BRANCH: Postgres | MySQL] Use `pg_stat_activity`/`pg_locks` or `SHOW ENGINE INNODB STATUS`. → *Expect:* blocked and blocking sessions are visible or the deadlock report is available.
3. **Identify lock order.** Trace which rows/tables each transaction locks and in what sequence. → *Expect:* a concrete cycle such as transaction A locks order then user while transaction B locks user then order.
4. **Add safe retry handling.** Catch deadlock-specific errors such as Postgres SQLSTATE `40P01` or MySQL error `1213`, then retry idempotent transactions with jittered backoff. → *Expect:* transient deadlocks no longer fail user requests immediately.
5. **Fix the lock-order cause.** Make code acquire locks in a consistent order, shorten transactions, add selective indexes, or move external calls outside transactions. → *Expect:* the cycle is removed or lock duration is reduced.
6. **Reproduce with concurrency.** Run a focused concurrent test or script that previously triggered the deadlock. → *Expect:* operations complete or retry successfully without unhandled deadlock errors.
7. **Monitor after deploy.** Track deadlock count, transaction duration, and retry rate. → *Expect:* deadlock frequency drops and retries remain rare.

## Decision points

- Operation is not idempotent → add idempotency keys or avoid automatic retry until side effects are controlled.
- Deadlock involves missing indexes → add the index to reduce scanned/locked rows.
- Deadlock happens during batch jobs → process rows in a stable order and smaller batches.
- Deadlock rate is high during incident → throttle the offending job or disable the feature while fixing.

## Failure modes & recovery

- **F1 Retry duplicates side effects:** detect duplicate emails, payments, or jobs → move side effects after commit or add idempotency keys before retrying.
- **F2 Deadlock report lacks SQL:** detect incomplete logs → enable database deadlock logging or application query tags.
- **F3 Long transactions persist:** detect high lock wait times → shorten transaction scope and remove network calls from transactions.
- **F4 Retry storm:** detect many concurrent retries increasing load → add exponential backoff, jitter, and retry limits.

## Verification

A concurrent reproduction test exits 0, application code retries deadlock SQLSTATE/error codes safely, and database metrics show deadlock count decreasing after the fix.

## Variations

- `Postgres`: inspect `pg_stat_activity`, `pg_locks`, and deadlock logs; retry SQLSTATE `40P01`.
- `MySQL/InnoDB`: inspect `SHOW ENGINE INNODB STATUS`; retry error `1213` and sometimes lock wait timeout `1205` if safe.
- `ORM`: use transaction retry helpers only around idempotent transaction blocks.

## Safety & privacy

Medium risk because deadlock fixes touch transaction behavior and can duplicate side effects if retries are unsafe. Do not log sensitive query parameters, keep retry counts bounded, and review changes involving payments or irreversible actions.
