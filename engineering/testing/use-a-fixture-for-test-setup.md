---
name: use-a-fixture-for-test-setup
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

Create reusable test setup that makes tests shorter, deterministic, and isolated without hiding the behavior being asserted.

## Preconditions

- The test framework supports fixtures, setup hooks, factories, or helper builders.
- At least two tests need the same setup or teardown.
- The setup data can be synthetic and deterministic.

## Steps

1. **Identify repeated setup.** Find duplicated object creation, temporary resources, authenticated clients, or database rows. → *Expect:* the shared setup has a clear name and responsibility.
2. **Choose fixture scope.** [BRANCH: pytest | Jest] Use function scope by default; use module or session scope only for expensive immutable resources. → *Expect:* tests remain isolated unless sharing is intentional.
3. **Create the fixture or factory.** Add a `@pytest.fixture`, `beforeEach` helper, or test factory near related tests. → *Expect:* tests can request or call setup by name.
4. **Include teardown.** Use `yield` fixtures, `afterEach`, temporary directories, transactions, or cleanup callbacks. → *Expect:* resources are removed after the test.
5. **Refactor one test first.** Replace local setup with the fixture while keeping assertions visible. → *Expect:* the test still reads clearly and passes.
6. **Refactor the remaining tests.** Apply the fixture where it reduces duplication without creating mystery state. → *Expect:* duplicated setup shrinks and test intent is clearer.
7. **Run the affected tests repeatedly.** Execute the file twice. → *Expect:* both runs pass, proving cleanup and isolation.

## Decision points

- Setup differs meaningfully between tests → use a factory with explicit parameters instead of a single magical fixture.
- Fixture becomes large or hard to name → split it into smaller fixtures.
- Shared resource is mutable → use function scope or reset state between tests.

## Failure modes & recovery

- **F1 Hidden dependency:** detect tests that pass only in a certain order → make fixture dependencies explicit and reset state.
- **F2 Fixture too broad:** detect unused data in many tests → split setup into smaller fixtures or builders.
- **F3 Slow suite:** detect expensive setup per test → share immutable resources safely or use lighter fakes.
- **F4 Cleanup missing:** detect leftover files, rows, or containers → add teardown and verify repeated runs.

## Verification

Run the affected test file twice, for example `pytest tests/test_orders.py -q && pytest tests/test_orders.py -q` or `npm test -- orders.test.ts`; both runs exit 0 and no leftover temporary resources remain.

## Variations

- `pytest`: compose small fixtures and use `yield` for teardown.
- `Jest or Vitest`: use `beforeEach` for fresh setup and helper functions for builders.
- `JUnit`: use `@BeforeEach` and test data builders.

## Safety & privacy

Low risk because fixtures are test-only. Keep fixture data synthetic, avoid real credentials, and do not introduce broad global state that changes unrelated tests.
