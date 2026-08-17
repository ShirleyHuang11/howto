---
name: rename-a-file
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

Give an existing file a new name without changing its contents or location.

## Preconditions

- The file is visible in a file manager or on the desktop.
- You know the new name and should keep the file extension unless you intentionally need to change it.

## Steps

1. **Select the file.** Click the file once in File Explorer, Finder, or the desktop. → *Expect:* the file is highlighted.
2. **Start renaming.** [BRANCH: Windows | Mac] Windows: press `F2` or right-click and choose `Rename`; Mac: press `Return` or choose `File > Rename`. → *Expect:* the filename text becomes editable.
3. **Type the new name.** Replace only the name part and leave extensions such as `.pdf`, `.jpg`, or `.docx` unchanged unless needed. → *Expect:* the typed name appears in the edit box.
4. **Save the name.** Press `Enter` on Windows or `Return` on Mac. → *Expect:* the file remains in place with the new name.

## Decision points

- Extension is visible → keep it unchanged to preserve the file type.
- Name already exists in the folder → choose a unique name or add a short suffix such as `-copy`.

## Failure modes & recovery

- **F1 Name rejected:** invalid characters or a duplicate name appear → remove characters like `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|` and try again.
- **F2 File opens instead:** double-click opened the file → close it and single-click before renaming.
- **F3 Extension changed accidentally:** file icon or type changes → rename again and restore the original extension.

## Verification

The file appears in the same folder with the exact new filename and opens normally.

## Variations

- `windows`: `F2` is the fastest rename shortcut in File Explorer.
- `macos`: `Return` renames a selected file; `Command+O` opens it.

## Safety & privacy

Low risk. Do not remove extensions unless you understand the file type change, and avoid adding private information to filenames that may be shared.
