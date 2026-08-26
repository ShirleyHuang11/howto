---
name: set-up-a-hardware-security-key
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

You add a hardware security key to an account so sign-ins require a physical key that phishing pages cannot easily steal.

## Preconditions

- You can sign in to the account and complete current 2FA.
- You have at least one FIDO2/WebAuthn-compatible security key, and preferably two.
- Your browser, phone, or computer supports USB, NFC, or Bluetooth for the key type.

## Steps

1. **Open the account's 2FA settings.** Go to Security, Two-step verification, Passkeys, Security keys, or Multi-factor authentication. → *Expect:* the account offers an option to add a security key or passkey.
2. **Choose hardware security key enrollment.** Select Security key, FIDO2 key, WebAuthn key, or physical key rather than SMS. → *Expect:* the site prompts you to insert, tap, or activate the key.
3. **Register the primary key.** Insert or tap the key, touch its sensor or button, and set a PIN if the platform requires one. → *Expect:* the account confirms the key was added.
4. **Name the key clearly.** Use a label such as "YubiKey USB-C on keyring" or "Backup key in safe." → *Expect:* the device list shows a recognizable key name.
5. **Register a backup key.** Add a second key and store it separately from the first. → *Expect:* at least two keys are listed, reducing lockout risk.
6. **Save backup codes and review fallback methods.** Generate fresh recovery codes and remove weak fallback methods only if you still have a reliable recovery path. → *Expect:* recovery remains possible without relying only on SMS.
7. **Test sign-in with the key.** Sign out or use a private browser window, then sign in using the hardware key. → *Expect:* the account accepts the key and shows the expected logged-in page.

## Decision points

- Account allows only one key → keep backup codes and a strong recovery method before relying on the key.
- You are protecting a high-value account → register two or more keys and remove SMS fallback if the provider allows safer alternatives.
- The key is shared or secondhand → reset it with the manufacturer's tool before enrollment.

## Failure modes & recovery

- **F1 Browser cannot see the key:** detect no prompt after insertion → try another port, cable, browser, or NFC position.
- **F2 PIN forgotten:** detect repeated PIN failures → use a backup key or backup codes; resetting the key erases its credentials.
- **F3 Key not accepted on mobile:** detect sign-in failure on phone → enroll an NFC-capable key or add a synced passkey as a fallback.
- **F4 Only key is lost:** detect no available hardware key → use backup codes or account recovery and enroll new keys immediately.

## Verification

The account lists the primary and backup hardware keys by name, a test login succeeds with a key, and recovery codes are stored separately.

## Variations

- Passkeys: some providers display hardware keys and synced passkeys on the same page, but a hardware key remains a physical possession factor.
- Enterprise accounts: administrator policy may require a specific key type, PIN length, or attestation.
- Mobile-only services: enrollment may require the official app instead of a desktop browser.

## Safety & privacy

Medium risk because losing all enrolled keys and backup methods can lock you out. Keep a backup key in a separate secure location, never lend a key for someone else's account, and do not remove all fallback methods until the key has been tested.
