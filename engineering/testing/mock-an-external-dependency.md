---
name: mock-an-external-dependency
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

Replace an external dependency in a test with a deterministic mock, stub, fake, or emulator while still asserting the contract your code relies on.

## Preconditions

- The dependency boundary is known, such as HTTP client, SDK, queue, clock, filesystem, or payment provider.
- The test framework supports mocks or the code allows dependency injection.
- You know which behavior of the dependency matters for the test.

## Steps

1. **Choose the narrow boundary to replace.** Mock the HTTP client or adapter layer, not deep internals throughout the codebase. → *Expect:* the test setup changes one dependency seam.
2. **Define realistic responses.** Copy the shape from provider documentation or recorded sandbox responses, removing secrets and personal data. → *Expect:* fields, status codes, and error shapes match production expectations.
3. **Install the mock in test setup.** [BRANCH: pytest | Jest] Use `monkeypatch`, `unittest.mock`, `jest.mock`, `vi.mock`, or a fake implementation. → *Expect:* the production network or SDK call is not executed.
4. **Exercise the code under test.** Call the service or function normally. → *Expect:* your code consumes the mocked dependency through the same public path.
5. **Assert both result and interaction.** Verify returned behavior and important calls, such as URL, method, idempotency key, or payload. → *Expect:* the test fails if the code calls the dependency incorrectly.
6. **Add an error-path mock.** Simulate timeout, 429, 500, or malformed response where relevant. → *Expect:* retry, fallback, or surfaced error behavior is covered.
7. **Prevent real external calls.** Configure the test runner to block network access when possible. → *Expect:* an accidental live call fails fast.
8. **Run the targeted tests.** Execute the test file. → *Expect:* tests pass offline and deterministically.

## Decision points

- Provider contract is complex → prefer a local emulator, contract test, or recorded fixture over handcrafted mocks.
- You need to test retry timing → inject a fake clock and backoff strategy.
- Mock duplicates too much implementation → move the boundary to a public adapter interface.

## Failure modes & recovery

- **F1 Mock not applied:** detect real network traffic or credential errors → patch the symbol where it is looked up by the code under test.
- **F2 Unrealistic fixture:** detect production bug not caught by tests → update mock payloads from current provider docs or sandbox responses.
- **F3 Over-specified calls:** detect frequent failures after harmless refactors → assert required contract fields, not every incidental argument.
- **F4 Hidden global state:** detect one test's mock affecting another → reset mocks in teardown or use per-test fixtures.

## Verification

Run the targeted test command with network disabled if available, such as `pytest tests/test_payments.py -q` or `npm test -- payments.test.ts`; it exits 0 and logs or network-blocking tools show no live external requests.

## Variations

- `HTTP`: use `responses`, `respx`, `nock`, `msw`, or WireMock.
- `Cloud SDK`: inject a fake client or use the provider's local emulator.
- `Time`: mock the clock through dependency injection or framework fake timers.

## Safety & privacy

Low risk when mocks use synthetic data. Never commit real provider tokens, redact recorded fixtures, and keep at least one higher-level contract or integration test for critical provider behavior.
