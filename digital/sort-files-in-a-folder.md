---
name: sort-files-in-a-folder
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

Change how files are ordered in a folder so you can find or compare items more easily.

## Preconditions

- The folder is open in File Explorer or Finder.
- You know the attribute to sort by, such as name, date, type, or size.

## Steps

1. **Open view controls.** [BRANCH: Windows | Mac] Windows: use File Explorer's `Sort` menu or column headers; Mac: use Finder's `View > Sort By` or `View > Show View Options`. → *Expect:* sorting choices are available.
2. **Choose a sort field.** Select `Name`, `Date modified`, `Kind` or `Type`, or `Size`. → *Expect:* files reorder by that field.
3. **Set direction if needed.** Click the column header again or choose ascending or descending order. → *Expect:* newest-to-oldest, oldest-to-newest, A-to-Z, or Z-to-A order matches your choice.
4. **Group only if useful.** Turn grouping on for categories like type or date, or turn it off for a simple list. → *Expect:* the folder layout becomes easier to scan.

## Decision points

- Looking for a recent download → sort by date modified descending.
- Comparing large files → sort by size descending.
- Finding a file type → sort or group by type or kind.

## Failure modes & recovery

- **F1 Files appear missing:** detect by unexpected groups or collapsed sections → turn off grouping or expand all groups.
- **F2 Sort changes every folder:** detect by other folders using the same view → adjust only the current folder's view options where possible.
- **F3 Cannot see columns:** detect by icon view without details → switch to Details/List view.

## Verification

The visible file list is ordered by the selected field and direction in the active folder.

## Variations

- `windows`: Details view exposes clickable column headers such as `Name`, `Date modified`, `Type`, and `Size`.
- `macos`: Finder can sort independently from grouping, depending on the view mode.

## Safety & privacy

Low risk. Sorting changes only the view, but filenames and recent activity can be visible during screen sharing.
