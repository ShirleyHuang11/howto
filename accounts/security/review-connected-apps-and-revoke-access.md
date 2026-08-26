---
name: review-connected-apps-and-revoke-access
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: basic
est_time: 20min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You review third-party apps, browser extensions, devices, and integrations that can access your account, then remove anything you no longer recognize, use, or trust.

## Preconditions

- You can sign in to the account and complete any 2FA challenge.
- You have a few minutes to reauthorize legitimate apps afterward if needed.
- You know which devices and services you currently use with this account.

## Steps

1. **Open the account security settings.** Sign in and look for Security, Privacy, Apps, Integrations, Connected apps, Authorized apps, or Account access. → *Expect:* a page listing apps, services, extensions, devices, or sessions with account permissions.
2. **Sort by access level and last used date if available.** Prioritize apps with email, files, contacts, payment, admin, or "full account" access. → *Expect:* the highest-risk and least-recently-used connections are easy to identify.
3. **Inspect each connected app.** Open its details and read what data it can access, who published it, when it was authorized, and when it last accessed the account. → *Expect:* each app can be categorized as needed, unknown, stale, or suspicious.
4. **Revoke stale or suspicious access.** Remove apps you do not recognize, no longer use, or cannot verify from the publisher name and purpose. → *Expect:* the app disappears from the connected-apps list or is marked revoked.
5. **Keep only necessary integrations.** Leave access in place only for services you actively use and trust, such as a password manager, calendar sync, or official mobile app. → *Expect:* the remaining list is short and explainable.
6. **Check for account changes after revocation.** Review recent security activity for new logins, forwarding rules, app passwords, or permission grants you did not create. → *Expect:* no unexplained account activity remains, or suspicious items are queued for removal.
7. **Test critical workflows.** Open any important service that depends on the account and reconnect it only if it fails and you still trust it. → *Expect:* necessary services work, and unnecessary apps stay disconnected.

## Decision points

- Unknown app has broad access → revoke it first, then investigate; legitimate apps can usually be reconnected.
- App is from your employer, school, or managed device → check policy before removal if it may affect work access.
- You find repeated suspicious grants → change the account password and review 2FA before reconnecting anything.

## Failure modes & recovery

- **F1 Revoked a needed app:** detect a broken sync or login → reconnect from the app's official site and grant only the minimum permissions requested.
- **F2 App will not revoke:** detect an error or app reappearing → sign out of all sessions, change the password, then retry removal.
- **F3 Publisher name is unclear:** detect a generic or misspelled developer name → search from the official service documentation, not from links inside the app entry.
- **F4 Suspicious activity remains:** detect unknown logins, forwarding rules, or app passwords → secure the account after a breach and contact the provider if changes cannot be removed.

## Verification

The connected-apps list contains only apps you can name and justify, each stale or suspicious app is removed, and the security-activity log shows no new unexplained app authorizations.

## Variations

- Google/Microsoft/Apple: connected apps may be split across Security, Privacy, Sign in with, app passwords, and device pages.
- Business accounts: some integrations are tenant-approved by an administrator and cannot be removed by an individual user.
- OAuth apps: revoking access stops future API access but does not delete data the third party already copied.

## Safety & privacy

Medium risk because connected apps may read private messages, files, contacts, or payment data. Confirm an app is unnecessary before revoking if it supports work, backups, medical portals, or financial records, but remove suspicious broad-access apps immediately.
