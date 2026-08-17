---
name: pin-an-app-to-the-taskbar
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

Pin a frequently used app to the Windows taskbar or Mac Dock for quick access.

## Preconditions

- The app is installed.
- You can see the Start menu, taskbar, Launchpad, Applications folder, or Dock.

## Steps

1. **Find the app.** [BRANCH: Windows | Mac] Windows: press `Win` and type the app name; Mac: open Launchpad or Finder `Applications`. → *Expect:* the app appears in search or the app list.
2. **Open or select pin controls.** [BRANCH: Windows | Mac] Windows: right-click the app and choose `Pin to taskbar`; Mac: open the app, then right-click or Control-click its Dock icon. → *Expect:* a menu with pin or Dock options appears.
3. **Pin the app.** [BRANCH: Windows | Mac] Windows: click `Pin to taskbar`; Mac: choose `Options > Keep in Dock`. → *Expect:* the app icon stays in the taskbar or Dock.
4. **Test the pinned icon.** Close or minimize the app, then click the pinned icon. → *Expect:* the app opens or comes forward.

## Decision points

- App is used rarely → avoid pinning to keep the taskbar or Dock uncluttered.
- App is a web app → install or create the app shortcut first if you want a separate pinned icon.

## Failure modes & recovery

- **F1 Pin option missing:** detect by no menu item → open the app first, then right-click its running icon.
- **F2 Wrong app pinned:** detect by icon or title mismatch → right-click it and choose `Unpin from taskbar` or `Options > Remove from Dock`.
- **F3 Managed device blocks changes:** detect by policy message → ask the device administrator if pinning is disabled.

## Verification

The app icon remains visible on the taskbar or Dock after the app is closed and launches the intended app when clicked.

## Variations

- `windows`: Taskbar pinning is the standard location for quick app launch.
- `macos`: The equivalent persistent launcher area is the Dock, not a taskbar.

## Safety & privacy

Low risk. Pinned apps reveal usage habits during screen sharing or on shared computers.
