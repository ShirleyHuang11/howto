---
name: recover-a-social-media-account
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You regain control of a locked, hacked, or inaccessible social media account and secure it so the problem does not immediately recur.

## Preconditions

- Access to any email address, phone number, authenticator, or device previously used with the account.
- A trusted device and network.
- Government ID only if the platform's official recovery process requires identity verification.

## Steps

1. **Start at the platform's official recovery page.** Type the site address or open the official app, then choose Forgot password, Get help logging in, or Hacked account. → *Expect:* the platform asks for username, email, or phone.
2. **Try known identifiers.** Enter username, old email addresses, current phone numbers, and profile URL if supported. → *Expect:* the platform finds the account or shows recovery options.
3. **Use the safest available verification method.** Prefer an email or authenticator you control; use SMS if that is the only option. → *Expect:* you receive a legitimate recovery code or link.
4. **Reset the password.** Choose a unique password and save it in a password manager. → *Expect:* the platform accepts the new password.
5. **Revoke unknown sessions and apps.** Go to Security, Login activity, Devices, Apps, or Connected accounts. → *Expect:* unfamiliar sessions and third-party apps are removed.
6. **Repair account details.** Restore your email, phone, username, bio links, and recovery settings if an attacker changed them. → *Expect:* contact and recovery information belongs to you.
7. **Enable two-factor authentication.** Use an authenticator app or security key if available, and save backup codes. → *Expect:* future sign-ins require a second factor.
8. **Notify contacts if abuse occurred.** Post or message a brief warning if scams, spam, or impersonation messages were sent. → *Expect:* contacts know not to trust suspicious recent messages.

## Decision points

- Account email was changed by an attacker → use "secure your account" or "this wasn't me" links from the platform's original email-change notice.
- Platform requests ID → upload only through the official recovery flow and check the URL/app carefully first.
- Account is a business or creator account → also review ad accounts, payment methods, page admins, and connected commerce tools.

## Failure modes & recovery

- **F1 Recovery code goes to attacker-controlled contact:** use an older trusted device, prior email-change notice, or identity verification path.
- **F2 Platform says no account found:** try exact username, profile URL, old phone formats, and old email addresses.
- **F3 Recovery link expired:** request a new link and complete it immediately from the same browser session.
- **F4 Account disabled for attacker activity:** appeal through the platform's disabled-account form and include concise evidence of compromise.

## Verification

You can sign in with the new password, only your contact methods and devices remain, two-factor authentication is enabled, and no unauthorized posts, messages, ads, or connected apps remain active.

## Variations

- `instagram-facebook`: Meta may offer hacked-account flows, selfie video, or ID review depending on account type.
- `x`: recovery may depend heavily on verified email/phone and appeals through Help Center forms.
- `tiktok`: check both Security alerts and Manage account for changed phone, email, and linked social accounts.

## Safety & privacy

Medium risk because compromised accounts can scam contacts and expose private messages. Do not pay "recovery agents," share codes, or upload ID outside the official platform flow.
