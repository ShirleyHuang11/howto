---
name: remotely-wipe-a-lost-device
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: advanced
est_time: 30min
risk: high
prerequisites: [accounts/log-in, accounts/security/set-up-find-my-device]
status: draft
last_verified: 2026-08-25
---

## Goal

You erase a lost or stolen device remotely when recovery is unlikely and the data risk is greater than the chance of getting the device back.

## Preconditions

- Access to the account linked to the device.
- The device was previously enrolled in a find-my-device service or mobile-device-management system.
- Recent backups exist, or you accept that unsynced local data may be lost.

## Steps

1. **Confirm the device identity.** In the official recovery portal, match device name, model, serial number if shown, and last location. → *Expect:* you are looking at the exact missing device.
2. **Try lower-risk recovery actions first.** Use locate, play sound, lost mode, lock, or contact-message features if recovery is plausible. → *Expect:* the device is locked and marked lost, or you decide recovery is not realistic.
3. **Check backup status.** Confirm photos, documents, authenticator recovery, and important files are backed up or already synced. → *Expect:* you know what data will survive the wipe.
4. **Remove payment exposure where needed.** Suspend mobile wallets, transit cards, and carrier service if the phone is stolen. → *Expect:* payment and SIM misuse risk is reduced.
5. **Start the remote erase from the official portal.** ⚠️ *Irreversible:* confirm the device, account, backup status, and that you are ready to lose unsynced local data before choosing erase. → *Expect:* the portal accepts the erase request and shows it as pending or in progress.
6. **Record the confirmation.** Save the timestamp, device name, and any confirmation number or status message. → *Expect:* you have evidence that the erase was requested.
7. **Rotate critical credentials.** Change passwords for email, banking, password manager, and work accounts that were accessible on the device. → *Expect:* new sessions require fresh authentication.

## Decision points

- Device may be at home or a known safe location -> use sound, lock, and location before wiping.
- Device contains regulated work, medical, legal, or client data -> follow employer or legal incident-response rules immediately.
- Portal says erase will occur when the device comes online -> leave the request active and continue credential rotation.

## Failure modes & recovery

- **F1 Wrong device selected:** the listed devices have similar names -> stop before confirming erase, verify serial numbers in purchase records, and rename remaining devices later.
- **F2 Device is offline:** erase remains pending -> keep the request active, report stolen if appropriate, and change passwords now.
- **F3 Backups are missing:** you discover local-only files were not synced -> decide whether data exposure justifies erase despite data loss.
- **F4 Activation lock or factory reset confusion:** thief resets the device but it stays linked to your account -> do not remove it from your account until you understand the anti-theft implications.

## Verification

The official recovery portal shows the erase request as pending, in progress, or completed for the correct device, and critical account passwords have been changed after the request.

## Variations

- iOS and macOS: Find My can erase devices and may preserve Activation Lock after erase.
- Android: Google Find My Device can erase supported devices but may not erase removable storage on all models.
- Work-managed device: the employer's MDM administrator may need to perform or confirm the wipe.

## Safety & privacy

High risk because remote wipe can permanently destroy data and can affect anti-theft recovery. Use only official portals, explicitly confirm the target device before erase, and preserve police or insurance information before removing the device from your account.
