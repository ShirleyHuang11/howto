---
name: create-a-desktop-shortcut
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

Create a desktop shortcut or alias that opens a file, folder, app, or website without moving the original item.

## Preconditions

- You know the item or website the shortcut should open.
- You can edit the desktop.

## Steps

1. **Locate the target.** Find the app, file, folder, or website address you want the shortcut to open. → *Expect:* the target is visible or its URL is copied.
2. **Create the shortcut.** [BRANCH: Windows | Mac] Windows: right-click the target and choose `Show more options > Send to > Desktop (create shortcut)` or right-click Desktop and choose `New > Shortcut`; Mac: select the item and choose `File > Make Alias` or press `Option+Command` while dragging to the desktop. → *Expect:* a shortcut or alias appears.
3. **Name it clearly.** Rename the shortcut if the default name is unclear. → *Expect:* the desktop label identifies the target.
4. **Test it.** Double-click the shortcut or alias. → *Expect:* the intended item opens.

## Decision points

- Shortcut is for a website → use browser menu `More tools > Create shortcut` when available, or create a URL shortcut from the desktop.
- Original file is on removable storage → the shortcut works only when that storage is connected.

## Failure modes & recovery

- **F1 Shortcut opens nothing:** detect by an error about missing target → recreate it from the current target location.
- **F2 Original moved:** detect by shortcut failure after reorganizing files → update or recreate the shortcut.
- **F3 Created a copy instead:** detect by full file size and no shortcut marker → delete the copy if unwanted and create a shortcut again.

## Verification

The desktop shortcut or alias opens the intended target while the original item remains in its original location.

## Variations

- `windows`: Shortcuts usually have a small arrow badge and `.lnk` behind the scenes.
- `macos`: Aliases may show a small arrow badge and can be moved like normal files.

## Safety & privacy

Low risk. Desktop shortcuts can reveal private project names, apps, or websites during screen sharing.
