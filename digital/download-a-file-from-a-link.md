---
name: download-a-file-from-a-link
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Download a file from a link and confirm it saved to the expected location.

## Preconditions

- The link is visible on a website or in a message.
- You trust the source enough to download the file.
- Your device has space for the file.

## Steps

1. **Inspect the link.** Hover over the link or long-press if on a touch device. → *Expect:* the destination or file name appears.
2. **Start the download.** Click the link, or right-click and choose `Save Link As`. → *Expect:* the browser starts a download or opens a save dialog.
3. **Choose a folder if asked.** Select Downloads or another known folder and keep or edit the filename. → *Expect:* the save location and filename are visible before saving.
4. **Wait for completion.** Watch the browser downloads button or shelf. → *Expect:* the download shows complete with no warning.
5. **Open the containing folder.** Use `Show in folder`, `Show in Finder`, or the downloads list. → *Expect:* the file appears in the expected folder.

## Decision points

- The file type is unexpected → cancel the download and verify the source.
- The browser warns the file may be harmful → do not keep it unless you can verify it independently.
- The link opens a preview instead of downloading → use the download button in the preview or `Save Link As`.

## Failure modes & recovery

- **F1 Download blocked:** detect a browser security warning → cancel and get the file from the official source.
- **F2 File saved in unknown folder:** detect you cannot find it → open the browser downloads list and choose `Show in folder`.
- **F3 Partial download:** detect a `.crdownload`, `.part`, or failed status → retry on a stable connection.
- **F4 Wrong file downloaded:** detect the filename, type, or size does not match → delete it and recheck the link destination.

## Verification

The expected file exists in the chosen folder and the browser download list shows it completed successfully.

## Variations

- Chrome: use the downloads button in the toolbar or `Ctrl+J`/`Command+Shift+J` for downloads.
- Firefox: use the downloads arrow or `Ctrl+J`/`Command+J`.
- Safari: use the downloads button or `Option+Command+L` to show downloads.

## Safety & privacy

Downloaded files can contain malware or sensitive information. Prefer official sources, scan suspicious files, and avoid opening unexpected executables or macros.
