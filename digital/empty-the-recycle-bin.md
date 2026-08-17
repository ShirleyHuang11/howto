---
name: empty-the-recycle-bin
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Permanently remove files already placed in Trash or Recycle Bin to free space.

## Preconditions

- You have reviewed the bin for files you might need.
- You understand this action is difficult or impossible to undo without backups or recovery tools.

## Steps

1. **Open the bin.** [BRANCH: Windows | Mac] Windows: double-click `Recycle Bin`; Mac: click `Trash` in the Dock. → *Expect:* deleted items are listed.
2. **Review the contents.** Scan filenames, dates, and folders for anything you may need. → *Expect:* only unwanted files remain in the bin.
3. **Restore mistakes first.** Right-click any needed item and choose `Restore` on Windows or `Put Back` on Mac. → *Expect:* needed items leave the bin before emptying.
4. **Empty the bin.** [BRANCH: Windows | Mac] Windows: choose `Empty Recycle Bin`; Mac: choose `Finder > Empty Trash` or click `Empty`. ⚠️ *Irreversible:* confirm that everything remaining can be permanently removed. → *Expect:* a permanent deletion confirmation appears.
5. **Confirm deletion.** Choose `Yes`, `Empty Recycle Bin`, or `Empty Trash`. → *Expect:* the bin becomes empty.

## Decision points

- You are unsure about any file → restore it instead of emptying the bin.
- Files came from a cloud-synced folder → check the cloud service's recovery window before relying on local undo.

## Failure modes & recovery

- **F1 Needed file removed:** detect after emptying → restore from backup, cloud trash, version history, or professional recovery if critical.
- **F2 File will not delete:** detect by an error during emptying → close apps using the file, restart, and empty again.
- **F3 Permission prompt appears:** detect by administrator request → cancel unless you know the files are safe to remove.

## Verification

Trash or Recycle Bin opens empty, and available disk space has increased if large files were removed.

## Variations

- `windows`: Recycle Bin properties can set whether files bypass the bin; check this before relying on recovery.
- `macos`: Finder can remove items older than 30 days automatically if enabled.

## Safety & privacy

Medium risk because emptying the bin is a permanent deletion step. Review before confirming, especially on shared computers and synced folders.
