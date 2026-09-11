---
name: seed-a-database-for-development
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Create deterministic, non-sensitive development data that lets the app run locally and tests exercise realistic workflows.

## Preconditions

- A local development database exists and migrations can run.
- Seed data requirements are known for login, permissions, and core entities.
- No production secrets or customer data will be copied into the seed.

## Steps

1. **Reset or migrate the local schema.** Run the project command, for example `npm run db:migrate` or `bin/rails db:migrate`. → *Expect:* the schema is current and the command exits 0.
2. **Use deterministic fixtures or factories.** Give records stable IDs, emails, and slugs where tests depend on them. → *Expect:* repeated seed runs produce the same logical records.
3. **Make seeds idempotent.** Use upserts or `find_or_create_by` patterns instead of blind inserts. → *Expect:* running the seed command twice does not create duplicates.
4. **Create representative roles and edge cases.** Include admin, normal user, empty account, and account with realistic child records. → *Expect:* common local flows work without manual setup.
5. **Keep secrets fake.** Use placeholders such as `dev-api-key-not-real` and hash passwords through the app's normal password code. → *Expect:* no real tokens or customer identifiers appear in seed files.
6. **Document the seed command in the script name.** Expose one command such as `npm run db:seed` or `make seed`. → *Expect:* a new developer can populate data without reading implementation files.
7. **Add a smoke test.** Query for required seed identities after seeding. → *Expect:* the local app can log in or load expected seeded records.

## Decision points

- Seeds are for tests → keep them minimal and isolated per test case.
- Seeds are for local demos → include richer scenarios but still fake data.
- IDs must be stable across services → use explicit UUIDs instead of autoincrement assumptions.
- Database reset is destructive → restrict reset commands to local or disposable environments.

## Failure modes & recovery

- **F1 Duplicate records:** detect unique-constraint failures on second seed run → replace inserts with upserts.
- **F2 Missing required flow:** detect local app errors after seeding → add the required parent and permission records.
- **F3 Production data leakage:** detect real emails, tokens, or names in seed files → remove them, rotate exposed secrets, and replace with generated fake data.
- **F4 Slow seeds:** detect local setup taking minutes for small data → reduce volume and move load testing data to a separate command.

## Verification

`npm run db:migrate && npm run db:seed && npm run db:seed` exits 0, and a query such as `SELECT email FROM users WHERE email = 'admin@example.test';` returns the expected development user.

## Variations

- `Rails`: use `bin/rails db:seed` and idempotent `find_or_create_by!`.
- `Django`: use fixtures with `loaddata` or a custom management command.
- `Prisma`: configure `prisma db seed` in `package.json`.

## Safety & privacy

Low risk when limited to local development. Guard reset commands with environment checks, never seed from production dumps without anonymization, and keep fake credentials clearly non-secret.
