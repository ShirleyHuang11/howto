---
name: set-a-default-app
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

Choose which app opens a file type or common task by default.

## Preconditions

- The preferred app is installed.
- You know the file type or task to change, such as `.pdf`, email, web browser, or photos.

## Steps

1. **Open default app settings.** [BRANCH: Windows | Mac] Windows: open `Settings > Apps > Default apps`; Mac: select a sample file in Finder and press `Command+I`. → *Expect:* default app controls are visible.
2. **Choose the target type.** [BRANCH: Windows | Mac] Windows: search for the app, file extension, or link type; Mac: expand `Open with` in the file Info window. → *Expect:* the current default is shown.
3. **Select the preferred app.** Choose the app from the list, or browse to it if needed. → *Expect:* the preferred app appears as the selected default.
4. **Apply broadly if needed.** [BRANCH: Windows | Mac] Windows: confirm each file type or protocol prompt; Mac: click `Change All` to apply to all files of that type. → *Expect:* the system accepts the new default.
5. **Test with a file or link.** Double-click the target file type or open the target link. → *Expect:* it opens in the chosen app.

## Decision points

- Changing browser or email defaults → check all related protocols such as HTTP, HTTPS, and mail links.
- Changing one file only on Mac → skip `Change All` and open that file with a one-time app choice.

## Failure modes & recovery

- **F1 App not listed:** detect by missing app in choices → install the app fully or use `Choose another app`.
- **F2 Default did not stick:** detect by the old app opening → repeat from system settings and confirm the prompt.
- **F3 Wrong type changed:** detect by unrelated files opening differently → restore the previous default for that type.

## Verification

A test file, link, or protocol opens automatically in the selected app without asking.

## Variations

- `windows`: Windows 11 often sets defaults by file extension and link type.
- `macos`: Finder's `Get Info > Open with > Change All` changes a file type default.

## Safety & privacy

Low risk. Default apps may receive file contents or links automatically, so choose trusted apps for sensitive documents and web links.
