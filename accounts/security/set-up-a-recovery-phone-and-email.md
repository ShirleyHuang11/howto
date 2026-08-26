---
name: set-up-a-recovery-phone-and-email
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

You add and verify recovery contact methods so you can regain account access without giving attackers an easy reset path.

## Preconditions

- You can sign in to the account.
- You control the recovery email inbox and phone number you plan to add.
- The recovery email itself has a strong password and 2FA.

## Steps

1. **Open recovery settings.** Go to Security, Account recovery, Personal information, Login and recovery, or Contact info. → *Expect:* the account shows current recovery email and phone fields.
2. **Review existing recovery methods.** Remove old work emails, inactive phone numbers, unknown contacts, and numbers you no longer control. → *Expect:* no stale or unfamiliar recovery method remains.
3. **Add a recovery email you control.** Enter a secure personal or backup email account that is not shared. → *Expect:* the provider sends a verification message or code.
4. **Verify the recovery email.** Open the recovery inbox directly and enter the code or confirm the verification link. → *Expect:* the account marks the recovery email as verified.
5. **Add a recovery phone if appropriate.** Enter a phone number you control long term, preferably not a temporary VoIP number if the service rejects those. → *Expect:* the provider sends an SMS or voice code.
6. **Verify the phone number.** Enter the code from the message or call. → *Expect:* the phone is marked verified or active.
7. **Check notification and reset behavior.** Confirm recovery methods are used for alerts and reset verification, not public profile display. → *Expect:* the recovery contacts are private and current.
8. **Store backup codes if offered.** Generate or refresh backup codes and save them securely. → *Expect:* you have a fallback if email or phone access fails.

## Decision points

- You recently changed phone numbers → keep both numbers only if you still control both; otherwise remove the old one immediately.
- The account is high value → use recovery email plus hardware key or authenticator, not phone-only recovery.
- The recovery email is less secure than the main account → secure the recovery email first.

## Failure modes & recovery

- **F1 Verification code never arrives:** detect no message after several minutes → check spam, blocked numbers, country code, and whether VoIP is unsupported.
- **F2 Old phone still listed:** detect resets can go to a number you lost → remove it and contact support if removal is blocked.
- **F3 Recovery email compromised:** detect unknown activity in the backup mailbox → secure that mailbox before trusting it for recovery.
- **F4 Shared email used:** detect multiple people can read the recovery inbox → replace it with an account only you control.

## Verification

The account shows a verified recovery email and, if used, a verified recovery phone that you control, with no stale or unknown recovery methods listed.

## Variations

- Financial accounts: phone and email changes may require a waiting period or customer-service confirmation.
- Work or school accounts: recovery methods may be managed through an identity portal such as Microsoft, Google Workspace, Okta, or Duo.
- Privacy-sensitive accounts: use a secure recovery email but avoid exposing a personal phone number unless required.

## Safety & privacy

Medium risk because recovery contacts can reset the account. Confirm every listed email and phone belongs to you, and never read verification codes aloud to someone who called you unexpectedly.
