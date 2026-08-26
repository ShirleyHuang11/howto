---
name: spot-a-phishing-login-page
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You decide whether a login page is legitimate before entering a password, passkey prompt, or one-time code.

## Preconditions

- You have a login page, email link, text link, QR code, or pop-up you are unsure about.
- You can independently navigate to the service's official website or app.
- You have not yet entered credentials into the suspicious page.

## Steps

1. **Stop before typing.** Do not enter your password, one-time code, backup code, or recovery information while the page is in doubt. → *Expect:* no credential has been submitted to the suspicious page.
2. **Inspect the domain carefully.** Read the address bar from right to left before the first single slash, watching for misspellings, extra words, lookalike characters, or misleading subdomains. → *Expect:* you can identify the actual registered domain.
3. **Check HTTPS without trusting it alone.** Confirm the browser shows a secure connection, but remember phishing sites can also use HTTPS. → *Expect:* HTTPS is treated as necessary but not sufficient.
4. **Compare with an independent route.** Open a new tab, type the known official address, use a bookmark, or open the official app. → *Expect:* the real login page appears without using the suspicious link.
5. **Look for context mismatch.** Check whether the page asks for unusual data, urgent payment, backup codes, full SSN, remote-access software, or a 2FA code when you did not start a login. → *Expect:* suspicious requests are recognized before disclosure.
6. **Use the official page if login is needed.** Close the suspicious page and sign in only through the independently reached site or app. → *Expect:* you can access the account without using the questionable link.
7. **Report and delete the lure.** Use the service's phishing report address, browser report feature, or workplace security process. → *Expect:* the suspicious message or page is reported and removed from your inbox if applicable.

## Decision points

- You already entered a password → change it immediately from the official site and sign out all sessions.
- You entered a 2FA code → treat the account as actively compromised and secure it immediately.
- The message claims to be from work, school, bank, or government → verify through a known phone number or official portal, not the link.

## Failure modes & recovery

- **F1 Lookalike domain missed:** detect a tiny spelling or character difference later → change the password and review account activity.
- **F2 Fake browser window:** detect a login prompt inside another page or pop-up with a drawn address bar → close it and use a real browser window.
- **F3 QR phishing:** detect a QR code leading to login → inspect the opened URL before entering anything.
- **F4 Push fatigue attack:** detect repeated 2FA prompts you did not initiate → deny prompts, change password, and report the incident.

## Verification

You either confirm the login page's exact official domain through an independent route or close it without entering credentials, and any suspicious lure is reported or deleted.

## Variations

- Mobile apps: long-press links to preview domains where possible, but use the official app for sensitive logins.
- Single sign-on: a legitimate work login may redirect to an identity provider, but the final domain should match the organization's approved provider.
- Internationalized domains: browsers may show lookalike Unicode characters; if uncertain, type the official address manually.

## Safety & privacy

Medium risk because phishing can hand over passwords, 2FA codes, money, or identity data. Never provide backup codes or approve login prompts unless you personally initiated the login on a verified site.
