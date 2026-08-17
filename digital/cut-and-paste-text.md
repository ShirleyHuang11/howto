---
name: cut-and-paste-text
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

Selected text is moved from one location to another in the same document or text editor.

## Preconditions

- A document or editable text field is open.
- You can select the text you want to move.

## Steps

1. **Select the text to move.** Drag across the text or use `Shift` with arrow keys. → *Expect:* only the text you want to move is highlighted.
2. **Cut the selection.** Press `Ctrl+X` on Windows/Linux or `Command+X` on Mac, or choose Edit > Cut. → *Expect:* the selected text disappears from its original location.
3. **Click the new location.** Place the cursor where the text should go. → *Expect:* the insertion cursor blinks at the target spot.
4. **Paste the text.** Press `Ctrl+V` on Windows/Linux or `Command+V` on Mac, or choose Edit > Paste. → *Expect:* the moved text appears at the new location.
5. **Repair surrounding punctuation.** Check spaces, commas, periods, and paragraph breaks around both locations. → *Expect:* the sentence or paragraph reads correctly after the move.

## Decision points

- You are unsure about removing the original → copy and paste instead, then delete the original after checking.
- The text is in a shared document → confirm that moving it will not disrupt someone else's edits.

## Failure modes & recovery

- **F1 Text disappears:** detect: the text is gone and not pasted → recover by pressing `Ctrl+Z` or `Command+Z`, then try again.
- **F2 Wrong text was cut:** detect: an unintended selection disappeared → recover by undoing immediately and selecting more carefully.
- **F3 Paste target is wrong:** detect: text appears in the wrong paragraph or field → recover by undoing and placing the cursor again.

## Verification

The selected text no longer appears in its original location and appears once at the intended new location.

## Variations

- `word`: Right-clicking selected text also offers Cut and Paste.
- `google-docs`: Browser security may require using keyboard shortcuts instead of menu paste.

## Safety & privacy

Cut text is stored on the clipboard until replaced. Be careful when moving sensitive text between apps or browser tabs.
