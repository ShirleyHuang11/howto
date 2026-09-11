---
name: seed-test-data
domain: engineering
subdomain: testing
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

You create deterministic test data that makes a test or suite repeatable without depending on production state, timing, or random external services.

## Preconditions

- The test framework and local dependencies are installed.
- You know whether the test data should live in factories, fixtures, SQL seeds, or API setup code.
- A disposable local or CI test database is available if persistence is involved.

## Steps

1. **Identify the exact state the test needs.** Read the code path and list only the rows, files, users, feature flags, queues, or clock values required for the assertion. → *Expect:* a short setup checklist with no production-only dependencies.
2. **Choose the narrowest seeding mechanism.** [pytest | Jest] prefer per-test factories or fixtures; [Rails | Django] prefer factories over global seed files unless the whole suite needs reference data. → *Expect:* the seed data is scoped to the tests that need it.
3. **Make identifiers deterministic.** Use fixed IDs, emails such as `user-001@example.test`, frozen timestamps, and seeded random generators such as `faker.Faker.seed(1234)`. → *Expect:* repeated test runs create the same logical records.
4. **Create data through stable APIs when behavior matters.** Use factories or application services when hooks, validations, or derived fields are part of the scenario; use bulk SQL only for inert reference rows. → *Expect:* records match real application invariants.
5. **Isolate and clean up the data.** Wrap each test in a transaction, truncate test tables between tests, or create unique namespaces per worker such as `TEST_RUN_ID`. → *Expect:* re-running the same test does not fail on duplicate keys or leaked state.
6. **Add one assertion that proves the seed exists.** Query the fixture, count rows, or assert the returned object has the expected fields before exercising the behavior under test. → *Expect:* a bad seed fails at setup with a clear error.
7. **Run the target test twice.** Use `pytest tests/test_orders.py::test_refund_flow -q` or `npm test -- refund-flow --runInBand` twice in a clean shell. → *Expect:* both runs exit 0 and produce the same assertions.

## Decision points

- Seed has complex invariants → create through factories or application services instead of raw inserts.
- Seed is large static reference data → load a versioned fixture file and validate checksums or row counts.
- Parallel tests mutate shared seed rows → copy the seed per worker or make it read-only.
- Test needs time-dependent state → freeze time with the framework clock helper instead of using the wall clock.

## Failure modes & recovery

- **F1 Duplicate key on rerun:** detect `UNIQUE constraint failed` or `duplicate key value violates unique constraint` → clean tables between tests or generate namespaced IDs from the test name.
- **F2 Hidden production dependency:** detect tests passing locally but failing in CI because a record is missing → move the required record into the test fixture.
- **F3 Flaky random data:** detect occasional validation failures from generated values → seed the generator and constrain values to valid ranges.
- **F4 Parallel worker collision:** detect failures only with `-n auto` or CI parallelism → partition test databases or include worker IDs in seeded data.

## Verification

`pytest -q tests/path/to/test_file.py --maxfail=1` or the equivalent focused test command exits 0 twice in a row from a clean test database, and a setup assertion confirms the expected seeded rows or objects exist.

## Variations

- `pytest`: put reusable setup in fixtures and prefer function scope unless setup cost forces module scope.
- `Jest`: create data in `beforeEach`, reset mocks with `jest.clearAllMocks()`, and reset persistent stores after each test.
- `Postgres`: use transaction rollback for isolation; use `TRUNCATE ... RESTART IDENTITY CASCADE` only against a disposable test database.
- `Rails/Django`: prefer FactoryBot or factory_boy for behavioral records and migrations for schema, not seed scripts.

## Safety & privacy

Medium risk because seed scripts can erase or overwrite data if pointed at the wrong database. Confirm the database name includes `test` or a CI worker suffix before destructive cleanup, never copy production personal data into fixtures, and use synthetic `.test` addresses and placeholder tokens.
