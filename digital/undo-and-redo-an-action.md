---
name: undo-and-redo-an-action
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

The most recent edit is reversed, and optionally restored, in a document or text editor.

## Preconditions

- A document, note, email draft, or text editor is open.
- At least one recent editable action has happened.

## Steps

1. **Undo the last action.** Press `Ctrl+Z` on Windows/Linux or `Command+Z` on Mac, or choose Edit > Undo. → *Expect:* the most recent change reverses.
2. **Repeat only if needed.** Press the same undo shortcut again for earlier actions. → *Expect:* each press steps back one edit.
3. **Redo if you went too far.** Press `Ctrl+Y` or `Ctrl+Shift+Z` on Windows/Linux, or `Command+Shift+Z` on Mac, or choose Edit > Redo. → *Expect:* the undone change returns.
4. **Stop at the correct state.** Read the affected sentence, paragraph, or object before continuing. → *Expect:* the document shows the intended version.

## Decision points

- The app shows an Undo drop-down history → choose the exact action if you need to reverse several edits at once.
- The action was saved or synced → undo may still work, but version history may be safer for larger reversions.

## Failure modes & recovery

- **F1 Undo is unavailable:** detect: the menu item is gray or shortcut does nothing → recover by checking version history, backups, or reopening the file's previous version.
- **F2 Too many actions undone:** detect: earlier wanted content disappears → recover by using Redo until the wanted content returns.
- **F3 Focus is in the wrong app:** detect: another app changes or nothing changes → recover by clicking inside the intended document and trying again.

## Verification

The unwanted action is no longer visible, or the redone action is visible again if redo was used.

## Variations

- `word`: Quick Access Toolbar arrows provide Undo and Redo.
- `google-docs`: File > Version history can recover older saved states when undo history is not enough.

## Safety & privacy

Undo and redo are low risk, but rapid repeated shortcuts can remove more work than intended. Pause and verify after each major change.
