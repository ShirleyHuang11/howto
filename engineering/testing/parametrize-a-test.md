---
name: parametrize-a-test
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

Convert repeated tests for the same behavior into a parameterized test with clear cases and independently reported failures.

## Preconditions

- Multiple test cases share the same arrange, act, and assert shape.
- The test framework supports parameterized or table-driven tests.
- Each case has a meaningful expected result.

## Steps

1. **Group equivalent cases.** Identify examples that exercise the same behavior with different inputs. → *Expect:* each case fits the same assertion pattern.
2. **Name the cases.** Add IDs such as `empty_cart`, `single_item`, or `rounds_tax`. → *Expect:* failure output identifies which case failed.
3. **Create the parameter table.** [BRANCH: pytest | Jest | Go] Use `@pytest.mark.parametrize`, `test.each`, or a slice of structs. → *Expect:* inputs and expected values are visible together.
4. **Move shared logic into one test body.** Keep the action and assertion identical for each case. → *Expect:* the test body has no branch logic except what the production call needs.
5. **Run the parameterized test.** Execute the targeted test command. → *Expect:* the runner reports one result per case.
6. **Check failure readability.** Temporarily inspect or reason about a failing case name and assertion diff. → *Expect:* a future failure points to the bad input and expected value.
7. **Remove duplicate tests.** Delete only the covered duplicates after the parameterized test passes. → *Expect:* coverage remains while test code shrinks.

## Decision points

- Cases need different setup or assertions → keep them as separate tests.
- Many cases hide intent → split into multiple parameterized tests by behavior.
- Edge cases are generated rather than listed → consider property-based testing.

## Failure modes & recovery

- **F1 Unclear failure names:** detect failures named only by index → add explicit case IDs.
- **F2 Branchy test body:** detect `if case.type` inside the test → split into separate tests.
- **F3 Mutable shared cases:** detect one case affecting the next → copy data per case or use immutable literals.
- **F4 Removed unique coverage:** detect a deleted test had different assertions → restore it or add another parameterized group.

## Verification

Run the targeted command, such as `pytest tests/test_totals.py::test_totals_for_cases -q` or `npm test -- totals.test.ts -t "totals"`; it exits 0 and reports each parameter case separately.

## Variations

- `pytest`: use `@pytest.mark.parametrize(..., ids=[...])`.
- `Jest or Vitest`: use `test.each(cases)("$name", ...)`.
- `Go`: use table-driven tests with `t.Run(tc.name, func(t *testing.T) { ... })`.

## Safety & privacy

Low risk because this is test structure only. Do not collapse tests with different business meaning into one table, and keep case data synthetic and readable.
