---
name: write-a-schema-migration
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You write and test a schema migration that changes database structure safely and can be applied through the project's normal release process.

## Preconditions

- The desired schema change and application compatibility requirements are known.
- Migration tooling is configured for the project.
- A local or test database can be reset or restored.
- For shared environments, backup and rollback expectations are clear.

## Steps

1. **Classify the change.** Decide whether it is additive, destructive, data backfill, index-only, or constraint-enforcing. → *Expect:* risk level and deployment sequence are understood.
2. **Choose a compatible migration pattern.** For required columns or renamed fields, use expand/migrate/contract rather than one breaking change. → *Expect:* old and new app versions can coexist during deployment.
3. **Generate the migration file.** Run the project command such as `alembic revision -m add_status_to_orders`, `rails generate migration AddStatusToOrders`, or `npx prisma migrate dev --name add-status`. → *Expect:* a new migration file exists in the expected directory.
4. **Write explicit schema operations.** Add table, column, index, constraint, or data statements with clear names and reversible down steps where supported. → *Expect:* migration code reflects the planned schema and names objects deterministically.
5. **Run the migration locally.** Execute `alembic upgrade head`, `rails db:migrate`, or the project equivalent. → *Expect:* the command exits 0 and the schema changes appear.
6. **Run rollback locally if supported.** Execute `alembic downgrade -1`, `rails db:rollback STEP=1`, or equivalent. → *Expect:* rollback exits 0 or the migration documents why it is irreversible.
7. **Run application tests.** Execute the relevant test suite or focused database tests. → *Expect:* tests pass against the migrated schema.
8. **Inspect generated SQL for shared environments.** Review locks, table rewrites, and online DDL support. → *Expect:* any production-risky operation has a mitigation plan.

## Decision points

- Migration removes or renames a used column → deploy code that stops using it first, then remove in a later release.
- Migration backfills many rows → do it in batches outside the schema transaction or through a background job.
- Migration adds a not-null constraint → add nullable column, backfill, validate, then enforce.
- Migration is irreversible → mark it explicitly and require backup/restore plan before production.

## Failure modes & recovery

- **F1 Migration fails locally:** detect command exits nonzero → fix SQL/tool syntax and rerun on a reset test database.
- **F2 Rollback fails:** detect downgrade/rollback error → add a valid reverse operation or document restore-from-backup as the only rollback.
- **F3 App incompatible with old schema:** detect tests fail before migration or during rolling deploy simulation → split into expand/contract steps.
- **F4 Production lock risk:** detect table rewrite or blocking DDL → use online DDL, concurrent indexes, or a maintenance window.

## Verification

The migration command exits 0 on a clean test database, schema inspection shows the intended change, rollback or documented restore path is validated, and relevant application tests pass.

## Variations

- `Alembic`: implement `upgrade()` and `downgrade()`, then test `alembic upgrade head` and `alembic downgrade -1`.
- `Rails`: use reversible migrations when possible and strong-migrations-style checks for production safety.
- `Prisma`: review generated SQL before applying to shared environments with `prisma migrate deploy`.
- `Django`: inspect SQL with `python manage.py sqlmigrate app migration`.

## Safety & privacy

Medium risk because migrations can break deployed code or lock tables. Avoid destructive changes in the same deploy as code changes, never include secrets in migration files, and require backup/approval before irreversible production migrations.
