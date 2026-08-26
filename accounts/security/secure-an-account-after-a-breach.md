---
name: secure-an-account-after-a-breach
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You lock down an account after a suspected breach by removing unauthorized access, replacing credentials, and checking for harmful changes.

## Preconditions

- You can access the account or its recovery process.
- You have a trusted device and secure internet connection.
- You can receive 2FA and recovery notifications.

## Steps

1. **Sign in through the official site or app.** Type the address yourself and avoid links from breach or alert emails. → *Expect:* you are on the legitimate account page.
2. **Change the password.** Set a unique strong password in a password manager. → *Expect:* the provider confirms the password changed.
3. **Sign out all sessions.** End active sessions on other devices and browsers. → *Expect:* only your current trusted session remains.
4. **Check recovery and 2FA settings.** Remove unknown emails, phone numbers, authenticators, passkeys, app passwords, and trusted devices; add strong 2FA if missing. → *Expect:* recovery and second factors belong only to you.
5. **Review connected apps and permissions.** Revoke unknown OAuth apps, integrations, extensions, API keys, and delegated access. → *Expect:* only recognized apps remain.
6. **Inspect high-risk account settings.** Check payment methods, shipping addresses, email forwarding, profile details, security questions, saved cards, and notification preferences. → *Expect:* no attacker-controlled setting remains.
7. **Review recent activity.** Look for logins, orders, messages, transfers, posts, or data exports you did not authorize. → *Expect:* unauthorized activity is documented and reported where needed.
8. **Monitor for recurrence.** Turn on login alerts and watch email, bank, and account notifications for the next few weeks. → *Expect:* new suspicious activity triggers prompt alerts.

## Decision points

- The account contains money, identity, or health data → contact provider support and preserve confirmation numbers.
- The same password was reused elsewhere → change it everywhere it was reused, starting with email and financial accounts.
- You cannot remove an unknown setting → open a support case before assuming the account is clean.

## Failure modes & recovery

- **F1 Password reset blocked:** detect a lockout or "too many attempts" message → wait the stated time or use official recovery support.
- **F2 Unknown recovery method remains:** detect a grayed-out or admin-controlled method → contact the provider or organization administrator.
- **F3 Unauthorized charges or orders:** detect transactions you did not make → dispute through the provider and payment issuer immediately.
- **F4 Breach returns:** detect new unknown sessions after cleanup → secure email and phone carrier accounts because recovery channels may be compromised.

## Verification

The account has a new unique password, strong 2FA, clean recovery methods, no unknown sessions or connected apps, and documented resolution of any unauthorized activity.

## Variations

- Financial accounts: also freeze cards, dispute transactions, and confirm transfer limits.
- Social accounts: review posts, messages, ad accounts, pages, and connected business tools.
- Developer accounts: rotate API keys, SSH keys, deploy tokens, webhooks, and OAuth apps.

## Safety & privacy

Medium risk because breach response involves identity, money, and private data. Do not share one-time codes with support callers, and preserve evidence before deleting suspicious messages or activity.
