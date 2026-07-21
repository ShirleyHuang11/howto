---
name: revoke-third-party-app-access
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Unknown, unused, or risky third-party app access is removed from important accounts, including OAuth grants, integrations, and connected devices.

## Preconditions

- You can log in to the account whose access you want to review.
- You know which apps or services you still use.
- You have a current password manager and two-factor authentication for important accounts.

## Steps

1. **Start with high-value accounts.** Review email, cloud storage, social, finance, password manager, and work accounts first. → *Expect:* you are in the account security or privacy settings.
2. **Find connected app settings.** Look for Security, Privacy, Apps with access, Third-party access, Integrations, Authorized apps, or Devices. → *Expect:* a list of apps, services, grants, or sessions appears.
3. **Open details for each item.** Check app name, publisher, permissions, last used date, and connected account. → *Expect:* you can tell what data each app can read or change.
4. **Classify each grant.** [BRANCH: known and still needed | unknown | unused | over-permissioned] Keep only grants that have a current purpose. → *Expect:* each item has a keep or revoke decision.
5. **Revoke unknown or unused access.** Click Remove, Revoke, Disconnect, or Delete access for items you do not recognize or no longer need. → *Expect:* the app disappears from the list or shows access revoked.
6. **Review OAuth scope warnings.** Pay special attention to grants that can read email, files, contacts, calendars, financial data, or act on your behalf. → *Expect:* broad grants are either justified or removed.
7. **Check active sessions and devices too.** Sign out old browsers, phones, TVs, and locations you do not use. → *Expect:* only current devices remain signed in.
8. **Repeat on linked accounts.** If an app connected Google to Dropbox, Slack, or Microsoft, review both sides when practical. → *Expect:* the same unused integration is not still alive elsewhere.
9. **Set a periodic re-check.** Add a quarterly or semiannual reminder for important accounts. → *Expect:* access review will happen again without relying on memory.

## Decision points

- [BRANCH: personal account | work account] Personal accounts can be changed directly; work accounts may require IT approval before revoking business integrations.
- App is unfamiliar but business-critical → ask the owner or support contact before revoking, then document the decision.
- App has broad read/write access but is still needed → see whether narrower permissions, service accounts, or official integrations exist.
- Recent unknown access appears after suspicious activity → change password, review 2FA, and check account recovery settings.

## Failure modes & recovery

- **F1 Broke a useful integration:** detect failed sync or automation; recover by reconnecting deliberately and choosing the narrowest permission set.
- **F2 Fake app name:** detect generic names, odd publishers, or recent unknown access; recover by revoking and reviewing account activity.
- **F3 Access list hidden:** detect no visible connected apps page; recover by searching provider help for "third-party access" plus the service name.
- **F4 Revoked on one side only:** detect app still shows connected elsewhere; recover by disconnecting from both the provider and the consuming app.

## Verification

The connected-app list contains only recognized, currently used apps, and high-risk grants for email, files, contacts, calendars, or financial data are either removed or explicitly justified.

## Variations

- `mobile-app`: some providers hide OAuth details on mobile, so use desktop web for full permission lists.
- Social accounts: also review ad tools, business pages, and developer apps.
- Cloud storage: check shared folders and public links after revoking apps.

## Safety & privacy

Medium risk because connected apps can keep access after you stop using them. Revoke first when uncertain, reauthorize only when needed, and treat unknown broad grants as account-security incidents.
