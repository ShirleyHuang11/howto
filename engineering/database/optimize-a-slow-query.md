---
name: optimize-a-slow-query
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 45min
risk: medium
prerequisites: [engineering/database/write-a-sql-query]
status: draft
last_verified: 2026-09-11
---

## Goal

You improve a slow database query using evidence from execution plans and metrics, without changing the query's intended results.

## Preconditions

- The exact slow query, parameters, and environment are known.
- Representative data is available in staging, a replica, or production with safe read-only access.
- You can run `EXPLAIN` and inspect existing indexes.
- A correctness check exists for the query result.

## Steps

1. **Capture the baseline.** Record query text, parameters, runtime, row count, and frequency from logs or APM. → *Expect:* a measurable target such as "p95 4s for tenant dashboard query."
2. **Run the execution plan.** [BRANCH: Postgres | MySQL] Use `EXPLAIN (ANALYZE, BUFFERS) <query>;` in a safe environment or `EXPLAIN ANALYZE <query>;` where supported. → *Expect:* the dominant cost is visible.
3. **Check result correctness before edits.** Save a small expected result set or aggregate checksum. → *Expect:* you can compare optimized output against baseline.
4. **Look for missing filters and bad joins.** Verify tenant/date filters, join predicates, and accidental row multiplication. → *Expect:* query logic matches the intended data shape.
5. **Improve the cheapest safe thing first.** Add/select indexes, rewrite predicates to be sargable, reduce selected columns, or pre-aggregate where appropriate. → *Expect:* one change has a clear reason tied to the plan.
6. **Compare plans and results.** Rerun the plan and correctness check. → *Expect:* runtime or scanned rows improve while result count/checksum stays the same.
7. **Deploy through migration or code review.** Put schema or query changes in normal review and CI. → *Expect:* tests and migration checks pass before production.
8. **Monitor production impact.** After deploy, compare p95 latency, database CPU, and error rate. → *Expect:* the slow query metric improves without new load elsewhere.

## Decision points

- Query returns too much data → paginate, narrow filters, or move bulk export to an async path.
- Predicate wraps indexed column in a function → rewrite to compare raw column values.
- Missing index is the bottleneck → add the smallest useful index and verify write overhead.
- Query is inherently expensive analytics → move to a read replica, materialized view, or warehouse.

## Failure modes & recovery

- **F1 Faster but wrong result:** detect result count/checksum mismatch → revert the rewrite and add tests for the missed case.
- **F2 Planner still scans table:** detect plan unchanged → update statistics, adjust index order, or revise predicates.
- **F3 New index hurts writes:** detect higher write latency or bloat → drop or replace the index after review.
- **F4 Optimization shifts bottleneck:** detect database improves but app latency remains high → profile serialization, network, or downstream calls.

## Verification

The optimized query returns the same validation count/checksum as the baseline, and `EXPLAIN (ANALYZE, BUFFERS)` or equivalent shows reduced runtime, scanned rows, or buffer reads on representative data.

## Variations

- `Postgres`: use `EXPLAIN (ANALYZE, BUFFERS)`, `pg_stat_statements`, partial indexes, and materialized views where justified.
- `MySQL`: use `EXPLAIN ANALYZE`, `performance_schema`, and composite indexes aligned to filters and ordering.
- `ORM`: inspect generated SQL and benchmark the SQL directly, not only application-level timing.

## Safety & privacy

Medium risk because performance fixes can alter results, add write overhead, or stress production during analysis. Use read-only access for investigation, avoid dumping sensitive rows, and deploy schema changes with rollback plans.
