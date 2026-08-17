---
name: format-cells-as-currency
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

Display selected spreadsheet numbers as currency.

## Preconditions

- A spreadsheet contains numeric amounts.
- You know which currency symbol should be shown.

## Steps

1. **Select the amount cells.** Drag across the cells that should show currency. → *Expect:* all intended amount cells are highlighted.
2. **Apply currency format.** [BRANCH: Excel | Google Sheets] Excel: choose `Home > Number Format > Currency`; Google Sheets: choose `Format > Number > Currency`. → *Expect:* the selected numbers display with a currency symbol and decimal places.
3. **Adjust the symbol if needed.** [BRANCH: Excel | Google Sheets] Excel: choose `Home > Number Format > More Number Formats`; Google Sheets: choose `Format > Number > Custom currency`. → *Expect:* the selected cells use the intended currency symbol.
4. **Check one formula cell.** Click a formatted cell and inspect the formula bar. → *Expect:* the underlying value remains numeric, without a typed currency symbol in the formula bar.

## Decision points

- Need accounting alignment → choose `Accounting` format instead of `Currency`.
- Need no cents → decrease decimal places from the number formatting controls.
- Need a nonlocal currency → use the custom currency or more formats menu.

## Failure modes & recovery

- **F1 Values become text:** detect formulas ignore the amounts → remove typed symbols, convert to numbers, and apply formatting again.
- **F2 Wrong currency symbol:** detect `$` where another symbol is needed → choose the correct symbol in custom currency settings.
- **F3 Rounding surprise:** detect displayed cents differ from source values → adjust decimal places or round with a formula such as `=ROUND(B2,2)`.

## Verification

The selected cells display the intended currency symbol, and calculations still treat the values as numbers.

## Variations

- `excel`: Keyboard shortcut `Ctrl+Shift+$` applies currency formatting on many keyboards.
- `google-sheets`: The toolbar currency button applies the spreadsheet locale's default currency.

## Safety & privacy

Low risk. Formatting does not change value precision, so clarify rounding before using displayed amounts in reports.
