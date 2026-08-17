---
name: sum-a-column
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

Calculate the total of numbers in one spreadsheet column.

## Preconditions

- A spreadsheet contains a column of numbers.
- There is an empty cell where the total can be placed.

## Steps

1. **Click the total cell.** Select the empty cell below or beside the numbers. → *Expect:* the intended total cell is active.
2. **Enter the sum formula.** Type `=SUM(B2:B20)`, replacing `B2:B20` with the actual number range. → *Expect:* the formula appears with the selected range highlighted.
3. **Confirm the total.** Press `Enter` or `Return`. → *Expect:* the total appears in the cell.
4. **Check the included cells.** Click the total cell and inspect the range in the formula bar. → *Expect:* the range covers all intended numbers and excludes labels or unrelated rows.

## Decision points

- Numbers may grow later → use a table total row in Excel or a broader range such as `=SUM(B2:B)` in Google Sheets.
- Blank rows interrupt the data → manually select the full range instead of relying on auto-selection.
- Need only visible filtered rows → use `=SUBTOTAL(109,B2:B20)` instead of `SUM`.

## Failure modes & recovery

- **F1 Missing rows:** detect a total that is too low → expand the formula range to include the omitted cells.
- **F2 Text numbers ignored:** detect numeric-looking values not included → convert them with `Data > Text to Columns` in Excel or `Format > Number > Number` in Google Sheets.
- **F3 Error in range:** detect the total cell shows an error → fix or remove error values inside the summed range.

## Verification

The total cell contains a `SUM` or `SUBTOTAL` formula whose range matches the intended column cells, and the displayed result changes when one included number changes.

## Variations

- `excel`: Select the cell below the column and choose `Home > AutoSum`.
- `google-sheets`: Select the cell below the column and choose `Insert > Function > SUM`.

## Safety & privacy

Low risk. Totals can drive financial or operational decisions, so verify the included range before sharing.
