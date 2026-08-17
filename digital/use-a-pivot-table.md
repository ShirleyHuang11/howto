---
name: use-a-pivot-table
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create a simple pivot table that summarizes spreadsheet rows by category.

## Preconditions

- The source data has a header row and no blank header names.
- At least one column contains categories and one column contains numeric values.

## Steps

1. **Select the source data.** Click inside the data table or highlight the full range. → *Expect:* the intended source data is active.
2. **Insert the pivot table.** [BRANCH: Excel | Google Sheets] Excel: choose `Insert > PivotTable`; Google Sheets: choose `Insert > Pivot table`. → *Expect:* a pivot table setup dialog appears.
3. **Choose the destination.** Place the pivot table on a new worksheet or new sheet. → *Expect:* an empty pivot table area opens with a field list or editor.
4. **Add a row field.** Drag or add the category column to Rows, such as `Region` or `Product`. → *Expect:* category names appear down the pivot table.
5. **Add a value field.** Drag or add a numeric column to Values, such as `Sales`. → *Expect:* summarized numbers appear beside the categories.
6. **Set the summary function.** Choose `SUM`, `COUNT`, or `AVERAGE` as needed. → *Expect:* the value heading shows the selected summary type.

## Decision points

- Need counts instead of totals → summarize the value field by `COUNT`.
- Need a second breakdown → add another category to Columns or Rows.
- Source data changes later → refresh the pivot table in Excel or check that Google Sheets updates the source range.

## Failure modes & recovery

- **F1 Missing fields:** detect a blank or unnamed field in the editor → add headers to every source column.
- **F2 Numbers counted instead of summed:** detect the value field says `COUNT` unexpectedly → convert source values to numbers and change summarize by to `SUM`.
- **F3 New rows excluded:** detect recent records missing → expand the source range or convert the source to a table.

## Verification

The pivot table lists categories from the chosen row field and shows the selected summary calculation for the intended numeric field.

## Variations

- `excel`: Use `PivotTable Analyze > Refresh` after source data changes.
- `google-sheets`: Use the Pivot table editor to add Rows, Columns, Values, and Filters.

## Safety & privacy

Low risk. Pivot tables can reveal aggregated patterns from sensitive records, so check sharing permissions and included fields.
