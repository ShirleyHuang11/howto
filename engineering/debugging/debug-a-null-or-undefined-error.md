---
name: debug-a-null-or-undefined-error
domain: engineering
subdomain: debugging
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

You find why a value is unexpectedly null, undefined, or absent, then fix the source or handle the missing state explicitly.

## Preconditions

- You have the stack trace or failing test showing the null or undefined access.
- The relevant input data or request can be reproduced safely.
- Type checks, linting, or runtime assertions are available if the stack supports them.

## Steps

1. **Locate the failing dereference.** Find the line from the stack trace, such as `user.profile.name` or `order.customer!.email`. → *Expect:* the exact missing value is identified.
2. **Reproduce the failure with one command.** Run the focused test, route, or script that triggers the error. → *Expect:* the same null or undefined error appears.
3. **Trace the value backward.** Follow assignments, function returns, database reads, and API responses until the value first becomes missing. → *Expect:* there is a concrete producer of the null value.
4. **Classify the absence.** Decide whether missing is invalid input, legitimate optional state, stale data, or a broken invariant. → *Expect:* the fix direction is clear.
5. **Fix at the correct boundary.** Validate required inputs early, handle optional values with explicit branches, or repair the data invariant. → *Expect:* code no longer dereferences unknown state blindly.
6. **Add a regression test.** Include the missing-value case and the normal case. → *Expect:* the bug cannot return silently.
7. **Run type checks and tests.** Use `npm run typecheck && npm test` or `pytest -q`. → *Expect:* checks exit 0.

## Decision points

- Missing value is invalid user input → return a clear validation error near the boundary.
- Missing value is allowed by the domain → represent it in types and branch explicitly.
- Missing value comes from database drift → add a migration or cleanup after confirming scope.
- Non-null assertion caused the crash → remove it and make the invariant provable.

## Failure modes & recovery

- **F1 Fix masks real invariant break:** detect default values hiding corrupt state → fail early with a clear error instead of substituting nonsense.
- **F2 Optional chaining hides bad UX:** detect blank UI or missing action with no explanation → render an explicit empty or error state.
- **F3 Type checker still permits null:** detect `any`, loose config, or unchecked JSON → add schema validation or stricter types at the boundary.
- **F4 Production data contains unexpected nulls:** detect many affected rows → write a safe cleanup plan and backfill before enforcing constraints.

## Verification

The original reproduction command exits 0 after the fix, a regression test covers the missing-value case, and the project type-check command reports no nullable access error for the changed path.

## Variations

- `TypeScript`: enable or respect `strictNullChecks`; validate external JSON before trusting it.
- `Python`: assert optional values explicitly and use type checkers such as mypy or pyright where configured.
- `SQL`: distinguish nullable schema columns from application invariants and add `NOT NULL` only after backfilling.
- `React`: render loading, empty, and error states instead of dereferencing data before fetch completion.

## Safety & privacy

Medium risk when the fix touches validation or database constraints. Avoid logging raw payloads while tracing, and confirm data backfills on staging before changing production nullability.
