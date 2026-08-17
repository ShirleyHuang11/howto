---
name: pin-a-site-as-an-app
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

Install or pin a website so it opens like an app from the desktop, dock, taskbar, or launcher.

## Preconditions

- The website is open in a browser that supports web apps or shortcuts.
- You trust the site enough to add it to your device launcher.

## Steps

1. **Open the site.** Navigate to the website you want to pin. → *Expect:* the site loads and shows the account or page you want.
2. **Open app or shortcut controls.** [BRANCH: Chrome | Firefox | Safari] open the browser menu and look for `Install`, `Save and Share`, `Add to Dock`, or shortcut options. → *Expect:* the browser offers an install, app, or shortcut action if supported.
3. **Create the app shortcut.** Choose `Install`, `Create shortcut`, or `Add to Dock`, then confirm the name. → *Expect:* the site is added as an app or shortcut.
4. **Launch it once.** Open the new app from the desktop, dock, taskbar, Start menu, or launcher. → *Expect:* the site opens in its own window or browser shortcut.
5. **Pin it if needed.** Right-click the launched app icon and choose pin, keep in dock, or add to taskbar. → *Expect:* the app remains available from the chosen launcher.

## Decision points

- The browser offers only a bookmark → use a bookmark if app installation is unavailable.
- The site handles sensitive accounts → pin it only on a private device profile.
- You need notifications → allow them only after confirming the site is legitimate.

## Failure modes & recovery

- **F1 Install option missing:** detect no app or shortcut command → use Chrome or Safari, or create a normal bookmark.
- **F2 Wrong page pinned:** detect the app opens a subpage you did not want → remove it and create the shortcut from the correct page.
- **F3 App opens in normal browser:** detect it launches as a regular tab → recreate it using the browser's install app option if available.

## Verification

The site appears in the operating system launcher, dock, taskbar, or desktop and opens successfully from that pinned entry.

## Variations

- Chrome: use the three-dot menu, then `Save and Share` > `Create shortcut` or `Install` when offered.
- Firefox: built-in site app support is limited on desktop, so use bookmarks or operating system shortcuts.
- Safari: use `File` > `Add to Dock` on supported macOS versions.

## Safety & privacy

Pinned site apps can show notifications, account names, or private content outside the main browser window. Pin only trusted sites on trusted profiles.
