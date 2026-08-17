---
name: wrap-text-in-a-cell
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Make long text display on multiple lines inside spreadsheet cells.

## Preconditions

- A spreadsheet contains cells with text longer than the column width.
- You can select the cells to format.

## Steps

1. **Select the text cells.** Highlight the cell or range with long text. → *Expect:* the intended cells are selected.
2. **Turn on text wrapping.** [BRANCH: Excel | Google Sheets] Excel: choose `Home > Wrap Text`; Google Sheets: choose `Format > Wrapping > Wrap`. → *Expect:* long text breaks onto multiple lines inside each cell.
3. **Adjust row height if needed.** Double-click the row boundary or use auto-fit. → *Expect:* all wrapped lines are visible.

## Decision points

- Text should stay on one line → use overflow or clip instead of wrap.
- Only one cell needs a manual line break → press `Alt+Enter` in Excel or `Ctrl+Enter` on Windows ChromeOS Sheets, `Command+Enter` on Mac Sheets.
- Wrapped rows are too tall → widen the column before wrapping.

## Failure modes & recovery

- **F1 Text still hidden:** detect clipped lines → auto-fit row height or widen the column.
- **F2 Layout becomes too tall:** detect rows crowding the sheet → narrow the selected range or use clip formatting.
- **F3 Wrong cells wrapped:** detect unrelated cells changed → undo and select only the intended range.

## Verification

The selected long text is visible on multiple lines within each cell, without spilling over adjacent cells.

## Variations

- `excel`: `Home > Format > AutoFit Row Height` can reveal wrapped lines.
- `google-sheets`: The toolbar wrapping icon offers overflow, wrap, and clip.

## Safety & privacy

Low risk. Wrapping may reveal text that was previously hidden by column width, so check screenshots and shared views.
