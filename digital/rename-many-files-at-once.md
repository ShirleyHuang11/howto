---
name: rename-many-files-at-once
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

Rename a group of selected files with a shared base name or batch rename tool.

## Preconditions

- The files to rename are in one folder.
- You have reviewed the selection and can undo immediately if the result is wrong.

## Steps

1. **Open the folder.** Navigate to the files in File Explorer or Finder. → *Expect:* all target files are visible.
2. **Select the files.** Use `Ctrl+click` on Windows or `Command+click` on Mac for individual files, or `Shift+click` for a range. → *Expect:* only the files to rename are highlighted.
3. **Start batch rename.** [BRANCH: Windows | Mac] Windows: press `F2`, type a base name, and press `Enter`; Mac: right-click the selection and choose `Rename`. → *Expect:* a batch rename action begins.
4. **Choose the naming pattern.** [BRANCH: Windows | Mac] Windows: use one base name and let Windows add numbers; Mac: choose `Format`, `Replace Text`, or `Add Text`, then set the exact pattern. → *Expect:* the preview or selected files show the intended naming style.
5. **Apply the rename.** Confirm the rename action. → *Expect:* all selected files now share the new pattern.

## Decision points

- You need precise names with dates or sequence numbers → use Mac Finder's `Format` option or a dedicated renaming tool.
- The selected files include folders or unrelated items → cancel and refine the selection.

## Failure modes & recovery

- **F1 Wrong files renamed:** detect by unexpected names → immediately press `Ctrl+Z` on Windows or `Command+Z` on Mac in the same folder.
- **F2 Bad numbering order:** detect by numbers not matching the intended sequence → undo, sort the folder correctly, and rename again.
- **F3 Extensions changed:** detect by file types changing → undo or rename again while preserving extensions.

## Verification

Every intended file has the new naming pattern, no unintended file was renamed, and files still open normally.

## Variations

- `windows`: Windows renames selected files as `Name (1)`, `Name (2)`, and so on.
- `macos`: Finder's batch rename dialog can replace text, add text, or format names with numbers.

## Safety & privacy

Low risk. Batch operations can affect many files quickly; verify the selection before applying and use undo immediately if needed.
