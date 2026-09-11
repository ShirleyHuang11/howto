---
name: assert-an-exception-is-raised
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You add a test that proves invalid input or an expected failure path raises the correct exception, with the correct message or error code when that is part of the contract.

## Preconditions

- The project test framework runs locally.
- The expected exception type is part of the public contract or meaningful internal behavior.
- The test can trigger the failure without depending on network or production services.

## Steps

1. **Locate the failure contract.** Read the function, API handler, or caller that should reject the input and identify the exact exception class or error response. → *Expect:* one expected error type and one triggering condition are written down.
2. **Write the smallest failing call.** Build only the inputs needed to hit the branch, such as `parse_config({"port": "bad"})`. → *Expect:* running the call manually or in the test raises the intended failure.
3. **Use the framework exception assertion.** [pytest | Jest] write `with pytest.raises(ValueError, match="port"):` or `expect(() => parseConfig(input)).toThrow(/port/)`. → *Expect:* the test fails if no exception or the wrong exception is raised.
4. **Assert important details.** Check message text, error code, cause, or custom fields only when callers rely on them. → *Expect:* the test guards the observable contract without overfitting incidental wording.
5. **Prevent false positives.** Put only the single expression expected to raise inside the exception block. → *Expect:* setup code failures are not swallowed by the assertion.
6. **Run the focused test.** Use `pytest -q tests/test_config.py::test_bad_port_raises` or `npm test -- parse-config`. → *Expect:* the new test exits 0.

## Decision points

- Public API returns structured errors instead of exceptions → assert the HTTP status and JSON body.
- Async function throws → use `await pytest.raises` patterns where available or `await expect(promise).rejects.toThrow(...)`.
- Message text is localized or unstable → assert error code or exception type rather than exact prose.
- Broad exception such as `Exception` catches too much → narrow it to the specific class.

## Failure modes & recovery

- **F1 Assertion swallows setup failure:** detect a passing test when setup is placed inside the raise block → move setup outside and keep only the call inside.
- **F2 Wrong exception type:** detect failure such as `DID NOT RAISE` or a different stack trace → update the implementation or expected contract after reading callers.
- **F3 Brittle message match:** detect failures from harmless punctuation changes → match a stable phrase or assert a machine-readable error code.
- **F4 Async rejection not awaited:** detect test passes with an unhandled rejection warning → return or await the promise assertion.

## Verification

The focused test command, for example `pytest -q tests/test_config.py::test_bad_port_raises`, exits 0, and temporarily changing the input to a valid value makes the test fail with `DID NOT RAISE` or the framework equivalent.

## Variations

- `pytest`: use `pytest.raises(ExpectedError, match="stable phrase")` and inspect `exc_info.value` for custom fields.
- `unittest`: use `with self.assertRaisesRegex(ExpectedError, "stable phrase")`.
- `Jest/Vitest`: use `toThrow` for sync functions and `await expect(promise).rejects.toThrow(...)` for async functions.
- `Go`: idiomatic code usually returns `error`; assert `require.ErrorIs(t, err, target)` or `require.ErrorContains(t, err, text)`.

## Safety & privacy

Low risk because this is local test code. Keep fixtures synthetic, avoid asserting secrets in error messages, and do not broaden production error output just to make a test easier.
