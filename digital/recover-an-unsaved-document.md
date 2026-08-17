---
name: recover-an-unsaved-document
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Recover the newest usable version of a document that was closed, crashed, or never saved, then save it in a durable location.

## Preconditions

- You know which app created the document.
- The computer or device has not been wiped since the loss.
- You can sign in to the account used by the app if cloud autosave was enabled.

## Steps

1. **Do not create more confusion.** Stop editing similarly named files and keep the app open if a recovery pane is visible. → *Expect:* the current recovery state is preserved.
2. **Check the app recovery pane.** Reopen the app and look for Document Recovery, Recovered files, Recent, or Restore previous session. → *Expect:* the app lists one or more recovered drafts or recent files.
3. **Search recent files.** Use the app's File > Open Recent or Home > Recent list and sort by modified date. → *Expect:* likely versions appear near the top of the recent list.
4. **Check autosave cloud history.** [BRANCH: Microsoft 365 | Google Docs | Apple iWork] open OneDrive/SharePoint version history, Google Drive version history, or iCloud Drive Browse Versions if available. → *Expect:* older versions or autosaved drafts are available to inspect.
5. **Search temporary recovery folders.** [BRANCH: Windows | Mac] search File Explorer for `*.asd`, `*.wbk`, or the document name, or search Finder Recents and app containers for the title. → *Expect:* candidate temporary files appear with plausible timestamps.
6. **Open candidates read-only when possible.** Open each candidate and compare the timestamp and contents before saving over anything. → *Expect:* the best recovered version is identified.
7. **Save the recovered copy immediately.** Use Save As to put the file in Documents, Desktop, OneDrive, Google Drive, or iCloud Drive with a clear name. → *Expect:* the document has a normal filename and appears in a known folder.
8. **Enable autosave for next time.** Turn on AutoSave or automatic backup in the app and confirm the save location syncs. → *Expect:* future edits show saved or synced status.

## Decision points

- The file was in a cloud editor → version history is more likely than local temp folders.
- The app crashed but recovery pane appears → save the recovered copy before opening other files.
- The document contained sensitive data → avoid uploading it to random recovery services.

## Failure modes & recovery

- **F1 Recovery pane is empty:** detect no recovered files → search recent files and cloud version history.
- **F2 Temporary file will not open:** detect file format error → copy it first, then try opening with the original app and a compatible viewer.
- **F3 Wrong version recovered:** detect missing latest edits → compare all candidates by modified time and version history.
- **F4 Autosave overwrote content:** detect unwanted cloud version → restore a previous version from the cloud history.

## Verification

The recovered document opens in the correct app, contains the needed content, has been saved with a normal filename in a known folder, and that folder shows saved or synced status.

## Variations

- Microsoft Word: check File > Info > Manage Document and OneDrive version history.
- Google Docs: check File > Version history > See version history.
- Apple Pages/Numbers/Keynote: check File > Revert To > Browse All Versions when available.

## Safety & privacy

Low risk. Recovery files may contain private drafts, so inspect them locally and avoid third-party upload sites unless you trust the provider and understand the data exposure.
