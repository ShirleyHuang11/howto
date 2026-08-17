---
name: make-text-bold-or-italic
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

Selected text is formatted as bold, italic, or both.

## Preconditions

- A document or editable text field is open.
- The text to format is selectable.

## Steps

1. **Select the text.** Highlight the word, sentence, or paragraph to format. → *Expect:* the intended text is highlighted.
2. **Apply bold if needed.** Press `Ctrl+B` on Windows/Linux or `Command+B` on Mac, or click the Bold `B` button. → *Expect:* the selected text appears heavier.
3. **Apply italic if needed.** Press `Ctrl+I` on Windows/Linux or `Command+I` on Mac, or click the Italic `I` button. → *Expect:* the selected text appears slanted.
4. **Click away or move the cursor.** Place the cursor where you want to keep typing. → *Expect:* the formatted text remains bold, italic, or both.

## Decision points

- You are formatting a heading → use a heading style instead of manual bold when the text marks document structure.
- New typed text is also bold or italic → turn the same button or shortcut off before continuing.

## Failure modes & recovery

- **F1 No visible change:** detect: selected text looks unchanged → recover by checking that the editor supports rich text and the selection is active.
- **F2 Wrong text changed:** detect: nearby text is bold or italic unexpectedly → recover by undoing and selecting only the intended text.
- **F3 Formatting continues:** detect: new text keeps bold or italic → recover by pressing the same shortcut again to toggle it off.

## Verification

Only the intended text displays with bold, italic, or both, and surrounding text keeps its prior style.

## Variations

- `word`: Home > Font contains Bold and Italic controls.
- `google-docs`: Format > Text contains Bold and Italic options.

## Safety & privacy

This is low risk. In formal documents, avoid using manual emphasis where required templates specify exact styles.
