---
name: move-a-file
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

Move a file from one location to another so it exists only in the destination.

## Preconditions

- The file exists and is not currently being edited by another app.
- You know the destination folder.

## Steps

1. **Locate the file.** Open the folder containing the file in File Explorer or Finder. → *Expect:* the file is visible.
2. **Select the file.** Click the file once. → *Expect:* the file is highlighted.
3. **Cut the file.** [BRANCH: Windows | Mac] Windows: press `Ctrl+X` or right-click and choose `Cut`; Mac: press `Command+C` first because Finder moves during paste. → *Expect:* Windows dims the file, or Mac keeps it selected for moving later.
4. **Open the destination.** Navigate to the folder where the file should go. → *Expect:* the destination folder contents are visible.
5. **Paste as a move.** [BRANCH: Windows | Mac] Windows: press `Ctrl+V`; Mac: press `Option+Command+V` or choose `Edit > Move Item Here`. → *Expect:* the file appears in the destination.
6. **Check the original location.** Return to the source folder if needed. → *Expect:* the file is no longer in the original folder.

## Decision points

- You want the file in both places → use copy instead of move.
- Destination already has a file with that name → replace only if you mean to overwrite; otherwise rename first.

## Failure modes & recovery

- **F1 Paste unavailable:** the paste command is disabled → reselect the file and repeat the cut or copy step.
- **F2 Permission denied:** the system blocks the move → choose a writable destination or authenticate if appropriate.
- **F3 Wrong destination:** file landed in the wrong folder → move it again from that folder to the correct one.

## Verification

The file appears in the destination folder and no longer appears in the original folder.

## Variations

- `windows`: Dragging between folders on the same drive usually moves; dragging to another drive usually copies.
- `macos`: Hold `Command` while dragging to force a move between drives.

## Safety & privacy

Low risk. Moving files into shared or synced folders can expose them to others, so check the destination before moving sensitive files.
