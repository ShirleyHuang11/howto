---
name: turn-on-biometric-login
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You enable fingerprint, face, or device biometric login for faster access while keeping a strong account password and device lock.

## Preconditions

- Your device supports biometric unlock and has a secure screen lock set.
- You can sign in to the account normally.
- You understand that biometrics usually unlock a device-held credential rather than replacing the account password everywhere.

## Steps

1. **Secure the device lock first.** Set a strong passcode, PIN, or password on the phone or computer before enabling biometrics. → *Expect:* the device requires a secure fallback unlock method.
2. **Enroll biometrics at the device level.** Add your fingerprint or face in the operating system settings. → *Expect:* the device unlocks successfully with your biometric and fallback passcode.
3. **Open the account or app security settings.** Look for Biometric login, Face ID, Touch ID, fingerprint unlock, Windows Hello, passkey, or device unlock. → *Expect:* the app offers biometric login or passkey setup.
4. **Enable biometric login.** Confirm with your account password, 2FA, or device unlock as requested. → *Expect:* the app marks biometric login as enabled.
5. **Test lock and unlock.** Fully close or lock the app, then reopen and authenticate with the biometric method. → *Expect:* the app grants access only after a successful biometric or fallback unlock.
6. **Review fallback and recovery settings.** Confirm you still know the account password and have current recovery methods. → *Expect:* losing biometric access will not lock you out permanently.
7. **Remove biometrics for other users if needed.** On shared devices, ensure only authorized fingerprints or faces are enrolled. → *Expect:* no unauthorized user can unlock the app through the device.

## Decision points

- Device is shared with family or coworkers → avoid biometric login for sensitive accounts unless each user has separate OS accounts.
- Account is high value → use biometric login with 2FA or passkeys, not as the only protection.
- You are crossing a legal or workplace boundary where forced unlock is a concern → consider disabling biometrics temporarily and relying on the passcode.

## Failure modes & recovery

- **F1 Biometric prompt not offered:** detect password prompt only → update the app, enable device biometrics, or check whether the account supports the feature.
- **F2 Face or fingerprint fails repeatedly:** detect fallback required → use device passcode, then re-enroll biometrics in better lighting or with clean sensor contact.
- **F3 Shared biometric access:** detect another enrolled user can open the app → remove their biometric, use separate device accounts, or disable the feature.
- **F4 Forgot account password:** detect biometric works but password is unknown → reset and store the password before replacing the device.

## Verification

The app or account opens with biometric authentication on your device, still requires the device fallback lock when biometrics fail, and recovery methods remain current.

## Variations

- iOS/macOS: Face ID and Touch ID may unlock app sessions, passkeys, and password-manager entries.
- Android/Windows: biometric strength and app support vary by device and operating system version.
- Banking apps: biometric login may require periodic full password re-entry or SMS/app verification.

## Safety & privacy

Medium risk because anyone who can unlock the device may reach sensitive accounts. Keep the device passcode strong, do not enroll other people's biometrics on your device, and keep the account password stored securely.
