---
name: paginate-query-results
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Return large query result sets in stable, bounded pages so clients can resume without duplicates, skipped rows, or full-table memory pressure.

## Preconditions

- A database client, test database, and representative rows exist.
- The result has a deterministic sort key, ideally a unique indexed column such as `id` or `(created_at, id)`.
- You can run the application tests and an `EXPLAIN` query.

## Steps

1. **Choose the pagination contract.** Prefer cursor/keyset pagination for mutable or large tables; reserve `LIMIT/OFFSET` for small admin views. → *Expect:* the endpoint or repository method accepts `limit` plus `after` or `before` cursor.
2. **Define a stable ordering.** Sort by a unique tuple, for example `ORDER BY created_at DESC, id DESC`. → *Expect:* every row has one unambiguous position in the ordered result.
3. **Add a covering index for the order and filters.** [Postgres] run `CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_events_feed ON events (tenant_id, created_at DESC, id DESC);` outside a transaction. → *Expect:* the index build completes and does not take an exclusive table lock.
4. **Implement the page query.** Use a tuple comparison such as `WHERE tenant_id = $1 AND (created_at, id) < ($2, $3) ORDER BY created_at DESC, id DESC LIMIT $4`. → *Expect:* the first page works with no cursor, later pages start after the last seen tuple.
5. **Fetch one extra row.** Query `limit + 1`, return only `limit`, and set `has_next_page` when the extra row exists. → *Expect:* clients know whether to request another page without a separate count query.
6. **Encode opaque cursors.** Store the last row's sort tuple in base64url JSON, for example `{"created_at":"2026-09-11T12:00:00Z","id":123}`. → *Expect:* clients cannot accidentally forge SQL fragments or depend on internal column names.
7. **Add boundary tests.** Insert rows with equal timestamps and verify page 1 plus page 2 returns each row exactly once. → *Expect:* the test fails if ordering is non-unique or comparison signs are wrong.
8. **Check the query plan.** Run `EXPLAIN (ANALYZE, BUFFERS) SELECT ... LIMIT 51;` against realistic data. → *Expect:* the plan uses the intended index and does not perform a full table scan for normal filters.

## Decision points

- Results can change while users browse → use keyset pagination and document eventual consistency.
- Users need random page numbers → `OFFSET` may be acceptable, but cap the maximum offset and monitor latency.
- Sort field is not unique → append a unique tiebreaker such as `id`.
- Cursor contains tenant or permission scope → sign it or revalidate the scope server-side.

## Failure modes & recovery

- **F1 Duplicate rows across pages:** detect repeated IDs in an integration test → add a unique tiebreaker to `ORDER BY` and the cursor.
- **F2 Skipped rows:** detect missing IDs when stitching pages → align comparison operators with sort direction.
- **F3 Slow deep pages:** detect high latency or `Rows Removed by Filter` in `EXPLAIN` → switch from `OFFSET` to keyset pagination and add the matching index.
- **F4 Invalid cursor crashes:** detect 500s on malformed cursor input → validate, return `400`, and never interpolate cursor content into SQL.

## Verification

`pytest -q tests/test_pagination.py` exits 0, and `EXPLAIN (ANALYZE, BUFFERS)` for the paginated query shows an index scan with bounded rows for a normal page size.

## Variations

- `GraphQL Relay`: expose `edges`, `node`, `cursor`, and `pageInfo.hasNextPage`.
- `MySQL`: use composite indexes with matching order; tuple comparisons are supported, but verify with `EXPLAIN FORMAT=JSON`.
- `Elasticsearch`: use `search_after` with a deterministic sort tuple instead of SQL cursors.

## Safety & privacy

Medium risk because pagination bugs can expose cross-tenant data or overload a database. Keep tenant filters outside opaque cursors, validate cursor input, cap `limit`, and avoid logging cursors if they contain sensitive identifiers.
