---
name: archive-old-rows
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Move old rows out of a hot table into an archive location while preserving records needed for audit, restore, or analytics.

## Preconditions

- Retention requirements and legal holds are known.
- A backup or restore point exists before deleting from the source table.
- The archive table, bucket, or warehouse is access-controlled and tested.

## Steps

1. **Define the archive predicate.** Write a precise condition such as `created_at < now() - interval '18 months' AND status = 'closed'`. → *Expect:* a count query returns the intended candidate set.
2. **Create the archive destination.** Use a table with compatible columns, for example `CREATE TABLE IF NOT EXISTS orders_archive (LIKE orders INCLUDING ALL);`. → *Expect:* archived rows can store all required fields and metadata.
3. **Take a backup or snapshot.** ⚠️ *Irreversible:* before deleting source rows, create a verified backup such as `pg_dump --format=custom --file=orders_before_archive.dump "$DATABASE_URL"`. → *Expect:* the backup command exits 0 and the file or snapshot is visible.
4. **Archive in bounded batches.** Insert candidates with a batch limit, for example `INSERT INTO orders_archive SELECT * FROM orders WHERE ... ORDER BY id LIMIT 5000 ON CONFLICT DO NOTHING;`. → *Expect:* each batch copies a known number of rows without long locks.
5. **Verify each copied batch.** Compare source candidate IDs to archive IDs before deletion. → *Expect:* every row selected for deletion exists in the archive.
6. **Delete only verified rows.** Run `DELETE FROM orders WHERE id IN (SELECT id FROM orders_archive WHERE archived_at >= $run_started_at) AND ...;`. → *Expect:* source row count decreases by the verified copied count.
7. **Record the archive run.** Store run ID, predicate, counts, checksum, actor, and timestamp. → *Expect:* future auditors can explain what moved and when.
8. **Vacuum or optimize later.** [Postgres] schedule `VACUUM (ANALYZE) orders;` after large deletes. → *Expect:* query plans and table statistics reflect the smaller hot table.

## Decision points

- Rows must remain queryable in product → use partitioning or an archive table behind a view.
- Legal hold applies → exclude held rows and log the exclusion query.
- Delete volume is large → batch by primary key ranges and pause between batches.
- Archive is cold storage → write checksums and test restore before deleting source rows.

## Failure modes & recovery

- **F1 Archive copy incomplete:** detect mismatched ID counts or checksums → stop deletion, rerun copy idempotently, and inspect failed rows.
- **F2 Delete locks hot table:** detect blocked writes or lock timeout → reduce batch size and run during a maintenance window.
- **F3 Wrong predicate:** detect unexpectedly high candidate count → stop, restore from backup if deleted, and add a reviewed dry-run step.
- **F4 Archive unreadable:** detect permission or schema errors during restore test → fix archive access before deleting any source rows.

## Verification

The dry-run count matches the recorded archive count, `SELECT count(*) FROM orders o WHERE <predicate> AND NOT EXISTS (SELECT 1 FROM orders_archive a WHERE a.id = o.id);` returns 0 before deletion, and restore from the backup or archive succeeds in a test database.

## Variations

- `Partitioned tables`: detach or exchange old partitions instead of row-by-row deletes.
- `BigQuery/Snowflake`: copy to partitioned archive tables and validate with row counts plus checksums.
- `S3/object storage`: export as compressed Parquet or CSV with manifest and checksum files.

## Safety & privacy

High risk because source deletion is irreversible without a working backup. Confirm retention policy, legal holds, backup restoreability, and least-privilege archive permissions before deleting any production data.
