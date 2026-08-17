---
name: preview-a-file-without-opening-it
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

View a file's contents quickly without fully opening it in its default app.

## Preconditions

- The file is visible in a file manager.
- The file type supports preview or thumbnail viewing.

## Steps

1. **Select the file.** Click the file once in File Explorer or Finder. → *Expect:* the file is highlighted but not opened.
2. **Open preview.** [BRANCH: Windows | Mac] Windows: press `Alt+P` in File Explorer to show the Preview pane; Mac: press `Space` to open Quick Look. → *Expect:* a preview pane or floating preview appears.
3. **Review the content.** Scroll, zoom, or page through if the preview supports it. → *Expect:* enough content is visible to identify the file.
4. **Close preview.** [BRANCH: Windows | Mac] Windows: press `Alt+P` again or select another file; Mac: press `Space` again or `Esc`. → *Expect:* the preview closes or updates.

## Decision points

- Preview shows the wrong file → select a different file and preview again.
- File is sensitive → avoid previewing it while screen sharing or in public.

## Failure modes & recovery

- **F1 Preview unavailable:** detect by blank pane or unsupported message → open the file in a trusted app if needed.
- **F2 File opens fully:** detect by the default app launching → close it and use single-click plus the preview shortcut.
- **F3 Content looks stale:** detect by preview not matching expected updates → close and reopen the preview or refresh the folder.

## Verification

A preview displays the selected file's recognizable contents without launching the full default editing app.

## Variations

- `windows`: `Alt+P` toggles File Explorer's Preview pane.
- `macos`: Quick Look with `Space` supports many documents, images, videos, and PDFs.

## Safety & privacy

Low risk. Previewing can still expose document contents on screen, and some file types may require opening in an app to inspect safely.
