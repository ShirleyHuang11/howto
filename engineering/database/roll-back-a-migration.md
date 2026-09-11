---
name: roll-back-a-migration
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 45min
risk: high
prerequisites: [engineering/database/write-a-schema-migration]
status: draft
last_verified: 2026-09-11
---

## Goal

You reverse a database migration safely, preserving data where possible and restoring application compatibility.

## Preconditions

- The failed migration, target environment, and current application version are known.
- A recent backup or snapshot exists for production or any irreversible change.
- The migration has a tested down step or a documented manual rollback.
- You have approval to change the target database.

## Steps

1. **Identify the migration state.** Run the tool command such as `alembic current`, `rails db:migrate:status`, or `python manage.py showmigrations`. → *Expect:* the database reports the migration that is currently applied.
2. **Confirm application compatibility.** Verify the running app version can operate after the rollback. → *Expect:* no deployed code depends only on the rolled-back schema.
3. **Take or verify a backup.** ⚠️ *Irreversible:* rollback can drop columns or data; confirm a current backup or snapshot before running it. → *Expect:* backup ID, timestamp, and restore path are recorded.
4. **Run rollback in staging or a restored copy.** Execute `alembic downgrade -1`, `rails db:rollback STEP=1`, or equivalent. → *Expect:* rollback exits 0 and the app works against the reverted schema.
5. **Schedule or announce production rollback.** Coordinate with the incident or release owner and pause conflicting deploys. → *Expect:* all responders know the database rollback is starting.
6. **Run the production rollback.** ⚠️ *Irreversible:* confirm database host, name, and migration target before executing the rollback command. → *Expect:* command exits 0 or fails without partial destructive work.
7. **Verify schema and app health.** Inspect schema state and run smoke tests. → *Expect:* database reports the expected migration version and app health checks pass.
8. **Document residual data work.** Note any data that could not be restored by the down migration. → *Expect:* follow-up tasks exist for cleanup or replay.

## Decision points

- Down migration drops data → restore from backup or write a forward repair instead of rolling back blindly.
- App code already deployed requires the new schema → roll back code first or deploy compatibility code.
- Migration partially applied → inspect actual schema before running automated rollback.
- Replicas lag or logical replication exists → coordinate rollback with replication health and subscribers.

## Failure modes & recovery

- **F1 Rollback command fails:** detect nonzero exit or SQL error → stop, inspect schema, and use a manual rollback reviewed by a database owner.
- **F2 Data loss discovered:** detect missing column/table data after rollback → restore from backup to a side database and copy back approved data.
- **F3 App breaks after rollback:** detect 5xx or missing-column errors → redeploy compatible code or roll forward the schema again.
- **F4 Migration history mismatch:** detect tool metadata disagrees with actual schema → repair migration metadata only after schema inspection and review.

## Verification

The migration tool reports the target previous version, schema inspection confirms the reverted objects, and `curl -fsS -o /dev/null -w '%{http_code}\n' https://app.example.com/healthz` returns `200` after rollback.

## Variations

- `Alembic`: use `alembic downgrade <revision>` and verify `alembic current`.
- `Rails`: use `rails db:rollback STEP=1` or `rails db:migrate:down VERSION=<version>`.
- `Django`: use `python manage.py migrate app_label previous_migration`.
- `Forward-only systems`: create a new corrective migration instead of using a down step.

## Safety & privacy

High risk because rollback can permanently remove data and break deployed code. Confirm backups, target database, and application compatibility before production rollback; restrict credentials to the database and environment being changed.
