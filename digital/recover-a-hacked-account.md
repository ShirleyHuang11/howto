---
name: recover-a-hacked-account
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Regain control of a compromised online account and reduce the chance that the attacker can re-enter.

## Preconditions

- You can use a clean device that you believe is not infected or signed in to the attacker.
- You still control at least one recovery method, such as email, phone, backup code, or identity document.
- You know the official sign-in or account recovery page for the service.
- You can contact close contacts through another trusted channel if needed.

## Steps

1. **Move to a clean device and network.** Use a trusted phone or computer, update the browser, and avoid links from suspicious emails. → *Expect:* you are on the service's official site or app.
2. **Change the password first.** Use the account security page or recovery flow to set a new unique password from a password manager. → *Expect:* the service confirms the password changed.
3. **Revoke active sessions.** Sign out of all devices, apps, browsers, and remembered logins. → *Expect:* the account lists only your current clean session afterward.
4. **Check recovery settings.** Remove unknown emails, phone numbers, security questions, forwarding rules, and backup addresses. → *Expect:* every recovery option belongs to you.
5. **Turn on two-factor authentication.** [BRANCH: authenticator app | security key | SMS] choose the strongest method available and save backup codes somewhere private. → *Expect:* future sign-ins require the second factor.
6. **Review connected apps and permissions.** Remove unknown third-party apps, tokens, mail clients, and browser extensions. → *Expect:* only services you recognize still have access.
7. **Inspect recent account activity.** Look for password changes, purchases, messages, posts, bank changes, or forwarding rules made during the compromise. → *Expect:* suspicious actions are identified for cleanup or reporting.
8. **Notify affected contacts.** Tell people who may have received scams from your account not to click links or send money. → *Expect:* key contacts know the compromise is contained.
9. **Secure related accounts.** Change passwords anywhere the old password was reused, starting with email, banking, and phone carrier accounts. → *Expect:* reused credentials no longer unlock other accounts.

## Decision points

- You cannot sign in or reset the password → use the official account recovery or hacked-account form.
- The attacker changed the recovery email or phone → gather proof of ownership before submitting recovery.
- Financial charges or identity documents are involved → contact the bank or relevant institution immediately.
- The clean device may also be infected → stop account work and use another device before continuing.

## Failure modes & recovery

- **F1 Reset loop:** detect by repeated recovery codes going to an attacker-controlled method, recover by using the service's compromised-account escalation path.
- **F2 Hidden email forwarding:** detect by contacts receiving replies you did not send, recover by deleting forwarding and filter rules.
- **F3 Reused password spread:** detect by login alerts on other services, recover by changing those passwords and enabling 2FA.
- **F4 Malicious app token:** detect by unknown connected app retaining access after password change, recover by revoking the app and rechecking sessions.

## Verification

The password is unique, unknown sessions and recovery methods are gone, 2FA is enabled, and recent activity shows no new unauthorized actions after the cleanup.

## Variations

- Social media: also review posts, ads, payment methods, and delegated page managers.
- Email account: inspect forwarding, filters, app passwords, and connected mail clients carefully.
- Work account: report to IT before deleting evidence because logs may matter.

## Safety & privacy

High risk because the account may expose identity, money, private messages, and contacts. Do not send ID photos or recovery codes through links from emails or chats; use only official recovery pages.
