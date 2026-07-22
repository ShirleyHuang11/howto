---
name: force-quit-a-frozen-app
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min-10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A frozen app is closed without restarting the whole device unless the system itself is unresponsive.

## Preconditions

- The app is not responding to normal close, back, or quit controls.
- You understand unsaved work inside the frozen app may be lost.

## Steps

1. **Wait briefly.** Give the app 30 to 60 seconds if it froze during saving, printing, syncing, or exporting. → *Expect:* either it recovers or stays clearly frozen.
2. **Try the normal quit path.** Use the app menu, close button, or back gesture once. → *Expect:* the app closes or remains stuck without responding.
3. **Open the force-quit tool.** [BRANCH: Windows | macOS | iPhone/iPad | Android] Windows: Ctrl+Shift+Esc. macOS: Option+Command+Esc. iPhone/iPad: open the app switcher. Android: open Recents or App info. → *Expect:* a list of running apps appears.
4. **Select the frozen app.** Choose only the app that is not responding, not system services or unrelated background tasks. → *Expect:* the target app is highlighted or shown in app details.
5. **Force close it.** Use End task, Force Quit, swipe up, or Force stop. ⚠️ *Irreversible:* unsaved changes in that app can be lost, so confirm no visible save is still progressing. → *Expect:* the app disappears or its process ends.
6. **Relaunch the app.** Open it again from the launcher, taskbar, dock, or home screen. → *Expect:* the app starts fresh, sometimes with a recovery prompt.
7. **Recover available work.** Accept document recovery, reopen recent files, or check autosave/cloud history. → *Expect:* the newest available saved version is visible.
8. **Escalate only if the device is frozen.** If keyboard, pointer, touch, and system controls do not respond, restart the device using the normal power menu or hardware restart recipe. → *Expect:* the device, not just the app, restarts.

## Decision points

- App froze while saving → wait longer before force quitting because storage writes may still finish.
- Only one browser tab is frozen → use the browser's task manager if available rather than closing the whole browser.
- The whole screen ignores input → treat it as a device freeze, not an app freeze.

## Failure modes & recovery

- **F1 Unsaved work lost:** detect the recovered document is old, recover by checking autosave, cloud version history, temp recovery files, or recent backups.
- **F2 App reopens frozen:** detect immediate freeze on relaunch, recover by starting without reopening windows or clearing that app's cache.
- **F3 Wrong process ended:** detect another app closed, recover by reopening it and checking autosave before continuing.
- **F4 System remains unresponsive:** detect force-quit tool will not open, recover by restarting the device.

## Verification

The frozen app is closed, relaunches to a usable state, and the device responds normally without repeated hangs.

## Variations

- Windows: Task Manager may show Not responding beside the app; End task closes it.
- macOS: Force Quit Applications shows stalled apps, and Activity Monitor is the advanced option.
- Mobile apps: force close is usually safe for the app, but drafts and unsynced edits can be lost.

## Safety & privacy

Force quitting can interrupt saves, uploads, payments, and encryption tasks. Do not force quit during visible financial submission or file-writing progress unless waiting has clearly failed.
