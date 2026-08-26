---
name: move-a-passkey-to-a-new-device
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You set up passkey sign-in on a new phone, computer, password manager, or security key, then remove passkeys tied to devices you no longer use.

## Preconditions

- You can still sign in on the old trusted device or with another recovery method.
- The new device has screen lock enabled and is signed in to its platform account if using iCloud Keychain, Google Password Manager, Windows Hello, or a password manager.
- You know whether the service allows multiple passkeys.

## Steps

1. **Sign in using a current trusted method.** Open the account's Security or Sign-in methods page. → *Expect:* you can manage passkeys without starting account recovery.
2. **Find the passkey section.** Look for Passkeys, Security keys, Passwordless sign-in, or FIDO credentials. → *Expect:* existing passkeys are listed with device names or creation dates.
3. **Add the new passkey before deleting the old one.** Select Add passkey or Create passkey, then approve on the new device, password manager, or hardware security key. → *Expect:* the service confirms a new passkey was created.
4. **Name the passkey clearly.** Use a label such as "iPhone 16 Aug 2026" or "YubiKey USB-C". → *Expect:* you can distinguish old and new credentials later.
5. **Test sign-in in a private window or second browser.** Choose passkey sign-in and complete biometric, PIN, or security-key approval on the new device. → *Expect:* the new passkey signs in successfully.
6. **Add a backup method if available.** Keep another passkey, authenticator, recovery code, or hardware key in case the new device is lost. → *Expect:* at least one alternate recovery path is active.
7. **Remove obsolete passkeys.** ⚠️ *Irreversible:* only delete a passkey after the new one has been tested and recovery methods are confirmed. Remove passkeys for sold, lost, or reset devices. → *Expect:* old credentials no longer appear in the account.
8. **Update your password manager note.** Record where active passkeys live and where backup codes are stored. → *Expect:* you can recover the account without guessing later.

## Decision points

- Service supports synced passkeys → adding on one device may make it available on devices in the same Apple, Google, Microsoft, or password-manager account.
- Service only supports hardware security keys → enroll at least two keys before removing the old one.
- Old device is already lost → use account recovery, then revoke all passkeys tied to that device.

## Failure modes & recovery

- **F1 New device prompt never appears:** check Bluetooth, same platform account, nearby-device prompts, and browser support → retry from the account security page.
- **F2 Passkey test fails:** keep the old passkey, add a different method, and check whether the site requires the same browser profile.
- **F3 Deleting old passkey locks out sign-in:** use backup codes, authenticator, password recovery, or support verification.
- **F4 Device label is ambiguous:** compare creation dates and last-used times → delete only after testing the intended replacement.

## Verification

A fresh sign-in succeeds using the new passkey, the account lists that passkey as active, and obsolete passkeys are removed only after a backup method is confirmed.

## Variations

- `ios-macos`: passkeys may sync through iCloud Keychain when the same Apple Account and Keychain are enabled.
- `android-chrome`: passkeys may sync through Google Password Manager on devices signed in to the same Google account.
- `enterprise`: work accounts may block synced passkeys and allow only managed devices or hardware keys.

## Safety & privacy

Medium risk because deleting the last working passkey can lock you out. Do not remove old passkeys until a new one has been tested from a separate sign-in flow and recovery methods are current.
