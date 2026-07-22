---
name: zip-and-unzip-files
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min-15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Files are compressed into a ZIP archive or extracted from one into a normal folder you can use.

## Preconditions

- The files or ZIP archive are on your device, and you have permission to read and write in the folder.
- Enough free storage for both the archive and extracted copy.

## Steps

1. **Collect the source files.** Put the files in one folder and remove temporary items you do not want to share. → *Expect:* the folder contains only the intended files.
2. **Compress the folder.** [BRANCH: Windows | macOS | mobile] Windows: right-click > Compress to ZIP file. macOS: right-click > Compress. Mobile: use Files or a trusted file manager. → *Expect:* a `.zip` file appears beside the folder.
3. **Rename the archive clearly.** Use a short name without odd punctuation if it will be emailed or uploaded. → *Expect:* the ZIP name describes the contents and ends in `.zip`.
4. **Add a password only if needed.** Use 7-Zip, Keka, WinZip, or similar when the built-in tool lacks encryption. → *Expect:* opening the ZIP prompts for the password on another device.
5. **Share the ZIP.** Attach or upload the archive, and send any password in a separate channel. → *Expect:* the destination receives one archive instead of many loose files.
6. **Extract a ZIP before editing.** Double-click or right-click Extract All, then choose a destination folder. → *Expect:* a normal folder appears with the files inside.
7. **Avoid the already-extracted trap.** If you see both `Project.zip` and a `Project` folder, edit files in the folder, not inside the ZIP preview window. → *Expect:* saved edits remain visible after closing and reopening the file.
8. **Delete extras only after checking.** Remove duplicate archives or extracted folders once you know which copy is current. → *Expect:* storage is cleaned without losing the working copy.

## Decision points

- Sending many small files → ZIP keeps them together and preserves folders.
- Sending one huge video → ZIP may not shrink it much, because many media formats are already compressed.
- Sharing confidential files → use encrypted ZIP or a secure file-sharing service with access controls.

## Failure modes & recovery

- **F1 Cannot open archive:** detect an error about corruption or unsupported method, recover by downloading again or asking for a standard ZIP instead of RAR or 7z.
- **F2 Password fails:** detect repeated password prompts, recover by checking capitalization, keyboard layout, and whether the sender used a different archive password.
- **F3 Missing files:** detect an empty or partial extracted folder, recover by re-extracting to a new folder and checking whether the ZIP finished downloading.
- **F4 Edits disappear:** detect changes made from inside a ZIP preview, recover by extracting first and redoing the edits in the extracted folder.

## Verification

The ZIP opens on another device or the extracted folder contains every expected file and can be edited normally.

## Variations

- Windows: Extract All creates a folder and can show it after extraction.
- macOS: Archive Utility extracts into a same-named folder automatically.
- Cloud drives: some services unzip in the browser, but large archives may time out and need desktop extraction.

## Safety & privacy

ZIP files can hide many files, so inspect archives from unknown senders before opening content. Password-protected ZIPs protect contents only if the password is strong and shared separately.
