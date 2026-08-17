---
name: open-the-task-manager
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

Open the system tool that shows running apps and resource usage.

## Preconditions

- You are signed in to the computer.
- You want to inspect running apps, CPU, memory, disk, or network use.

## Steps

1. **Use the quick shortcut.** [BRANCH: Windows | Mac] Windows: press `Ctrl+Shift+Esc`; Mac: press `Command+Space`, type `Activity Monitor`, and press `Return`. → *Expect:* Task Manager or Activity Monitor opens.
2. **Use the menu path if needed.** [BRANCH: Windows | Mac] Windows: right-click the taskbar and choose `Task Manager`, or press `Ctrl+Alt+Delete` and choose `Task Manager`; Mac: open `Applications > Utilities > Activity Monitor`. → *Expect:* the system monitor window is visible.
3. **Choose the relevant tab or column.** [BRANCH: Windows | Mac] Windows: use `Processes` or `Performance`; Mac: use CPU, Memory, Energy, Disk, or Network tabs. → *Expect:* running apps and resource values are shown.

## Decision points

- Computer is frozen but keyboard works → use the shortcut first.
- You only need to quit a Mac app → `Option+Command+Esc` opens Force Quit instead of Activity Monitor.

## Failure modes & recovery

- **F1 Shortcut intercepted:** detect by nothing opening → use the menu path or system search.
- **F2 Window opens minimized:** detect by taskbar or Dock indicator → click the app icon to bring it forward.
- **F3 Managed device blocks access:** detect by policy message → contact the administrator for monitoring access.

## Verification

Task Manager on Windows or Activity Monitor on Mac is open and lists running processes or resource usage.

## Variations

- `windows`: `Ctrl+Shift+Esc` opens Task Manager directly.
- `macos`: Activity Monitor is the closest equivalent to Task Manager.

## Safety & privacy

Low risk when viewing. Ending processes can close unsaved work, so do not force quit apps unless you have saved or accepted possible data loss.
