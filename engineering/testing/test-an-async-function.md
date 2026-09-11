---
name: test-an-async-function
domain: engineering
subdomain: testing
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

Write a deterministic test for asynchronous code that awaits real completion and fails on rejected promises, exceptions, or timeouts.

## Preconditions

- The test framework supports async tests or an async plugin.
- The async function exposes an awaitable promise, coroutine, task, callback wrapper, or event.
- External timing and network dependencies can be controlled or mocked.

## Steps

1. **Confirm the async test pattern.** [BRANCH: pytest | Jest] Use `pytest.mark.asyncio` or `async def`, and in Jest use `test("...", async () => { ... })`. → *Expect:* the runner waits for the async body.
2. **Arrange deterministic dependencies.** Mock network calls, inject a fake clock, or use an in-memory queue. → *Expect:* the test does not depend on wall-clock sleeps or live services.
3. **Await the operation.** Call `result = await function_under_test(...)` or `await expect(promise).resolves...`. → *Expect:* exceptions surface as test failures.
4. **Assert the completed result.** Check returned values, emitted events, persisted state, or calls after the await. → *Expect:* assertions run only after async work finishes.
5. **Test rejection or cancellation when relevant.** Use `pytest.raises` around `await` or `await expect(promise).rejects...`. → *Expect:* expected async errors are asserted, not swallowed.
6. **Avoid arbitrary sleeps.** Replace `sleep(1)` with awaiting a task, polling with timeout, fake timers, or event synchronization. → *Expect:* the test is fast and stable.
7. **Run the test repeatedly.** Execute the targeted async test multiple times. → *Expect:* each run exits 0 without unhandled rejection warnings.

## Decision points

- Code launches background tasks → expose a completion signal or inject a task supervisor for tests.
- Timer behavior is central → use fake timers and advance time explicitly.
- Async function touches database or queue → make it an integration test with disposable resources.

## Failure modes & recovery

- **F1 Test passes without awaiting:** detect runtime warning about unawaited coroutine or unhandled promise → mark the test async and await the call.
- **F2 Timeout:** detect test runner timeout → replace sleeps with readiness signals and inspect deadlocks.
- **F3 Event loop conflict:** detect `event loop is closed` or nested loop errors → use the framework's async plugin correctly and avoid creating global loops.
- **F4 Swallowed rejection:** detect warning after test completion → return or await every promise and fail on unhandled rejections.

## Verification

Run the targeted async test repeatedly, for example `pytest tests/test_worker.py::test_processes_message -q && pytest tests/test_worker.py::test_processes_message -q` or `npm test -- worker.test.ts -t "processes message"`; every run exits 0 with no unhandled async warnings.

## Variations

- `pytest`: use `pytest-asyncio` or AnyIO fixtures.
- `Jest or Vitest`: return or await promises and use fake timers for scheduled work.
- `Go`: synchronize goroutines with contexts, channels, and timeouts instead of sleeps.

## Safety & privacy

Low risk when async dependencies are controlled. Use synthetic data, avoid live network calls, and set bounded timeouts so a hung async test cannot stall CI indefinitely.
