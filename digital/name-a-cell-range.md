---
name: name-a-cell-range
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Give a spreadsheet cell range a reusable name for formulas.

## Preconditions

- A spreadsheet contains the range to name.
- You know a short name using letters, numbers, and underscores, such as `Sales_Q1`.

## Steps

1. **Select the range.** Drag across the cells that should be named. → *Expect:* the intended range is highlighted.
2. **Open named range tools.** [BRANCH: Excel | Google Sheets] Excel: click the Name Box left of the formula bar or choose `Formulas > Define Name`; Google Sheets: choose `Data > Named ranges`. → *Expect:* a field or panel for naming the range appears.
3. **Enter the range name.** Type a valid name such as `Sales_Q1` and confirm. → *Expect:* the name appears in the Name Box or named ranges panel.
4. **Use the name in a formula.** Enter a formula such as `=SUM(Sales_Q1)`. → *Expect:* the formula returns a result using the named range.

## Decision points

- Name contains spaces → replace spaces with underscores.
- Range should expand automatically → use an Excel table or update the named range after adding rows.
- Name conflicts with a cell address → choose a different name, such as `Q1_Sales` instead of `A1`.

## Failure modes & recovery

- **F1 Invalid name rejected:** detect the name will not save → start with a letter or underscore and remove spaces or punctuation.
- **F2 Wrong cells named:** detect formulas include wrong values → edit the named range reference.
- **F3 Name not recognized:** detect `#NAME?` → check spelling and whether the named range exists in this workbook or sheet.

## Verification

The named range appears in the workbook's named range list, and `=SUM(range_name)` or another formula using it returns the expected value.

## Variations

- `excel`: Use `Formulas > Name Manager` to edit or delete names.
- `google-sheets`: Named ranges are managed from the right-side `Named ranges` panel.

## Safety & privacy

Low risk. Descriptive range names may reveal business logic or sensitive categories in shared workbooks.
