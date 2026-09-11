---
name: back-up-a-database
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

You create a database backup that is complete enough for the recovery objective, stored securely, and verified enough to be trusted.

## Preconditions

- You know the database engine, host, database name, and backup scope.
- Backup credentials have read/backup privileges but not unnecessary write access.
- Storage destination is encrypted and access-controlled.
- Retention and recovery point requirements are known.

## Steps

1. **Confirm the target database.** Run a safe identity query such as `SELECT current_database(), current_user;` or engine equivalent. → *Expect:* the output matches the intended environment.
2. **Choose logical or physical backup.** Use logical dumps for portability and smaller systems; use provider snapshots or physical backups for large databases. → *Expect:* backup method fits size, restore objective, and engine.
3. **Run the backup command.** [BRANCH: Postgres | MySQL] For Postgres, run `pg_dump --format=custom --file=backup.dump "$DATABASE_URL"`; for MySQL, run `mysqldump --single-transaction --routines --triggers --databases <db> > backup.sql`. → *Expect:* command exits 0 and creates a nonempty backup file or snapshot.
4. **Record metadata.** Capture database name, engine version, backup start/end time, command, and checksum. → *Expect:* a manifest exists beside the backup or in the backup system.
5. **Encrypt and upload if needed.** Store in approved object storage or backup service with restricted access. → *Expect:* backup is present in the destination and not publicly accessible.
6. **Verify backup readability.** Run `pg_restore --list backup.dump > /tmp/backup.list` or inspect dump headers/checksum. → *Expect:* the backup tool can read the file and checksum verification passes.
7. **Test restore periodically.** Restore to an isolated database on a schedule or for high-risk changes. → *Expect:* restore completes and validation queries return expected counts.

## Decision points

- Database is production and large → prefer managed snapshots or physical backup tooling with point-in-time recovery.
- Consistent dump needed while writes continue → use transactionally consistent options such as `--single-transaction`.
- Backup contains personal data → encrypt at rest and restrict access to approved operators.
- Backup precedes a risky migration → verify restore on a scratch database before proceeding.

## Failure modes & recovery

- **F1 Backup command times out:** detect nonzero exit or truncated file → use snapshot/physical backup or run from a replica with appropriate timeout.
- **F2 Inconsistent dump:** detect tables from different points in time → rerun with transactional consistency options or pause writes where required.
- **F3 Backup unreadable:** detect restore/list command fails → discard the backup, fix tooling/version mismatch, and create a new one.
- **F4 Storage access too broad:** detect public bucket or excessive IAM permissions → lock down access and rotate exposed credentials if needed.

## Verification

The backup command exits 0, the backup artifact is nonempty, checksum verification passes, and a restore-list command such as `pg_restore --list backup.dump` exits 0.

## Variations

- `Postgres`: use `pg_dump --format=custom` for logical backups and `pg_basebackup` or managed snapshots for physical backups.
- `MySQL`: use `mysqldump --single-transaction` for InnoDB logical backups or provider snapshots for large databases.
- `Managed cloud`: use automated snapshots/PITR and verify backup status through the provider API.

## Safety & privacy

Medium risk because backups contain sensitive production data and are only useful if restorable. Encrypt backups, limit access, never store dumps in source control, and verify restore paths before relying on a backup for destructive work.
