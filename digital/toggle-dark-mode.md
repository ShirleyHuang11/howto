---
name: toggle-dark-mode
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

Switch the device or app between light mode and dark mode.

## Preconditions

- You can access the device or app appearance settings.
- The app or operating system supports light and dark appearance.

## Steps

1. **Open appearance settings.** [BRANCH: Windows | Mac | mobile-app] Windows: Settings > Personalization > Colors; Mac: System Settings > Appearance; mobile: open Display or Appearance settings. → *Expect:* light and dark appearance options are visible.
2. **Choose the mode.** Select `Dark`, `Light`, or automatic scheduling. → *Expect:* menus and windows change appearance.
3. **Check app-specific settings.** If one app does not follow the system, open that app's theme or appearance setting. → *Expect:* the app uses the intended theme.
4. **Confirm readability.** Look at text, icons, and buttons in a common app. → *Expect:* contrast is comfortable and content remains readable.

## Decision points

- You want automatic switching → choose sunset-to-sunrise or a custom schedule if available.
- Only one app should change → use that app's theme setting instead of system settings.
- Text becomes hard to read → switch back or choose a higher-contrast theme.

## Failure modes & recovery

- **F1 App ignores system mode:** detect one app stays light or dark → change the app's own theme setting.
- **F2 Scheduled mode surprises you:** detect mode changes at unwanted times → turn off automatic scheduling.
- **F3 Low contrast:** detect text blends into the background → choose light mode, dark mode, or accessibility contrast settings.

## Verification

The operating system or target app visibly uses the selected light, dark, or automatic appearance setting.

## Variations

- `windows`: Windows separates default Windows mode and default app mode.
- `mac`: options usually include Light, Dark, and Auto.
- `mobile-app`: some apps provide theme choices independent of phone settings.

## Safety & privacy

Dark mode is low risk. During screen sharing, theme changes may briefly reveal open settings or apps, so switch before presenting.
