---
name: trace-a-slow-database-query
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

You identify why a database query is slow, validate the query plan with realistic parameters, and apply a fix that improves measured latency without unsafe production locks.

## Preconditions

- You have the exact SQL or ORM-generated query, parameters, and database engine.
- You can run `EXPLAIN` or equivalent on staging, a read replica, or a scrubbed local snapshot.
- You know the latency budget and affected endpoint or job.
- For production changes, you have approval and a rollback plan.

## Steps

1. **Capture the exact query and parameters.** Enable safe SQL logging or copy the query from traces with literals redacted where needed. → *Expect:* the same query shape that production executes.
2. **Measure baseline latency.** [Postgres | MySQL] run `EXPLAIN (ANALYZE, BUFFERS) <query>` on Postgres or `EXPLAIN ANALYZE <query>` on MySQL 8+. → *Expect:* actual time, row counts, join methods, and scan types are visible.
3. **Compare estimated and actual rows.** Inspect plan nodes where actual rows differ greatly from estimates. → *Expect:* candidate causes such as stale statistics, missing index, bad predicate, or join explosion.
4. **Check existing indexes and constraints.** [Postgres | MySQL] run `\d+ table_name` or `SHOW INDEX FROM table_name;`. → *Expect:* a list showing whether predicates, joins, and order clauses are covered.
5. **Test a safe fix on non-production data.** Add or adjust an index, rewrite the query, limit selected columns, or split the query. For Postgres, prefer `CREATE INDEX CONCURRENTLY idx_table_col ON table_name (col);` when creating in production. → *Expect:* the plan uses fewer rows, lower cost, or a better index without changing result rows.
6. **Verify result equivalence.** Compare old and new query results with checksums or counts for representative parameters. → *Expect:* identical result sets or a documented intentional change.
7. **Plan production rollout.** ⚠️ *Irreversible:* schema changes can lock or degrade production; confirm backup, lock behavior, migration timeout, and rollback before applying. → *Expect:* an approved migration plan with lock-safe DDL.
8. **Apply and monitor.** Run the migration through the standard deploy path and watch database CPU, locks, query latency, and error rate. → *Expect:* latency improves and no lock pileup or error spike appears.

## Decision points

- Sequential scan reads a small table → do not add an index unless measured latency justifies it.
- Bad estimates dominate the plan → update statistics before changing query structure.
- Query waits on locks rather than CPU/IO → identify blockers instead of adding indexes.
- ORM emits inefficient SQL → add a targeted query, preload, or pagination change rather than broad ORM settings.

## Failure modes & recovery

- **F1 Migration lock timeout:** detect lock timeout or blocked sessions → cancel the migration, retry during a low-traffic window, or use online DDL.
- **F2 Index not used:** detect plan still scans the table → verify predicate order, data type casts, selectivity, and statistics.
- **F3 Faster query returns different rows:** detect checksum or count mismatch → revert the rewrite and add tests for the intended semantics.
- **F4 Replica plan differs from primary:** detect different statistics or parameter values → test against representative data and engine settings.

## Verification

`EXPLAIN (ANALYZE, BUFFERS) <query>` or the engine equivalent shows lower actual runtime under the target budget, result comparison returns identical rows, and the endpoint or job performance test exits 0.

## Variations

- `Postgres`: use `pg_stat_statements`, `EXPLAIN (ANALYZE, BUFFERS)`, `VACUUM ANALYZE`, and `CREATE INDEX CONCURRENTLY`.
- `MySQL`: use `performance_schema`, `EXPLAIN ANALYZE`, and online DDL options supported by the engine.
- `SQLite`: use `EXPLAIN QUERY PLAN` and `ANALYZE`; watch for missing indexes on joins.
- `ORM`: log generated SQL and assert query counts in tests to catch N+1 regressions.

## Safety & privacy

Medium risk because query changes and indexes can affect shared databases. Use scrubbed data where possible, avoid selecting personal data into logs, and get explicit review for production DDL or data migrations.

