---
name: search-your-computer-for-a-file
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

Find a file on your computer by searching for its name, type, or recent location.

## Preconditions

- You know at least part of the filename, file type, or likely folder.
- The drive or cloud folder containing the file is connected or synced.

## Steps

1. **Open system search.** [BRANCH: Windows | Mac] Windows: press `Win` and type, or open File Explorer and use the search box; Mac: press `Command+Space` for Spotlight or open Finder search. → *Expect:* a search field is active.
2. **Enter a useful query.** Type the exact name, part of the name, or an extension such as `.pdf`, `.jpg`, or `.xlsx`. → *Expect:* results begin to appear.
3. **Narrow by location if needed.** Search inside Documents, Downloads, Desktop, or the likely project folder. → *Expect:* fewer and more relevant results appear.
4. **Check details before opening.** Look at the file path, date modified, size, and icon. → *Expect:* one result looks like the intended file.
5. **Open or reveal the file.** Double-click to open it, or use right-click `Open file location` on Windows or `Show in Finder` on Mac. → *Expect:* the file or its containing folder opens.

## Decision points

- You remember the file type but not the name → search by extension or kind.
- Search returns too many results → add another word from the filename or search in a likely folder.
- File may be in cloud storage → check OneDrive, Google Drive, Dropbox, or iCloud sync status.

## Failure modes & recovery

- **F1 No results:** detect by an empty result list → search a broader folder, check spelling, or search by extension.
- **F2 Wrong version found:** detect by old modified date or wrong contents → sort by modified date and open the newest likely match.
- **F3 External drive missing:** detect by the drive not appearing → reconnect the drive and search again.

## Verification

The intended file is visible in its containing folder or opens with the expected contents.

## Variations

- `windows`: File Explorer supports filters such as `kind:document` and `datemodified:this week`.
- `macos`: Finder search can filter by `Kind`, `Name`, or `Last opened date`.

## Safety & privacy

Low risk. Search results can expose sensitive filenames on shared screens, so avoid searching private terms while others can see.
