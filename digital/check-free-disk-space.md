---
name: check-free-disk-space
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

Check how much storage space remains on your computer or a connected drive.

## Preconditions

- The computer or drive is powered on and accessible.
- You know which disk or volume you want to check.

## Steps

1. **Open storage location.** [BRANCH: Windows | Mac] Windows: open File Explorer and choose `This PC`; Mac: choose `Apple menu > System Settings > General > Storage` or select a disk in Finder. → *Expect:* available disks or storage categories are visible.
2. **Read free space.** [BRANCH: Windows | Mac] Windows: look under the drive name or right-click the drive and choose `Properties`; Mac: read available storage in Settings or press `Command+I` on a selected disk. → *Expect:* used and free space values are shown.
3. **Check the correct drive.** Confirm you are reading the internal disk, external drive, or cloud-synced local storage you care about. → *Expect:* the disk name matches the target.
4. **Note whether action is needed.** Compare free space with the task requirement, such as an update, download, or copy. → *Expect:* you know whether there is enough space.

## Decision points

- Free space is very low → empty Trash or Recycle Bin, remove large unwanted files, or move files to another drive.
- Checking a phone or tablet from a computer → use the device's own storage settings for the most accurate number.

## Failure modes & recovery

- **F1 Wrong disk checked:** detect by an unfamiliar disk name or size → select the intended drive and read its properties.
- **F2 Values do not update:** detect by stale free space after deleting files → empty Trash or Recycle Bin and refresh the window.
- **F3 Cloud placeholder confusion:** detect by cloud files not using full local space → check the cloud app's local availability status.

## Verification

The intended disk shows a specific free-space amount, such as `42 GB available`, that can be compared with the needed amount.

## Variations

- `windows`: `Settings > System > Storage` shows internal storage categories.
- `macos`: `Apple menu > System Settings > General > Storage` summarizes system storage use.

## Safety & privacy

Low risk. Storage screens can reveal filenames, app names, and account-linked cloud services if shared.
