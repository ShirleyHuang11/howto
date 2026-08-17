---
name: copy-and-paste-text
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

Selected text is duplicated into a new location without removing it from the original location.

## Preconditions

- A document, message, note, or text field is open.
- The text to copy is visible or selectable.

## Steps

1. **Select the text.** Drag across the text, or click at the start, hold `Shift`, and click at the end. → *Expect:* the selected text is highlighted.
2. **Copy the selection.** Press `Ctrl+C` on Windows/Linux or `Command+C` on Mac, or choose Edit > Copy. → *Expect:* the original text remains in place.
3. **Place the cursor.** Click where the copied text should appear. → *Expect:* the insertion cursor blinks at the target location.
4. **Paste the text.** Press `Ctrl+V` on Windows/Linux or `Command+V` on Mac, or choose Edit > Paste. → *Expect:* the copied text appears at the cursor.
5. **Check spacing.** Add or remove spaces or line breaks around the pasted text if needed. → *Expect:* the pasted text reads naturally in its new location.

## Decision points

- Target should match the surrounding style → paste normally first, then adjust formatting if needed.
- Target should be plain text only → use Edit > Paste and Match Style, `Ctrl+Shift+V`, or `Command+Shift+V` when available.

## Failure modes & recovery

- **F1 Nothing pastes:** detect: no text appears after paste → recover by copying again and confirming the text is highlighted first.
- **F2 Wrong text pastes:** detect: old clipboard content appears → recover by undoing, selecting the intended text, and copying again.
- **F3 Formatting looks wrong:** detect: font, size, or color does not match nearby text → recover by using paste without formatting or applying the surrounding style.

## Verification

The original text is still present, and the same text appears in the intended new location.

## Variations

- `word`: Home > Clipboard > Paste can show paste formatting options.
- `google-docs`: Edit > Paste special > Paste values only is available for some content types.

## Safety & privacy

Clipboard contents may be available to other apps or browser pages. Avoid copying passwords, private IDs, or sensitive text unless necessary.
