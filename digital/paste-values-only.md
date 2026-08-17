---
name: paste-values-only
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

Paste spreadsheet results as fixed values without formulas or formatting.

## Preconditions

- A source cell or range is available to copy.
- A destination cell or range is ready to receive the pasted values.

## Steps

1. **Copy the source range.** Select the cells and press `Ctrl+C` or `Command+C`. → *Expect:* the source range has a moving border or copy highlight.
2. **Select the destination.** Click the top-left cell where the values should go. → *Expect:* the destination cell is active.
3. **Paste values only.** [BRANCH: Excel | Google Sheets] Excel: choose `Home > Paste > Paste Values` or press `Ctrl+Alt+V`, then `V`, then `Enter`; Google Sheets: choose `Edit > Paste special > Values only` or press `Ctrl+Shift+V` on Windows/Linux or `Command+Shift+V` on Mac. → *Expect:* displayed values appear in the destination cells.
4. **Inspect a pasted cell.** Click a destination cell and look at the formula bar. → *Expect:* the formula bar shows a fixed value, not a formula beginning with `=`.

## Decision points

- Need formulas preserved → use regular paste instead of values only.
- Need formatting preserved too → paste values first, then use format painter or paste formats separately.
- Pasting over existing data → confirm the destination range is replaceable before applying.

## Failure modes & recovery

- **F1 Formula pasted:** detect the formula bar starts with `=` → undo and use paste special values only.
- **F2 Wrong destination size:** detect values overflow into unwanted cells → undo, select the correct top-left cell, and paste again.
- **F3 Formatting changed unexpectedly:** detect number or date appearance changed → apply the desired number format after pasting values.

## Verification

The destination cells show the copied results, and their formula bars contain fixed values rather than formulas.

## Variations

- `excel`: Right-click the destination and choose the clipboard icon labeled `Values`.
- `google-sheets`: `Ctrl+Shift+V` or `Command+Shift+V` pastes values only in most browsers.

## Safety & privacy

Low risk. Pasting values breaks live formula links, so keep the formula source if future recalculation is needed.
