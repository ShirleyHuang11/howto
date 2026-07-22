---
name: recover-a-deleted-file
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 10min-2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A deleted file is restored from trash, recently deleted, cloud history, backup, or recovery tools with the best chance of preserving the original content.

## Preconditions

- You know the file name, type, approximate folder, and when it was deleted.
- You can stop using the affected drive or device if the file was deleted from local storage.

## Steps

1. **Stop writing to the drive.** If the file was on a hard drive, SSD, memory card, or USB drive, stop saving, installing, downloading, or editing there. → *Expect:* no new files are intentionally written to the affected storage.
2. **Check Trash or Recycle Bin.** Search by name, date deleted, or original location, then restore if found. → *Expect:* the file returns to its original folder or a chosen folder.
3. **Check app-level recently deleted.** [BRANCH: photos | notes | cloud docs] Look inside the app's Recently Deleted, Trash, Deleted Items, or Archive area. → *Expect:* the file or item appears with a restore option.
4. **Check cloud storage.** Search Google Drive, OneDrive, Dropbox, iCloud Drive, or SharePoint trash and account activity. → *Expect:* a restorable deleted copy or previous version is listed.
5. **Use version history.** For cloud documents, right-click or open File > Version history and restore or copy the needed version. → *Expect:* older versions show timestamps and editors.
6. **Check backups.** Use File History, Time Machine, Windows Backup, phone backup, NAS snapshots, or organization backup portals. → *Expect:* a dated backup contains the file.
7. **Use recovery tools carefully.** Install recovery software on a different drive, scan the affected drive read-only, and recover to a different destination. → *Expect:* candidate files are found without overwriting the original space.
8. **Verify and rename.** Open the recovered file, compare size and date, and save a clean copy with a clear name. → *Expect:* the recovered file opens with expected content.

## Decision points

- File was on an SSD with TRIM enabled → recovery tools may fail quickly, so backups and cloud history are more realistic.
- File was on a shared work drive → contact IT early because retention windows can be short but backups may exist.
- File contains legal or business-critical data → stop DIY recovery and use professional or organizational recovery support.

## Failure modes & recovery

- **F1 Trash already emptied:** detect no match in trash, recover by moving to cloud history, backup snapshots, or read-only recovery scans.
- **F2 Recovered file is corrupt:** detect open errors or garbled content, recover by trying another version, backup date, or deeper scan.
- **F3 Wrong account checked:** detect no cloud activity where expected, recover by checking other signed-in accounts and shared drives.
- **F4 Overwrite risk:** detect recovery software wants to save to the same drive, recover by choosing an external drive or different disk.

## Verification

The recovered file opens successfully and contains the expected recent content, not just the correct filename.

## Variations

- Windows: Recycle Bin, OneDrive recycle bin, File History, and Previous Versions are common paths.
- macOS: Trash, iCloud Drive Recently Deleted, and Time Machine are common paths.
- Phones: Photos and Files apps often keep deleted items for a limited number of days.

## Safety & privacy

⚠️ Recovery attempts can overwrite the deleted data if you keep using the same drive. Recovery tools also see private files, so use reputable software and avoid uploading sensitive drives to unknown services.
