---
name: design-a-database-schema
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You design a database schema that represents the product model accurately, enforces important constraints, and can evolve through migrations.

## Preconditions

- Product requirements and core workflows are understood.
- Expected data volume, access patterns, and retention needs are known at least roughly.
- The target database engine is selected.
- Naming conventions and migration tooling for the codebase are known.

## Steps

1. **Model the entities and relationships.** Identify nouns, ownership, cardinality, and lifecycle states. → *Expect:* a short entity list with one-to-one, one-to-many, or many-to-many relationships called out.
2. **Choose primary keys and identifiers.** Decide between UUIDs, bigint sequences, or natural keys, and document external identifiers separately. → *Expect:* every table has a stable primary key plan.
3. **Define columns and types.** Pick precise types such as `timestamptz`, `numeric`, `jsonb`, or constrained enums where appropriate. → *Expect:* columns have types, nullability, defaults, and meaning.
4. **Add integrity constraints.** Specify foreign keys, unique constraints, check constraints, and not-null constraints. → *Expect:* the schema rejects invalid states the application should never allow.
5. **Plan indexes from queries.** Map read paths to indexes, especially foreign keys, lookup fields, and common filters. → *Expect:* each nontrivial query has a matching index strategy or a reason it does not need one.
6. **Design for migrations.** Split risky changes into expand/migrate/contract phases when adding required columns or changing existing data. → *Expect:* the first migration is deployable without breaking the current app version.
7. **Create the migration in the project tool.** Use a command such as `rails generate migration`, `alembic revision -m`, or `npx prisma migrate dev --name <name>`. → *Expect:* migration files contain the planned schema changes.
8. **Apply to a local or test database and inspect.** Run the migration and schema inspection commands. → *Expect:* tables, constraints, and indexes exist as designed.

## Decision points

- The relationship is many-to-many with attributes → create an explicit join table with its own primary key or composite uniqueness.
- A field has a small stable set of values → use a constrained enum/check; if values change often, use a lookup table or text with validation.
- A column will become required on a large existing table → add nullable, backfill, then enforce not-null in a later migration.
- Query pattern is unclear → avoid speculative indexes until a real query or performance target exists.

## Failure modes & recovery

- **F1 Missing constraint:** detect invalid duplicate or orphan data possible → add database constraints, not only app validation.
- **F2 Over-normalization:** detect common reads needing many joins with no integrity benefit → denormalize selectively with clear ownership.
- **F3 Migration blocks writes:** detect long locks or timeout in staging → split the migration, add indexes concurrently, or backfill in batches.
- **F4 Type mismatch:** detect money, time, or IDs stored imprecisely → switch to appropriate numeric, timestamp, or identifier types before production use.

## Verification

The migration applies cleanly to a fresh test database, schema inspection shows the intended tables/constraints/indexes, and a small fixture insert script proves valid rows insert while invalid rows fail with constraint errors.

## Variations

- `Postgres`: prefer `timestamptz`, `numeric` for exact decimals, `jsonb` only for intentionally flexible data, and concurrent indexes for large live tables.
- `MySQL`: choose `utf8mb4`, verify storage engine supports foreign keys, and account for online DDL limits.
- `Prisma/Rails/Django/Alembic`: generate migrations through the framework but inspect the actual SQL before applying to shared environments.

## Safety & privacy

Medium risk because schema choices shape long-term correctness and migrations can break services. Avoid storing unnecessary personal data, enforce tenant boundaries, review destructive changes, and test migrations against realistic data before production.
