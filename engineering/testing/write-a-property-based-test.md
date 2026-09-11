---
name: write-a-property-based-test
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Add a property-based test that checks an invariant across many generated inputs instead of only hand-picked examples.

## Preconditions

- The code has a clear invariant, round trip, ordering, idempotence, or safety property.
- A property-based testing library is available, such as Hypothesis, fast-check, ScalaCheck, or QuickCheck.
- Generated inputs can be constrained to valid and meaningful domains.

## Steps

1. **State the property.** Write the invariant in plain language, such as decoding an encoded value returns the original value. → *Expect:* the assertion is independent of specific examples.
2. **Choose input generators.** [BRANCH: Hypothesis | fast-check] Use strategies or arbitraries that produce valid values and important edge cases. → *Expect:* generated inputs match the domain contract.
3. **Add a few example tests if helpful.** Keep hand-picked examples for readability and known regressions. → *Expect:* future readers understand the intended behavior.
4. **Write the property test.** Use `@given(...)` in Hypothesis or `fc.assert(fc.property(...))` in fast-check. → *Expect:* the library runs many cases automatically.
5. **Assert the invariant.** Avoid duplicating the implementation; compare to a simpler oracle or reversible property. → *Expect:* failures indicate a real contract violation.
6. **Control runtime.** Set reasonable case counts, deadlines, or seeds according to project policy. → *Expect:* the test is reliable in CI.
7. **Run and inspect shrinking.** Execute the targeted test and read any minimal failing example. → *Expect:* passing tests exit 0; failing tests show a small reproducible input.
8. **Persist regressions.** If a generated case finds a bug, add it as a named example or regression test. → *Expect:* the bug remains covered even if generator settings change.

## Decision points

- Inputs require complex validity constraints → generate valid structures directly instead of filtering heavily.
- Property fails on ambiguous behavior → clarify the production contract before changing the test.
- Runtime is too high → reduce case count or split expensive integration checks from pure properties.

## Failure modes & recovery

- **F1 Too many discarded examples:** detect Hypothesis health check or slow filtering → improve strategies to generate valid inputs directly.
- **F2 Flaky property:** detect different failures from randomness or time → fix seeds only for diagnosis and remove nondeterministic dependencies.
- **F3 Assertion duplicates implementation:** detect same algorithm in test and code → use a simpler oracle or invariant.
- **F4 CI timeout:** detect long property runs → tune max examples and shrink expensive setup.

## Verification

Run the property test command, for example `pytest tests/test_codec_properties.py -q` or `npm test -- codec.property.test.ts`; it exits 0 with the configured number of generated cases, and any discovered counterexample is reproducible from the runner output.

## Variations

- `Hypothesis`: use strategies, `@example`, and settings for max examples and deadlines.
- `fast-check`: use arbitraries, `fc.property`, and recorded seeds for reproduction.
- `QuickCheck-style`: express invariants with generated values and minimal side effects.

## Safety & privacy

Low risk when generators use synthetic data. Do not generate real-looking secrets or personal identifiers unnecessarily, and keep runtime bounded so CI remains predictable.
