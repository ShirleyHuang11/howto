---
name: debug-an-off-by-one-error
domain: engineering
subdomain: debugging
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

You identify and fix a boundary error where a loop, range, page, date, or index includes one too many or one too few items.

## Preconditions

- The incorrect boundary behavior can be reproduced with a test, query, or UI flow.
- You know the intended inclusive or exclusive semantics.
- Representative boundary cases are available or can be created.

## Steps

1. **Write the failing boundary in concrete numbers.** Example: page 2 starts at item 21 but should start at item 20, or date range excludes the end day. → *Expect:* the expected and actual boundaries are explicit.
2. **Add focused boundary cases.** Test zero, one, exact page size, page size plus one, start date, and end date where relevant. → *Expect:* at least one test fails for the current bug.
3. **Inspect indexing conventions.** Identify whether the code uses zero-based indexes, one-based page numbers, inclusive ends, or half-open intervals. → *Expect:* one convention is chosen for each boundary.
4. **Trace the conversion point.** Find where user-facing numbers become internal indexes, offsets, or ranges. → *Expect:* the incorrect `+1`, `-1`, `<`, or `<=` operation is located.
5. **Fix the conversion or comparison.** Prefer half-open intervals such as `[start, end)` internally when the stack allows it. → *Expect:* boundary tests match the intended behavior.
6. **Check adjacent features.** Inspect pagination links, totals, empty states, and date formatting. → *Expect:* the fix does not shift another boundary.
7. **Run focused and related tests.** Use `pytest -q tests/test_pagination.py` or equivalent. → *Expect:* all boundary and related tests exit 0.

## Decision points

- User input is one-based but arrays are zero-based → convert once at the boundary and keep internals zero-based.
- Date range uses whole days → use timezone-aware start-inclusive and next-day-exclusive end.
- SQL pagination is wrong → verify `LIMIT` and `OFFSET` from page and page size.
- Last page is empty → clamp page number or return a clear empty result depending on API contract.

## Failure modes & recovery

- **F1 Fix moves the bug:** detect first page passes but last page fails → add tests for both ends.
- **F2 Timezone boundary drift:** detect date tests fail in CI timezone → use timezone-aware datetimes and fixed timezone in tests.
- **F3 Mixed inclusive semantics:** detect API and UI disagree on totals → document and centralize range conversion.
- **F4 Empty collection crash:** detect index errors with zero items → add explicit empty case handling.

## Verification

The focused boundary test command exits 0, and tests cover at least the empty, single-item, exact-boundary, and boundary-plus-one cases for the changed logic.

## Variations

- `pagination`: test first page, second page, last page, and beyond-last page.
- `dates`: prefer half-open intervals in storage queries, such as `created_at >= start AND created_at < next_day`.
- `arrays`: check loop condition and slice end indexes.
- `UI`: verify visible item counts and navigation controls with an automated browser test.

## Safety & privacy

Low risk for local logic changes, but boundary bugs in billing, access windows, or retention policies can have higher impact. Use synthetic fixtures and get domain review when the boundary affects money, permissions, or deletion.
