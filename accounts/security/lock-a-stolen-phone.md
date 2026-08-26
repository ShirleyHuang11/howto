---
name: lock-a-stolen-phone
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: [accounts/log-in, accounts/security/set-up-find-my-device]
status: draft
last_verified: 2026-08-25
---

## Goal

You quickly lock a stolen phone, reduce account and payment exposure, and preserve the option to recover or erase it later.

## Preconditions

- Access to your Apple, Google, Samsung, carrier, or work account from another device.
- The stolen phone is enrolled in a recovery service if possible.
- A trusted phone or computer for account changes.

## Steps

1. **Get to a safe place before acting.** Do not chase or confront a thief. → *Expect:* you can work from a secure location with another device.
2. **Open the official find-my-device portal.** Sign in using a trusted browser or borrowed device in private mode. → *Expect:* the stolen phone appears in the device list, if it is reachable.
3. **Enable lost mode or remote lock.** Add a short callback message only if safe, and do not include your home address. → *Expect:* the portal shows the phone as locked, lost, or secured.
4. **Suspend payment cards and wallet access.** Use the wallet provider, bank app, or card issuer to suspend cards loaded on the phone. → *Expect:* mobile wallet transactions from that device are blocked or cards are removed.
5. **Contact the carrier to suspend the SIM or eSIM.** Ask for the line to be suspended for theft and request a replacement SIM or eSIM. → *Expect:* the carrier confirms service is suspended on the stolen phone.
6. **Change passwords for critical accounts.** Start with email, password manager, banking, and work accounts. → *Expect:* existing sessions are revoked where the service supports it.
7. **Decide whether to erase.** ⚠️ *Irreversible:* if the phone contains sensitive data and recovery is unlikely, confirm backups and use the remote wipe recipe. → *Expect:* you either keep lost mode active or start a documented erase request.

## Decision points

- Phone location shows a private residence or moving target -> do not go there yourself; provide information to police if filing a report.
- You need the phone number for account recovery -> move the number to a replacement SIM before changing accounts that require SMS codes.
- Work phone or work data is involved -> notify IT or security immediately.

## Failure modes & recovery

- **F1 Portal cannot locate the phone:** device is offline -> keep lost mode pending, suspend SIM, and rotate passwords.
- **F2 You lose access to SMS codes:** carrier suspension blocks login codes -> move the number to a new SIM or use backup codes and recovery methods.
- **F3 Thief uses unlocked session:** suspicious account activity appears -> revoke sessions, change passwords, and report fraud to affected services.
- **F4 Wallet suspension is incomplete:** cards still show active elsewhere -> contact issuers directly, not only the device wallet.

## Verification

The recovery portal shows the phone locked or marked lost, the carrier confirms the line is suspended or transferred, and critical account passwords or sessions have been secured.

## Variations

- iPhone: use Find My iPhone Lost Mode and Apple Wallet card suspension.
- Android: use Google Find My Device Secure device; Samsung devices may also support Samsung Find.
- Corporate phones: mobile-device-management policy may lock, wipe, or locate the phone through IT.

## Safety & privacy

High risk because theft can expose identity, money, location, and work data. Do not confront a thief, do not publish live location, and confirm backups before any wipe.
