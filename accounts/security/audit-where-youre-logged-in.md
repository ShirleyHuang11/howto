---
name: audit-where-youre-logged-in
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: basic
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You review every active login session for an account, keep only the sessions you recognize, and remove access from old or suspicious devices.

## Preconditions

- You can sign in to the account and pass any two-factor prompt.
- You have your current phone or authenticator available.
- You are using a trusted device and network.

## Steps

1. **Open the account security page.** Sign in and go to settings labeled Security, Privacy, Account access, Devices, Sessions, or Login activity. → *Expect:* a list of signed-in devices, browser sessions, or recent activity appears.
2. **Identify your current session first.** Match the current browser, device type, approximate location, and latest activity time. → *Expect:* you know which entry is the session you are actively using.
3. **Review each remaining session.** Check device names, operating systems, apps, IP locations, and last-used dates. → *Expect:* every session is marked mentally as recognized, old, or suspicious.
4. **Sign out old sessions.** Remove sessions from sold devices, borrowed computers, old phones, and unused apps. → *Expect:* the list shrinks to only sessions you still need.
5. **Remove suspicious sessions immediately.** Use Sign out, Revoke, Remove device, or Log out of all other sessions for anything you do not recognize. → *Expect:* the suspicious entry disappears or shows revoked.
6. **Change the password if anything looked wrong.** Choose a unique password from your password manager and save it. → *Expect:* the account accepts the new password and old sessions are forced to reauthenticate.
7. **Check recovery and two-factor settings.** Confirm the recovery email, phone, authenticator, and backup codes are yours. → *Expect:* only your current recovery methods can regain access.
8. **Record the audit.** Note the date and any sessions removed in your password manager or private security log. → *Expect:* you have a short record for future comparison.

## Decision points

- Unknown login from a distant location → revoke it, change the password, and review recovery methods.
- Session belongs to a shared work or school device → sign out unless policy requires it.
- Account offers "sign out everywhere" → use it after confirming you can still receive two-factor prompts.

## Failure modes & recovery

- **F1 Current session removed:** detect that you are logged out unexpectedly → sign in again using your password and two-factor method.
- **F2 Security page hides details:** detect only vague device labels → remove anything old or unclear, then watch for forced reauthentication.
- **F3 Password change fails:** detect rejection or rate limits → wait, use the account recovery flow, and try from a trusted device.
- **F4 Recovery method is unfamiliar:** detect an email or phone you do not control → remove it after adding a verified replacement.

## Verification

The account's devices or sessions page shows only recognized current devices, suspicious sessions are gone, and recovery plus two-factor methods belong to you.

## Variations

- `google`: check Security > Your devices and Third-party apps with account access.
- `apple`: check Account Settings > Devices and remove any device you no longer own.
- `workplace`: managed accounts may require an administrator to revoke sessions or reset credentials.

## Safety & privacy

Medium risk because active sessions can expose identity, money, private messages, and files. Confirm you have working two-factor access before signing out everywhere or changing recovery settings.
