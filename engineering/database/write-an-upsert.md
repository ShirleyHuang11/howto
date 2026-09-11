---
name: write-an-upsert
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

Insert a row when it does not exist and update the intended fields when it does, without race conditions or accidental overwrites.

## Preconditions

- The table has a primary key or unique constraint that defines identity.
- You know which columns are safe to overwrite and which must remain immutable.
- A local or staging database is available for concurrency tests.

## Steps

1. **Identify the conflict target.** Choose the exact unique key, for example `(tenant_id, external_id)`. → *Expect:* the database rejects duplicate logical records before the upsert is added.
2. **Create the unique constraint if missing.** [Postgres] run `CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS idx_widgets_identity ON widgets (tenant_id, external_id);`. → *Expect:* duplicate inserts fail with a unique-violation error.
3. **Write the upsert explicitly.** [Postgres] use `INSERT INTO widgets (...) VALUES (...) ON CONFLICT (tenant_id, external_id) DO UPDATE SET name = EXCLUDED.name, updated_at = now() RETURNING *;`. → *Expect:* existing rows update only the named columns.
4. **Protect immutable fields.** Leave `created_at`, owner IDs, and source IDs out of `DO UPDATE SET` unless deliberately changed. → *Expect:* repeated upserts preserve immutable metadata.
5. **Handle conditional updates.** Add `WHERE widgets.version < EXCLUDED.version` or similar when stale payloads must not win. → *Expect:* older events do not overwrite newer state.
6. **Wrap dependent writes in a transaction.** Commit the upsert and any child rows together. → *Expect:* partial related data is not visible after a failure.
7. **Add concurrency coverage.** Run two workers inserting the same logical record at once. → *Expect:* one row exists afterward, with deterministic final values.

## Decision points

- Existing row must never change → use `ON CONFLICT DO NOTHING`.
- Event ordering matters → add a version or timestamp predicate to the update.
- Conflict target is nullable → normalize the key or use a partial unique index; SQL unique constraints treat `NULL` specially.
- Many rows are upserted → batch values and measure lock time.

## Failure modes & recovery

- **F1 No unique constraint:** detect duplicate logical rows after concurrent inserts → add the constraint after deduplicating data.
- **F2 Accidental data loss:** detect immutable columns changing → narrow the `SET` list and restore from backup or audit log.
- **F3 Deadlocks:** detect database deadlock errors under load → order batched keys consistently and retry the whole transaction.
- **F4 Stale event wins:** detect older payload overwriting newer fields → add conditional `WHERE` logic and an assertion on affected row count.

## Verification

`pytest -q tests/test_upsert.py` exits 0, and `SELECT tenant_id, external_id, count(*) FROM widgets GROUP BY 1,2 HAVING count(*) > 1;` returns zero rows.

## Variations

- `MySQL`: use `INSERT ... ON DUPLICATE KEY UPDATE name = VALUES(name)`, or aliases in newer MySQL versions.
- `SQLite`: use `INSERT ... ON CONFLICT(key) DO UPDATE SET ...`.
- `ORM`: prefer the ORM's native upsert only if it exposes conflict target and update column control.

## Safety & privacy

Medium risk because an upsert can silently overwrite shared data. Use least-privilege database credentials, avoid logging full payloads with secrets, and review every column in the update list before merging.
