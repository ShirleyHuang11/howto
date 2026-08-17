---
name: eject-a-usb-drive-safely
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

Safely disconnect a USB drive after the computer has finished reading from or writing to it.

## Preconditions

- The USB drive is connected and visible.
- Any files on the drive that you edited have been saved and closed.

## Steps

1. **Close drive files.** Close documents, media, installers, and folder windows that are using the USB drive. → *Expect:* no open app is actively using files from the drive.
2. **Choose eject.** [BRANCH: Windows | Mac] Windows: click the system tray USB icon and choose `Eject`, or right-click the drive in File Explorer and choose `Eject`; Mac: click the eject button next to the drive in Finder or drag the drive icon to Trash/Eject. → *Expect:* the system starts unmounting the drive.
3. **Wait for confirmation.** Watch for `Safe to Remove Hardware` on Windows or for the drive icon to disappear on Mac. → *Expect:* the operating system indicates the drive is no longer mounted.
4. **Unplug the drive.** Pull the USB connector straight out without bending it. → *Expect:* the drive is physically disconnected.

## Decision points

- A copy progress window is still running → wait until it finishes before ejecting.
- The drive is encrypted → make sure it is locked or unmounted before unplugging.

## Failure modes & recovery

- **F1 Drive is busy:** detect by an error saying it is in use → close apps, wait a few seconds, and eject again.
- **F2 Eject option missing:** detect by no eject control → close all drive windows and use the file manager sidebar or system tray method.
- **F3 Pulled too early:** detect by warning or missing files later → reconnect the drive and check files; recopy from the source if needed.

## Verification

The drive icon disappears or the system says it is safe to remove, and the drive can be unplugged without warnings.

## Variations

- `windows`: Some drives use quick removal, but ejecting is still safest after writes.
- `macos`: External disks should disappear from Finder before unplugging.

## Safety & privacy

Low risk. Unplugging during writes can corrupt files, and lost removable drives can expose data if they are not encrypted.
