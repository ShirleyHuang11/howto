---
name: write-a-unit-test
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Add a focused unit test that proves one small behavior of a function, method, or component without relying on external services.

## Preconditions

- The project has a test framework installed, such as pytest, Jest, Vitest, JUnit, or Go's `testing` package.
- You can run the relevant test file locally.
- The behavior under test has a stable public interface.

## Steps

1. **Find the nearest existing test style.** Open tests near the code under test and copy naming, assertions, and fixture patterns. → *Expect:* the new test matches local conventions.
2. **Choose one behavior.** State the input, action, and expected output or state change. → *Expect:* the test has one clear reason to fail.
3. **Create or edit the test file.** [BRANCH: pytest | Jest] Add `def test_returns_total_for_valid_items():` or `test("returns total for valid items", () => { ... })`. → *Expect:* the test runner discovers the test by name.
4. **Arrange minimal data.** Build the smallest input needed, using factories or fixtures only when they make the setup clearer. → *Expect:* setup is deterministic and local to the test.
5. **Act once.** Call the function or unit under test exactly as production code would. → *Expect:* the result is captured in a variable or observable state.
6. **Assert the externally visible behavior.** Use precise assertions such as `assert total == Decimal("12.50")` or `expect(total).toBe(12.5)`. → *Expect:* a wrong implementation would fail the assertion.
7. **Run the single test.** Execute a targeted command such as `pytest tests/test_billing.py::test_returns_total_for_valid_items -q` or `npm test -- billing.test.ts -t "returns total"`. → *Expect:* the single test exits 0.
8. **Run the surrounding suite.** Run the relevant package or module tests. → *Expect:* existing tests still pass.

## Decision points

- Test needs network, database, or filesystem state → it is probably an integration test; isolate the unit or choose `engineering/write-an-integration-test`.
- Many assertions describe different behaviors → split into multiple tests.
- Expected value is hard to read → name intermediate variables or use a table-driven test.

## Failure modes & recovery

- **F1 Test not discovered:** detect `collected 0 items` or no matching Jest test → fix filename, function name, or test registration.
- **F2 Assertion follows implementation detail:** detect mocks of private methods or fragile internal state checks → assert public output or observable side effect instead.
- **F3 Flaky timing:** detect intermittent failures from sleeps or timers → inject a clock or use the framework's fake timers.
- **F4 Shared mutable state:** detect pass alone but fail with suite → reset globals, use fresh fixtures, or avoid mutation across tests.

## Verification

Run the targeted test command and then the local suite command, for example `pytest tests/test_billing.py::test_returns_total_for_valid_items -q && pytest tests/test_billing.py -q`; both commands exit 0 and the new test fails if the asserted behavior is intentionally broken.

## Variations

- `pytest`: use plain `assert` and fixtures for setup.
- `Jest or Vitest`: use `test`, `expect`, and fake timers for clock behavior.
- `Go`: write `func TestReturnsTotalForValidItems(t *testing.T)` and run `go test ./path`.

## Safety & privacy

Low risk because this is local test code. Keep fixtures synthetic, avoid real credentials or customer data, and do not weaken existing assertions to make the new test pass.
