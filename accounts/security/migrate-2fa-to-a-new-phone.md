---
name: migrate-2fa-to-a-new-phone
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You move two-factor authentication from an old phone to a new phone without losing access to important accounts.

## Preconditions

- You still have the old phone, the new phone, and account passwords.
- The new phone has the authenticator, password manager, or platform app you plan to use.
- You have backup codes or another recovery method for each critical account.

## Steps

1. **Make a list of protected accounts.** Include email, banking, password manager, cloud storage, work/school, social, government, and domain registrar accounts. → *Expect:* a checklist of accounts that use authenticator codes, push prompts, passkeys, or SMS.
2. **Back up the old phone and authenticator if supported.** Use the authenticator's encrypted backup or export feature only if you trust it and understand where the backup is stored. → *Expect:* the old 2FA data is backed up or export-ready before any removal.
3. **Install and secure the new authenticator.** Enable device lock, app lock if available, and cloud backup only with a strong account password. → *Expect:* the new phone can store 2FA secrets securely.
4. **Transfer authenticator entries.** Use the app's transfer feature or update each account's 2FA settings by scanning a new QR code on the new phone. → *Expect:* the new phone generates current codes for each migrated account.
5. **Test each account before removing the old phone.** Sign in using the new phone's code or push prompt. → *Expect:* the account accepts the new 2FA method.
6. **Update SMS and push-prompt settings.** Change the recovery phone number if needed and remove the old device from trusted prompt devices. → *Expect:* 2FA prompts and texts go only to devices or numbers you control.
7. **Save fresh backup codes.** Generate new backup codes after migration and store them in a password manager or secure offline place. → *Expect:* old backup codes are replaced or confirmed still valid.
8. **Remove 2FA data from the old phone only after testing.** ⚠️ *Irreversible:* do not erase, trade in, or factory reset the old phone until every critical login works from the new phone. → *Expect:* the old phone is no longer needed for account access.

## Decision points

- You no longer have the old phone → use backup codes, recovery email, or account recovery before changing anything else.
- Work or school account uses managed authentication → enroll the new phone through IT-approved steps.
- Authenticator export is unencrypted or unclear → manually re-enroll accounts instead of exporting secrets.

## Failure modes & recovery

- **F1 Code rejected:** detect invalid-code errors → check time sync on the new phone and re-scan the account's QR code.
- **F2 Account asks for old phone prompt:** detect prompts still going to the old device → remove the old trusted device and add the new one in security settings.
- **F3 Lost backup codes:** detect no working fallback during migration → pause and generate new codes from any still-signed-in session.
- **F4 Locked out during test:** detect no accepted 2FA method → use provider recovery immediately and keep proof of identity ready.

## Verification

Every account on the checklist accepts 2FA from the new phone, recovery codes are stored, and the old phone is removed from trusted 2FA prompt devices.

## Variations

- iOS/Android passkeys: some passkeys sync through iCloud Keychain, Google Password Manager, or a password manager rather than an authenticator app.
- Banking and government accounts: some require re-verification or a waiting period before a new 2FA device is trusted.
- Work accounts: Microsoft Authenticator, Okta Verify, Duo, and similar apps may require administrator reset if the old phone is gone.

## Safety & privacy

Medium risk because a mistake can lock you out of email, money, work, or identity services. Keep the old phone active until verification is complete, and do not share QR codes, one-time codes, or backup codes with anyone.
