---
name: run-tests-in-parallel
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

You configure a test suite to run with multiple workers while keeping results deterministic and isolated.

## Preconditions

- The suite passes serially.
- Test data, ports, temporary directories, and databases can be isolated per worker.
- The CI runner has enough CPU and memory for the chosen worker count.

## Steps

1. **Prove the serial baseline is green.** Run `pytest -q`, `npm test -- --runInBand`, or the project’s serial test command. → *Expect:* the suite exits 0 before parallel changes.
2. **Install or enable the parallel runner.** [pytest | Jest | Go] use `pytest-xdist`, Jest’s default workers, or Go’s built-in package parallelism. → *Expect:* the command recognizes worker flags such as `pytest -n 2 --version`.
3. **Choose a conservative worker count.** Start with `2` workers locally or half the available CI CPU. → *Expect:* memory and database limits are not saturated.
4. **Isolate mutable resources.** Use worker-specific database names, temp directories, ports, and cache keys such as `TEST_WORKER_ID` or `PYTEST_XDIST_WORKER`. → *Expect:* no worker writes to another worker’s state.
5. **Run parallel tests with failure detail.** Execute `pytest -q -n 2 --maxfail=1` or `npm test -- --maxWorkers=50%`. → *Expect:* the suite exits 0 or exposes a specific shared-state failure.
6. **Repeat to detect flakes.** Run the parallel command at least three times locally or in a CI retry branch. → *Expect:* the same result occurs every run.
7. **Update CI with the proven command.** Change only the test command and required setup for worker isolation. → *Expect:* the CI job passes with a shorter duration than the serial baseline.

## Decision points

- Tests require a single global service port → allocate dynamic ports or mark those tests serial.
- Database cleanup assumes one worker → create one database/schema per worker.
- Worker overhead exceeds savings → keep serial execution or parallelize only slow test groups.
- A small set of tests is unsafe in parallel → mark them with a serial tag and document why.

## Failure modes & recovery

- **F1 Shared fixture mutation:** detect order-dependent failures or changed fixture values → clone fixtures per test or make them immutable.
- **F2 Port already in use:** detect `EADDRINUSE` or bind failures → use port `0` or worker-specific port ranges.
- **F3 Database lock contention:** detect deadlocks or lock timeouts → use isolated schemas and avoid suite-wide transactions shared across workers.
- **F4 OOM under parallelism:** detect worker exits, SIGKILL, or `OOMKilled` → reduce `--maxWorkers` or split jobs across CI machines.
- **F5 Hidden order dependency:** detect failure only under shuffled or parallel order → add explicit setup and remove reliance on prior tests.

## Verification

The command configured for CI, such as `pytest -q -n auto` or `npm test -- --maxWorkers=50%`, exits 0 three consecutive times and CI reports the parallel test job green.

## Variations

- `pytest`: use `pytest-xdist` with `-n auto`; read `PYTEST_XDIST_WORKER` for per-worker resources.
- `Jest/Vitest`: tune `--maxWorkers`; use setup files to reset global mocks and databases.
- `Go`: package-level tests already run in parallel; add `t.Parallel()` only to isolated test functions.
- `Ruby/Rails`: use `parallel_tests` or Rails parallel testing with one database per worker.

## Safety & privacy

Medium risk because parallel tests can corrupt shared development databases or leak state. Run only against test resources, namespace worker data, and keep secrets out of worker logs and temp artifacts.
