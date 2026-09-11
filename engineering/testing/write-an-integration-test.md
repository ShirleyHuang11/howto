---
name: write-an-integration-test
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [engineering/run-the-test-suite]
status: draft
last_verified: 2026-09-11
---

## Goal

Add a test that verifies two or more real components work together, such as a service plus database, queue, cache, or filesystem.

## Preconditions

- The integration boundary is intentional and cannot be proven by a smaller unit test.
- Test services can run locally or in CI with disposable data.
- The suite runs: `engineering/run-the-test-suite`.

## Steps

1. **Define the integration contract.** Identify the real components included and the external systems excluded. → *Expect:* the test scope is clear and bounded.
2. **Provision disposable dependencies.** [BRANCH: Docker Compose | Testcontainers] Start services with `docker compose up -d postgres` or create them from test code. → *Expect:* health checks or connection probes succeed.
3. **Create isolated test data.** Use transactions, unique schemas, temporary directories, or per-test IDs. → *Expect:* repeated runs do not collide.
4. **Write the integration test.** Exercise production wiring, not mocked internals, for example repository code against a real test database. → *Expect:* the test fails if the components stop speaking the same contract.
5. **Assert durable outcomes.** Check database rows, emitted messages, files, or returned API responses. → *Expect:* assertions verify observable state after the operation.
6. **Add cleanup.** Roll back transactions, truncate tables, delete queues, or remove temporary files. → *Expect:* a second run starts from a clean state.
7. **Run the test repeatedly.** Execute the targeted command at least twice, such as `pytest tests/integration/test_orders.py -q`. → *Expect:* both runs exit 0.
8. **Add CI service configuration.** Configure CI containers or managed test services. → *Expect:* the integration test passes in CI, not only locally.

## Decision points

- External dependency is slow or billed → replace it with a local emulator or contract test.
- Test needs production-like migrations → run migrations against a disposable database before assertions.
- Cleanup is complex → prefer transaction rollback or fresh containers over manual deletion.

## Failure modes & recovery

- **F1 Service not ready:** detect connection refused at test start → wait on a health endpoint or use Testcontainers readiness checks.
- **F2 State leakage:** detect pass alone but fail after another test → isolate data with unique IDs or transactional rollback.
- **F3 Migration mismatch:** detect missing table or column → run test migrations before the test or use the same setup as CI.
- **F4 CI-only timeout:** detect local pass but CI timeout → reduce service startup work, add readiness checks, or increase CI service resources.

## Verification

Run the targeted integration command twice, for example `pytest tests/integration/test_orders.py -q && pytest tests/integration/test_orders.py -q`; both runs exit 0. The CI job that provisions the same test service also passes.

## Variations

- `Postgres`: use a disposable database and wrap each test in a transaction when possible.
- `Kafka or queues`: use local containers and unique topic or queue names per test run.
- `Filesystem`: use framework temporary-directory fixtures instead of repository paths.

## Safety & privacy

Medium risk because integration tests touch real services or databases. Use only disposable local or CI resources, never production credentials, and make cleanup idempotent so failed tests do not poison later runs.
