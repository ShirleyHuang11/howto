---
name: scan-a-qr-code-safely
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Open a QR code only after checking where it leads and avoiding credential theft, payment scams, or malicious downloads.

## Preconditions

- A phone or tablet with a camera.
- Current system updates installed if possible.
- Enough light to inspect the printed code and surrounding sign.
- A separate way to reach the organization, such as typing its known website.
- Awareness that QR codes are just links.

## Steps

1. **Inspect the physical code.** Look for stickers placed over a real code, torn edges, mismatched branding, or a code added to a public surface. → *Expect:* the code appears original or you decide not to scan it.
2. **Use the built-in camera first.** Open the camera or trusted QR scanner, not a random scanner app from an ad. → *Expect:* the phone previews a URL before opening it.
3. **Read the preview URL.** Check the domain, spelling, country code, and whether it uses HTTPS. → *Expect:* the link visibly matches the organization or service you expected.
4. **Avoid automatic sign-in.** If the link opens a login page from a random poster, parking meter, restaurant table, or flyer, stop. → *Expect:* you do not enter passwords or one-time codes from an unverified QR link.
5. **Cross-check important actions.** For payments, fines, delivery issues, tickets, or account warnings, type the known official website yourself or use the official app. → *Expect:* the same action appears after independent navigation.
6. **Open low-risk links only.** Menus, event pages, and public documents are usually safer if the domain checks out. → *Expect:* the page content matches the physical context.
7. **Reject unexpected downloads.** Do not install apps, profiles, certificates, or files prompted by a scanned code. → *Expect:* no new app, configuration profile, or permission is granted.
8. **Close suspicious pages.** If the page redirects repeatedly, asks for payment immediately, or claims urgency, close the browser tab. → *Expect:* the suspicious page is no longer active.
9. **Report tampered codes.** Tell staff, the business, parking authority, or venue if a stickered or fake code is present. → *Expect:* the owner can remove or verify the code.

## Decision points

- The QR code is on a public payment point → verify through the official app, meter number, or typed website.
- The preview is a shortened URL → treat it as unknown unless the setting is low risk.
- The page asks for credentials → navigate independently before signing in.
- The code is private, such as from your bank app or ticket app → scan only inside the expected workflow.
- You already entered credentials → change the password and revoke sessions from the real site.

## Failure modes & recovery

- **F1 Sticker overlay:** detect raised edges or misaligned code; recover by not scanning and reporting it.
- **F2 Lookalike domain:** detect misspellings or odd endings; recover by closing it and typing the known address.
- **F3 Credential prompt:** detect a login page after a public QR scan; recover by opening the official app or site separately.
- **F4 Forced download:** detect an app, profile, or certificate prompt; recover by canceling and deleting any downloaded file.
- **F5 Payment scam:** detect a charge request that bypasses the expected vendor; recover by stopping payment and contacting the official provider.

## Verification

The opened page domain matches the intended organization, and you did not enter credentials, payment details, or install anything from an unverified QR link.

## Variations

- `restaurant-menu`: ask staff for a printed menu if the code looks tampered with.
- `parking`: compare the zone or meter number shown in the app with the sign or meter.
- `event-ticket`: scan within the official ticketing app when possible.
- `workplace`: managed devices may block unknown QR destinations.
- `android-ios`: both platforms can preview links from the default camera.

## Safety & privacy

A QR code can hide a phishing site as easily as any link. Treat security questions, passwords, one-time codes, payment cards, and device permission prompts as off limits unless you reached the page through an official path.
