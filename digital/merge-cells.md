---
name: merge-cells
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

Merge adjacent spreadsheet cells into one larger cell for a title or label.

## Preconditions

- The cells to merge are adjacent.
- Any important values in the selected cells have been moved or copied elsewhere.

## Steps

1. **Select adjacent cells.** Drag across the cells that should become one cell. → *Expect:* the intended cells are highlighted.
2. **Confirm only one value matters.** Check whether more than the upper-left cell contains data. → *Expect:* no important data will be discarded by the merge.
3. **Merge the cells.** [BRANCH: Excel | Google Sheets] Excel: choose `Home > Merge & Center` or its dropdown; Google Sheets: choose `Format > Merge cells > Merge all`. → *Expect:* the selected cells become one larger cell.
4. **Adjust alignment.** Set horizontal and vertical alignment as needed. → *Expect:* the merged cell content appears in the intended position.

## Decision points

- Need sorting or filtering later → avoid merging inside data tables.
- Need centered title only → consider `Center Across Selection` in Excel instead of merging.
- Need to undo → use `Ctrl+Z` or `Command+Z`, or choose unmerge from the same menu.

## Failure modes & recovery

- **F1 Data lost warning:** detect a warning that only one value will be kept → cancel, move values out of the merge range, then retry.
- **F2 Sorting breaks:** detect sort or filter errors in a merged range → unmerge cells before sorting or filtering.
- **F3 Wrong merge direction:** detect one large block when row-by-row merge was intended → undo and choose the correct merge option.

## Verification

The selected adjacent cells display as one cell, and the visible content is the intended title or label.

## Variations

- `excel`: The `Merge & Center` dropdown includes merge across, merge cells, and unmerge cells.
- `google-sheets`: `Format > Merge cells` offers merge all, horizontally, vertically, and unmerge.

## Safety & privacy

Low risk. Merging can discard all selected values except the upper-left value, so move important data before merging.
