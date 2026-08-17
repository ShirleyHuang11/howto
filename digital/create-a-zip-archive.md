---
name: create-a-zip-archive
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

Compress one or more files or folders into a `.zip` archive for sharing or storage.

## Preconditions

- The files or folders to compress are visible.
- You know where the zip archive should be created.

## Steps

1. **Select the items.** Click one item, or use `Ctrl+click` on Windows or `Command+click` on Mac to select multiple items. → *Expect:* every item to include is highlighted.
2. **Create the archive.** [BRANCH: Windows | Mac] Windows: right-click and choose `Compress to ZIP file` or `Send to > Compressed (zipped) folder`; Mac: right-click or Control-click and choose `Compress`. → *Expect:* a new `.zip` file appears in the same folder.
3. **Rename the archive.** Give the zip file a clear name and keep the `.zip` extension. → *Expect:* the archive has a useful filename.
4. **Open to inspect contents.** Double-click the zip or preview its contents without extracting if the system supports it. → *Expect:* the expected files are inside.

## Decision points

- Archive contains sensitive files → use encrypted transfer or an approved encrypted archive tool instead of a plain zip.
- Files are already compressed media → size reduction may be small, but packaging is still useful.

## Failure modes & recovery

- **F1 Missing item:** detect by inspecting the zip contents → recreate the archive with the full selection.
- **F2 Archive too large:** detect by upload or email limit → remove unneeded files or use cloud sharing.
- **F3 Zip will not open:** detect by extraction error → recreate it after closing files and checking disk space.

## Verification

The `.zip` archive exists, opens successfully, and contains exactly the selected files or folders.

## Variations

- `windows`: Newer Windows versions show `Compress to ZIP file`; older menus may show `Send to > Compressed (zipped) folder`.
- `macos`: Finder creates `Archive.zip` or a name based on the selected item.

## Safety & privacy

Low risk. Standard zip files are not private by default; anyone with the archive can read its contents unless encryption is used.
