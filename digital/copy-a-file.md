---
name: copy-a-file
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

Create a second copy of a file in another location while keeping the original.

## Preconditions

- The source file is visible.
- You know where the copy should be placed.

## Steps

1. **Select the source file.** Click the file once in File Explorer, Finder, or the desktop. → *Expect:* the file is highlighted.
2. **Copy it.** [BRANCH: Windows | Mac] Windows: press `Ctrl+C` or right-click and choose `Copy`; Mac: press `Command+C` or choose `Edit > Copy`. → *Expect:* the file is stored on the clipboard.
3. **Open the destination folder.** Navigate to where the copy should go. → *Expect:* the destination folder is visible.
4. **Paste the copy.** [BRANCH: Windows | Mac] Windows: press `Ctrl+V`; Mac: press `Command+V`. → *Expect:* a copy of the file appears in the destination.
5. **Resolve name conflicts.** If prompted, choose `Keep both`, `Replace`, or rename the copy intentionally. → *Expect:* the destination contains the intended version.

## Decision points

- You need the file only in the new place → move it instead of copying.
- A same-named file exists → keep both unless you are certain replacement is correct.

## Failure modes & recovery

- **F1 Nothing pastes:** detect by no new file appearing → copy the source again and paste in the destination.
- **F2 Copied shortcut instead:** detect by a small arrow badge or tiny shortcut file → copy the original file from its real folder.
- **F3 Storage full:** detect by a disk-space warning → free space or choose another drive.

## Verification

The original file remains in its source location, and a readable copy exists in the destination.

## Variations

- `windows`: Holding `Ctrl` while dragging usually forces a copy.
- `macos`: Holding `Option` while dragging creates a copy.

## Safety & privacy

Low risk. Copies can multiply sensitive data, especially in shared, cloud-synced, or removable drives.
