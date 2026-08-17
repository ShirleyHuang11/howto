---
name: select-all-text
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

All editable text or content in the active document, field, or page area is selected.

## Preconditions

- A document, text box, note, email draft, or editor is open.
- The active cursor is inside the area whose text should be selected.

## Steps

1. **Click inside the target area.** Place the cursor in the document body or text field you want to affect. → *Expect:* the insertion cursor appears in that area.
2. **Use Select All.** Press `Ctrl+A` on Windows/Linux or `Command+A` on Mac, or choose Edit > Select All. → *Expect:* the text or content in the active area is highlighted.
3. **Confirm the selection scope.** Look for whether only one field, the whole document, or the whole page is selected. → *Expect:* the highlighted area matches what you intend to change.
4. **Take the next action.** Copy, cut, delete, format, or replace the selected content. → *Expect:* the next action applies to the highlighted content.

## Decision points

- Only one paragraph should change → drag or use keyboard selection instead of Select All.
- A web page is selected instead of a text box → click inside the text box and press the shortcut again.

## Failure modes & recovery

- **F1 Wrong area selected:** detect: page controls or unrelated text highlight → recover by clicking inside the intended editor and using Select All again.
- **F2 Selection disappears:** detect: highlight vanishes before the next action → recover by repeating Select All immediately before acting.
- **F3 Accidental deletion:** detect: all content disappears after pressing a key → recover by pressing `Ctrl+Z` or `Command+Z`.

## Verification

Every intended piece of text is highlighted, and no unrelated area is included.

## Variations

- `word`: `Ctrl+A` or `Command+A` inside a table may first select the cell; press again to select more.
- `google-docs`: The shortcut selects the document body when the cursor is inside the document.

## Safety & privacy

Selecting all makes large edits easy. Verify the scope before typing, deleting, or applying formatting.
