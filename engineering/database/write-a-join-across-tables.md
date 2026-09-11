---
name: write-a-join-across-tables
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 25min
risk: low
prerequisites: [engineering/database/write-a-sql-query]
status: draft
last_verified: 2026-09-11
---

## Goal

You write a join query that combines related tables without losing required rows, duplicating data unexpectedly, or hiding missing relationships.

## Preconditions

- Read access to the database or a representative test copy.
- Foreign keys or relationship rules between the tables are known.
- You know whether unmatched rows should be included or excluded.
- The base table and desired grain are defined.

## Steps

1. **Choose the base table and grain.** Decide whether the result is one row per user, order, line item, or other entity. → *Expect:* the query has a stated primary table and row granularity.
2. **Inspect relationship columns.** Run schema commands such as `\d orders` and `\d customers`. → *Expect:* join keys and cardinality are known.
3. **Count the base rows.** Run `SELECT count(*) FROM orders WHERE created_at >= DATE '2026-01-01';`. → *Expect:* a baseline count before the join.
4. **Write the first join.** Use explicit `JOIN ... ON ...`, for example `SELECT o.id, c.email FROM orders o JOIN customers c ON c.id = o.customer_id;`. → *Expect:* rows combine only where keys match.
5. **Choose inner or outer join intentionally.** Use `LEFT JOIN` when base rows must remain even if the related row is missing. → *Expect:* unmatched related fields appear as NULL instead of disappearing.
6. **Check for row multiplication.** Compare `count(*)` and `count(DISTINCT base_id)` after the join. → *Expect:* duplication is either absent or explained by one-to-many relationships.
7. **Add filters in the correct place.** Put related-table filters in the `ON` clause for optional relationships when you need to preserve base rows. → *Expect:* left joins do not accidentally become inner joins.
8. **Validate sample rows.** Pick known IDs and trace values across both tables. → *Expect:* joined fields match the source records.

## Decision points

- Need only records with a match → use `INNER JOIN`.
- Need all base records even without a match → use `LEFT JOIN` and place optional filters carefully.
- Joining one-to-many tables → aggregate or pick a single row before joining if the final grain must stay one row per base entity.
- Ambiguous column names → qualify columns with table aliases.

## Failure modes & recovery

- **F1 Accidental row loss:** detect joined count below base count → switch to `LEFT JOIN` or fix the join predicate.
- **F2 Accidental duplicates:** detect `count(*)` greater than `count(DISTINCT base_id)` → aggregate the many-side table or include the intended grain in the output.
- **F3 Cross join explosion:** detect huge row count or slow query → add the missing `ON` predicate and stop the running query if safe.
- **F4 Optional filter breaks outer join:** detect NULL-preserving rows disappearing → move the related-table predicate from `WHERE` to `ON`.

## Verification

`SELECT count(*) AS rows, count(DISTINCT base_id) AS distinct_base FROM (<final join query>) q;` returns counts consistent with the intended grain, and spot-checked joined values match source-table records.

## Variations

- `Postgres`: use foreign key metadata in `\d` and `EXPLAIN (ANALYZE, BUFFERS)` for join plans.
- `MySQL`: use `SHOW CREATE TABLE` and `EXPLAIN FORMAT=TREE` to inspect keys and join order.
- `ORM`: inspect generated SQL and verify joins with database-level counts, not just object graphs.

## Safety & privacy

Low risk for read-only joins, but joins can expose more sensitive combinations of data than a single table. Select only necessary columns, preserve tenant filters, and avoid copying joined personal data into logs or tickets.
