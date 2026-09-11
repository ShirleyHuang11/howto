---
name: write-a-sql-query
domain: engineering
subdomain: database
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

You write a SQL query that returns the intended data, uses the correct filters, and can be checked against known rows or counts.

## Preconditions

- Read access to the database or a representative local/test copy.
- The table names, columns, and relationships are known or discoverable.
- The question being answered has expected row shape, filters, and ordering.
- Queries are run read-only unless explicitly approved.

## Steps

1. **State the result shape.** Write the columns, filters, grouping, and ordering the query must produce. → *Expect:* a clear target such as "one row per customer with total paid order value."
2. **Inspect the schema.** [BRANCH: Postgres | MySQL | SQLite] Run `\d table_name`, `DESCRIBE table_name;`, or `.schema table_name`. → *Expect:* column names and data types match the planned query.
3. **Start with a small select.** Run `SELECT col1, col2 FROM table_name LIMIT 10;`. → *Expect:* sample rows confirm the table contains the expected data.
4. **Add filters deliberately.** Add `WHERE` predicates for date ranges, status, tenant, or soft-delete fields. → *Expect:* row count narrows for intentional reasons.
5. **Add ordering or aggregation.** Use `ORDER BY`, `GROUP BY`, and aggregate functions only after base rows are correct. → *Expect:* grouped rows or sorted results match the requested shape.
6. **Check the query plan for large tables.** Run `EXPLAIN` or `EXPLAIN ANALYZE` in a safe environment. → *Expect:* the plan uses reasonable indexes or scans an acceptably small table.
7. **Validate against known examples.** Compare one or two returned rows with source records or fixtures. → *Expect:* manual spot checks agree with the query result.

## Decision points

- The query will run in production on a large table → use `LIMIT`, `EXPLAIN`, and an indexed filter before running the full query.
- Time ranges are involved → use half-open intervals such as `created_at >= $start AND created_at < $end`.
- NULL values are meaningful → handle `IS NULL`, `COALESCE`, or three-valued logic explicitly.
- The query feeds code → parameterize it rather than concatenating strings.

## Failure modes & recovery

- **F1 Wrong row count:** detect too many or too few rows → check filters, joins, soft-delete columns, and tenant constraints.
- **F2 Syntax differs by database:** detect errors near `LIMIT`, quoting, or date functions → adapt to the target engine's SQL dialect.
- **F3 Slow query:** detect full table scan or timeout → add selective predicates, use indexes, or run on a replica.
- **F4 NULL surprises:** detect missing or duplicated rows around NULL values → use explicit NULL predicates and test examples.

## Verification

The final query runs successfully in the target database, returns the expected columns, and a validation query such as `SELECT count(*) FROM (<final query>) q;` returns the expected count or an explainable bounded count.

## Variations

- `Postgres`: use `psql`, `\d`, `EXPLAIN (ANALYZE, BUFFERS)`, and positional parameters in app code.
- `MySQL`: use `DESCRIBE`, `EXPLAIN FORMAT=TREE`, and `?` placeholders through drivers.
- `SQLite`: use `.schema`, `EXPLAIN QUERY PLAN`, and local fixture databases for quick validation.

## Safety & privacy

Low risk when read-only, but production queries can still expose sensitive data or cause load. Select only needed columns, avoid exporting personal data unless approved, prefer replicas for heavy reads, and never paste customer rows into public channels.
