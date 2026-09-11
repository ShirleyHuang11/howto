---
name: migrate-data-between-databases
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 4h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Move data from one database to another with validated schema compatibility, controlled downtime or dual-write behavior, and provable row-level reconciliation.

## Preconditions

- Source and target connection strings are available through secrets management.
- Target schema migrations have been tested.
- A rollback plan, backup, and cutover window are approved for production.

## Steps

1. **Inventory source data.** Record tables, row counts, sizes, extensions, constraints, and triggers. → *Expect:* a migration checklist covers every table and dependency.
2. **Prepare the target schema.** Run migrations on the target, for example `DATABASE_URL=$TARGET_URL npm run db:migrate`. → *Expect:* target schema version matches the application expectation.
3. **Take a source backup.** ⚠️ *Irreversible:* before cutover, run a verified backup such as `pg_dump --format=custom --file=source_before_migration.dump "$SOURCE_URL"`. → *Expect:* backup exits 0 and a test restore starts successfully.
4. **Copy data with a repeatable tool.** [Postgres] use `pg_dump --data-only --format=custom "$SOURCE_URL" | pg_restore --data-only --disable-triggers --dbname "$TARGET_URL"` when compatible. → *Expect:* copy exits 0 or reports only reviewed benign warnings.
5. **Reconcile counts and checksums.** Run per-table counts and key checksums on both sides. → *Expect:* every migrated table has matching count and checksum or documented accepted differences.
6. **Run application smoke tests on target.** Point staging at the target with `DATABASE_URL=$TARGET_URL npm test` or equivalent. → *Expect:* core reads and writes pass against the new database.
7. **Cut over writes.** Pause writes, drain queues, perform final incremental sync, then update application configuration. → *Expect:* new writes land only in the target.
8. **Monitor and keep rollback ready.** Watch error rate, replication lag if any, and database metrics. → *Expect:* service health stays green through the cutover window.

## Decision points

- Databases are homogeneous → native dump/restore is usually safest.
- Cross-engine migration → use ETL with explicit type mapping and reconciliation tests.
- Near-zero downtime needed → use change data capture or dual writes with a clear source of truth.
- Data contains PII → keep dumps encrypted and access logged.

## Failure modes & recovery

- **F1 Schema mismatch:** detect restore or migration errors → fix target migrations and rerun on a fresh target.
- **F2 Row-count mismatch:** detect reconciliation differences → identify table ranges, recopy affected rows, and rerun checksums.
- **F3 Cutover write split:** detect writes in both databases → pause consumers, reconcile by timestamp/idempotency key, and reapply missing writes.
- **F4 Performance regression:** detect slow target queries → add indexes, analyze tables, and compare query plans.
- **F5 Authentication failure:** detect connection errors or `permission denied` → verify least-privilege roles and secret names.

## Verification

For each migrated table, `SELECT count(*)` matches source and target, checksum queries over primary-key ordered rows match, application smoke tests exit 0 with `DATABASE_URL=$TARGET_URL`, and production health checks remain green after cutover.

## Variations

- `Postgres`: use `pg_dump`, `pg_restore`, logical replication, or `COPY` depending on downtime.
- `MySQL`: use `mysqldump`, MySQL Shell dump/load, or replication.
- `Cloud managed`: use provider migration services but still run independent reconciliation queries.

## Safety & privacy

High risk because cutover can lose writes or expose data. Encrypt dumps, avoid printing connection strings, restrict credentials, confirm rollback steps before changing production configuration, and keep the source read-only until validation completes.
