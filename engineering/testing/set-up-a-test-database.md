---
name: set-up-a-test-database
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Provision a disposable database for automated tests, apply schema setup, and verify tests can read and write without touching shared or production data.

## Preconditions

- The application supports a configurable database URL or test settings file.
- A local database server, Docker, or managed CI service is available.
- Migrations or schema creation commands are documented.

## Steps

1. **Choose a disposable database name.** Use a clearly test-only name such as `app_test` or a per-run suffix. → *Expect:* the name cannot be confused with production or staging.
2. **Start the database service.** [BRANCH: Postgres | MySQL] Run `docker compose up -d postgres` or start the local service. → *Expect:* the service accepts connections on the configured test port.
3. **Create the test database and user.** For Postgres, run `createdb app_test` or an equivalent container command. → *Expect:* the database exists and is owned by a least-privilege test user.
4. **Set the test connection string.** Export `DATABASE_URL=postgres://app_test_user:password@localhost:5432/app_test` or use the framework's test config. → *Expect:* application test settings point to the test database only.
5. **Apply schema setup.** Run migrations or schema load, such as `alembic upgrade head`, `rails db:test:prepare`, or `npm run db:migrate:test`. → *Expect:* required tables and indexes exist.
6. **Run a connection smoke test.** Execute `psql "$DATABASE_URL" -c 'select 1;'` or the framework equivalent. → *Expect:* the command returns `1`.
7. **Run database-backed tests.** Execute the relevant test command. → *Expect:* tests can create, query, and clean up records.
8. **Reset between runs.** Use transactions, truncation, schema recreation, or container recreation. → *Expect:* rerunning tests starts from a clean state.

## Decision points

- Tests run in parallel → use isolated schemas or per-worker databases.
- Migrations are slow → load a schema snapshot, then run only pending migrations.
- Database features matter → use the same engine as production instead of SQLite if SQL behavior differs.

## Failure modes & recovery

- **F1 Wrong database URL:** detect production or staging hostname in `DATABASE_URL` → stop immediately and replace with a local disposable database.
- **F2 Migration failure:** detect missing extension, permission, or syntax errors → install extensions and grant test user privileges matching production needs.
- **F3 Dirty state between tests:** detect duplicate key or unexpected row failures → add transactional cleanup or recreate schema per run.
- **F4 Parallel collision:** detect workers clobbering each other's rows → use per-worker database names or unique schemas.

## Verification

Run `psql "$DATABASE_URL" -c 'select 1;'` or the engine equivalent and confirm it returns `1`, then run the database-backed suite, such as `pytest tests/integration -q` or `npm test -- db`; both commands exit 0 against the test database.

## Variations

- `Postgres`: use Docker, `createdb`, and transactional tests; create extensions in migrations.
- `MySQL`: create a test schema and run migrations with a least-privilege user.
- `SQLite`: acceptable for app logic only when production-specific SQL behavior is not under test.

## Safety & privacy

Medium risk because a misconfigured database URL can damage shared data. Use unmistakable test names, least-privilege users, disposable containers where possible, and never run destructive test setup against production or staging.
