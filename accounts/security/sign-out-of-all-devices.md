---
name: sign-out-of-all-devices
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

You invalidate active sessions across browsers, phones, tablets, and connected devices so only your current trusted session can regain access.

## Preconditions

- You can sign in to the account and complete 2FA.
- You have a current recovery email, phone, or backup codes in case the account asks you to sign in again.
- You know whether any household, work, or shared devices depend on the account.

## Steps

1. **Open the security or session page.** Look for Security, Login activity, Sessions, Devices, Where you're logged in, or Privacy and security. → *Expect:* the account shows active or recent sessions.
2. **Check for suspicious sessions before ending them.** Note unknown locations, devices, IP addresses, and times in case you need to report compromise. → *Expect:* suspicious details are recorded without clicking any unknown links.
3. **Use the global sign-out control.** Choose Sign out everywhere, Log out of all devices, End all sessions, or similar. → *Expect:* the account asks for confirmation or password re-entry.
4. **Confirm the action.** ⚠️ *Irreversible:* confirm you have recovery access first, because this may sign out your phone, TV, mail app, or authenticator prompts. → *Expect:* the provider confirms sessions were ended.
5. **Change the password if any session was unknown.** Set a unique password and keep it in a password manager. → *Expect:* old session cookies and saved passwords cannot be reused.
6. **Re-sign in only on trusted devices.** Start with your main device, then re-add phones or apps you still use. → *Expect:* each new session appears in the device list with a recognizable name and current timestamp.
7. **Review app passwords and connected apps.** Revoke old app passwords, unknown OAuth apps, and integrations that may keep access after browser sessions end. → *Expect:* no separate credential remains for an unknown device or app.

## Decision points

- You see a login from an impossible location → change the password and 2FA immediately after signing out.
- The account has no global sign-out button → manually sign out or remove each listed device.
- A work or school account is involved → follow organization policy and notify IT if compromise is suspected.

## Failure modes & recovery

- **F1 Current session is signed out too:** detect an unexpected login screen → sign back in using your recovery method and verify the session list.
- **F2 Mobile apps stay connected:** detect continued email or file sync → revoke app passwords and connected apps, not just browser sessions.
- **F3 Password change fails:** detect policy or lockout errors → use account recovery or contact the administrator before ending more sessions.
- **F4 Unknown session returns:** detect a new suspicious login after cleanup → rotate recovery methods, check forwarding rules, and contact provider support.

## Verification

The session list shows only newly authorized devices you recognize, old devices are signed out, and any suspicious session no longer has active access.

## Variations

- Email providers: IMAP/SMTP app passwords may survive a normal web sign-out and must be revoked separately.
- Streaming devices: some services take several hours to force TVs or consoles offline.
- Enterprise accounts: administrators may have audit logs and forced sign-out tools that are more complete than the user settings page.

## Safety & privacy

Medium risk because ending sessions protects private data but can disrupt access on important devices. Confirm recovery methods work before global sign-out, especially if your phone is the only 2FA method.
