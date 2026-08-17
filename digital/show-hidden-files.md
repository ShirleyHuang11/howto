---
name: show-hidden-files
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

Temporarily display hidden files and folders so you can inspect or select them.

## Preconditions

- You know why you need hidden files, such as finding a configuration file.
- You will avoid changing system files unless instructed by a trusted source.

## Steps

1. **Open the target folder.** Navigate to the folder where hidden files may be located. → *Expect:* normal files and folders are visible.
2. **Turn on hidden items.** [BRANCH: Windows | Mac] Windows: in File Explorer choose `View > Show > Hidden items`; Mac: press `Shift+Command+.` in Finder. → *Expect:* dimmed or dot-prefixed hidden files appear if present.
3. **Inspect the needed item.** Select or view the hidden file without editing unrelated files. → *Expect:* the target hidden item is visible and identifiable.
4. **Turn hidden items off when finished.** [BRANCH: Windows | Mac] Windows: uncheck `View > Show > Hidden items`; Mac: press `Shift+Command+.` again. → *Expect:* hidden files disappear from normal view.

## Decision points

- You are troubleshooting an app → follow app-specific instructions for the exact hidden file.
- You see system folders you do not recognize → leave them unchanged.

## Failure modes & recovery

- **F1 Shortcut does nothing:** detect by no visibility change → click a Finder window first on Mac or use the File Explorer View menu on Windows.
- **F2 File still missing:** detect by no target file after showing hidden items → confirm the path and search for the filename.
- **F3 Accidental edit:** detect by changed file contents or warning → undo immediately or restore from backup.

## Verification

Hidden items become visible while the setting is on and are hidden again after the setting is turned off.

## Variations

- `windows`: Some protected operating system files require a separate Folder Options setting and should usually remain hidden.
- `macos`: Files beginning with `.` are hidden in Finder by default.

## Safety & privacy

Low risk if viewing only. Hidden files may contain tokens, preferences, caches, or system settings, so do not share screenshots or edit casually.
