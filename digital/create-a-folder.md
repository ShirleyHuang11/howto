---
name: create-a-folder
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

Create a new empty folder in a chosen location.

## Preconditions

- You can access the location where the folder should be created.
- You know the folder name you want to use.

## Steps

1. **Open the destination.** Go to the desktop or open the parent folder in File Explorer or Finder. → *Expect:* the location where the folder will live is visible.
2. **Create the folder.** [BRANCH: Windows | Mac] Windows: press `Ctrl+Shift+N` or choose `New > Folder`; Mac: press `Shift+Command+N` or choose `File > New Folder`. → *Expect:* a new folder appears with its name selected.
3. **Name the folder.** Type the folder name and press `Enter` on Windows or `Return` on Mac. → *Expect:* the folder shows the chosen name.
4. **Open it if needed.** Double-click the folder to confirm it is empty or ready for files. → *Expect:* the folder opens with no unexpected contents.

## Decision points

- Folder should be shared or synced → create it inside the correct shared drive or cloud folder.
- Name already exists → choose a clearer unique name instead of merging contents by accident.

## Failure modes & recovery

- **F1 No permission:** creation fails or a lock message appears → choose a folder you can edit or ask the owner for access.
- **F2 Created in wrong place:** folder appears in the wrong parent → drag it to the correct location or cut and paste it.
- **F3 Name rejected:** the system refuses the name → remove unsupported characters and retry.

## Verification

The new folder exists at the intended location, has the intended name, and can be opened.

## Variations

- `windows`: Right-click blank space in File Explorer and choose `New > Folder`.
- `macos`: In Finder, use `File > New Folder` when the destination window is active.

## Safety & privacy

Low risk. Folder names may reveal project, client, or personal details if displayed in screenshots or shared drives.
