---
name: recover-a-hacked-email-account
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You regain control of a compromised email account, remove the attacker's persistence, and secure other accounts that depend on that email.

## Preconditions

- You have access to at least one recovery method, trusted device, backup code, or provider recovery form.
- You can use a clean device and network you trust.
- You have time to check forwarding, filters, sessions, and recovery settings after login.

## Steps

1. **Start from the provider's official recovery page.** Type the provider URL yourself or use its official app; do not use links from suspicious emails. → *Expect:* you reach the real sign-in or account-recovery flow.
2. **Regain access.** Use recovery email, phone, backup code, trusted device, or identity questions as offered. → *Expect:* the provider lets you reset the password or restore account access.
3. **Set a unique password immediately.** Use a password manager and do not reuse an old or similar password. → *Expect:* the old password no longer works.
4. **Review and replace recovery methods.** Remove unknown recovery emails, phone numbers, devices, passkeys, and authenticator methods; add only yours. → *Expect:* recovery points to contact methods you control.
5. **Sign out of all sessions.** End sessions on every device, browser, and mail app. → *Expect:* unknown sessions disappear or are marked signed out.
6. **Remove attacker persistence.** Check forwarding addresses, filters, rules, delegated mailbox access, app passwords, connected apps, POP/IMAP settings, signatures, and vacation replies. → *Expect:* no rule or integration can silently copy or send mail.
7. **Enable strong 2FA.** Prefer an authenticator, passkey, or hardware security key over SMS if available. → *Expect:* future sign-ins require a second factor you control.
8. **Warn contacts and secure linked accounts.** Check sent mail for scam messages, notify affected contacts, and reset passwords on banking, shopping, cloud, social, and password-manager accounts that use this email. → *Expect:* dependent accounts are no longer recoverable by the attacker.

## Decision points

- You cannot regain access → use the provider's account recovery form and be ready with creation date, devices, contacts, billing, or previous passwords.
- The attacker changed financial or government accounts → contact those providers directly and consider fraud alerts.
- The email is a work or school account → report it to IT immediately because administrators can inspect logs and revoke sessions.

## Failure modes & recovery

- **F1 Recovery loops fail:** detect repeated rejection of recovery answers → try from a known device and network, then use provider support or admin escalation.
- **F2 Forwarding rule remains hidden:** detect contacts receiving replies you did not send → inspect all filters, delegated access, and app passwords, including mobile mail clients.
- **F3 Attacker regains access:** detect a new password reset or recovery change → replace recovery methods again and remove compromised devices from your phone carrier and accounts.
- **F4 Linked accounts compromised:** detect password resets or orders elsewhere → secure those accounts, dispute transactions, and preserve evidence.

## Verification

The email account has a new unique password, only your recovery methods and sessions remain, forwarding and delegation are clean, 2FA is enabled, and linked high-value accounts have been reviewed.

## Variations

- Gmail/Google Workspace: check forwarding, filters, delegates, app passwords, third-party access, and Security Checkup.
- Outlook/Microsoft 365: check rules, forwarding, connected accounts, app passwords, aliases, and recent activity.
- Work email: administrators may need to revoke tokens, reset MFA, and review message trace logs.

## Safety & privacy

Medium risk because email controls password resets for many accounts. Work from a trusted device, never send recovery codes to anyone, and treat financial, medical, and identity accounts as exposed until reviewed.
