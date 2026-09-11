---
name: run-a-database-migration-safely
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-4h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You apply a database migration with backups, compatibility checks, and post-migration verification. Production data remains recoverable and the application stays compatible throughout the migration.

## Preconditions

- The migration has been reviewed and tested on a staging copy or representative dataset.
- A current backup or snapshot can be restored.
- Application deploy order is known, especially for expand/contract changes.
- You have database credentials with only the permissions needed.

## Steps

1. **Classify the migration risk.** Identify whether it adds nullable structures, backfills data, changes constraints, or drops/rewrites data. → *Expect:* migration notes state whether it is reversible and whether downtime is expected.
2. **Take and verify a backup.** Create a snapshot or dump before production changes, then confirm it exists. [BRANCH: Postgres, `pg_dump --format=custom --file backup.dump "$DATABASE_URL"` for logical backup | managed DB, create a provider snapshot] → *Expect:* backup command exits 0 or provider snapshot status is available.
3. **Check locks and long transactions.** [BRANCH: Postgres, query `pg_stat_activity` for long-running transactions | MySQL, inspect `information_schema.processlist`] → *Expect:* no active transaction is likely to block the migration.
4. **Run preflight on staging.** Apply the exact migration command to staging, such as `npm run db:migrate`, `alembic upgrade head`, `rails db:migrate`, or `prisma migrate deploy`. → *Expect:* staging migration exits 0 and application tests or smoke checks pass.
5. **Apply production-safe migration steps.** Use online patterns: add nullable columns first, create Postgres indexes with `CREATE INDEX CONCURRENTLY`, backfill in batches, then add constraints after validation. ⚠️ *Irreversible:* schema and data changes may be hard to undo; confirm backup, migration ID, and maintenance window before production execution. → *Expect:* migration command exits 0 and records the migration version.
6. **Verify schema and data.** Run read-only checks such as `SELECT count(*) FROM schema_migrations WHERE version = '<id>';` and targeted row-count or constraint queries. → *Expect:* migration version is present and data counts match expectations.
7. **Run application smoke checks.** Hit health endpoints and the code paths that read or write migrated data. → *Expect:* HTTP checks return 200 and logs show no new database errors.
8. **Record completion and cleanup tasks.** Note migration ID, backup location, verification queries, and any later contract migration. → *Expect:* release notes contain enough detail to audit or recover.

## Decision points

- Migration drops columns or data → split into a later contract migration after code no longer uses them.
- Table is large → use concurrent indexes, batched backfills, and lock-timeout settings.
- Migration blocks or exceeds lock timeout → cancel, investigate blockers, and retry during a safer window.
- Backup cannot be verified → stop before production mutation.

## Failure modes & recovery

- **F1 Lock timeout:** detect `lock timeout`, `deadlock`, or waiting DDL → cancel migration, find blockers, and retry with online strategy.
- **F2 Partial migration:** detect migration table missing final version or failed step → use framework repair commands or manually complete only after review.
- **F3 Application errors after migration:** detect SQL errors or 5xx → roll back application if compatible or apply forward fix; do not drop backup.
- **F4 Backfill overload:** detect high CPU, replication lag, or lock contention → pause batches, reduce batch size, and resume after metrics recover.

## Verification

The production migration command exits 0, the migration tracking table contains the expected migration ID, targeted SQL checks return expected counts or constraints, and application smoke checks against migrated paths return HTTP 200 without new database errors.

## Variations

- `Postgres`: use `CREATE INDEX CONCURRENTLY`, `VALIDATE CONSTRAINT`, `lock_timeout`, and batched updates.
- `MySQL`: use online DDL where supported and verify metadata locks.
- `Rails`: prefer reversible migrations, but treat destructive changes as separate reviewed steps.
- `Prisma/Alembic/Flyway`: use deploy-grade commands, not local dev reset commands.

## Safety & privacy

High risk because production data can be changed or lost. Back up first, avoid printing personal data in logs, use least-privilege database credentials, and require explicit human approval for destructive or irreversible migrations.
