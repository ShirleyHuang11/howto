---
name: transfer-a-messaging-app-to-a-new-phone
domain: digital
locale: [generic]
interface: mobile-app
difficulty: intermediate
est_time: 45min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your messaging app moves to a new phone with account verification, restored chats, and checked media, while the old phone is preserved until the transfer is confirmed.

## Preconditions

- The old phone still works and has the messaging app installed.
- The new phone has the same phone number, SIM, eSIM, or account access needed for verification.
- You know the cloud account and backup password or recovery key if encrypted backup is enabled.

## Steps

1. **Back up on the old phone first.** Open the app's backup settings and run a fresh backup before installing or verifying on the new phone. → *Expect:* the backup screen shows a successful backup dated today.
2. **Keep the old phone unchanged.** Do not delete the app, erase the phone, or trade it in yet. → *Expect:* the old chat history remains readable.
3. **Install the app on the new phone.** Download the same messaging app from the official app store. → *Expect:* the app opens to sign-in or phone verification.
4. **Verify the number or account.** Enter the phone number or account and complete SMS, call, passkey, or email verification. → *Expect:* the app recognizes the account.
5. **Choose restore or transfer.** [BRANCH: cloud restore | direct phone transfer] select the method your app offers and sign in to the matching cloud account if needed. → *Expect:* the app finds the backup or begins device transfer.
6. **Wait for chat restore.** Keep both phones charged and near Wi-Fi until messages finish restoring. → *Expect:* recent conversations appear on the new phone.
7. **Check media separately.** Open several older chats and confirm photos, videos, voice notes, and documents are present or downloading. → *Expect:* important media either appears or shows a clear download state.
8. **Confirm before wiping old phone.** ⚠️ *Irreversible:* erase or trade in the old phone only after chats, contacts, groups, and media have been checked on the new phone. → *Expect:* the old phone is no longer needed for recovery.

## Decision points

- The app warns that verifying will disconnect the old phone → stop until the backup is complete and visible.
- Moving between iPhone and Android → use the app's official cross-platform transfer path, not only cloud restore.
- Media is optional but important → keep the old phone until the oldest important media opens on the new phone.

## Failure modes & recovery

- **F1 Backup not found:** detect when the new phone says no backup exists, recover by checking the cloud account, phone number, and platform compatibility.
- **F2 Verification code missing:** detect no SMS or call, recover by checking signal, SIM activation, spam filters, and waiting for the retry timer.
- **F3 Chats restore but media missing:** detect blank thumbnails or unavailable files, recover by leaving the app on Wi-Fi and checking whether media was included in backup.
- **F4 Old phone erased too soon:** detect missing history after the old phone is gone, recover from any cloud backup available, but accept that non-backed-up data may be lost.

## Verification

The new phone can send and receive messages in the account, recent chats are present, and sampled older media opens before the old phone is erased.

## Variations

- `whatsapp`: use the current official backup or transfer-chat flow for your platform pair.
- `signal`: use the app's device transfer or local backup process before registering the new phone.
- `telegram`: cloud chats usually reappear after sign-in, but secret chats do not transfer like normal cloud chats.

## Safety & privacy

This is high risk because verifying on a new phone can change account state and erasing the old phone can permanently remove local-only chats. Back up first, keep both phones until verification passes, and protect codes and recovery keys.
