---
name: add-an-index-to-speed-up-a-query
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 45min
risk: medium
prerequisites: [engineering/database/optimize-a-slow-query]
status: draft
last_verified: 2026-09-11
---

## Goal

You add an index that improves a specific slow query while avoiding unnecessary write overhead or dangerous locks.

## Preconditions

- The slow query and database engine are known.
- You can run `EXPLAIN` on a representative dataset.
- Migration tooling is available.
- For production-sized tables, the database supports an online or low-lock index creation path.

## Steps

1. **Capture the current query plan.** [BRANCH: Postgres | MySQL] Run `EXPLAIN (ANALYZE, BUFFERS) <query>;` in a safe environment or `EXPLAIN ANALYZE <query>;` where supported. → *Expect:* the plan shows the expensive scan, join, sort, or filter.
2. **Choose index columns from the query.** Put equality filters first, then range filters, then order-by columns where useful. → *Expect:* the proposed index maps directly to the slow predicate or sort.
3. **Check existing indexes.** Run `\d table_name` or query system catalogs. → *Expect:* no existing equivalent or better index already covers the query.
4. **Create the migration safely.** For Postgres on a live large table, use `CREATE INDEX CONCURRENTLY index_name ON table_name (col1, col2);` outside a transaction. → *Expect:* the migration uses the engine's low-lock option when needed.
5. **Apply in a non-production environment.** Run the migration on staging or a restored copy. → *Expect:* index creation succeeds and table remains queryable.
6. **Compare the new query plan.** Run the same `EXPLAIN` again. → *Expect:* the plan uses the new index and total runtime or cost improves.
7. **Deploy with monitoring.** Apply the migration during an appropriate window and watch locks, CPU, disk, and write latency. → *Expect:* production remains healthy while the index builds.

## Decision points

- Query filters include low-cardinality boolean only → do not index alone; combine with selective columns or use a partial index.
- Query needs only a subset of rows → consider a partial index with the same predicate.
- Query returns many columns → consider a covering index only if read benefit justifies write/storage cost.
- Table is small → an index may not help; the optimizer may correctly prefer a sequential scan.

## Failure modes & recovery

- **F1 Index build blocks writes:** detect lock waits or application timeouts → cancel the build if safe and recreate using online/concurrent syntax.
- **F2 Planner ignores index:** detect unchanged plan → update statistics, verify predicate matches index order, or revise the index.
- **F3 Duplicate index:** detect an equivalent existing index → drop the new index in a separate reviewed migration.
- **F4 Disk pressure:** detect low free storage during build → stop the build, add capacity, or use a smaller/partial index.

## Verification

The migration exits 0, schema inspection shows the new index, and `EXPLAIN (ANALYZE, BUFFERS) <query>;` shows the index being used with improved runtime on representative data.

## Variations

- `Postgres`: use `CREATE INDEX CONCURRENTLY` for large live tables and avoid wrapping it in a transaction.
- `MySQL`: use online DDL options where available, such as `ALGORITHM=INPLACE` or `LOCK=NONE`, after confirming engine/version support.
- `Rails`: use `algorithm: :concurrently` and `disable_ddl_transaction!` for Postgres concurrent indexes.

## Safety & privacy

Medium risk because index builds can lock tables, consume disk, and slow writes. Do not add speculative indexes, avoid production builds without monitoring, and review indexes on sensitive columns for access-pattern exposure.
