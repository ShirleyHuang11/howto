---
name: set-up-email-on-a-new-device
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Add an existing email account to a new phone, tablet, or computer and confirm it can send, receive, and sync correctly.

## Preconditions

- Email address and current password.
- Access to the account's two-factor authentication method.
- The device is connected to the internet.
- Permission to add the account if it is a work or school account.
- Enough storage for mail sync.

## Steps

1. **Choose the mail app.** Use the provider's official app, the device mail app, or the approved work app. → *Expect:* the app opens an "add account" or "sign in" flow.
2. **Select the provider.** Pick Gmail, Outlook, Yahoo, iCloud, Exchange, or "Other" only if your provider is not listed. → *Expect:* the app asks for your email address.
3. **Sign in through the provider page.** Enter the email address and password only on the provider's real login screen. → *Expect:* the provider asks for a password, passkey, or 2FA approval.
4. **Complete 2FA.** Approve the prompt, enter the code, or use a security key. → *Expect:* the app advances to permissions or sync settings.
5. **Use an app password if required.** [BRANCH: modern sign-in | app password] For older mail apps, generate an app-specific password in account security settings. → *Expect:* the app accepts the generated password without exposing your main password.
6. **Choose sync settings.** Select mail, contacts, calendars, notes, sync range, and notification preferences. → *Expect:* the inbox begins loading recent messages.
7. **Verify incoming mail.** Send a test message to the account from another address or refresh the inbox. → *Expect:* the test message appears on the new device.
8. **Verify outgoing mail.** Send a short test message from the new device to another account. → *Expect:* the message appears in Sent and arrives at the destination.
9. **Secure the device.** Enable screen lock and remote wipe options if the device stores work or personal mail. → *Expect:* mail is protected if the device is lost.

## Decision points

- Work or school account requires device management → follow the organization's enrollment prompts.
- Provider blocks "less secure apps" → use OAuth sign-in or an app password if offered.
- You only need webmail → create a browser shortcut instead of syncing mail locally.
- Large mailbox slows the device → reduce sync range to recent mail.
- Shared device → do not add a private email account; use webmail and sign out.

## Failure modes & recovery

- **F1 Wrong password:** detect repeated sign-in failure; recover by testing the password in webmail and resetting it if needed.
- **F2 2FA unavailable:** detect missing codes or prompts; recover using backup codes or account recovery.
- **F3 Incoming works, outgoing fails:** detect sent messages stuck in outbox; recover by checking SMTP settings or using the provider app.
- **F4 Calendar or contacts missing:** detect only mail syncing; recover by enabling the extra sync toggles.
- **F5 Duplicate mail:** detect repeated notifications or duplicate folders; recover by removing one copy of the account and adding it through the preferred provider option.

## Verification

The new device receives a fresh test email, sends a test email that arrives elsewhere, and shows the account under the intended mail app settings.

## Variations

- `gmail`: use Google account sign-in and review device access at myaccount.google.com.
- `outlook-exchange`: work accounts may require Microsoft Authenticator or device compliance.
- `icloud`: non-Apple apps may require an app-specific password.
- `imap-other`: collect IMAP, SMTP, port, SSL, and username settings from the provider.
- `shared-mailbox`: add it as a delegated or shared mailbox, not by sharing a personal password.

## Safety & privacy

Email contains password resets, financial notices, and identity documents. Do not save mail on an unlocked device, and remove the account before selling, lending, or returning the device.
