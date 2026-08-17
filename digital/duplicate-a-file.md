---
name: duplicate-a-file
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

Make a copy of a file in the same folder so you can edit or rename it separately.

## Preconditions

- The file is visible in a folder or on the desktop.
- There is enough storage space for another copy.

## Steps

1. **Select the file.** Click the file once. → *Expect:* the file is highlighted.
2. **Duplicate it.** [BRANCH: Windows | Mac] Windows: press `Ctrl+C` then `Ctrl+V`; Mac: press `Command+D` or choose `File > Duplicate`. → *Expect:* a second file appears in the same folder.
3. **Rename the duplicate if needed.** Give the copy a clear name that distinguishes it from the original. → *Expect:* the duplicate has a unique filename.
4. **Open the duplicate if needed.** Double-click the copy, not the original. → *Expect:* the duplicate opens and can be edited independently.

## Decision points

- You want the copy in a different folder → use copy-a-file instead.
- The file is large → check free disk space before duplicating.

## Failure modes & recovery

- **F1 Duplicate not created:** detect by no second file → repeat the copy and paste or duplicate command.
- **F2 Edited original by mistake:** detect by original filename in the app title → close without saving if possible and open the duplicate.
- **F3 Name conflict confusing:** detect by similar names such as `copy` or `(1)` → rename the duplicate clearly.

## Verification

The folder contains the original file and a separate duplicate with its own filename.

## Variations

- `windows`: The duplicate often receives a name like `filename - Copy`.
- `macos`: Finder's `Command+D` creates a duplicate immediately.

## Safety & privacy

Low risk. Duplicates can preserve old sensitive contents, so delete unwanted copies when finished.
