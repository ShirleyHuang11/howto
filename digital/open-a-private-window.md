---
name: open-a-private-window
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Open a private browsing window for a session that should not be saved in local browser history.

## Preconditions

- A desktop browser is installed.
- You understand private browsing does not make you anonymous to websites, networks, employers, or internet providers.

## Steps

1. **Open a private window.** [BRANCH: Chrome | Firefox | Safari] press `Ctrl+Shift+N` in Chrome, `Ctrl+Shift+P` in Firefox, or `Command+Shift+N` on Mac browsers that support it. → *Expect:* a new private or incognito window opens.
2. **Confirm private mode.** Look for `Incognito`, `Private Browsing`, a mask icon, or a dark private-mode start page. → *Expect:* the window clearly indicates private browsing.
3. **Browse in that window only.** Type the address or search query into the private window. → *Expect:* pages open inside the private window, not in the normal window.
4. **Close the window when done.** Close all private tabs and the private window. → *Expect:* local history, cookies, and site data from that private session are discarded.

## Decision points

- You need saved passwords or extensions → they may be unavailable unless allowed in private mode.
- You need anonymity from a site or network → use privacy tools beyond private browsing.
- You are on a shared computer → sign out of accounts before closing the private window.

## Failure modes & recovery

- **F1 Normal window used:** detect no private-mode label or icon → open a private window and repeat the visit there.
- **F2 Download remains:** detect a file saved during private browsing → delete the downloaded file manually if it should not remain.
- **F3 Account sync reveals activity:** detect you sign into an account during private browsing → sign out and review account activity settings.

## Verification

The browser window shows a private or incognito indicator, and closing it removes that session's local cookies and history.

## Variations

- Chrome: use `Ctrl+Shift+N` on Windows/Linux or `Command+Shift+N` on Mac for Incognito.
- Firefox: use `Ctrl+Shift+P` on Windows/Linux or `Command+Shift+P` on Mac for Private Browsing.
- Safari: use `File` > `New Private Window` or `Command+Shift+N`.

## Safety & privacy

Private browsing mainly protects against local history on that device. Websites, schools, employers, internet providers, and downloaded files can still reveal activity.
