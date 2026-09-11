---
name: normalize-a-table-design
domain: engineering
subdomain: database
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

Reshape duplicated or inconsistent table data into a normalized design with clear entities, keys, and referential integrity.

## Preconditions

- You understand the current read/write paths and have sample production-like data.
- You can run schema migrations and application tests in a non-production database.
- A rollback plan or backup exists before changing shared data.

## Steps

1. **Map the current anomalies.** Query duplicates and repeated groups, for example `SELECT email, count(*) FROM customers GROUP BY email HAVING count(*) > 1;`. → *Expect:* a concrete list of redundancy or update-anomaly cases.
2. **Define entities and dependencies.** Separate fields that depend on different keys, such as moving repeated addresses to `customer_addresses`. → *Expect:* each proposed table has a primary key and columns that depend on that key.
3. **Create the new tables.** Add primary keys, `NOT NULL` columns where valid, and indexes for known joins. → *Expect:* migrations apply cleanly in a test database.
4. **Backfill data idempotently.** Use `INSERT INTO customer_addresses (...) SELECT DISTINCT ... FROM customers ON CONFLICT DO NOTHING;`. → *Expect:* rerunning the backfill does not create duplicates.
5. **Add foreign-key columns or mapping tables.** Populate references with joins from old values to new IDs. → *Expect:* every old row maps to the intended normalized record.
6. **Update application reads and writes.** Change code to write the normalized tables and read through joins or repository methods. → *Expect:* tests pass using only the new schema path.
7. **Validate referential integrity.** Add foreign keys after the backfill, using online validation where supported. → *Expect:* invalid references are rejected while valid existing rows pass.
8. **Remove obsolete columns later.** ⚠️ *Irreversible:* drop old duplicated columns only after backup, deploy soak time, and confirmed no reads depend on them. → *Expect:* the schema no longer stores the same fact in multiple places.

## Decision points

- Data is small and low-traffic → one migration may be acceptable.
- Data is large or production-critical → use expand/backfill/contract across multiple deploys.
- Existing duplicates disagree → define a deterministic winner and keep an audit table for manual review.
- Joins become too expensive → add indexes or denormalized read models, not duplicate write sources.

## Failure modes & recovery

- **F1 Backfill mismatch:** detect row counts that do not reconcile → pause contract work, inspect unmapped rows, and fix transformation logic.
- **F2 Foreign key validation fails:** detect constraint validation errors → query orphan references, repair data, then validate again.
- **F3 Application still reads old columns:** detect errors after dropping or hiding columns → roll back app deploy or restore columns from backup.
- **F4 Slow joins:** detect query latency regression → add targeted indexes and confirm with `EXPLAIN`.

## Verification

`pytest -q` exits 0, the migration command exits 0 on a restored production-like dump, and reconciliation SQL such as `SELECT count(*) FROM old_source EXCEPT SELECT count(*) FROM new_joined_view;` shows no missing records.

## Variations

- `Postgres`: use `NOT VALID` foreign keys followed by `VALIDATE CONSTRAINT` for safer production rollout.
- `Rails`: use separate migrations for add, backfill, validate, and drop steps.
- `Analytics warehouse`: favor dimensional modeling checks and dbt tests for uniqueness and relationships.

## Safety & privacy

Medium risk because schema changes can break writes and joins. Back up production data, run destructive drops separately, avoid exporting sensitive data to local machines, and get review before contract migrations.
