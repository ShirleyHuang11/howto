---
name: set-up-a-hardware-security-key
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Add a hardware security key to important accounts for phishing-resistant sign-in while preserving recovery access.

## Preconditions

- You have at least two compatible hardware security keys when the account allows backup keys.
- You can sign in to the account and access its security settings.

## Steps

1. **Choose priority accounts.** Start with email, password manager, financial, work, developer, and cloud accounts. → *Expect:* the first account to secure is identified.
2. **Check compatibility.** Confirm whether the account supports passkeys, FIDO2, WebAuthn, U2F, USB, NFC, or Lightning for your devices. → *Expect:* your key can work with the account and devices.
3. **Register the first key.** Open security settings, add a security key or passkey, touch the key when prompted, and name it clearly. → *Expect:* the account lists the key as registered.
4. **Register a backup key.** Add a second key and store it separately from the first. → *Expect:* loss of one key will not lock you out.
5. **Save recovery codes.** Download or copy backup codes to a password manager or offline secure place. ⚠️ *Irreversible:* removing other sign-in methods before recovery is tested can lock you out. → *Expect:* recovery material is stored before tightening settings.
6. **Test sign-in.** Sign out or use a private browser window and sign in with the key and recovery path. → *Expect:* both normal and backup access work.
7. **Tighten authentication.** Disable weaker methods only if the account supports safe recovery and you accept the lockout risk. → *Expect:* account security is stronger without single-point lockout.

## Decision points

- The account allows only one key → do not disable all other recovery methods.
- You travel often → keep one key with you and one in a secure separate location.
- The account is shared or managed → coordinate with administrators before changing authentication.

## Failure modes & recovery

- **F1 Key not recognized:** detect browser or device cannot read the key → recover by trying another port, NFC position, browser, or compatibility mode.
- **F2 Backup missing:** detect only one key registered → recover by adding a second key before enforcing strict login.
- **F3 Lockout risk:** detect recovery codes are missing or untested → recover by generating new codes and testing before removing weaker factors.

## Verification

The account lists at least one working hardware key, a backup key or recovery path is stored and tested, and sign-in succeeds using the key.

## Variations

- `mobile-app`: NFC keys may need the phone unlocked and held near the reader area.
- `work`: administrator policies may require managed keys or enrollment records.
- `passkeys`: some platforms sync passkeys; hardware-bound keys provide a separate security model.

## Safety & privacy

High risk because authentication changes can lock you out of critical accounts. Keep backup keys and recovery codes secure, and never register a key on a phishing page reached from an unsolicited link.
