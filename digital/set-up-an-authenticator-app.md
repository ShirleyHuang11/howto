---
name: set-up-an-authenticator-app
domain: digital
locale: [generic]
interface: mobile-app
difficulty: intermediate
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Add an authenticator app to an account so sign-ins require both the password and a time-based code.

## Preconditions

- You have a smartphone or trusted device where the authenticator app will stay installed.
- You can sign in to the account you want to protect.
- You have a safe place to store backup codes.

## Steps

1. **Install a trusted authenticator.** Use a well-known authenticator app from the official app store or your organization's required app. → *Expect:* the app opens without asking for your account password.
2. **Open account security settings.** Find two-factor authentication, multi-factor authentication, or two-step verification. → *Expect:* the account offers an authenticator app option.
3. **Start authenticator setup.** Choose app-based codes instead of SMS when available. → *Expect:* the site shows a QR code or setup key.
4. **Scan the QR code.** In the authenticator app, add an account and scan the displayed QR code. → *Expect:* a new entry appears with a six-digit or eight-digit changing code.
5. **Save backup codes first.** Download, print, or write the one-time backup codes before finishing setup. → *Expect:* backup codes are stored somewhere separate from the phone.
6. **Enter the current code.** Type the code from the app into the website before it expires. → *Expect:* the site accepts the code and confirms authenticator setup.
7. **Make a device-loss plan.** Add a second trusted method, backup phone, security key, or recovery email if the account supports it. → *Expect:* losing the phone will not permanently lock the account.
8. **Test in a fresh sign-in.** Sign out or use a private window, then sign in with password plus authenticator code. → *Expect:* the account asks for and accepts the app code.
9. **Remove weaker methods if appropriate.** ⚠️ *Irreversible:* removing SMS or email recovery can lock you out if the app is lost, so confirm backup codes and a second method first. → *Expect:* the account security page shows the intended methods only.

## Decision points

- The site only offers SMS → use it if better than nothing, but prefer app codes on accounts that support them.
- The authenticator app offers cloud backup → enable only if the backup account itself is strongly protected.
- You manage a work account → follow employer recovery and device-enrollment rules.
- You cannot store backup codes safely → pause setup until you can.
- The QR scan fails → use the manual setup key and account label.

## Failure modes & recovery

- **F1 Code rejected:** detect repeated invalid-code errors, recover by checking phone time sync and using the newest code.
- **F2 Backup codes lost:** detect no stored recovery codes, recover by generating new codes while still signed in.
- **F3 Phone replaced:** detect codes left on old device, recover by transferring the authenticator before wiping it.
- **F4 Wrong account label:** detect multiple similar entries, recover by renaming entries with service and username.
- **F5 Locked out:** detect no working code or backup method, recover through the account's official recovery process.

## Verification

A fresh sign-in succeeds only after entering a current authenticator code, and backup codes are stored off the phone.

## Variations

- Password managers: some include authenticator codes, which is convenient but puts more trust in one vault.
- Hardware keys: use them for accounts with high value or phishing risk.
- Shared family accounts: add recovery methods for the responsible adult, not every casual user.
- Offline travel: backup codes matter because SMS may not arrive.

## Safety & privacy

Authenticator codes protect accounts, but screenshots of QR codes or setup keys can let someone clone the second factor. Store backup codes like spare keys, not like ordinary notes.
