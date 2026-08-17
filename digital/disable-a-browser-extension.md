---
name: disable-a-browser-extension
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Turn off a browser extension temporarily without uninstalling it.

## Preconditions

- You can open the browser's extensions or add-ons settings.
- You know which browser profile contains the extension.

## Steps

1. **Open extension settings.** [BRANCH: Chrome | Firefox | Safari] open the browser menu and choose `Extensions`, `Add-ons and themes`, or `Settings` > `Extensions`. → *Expect:* a list of installed extensions appears.
2. **Find the extension.** Use the extension name, icon, or search field if available. → *Expect:* the target extension is visible in the list.
3. **Turn it off.** Toggle the extension off or clear its enable checkbox. → *Expect:* the extension shows disabled, off, or unchecked.
4. **Reload the affected page.** Return to the web page and refresh it with `Ctrl+R` or `Command+R`. → *Expect:* the page runs without that extension active.
5. **Re-enable if needed.** Return to the extensions list and toggle it back on when finished. → *Expect:* the extension becomes active again.

## Decision points

- You are troubleshooting a broken site → disable one extension at a time so the cause is clear.
- The extension looks unfamiliar or suspicious → leave it disabled and investigate before re-enabling.
- The browser says the extension is managed → contact the device or workplace administrator.

## Failure modes & recovery

- **F1 Extension not found:** detect it is absent from the list → check another browser profile or another browser.
- **F2 Page still broken:** detect the same issue after refresh → disable other likely extensions or test a private window.
- **F3 Toggle unavailable:** detect controls are greyed out → check managed browser policies or required extensions.

## Verification

The extension list shows the target extension disabled, and the affected page reloads with that extension inactive.

## Variations

- Chrome: open `chrome://extensions/` or use `Extensions` > `Manage Extensions`.
- Firefox: open `about:addons` and choose `Extensions`.
- Safari: open `Safari` > `Settings` > `Extensions` and clear the extension checkbox.

## Safety & privacy

Extensions can read or change page data depending on permissions. Disable unfamiliar extensions before entering sensitive information, and avoid removing workplace-required tools without approval.
