---
name: restore-a-database-from-backup
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-2h
risk: high
prerequisites: [engineering/database/back-up-a-database]
status: draft
last_verified: 2026-09-11
---

## Goal

You restore a database from a backup into the correct target environment and verify the restored data before allowing dependent applications to use it.

## Preconditions

- The backup artifact or snapshot ID is known and has passed readability checks.
- The restore target is identified and isolated from production unless this is an approved production recovery.
- Application owners approve any overwrite or point-in-time recovery.
- Credentials for restore and validation are available.

## Steps

1. **Confirm source backup metadata.** Check backup timestamp, database name, engine version, and checksum. → *Expect:* the backup matches the intended recovery point.
2. **Confirm the restore target.** Run `SELECT current_database(), current_user;` against the target or inspect cloud project/region. → *Expect:* the target is the intended empty/scratch database or approved recovery database.
3. **Block accidental writes from apps.** Stop dependent app connections or restore into an isolated database first. → *Expect:* no live application is writing to the target during restore.
4. **Run the restore command.** [BRANCH: Postgres | MySQL] For Postgres custom dumps, run `pg_restore --clean --if-exists --no-owner --dbname="$TARGET_DATABASE_URL" backup.dump`; for MySQL, run `mysql <target_db> < backup.sql`. → *Expect:* restore command exits 0 or reports only reviewed harmless object-exists notices.
5. **Run integrity checks.** Execute row counts, required table checks, and application-specific invariants. → *Expect:* critical tables exist and counts match the backup manifest or expected recovery point.
6. **Run application smoke tests against the restored database.** Point a staging app or one-off process at the restored target. → *Expect:* app starts and core read/write smoke tests pass.
7. **Promote only after approval.** ⚠️ *Irreversible:* replacing a live database can overwrite current data; confirm final approval, target, and backup before switching apps. → *Expect:* apps connect to the restored database only after verification.
8. **Monitor after reconnect.** Watch error rate, slow queries, replication, and write success. → *Expect:* service remains healthy on the restored data.

## Decision points

- Restore is for investigation → restore to isolated scratch database, not over an existing environment.
- Restore is production recovery → freeze writes, communicate impact, and record the accepted data-loss window.
- Engine versions differ → restore to a compatible version or perform documented upgrade steps.
- Backup contains secrets or personal data → restrict restore environment access to approved operators.

## Failure modes & recovery

- **F1 Wrong target selected:** detect production or unexpected database name before restore → stop immediately and correct connection strings.
- **F2 Restore fails on ownership/roles:** detect role or owner errors → use `--no-owner`, recreate roles, or adjust grants after restore.
- **F3 Data validation mismatch:** detect missing tables or row count differences → verify backup artifact, restore logs, and whether point-in-time was expected.
- **F4 App incompatible with restored schema:** detect migration/version errors → deploy matching app version or run required migrations after restore.

## Verification

The restore command exits 0, validation SQL returns expected table counts, application smoke tests pass against the restored database, and dependent apps report healthy after any approved promotion.

## Variations

- `Postgres`: use `pg_restore` for custom dumps, `psql` for plain SQL, and managed PITR for production recovery.
- `MySQL`: restore with `mysql` for logical dumps or provider snapshot restore for large databases.
- `Managed cloud`: prefer restoring snapshots to a new instance, validate, then switch connection endpoints.

## Safety & privacy

High risk because restore can overwrite live data and expose production records in lower environments. Confirm target twice, isolate restored data, restrict access, and require explicit approval before any production cutover.
