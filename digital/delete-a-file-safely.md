---
name: delete-a-file-safely
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

Send an unwanted file to Trash or Recycle Bin without permanently deleting the wrong item.

## Preconditions

- The file is visible and you are confident it is no longer needed.
- You have checked whether the file is the only copy.

## Steps

1. **Select the file.** Click the file once and confirm its name, icon, and location. → *Expect:* only the intended file is highlighted.
2. **Delete to recoverable storage.** [BRANCH: Windows | Mac] Windows: press `Delete` or right-click and choose `Delete`; Mac: press `Command+Delete` or choose `File > Move to Trash`. → *Expect:* the file disappears from the folder.
3. **Use confirmation carefully.** If a prompt appears, read the filename before choosing `Yes`, `Move to Trash`, or `Delete`. → *Expect:* the prompt closes and the file is moved to Trash or Recycle Bin.
4. **Leave the bin intact briefly.** Do not empty Trash or Recycle Bin until you are sure the file is not needed. → *Expect:* the file can still be restored if necessary.

## Decision points

- File is in cloud storage → deleting may remove it from other devices too.
- File is on a USB drive or network share → deletion may be immediate or harder to recover.

## Failure modes & recovery

- **F1 Wrong file deleted:** detect by noticing the mistake before emptying the bin → open Trash or Recycle Bin, right-click the file, and choose `Restore` or `Put Back`.
- **F2 File will be permanently deleted:** detect by a warning mentioning permanent deletion → cancel and back up first if uncertain.
- **F3 File is in use:** detect by an error saying the file is open → close the app using it and retry.

## Verification

The file no longer appears in its original folder and is recoverable from Trash or Recycle Bin unless the system explicitly warned otherwise.

## Variations

- `windows`: `Shift+Delete` bypasses Recycle Bin; avoid it for safe deletion.
- `macos`: Finder's `Put Back` restores many trashed files to their original location.

## Safety & privacy

Low risk when using Trash or Recycle Bin. Permanent deletion and cloud-synced deletion can be harder to reverse, so confirm the filename before approving prompts.
