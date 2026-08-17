---
name: enter-a-formula-in-a-spreadsheet
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Enter a working formula in a spreadsheet cell and see the calculated result.

## Preconditions

- A spreadsheet is open in Excel or Google Sheets.
- You know which cells the formula should use.

## Steps

1. **Select the result cell.** Click the empty cell where the answer should appear. → *Expect:* the cell border shows it is active.
2. **Start the formula.** Type `=` followed by the formula, such as `=B2*C2` or `=SUM(B2:B10)`. → *Expect:* the formula text appears in the cell or formula bar.
3. **Confirm the formula.** Press `Enter` or `Return`. → *Expect:* the cell shows the calculated result instead of the formula text.
4. **Review the references.** Click the result cell and inspect the formula bar. → *Expect:* the formula bar still shows the formula beginning with `=`.

## Decision points

- Need a built-in function → type the function name after `=`, such as `=AVERAGE(C2:C20)`.
- Formula should use text → wrap literal text in quotes, such as `="Total: "&A2`.
- Formula should stay visible → choose `Formulas > Show Formulas` in Excel or `View > Show > Formulas` in Google Sheets.

## Failure modes & recovery

- **F1 Formula stored as text:** detect the cell shows `=B2*C2` instead of a result → set the cell format to General or Automatic, then re-enter the formula.
- **F2 Reference error:** detect `#REF!` → replace missing or deleted cell references with valid cells.
- **F3 Syntax error:** detect a parse warning or `#ERROR!` → check parentheses, commas, quotes, and whether your locale uses semicolons.

## Verification

The selected cell displays a calculated value, and the formula bar shows a formula beginning with `=` that references the intended cells.

## Variations

- `excel`: Use the formula bar above the grid when entering long formulas.
- `google-sheets`: Function help appears while typing a formula name.

## Safety & privacy

Low risk. Formulas can expose hidden assumptions in shared files, so review references before sharing results.
