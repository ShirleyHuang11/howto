---
name: set-up-a-new-phone
domain: digital
locale: [generic]
interface: mobile-app
difficulty: intermediate
est_time: 1h-2h
risk: medium
prerequisites: [digital/connect-to-wifi, digital/back-up-your-files]
status: draft
last_verified: 2026-07-20
---

## Goal

A new phone ends up holding your accounts, apps, messages, and photos as they were on the old phone, and the old phone is safely wiped only after the new one is confirmed complete.

## Preconditions

- Both phones charged above 50% (or plugged in) and on the same WiFi network.
- The old phone still working, or at least a recent cloud/computer backup of it.
- Your account passwords and your 2FA method available. The single most common lockout is losing an authenticator app during the move (see F3).

## Steps

1. **Back up the old phone first, on purpose.** iPhone: Settings > your name > iCloud > iCloud Backup > Back Up Now, or an encrypted Finder/iTunes backup to a computer. Android: Settings > System > Backup > Back up now (Google One). → *Expect:* a "last backup: just now" timestamp, not one from days ago.
2. **Note what backups miss.** Two-factor authenticator codes, some app logins (banking, WhatsApp), and eSIM often do NOT ride along in a generic backup. List these to handle by hand. → *Expect:* a short written list of apps you will re-authenticate manually.
3. **Handle authenticator apps before wiping anything.** Use the app's built-in transfer (Google Authenticator export, Authy multi-device) or move each 2FA to the new phone while the old one still works. → *Expect:* the new phone generates valid codes for at least one critical account before you go further.
4. **Start the new phone and use the direct transfer flow.** iPhone: Quick Start, hold the phones near each other. Android: "Copy apps & data" with the cable or wireless option. Choose restore-from-backup or device-to-device. → *Expect:* a transfer progress bar with an item count and a time estimate.
5. **Wait for the transfer to finish fully.** Keep both phones close, awake, and on power. Do not "skip" to use the phone early; apps re-download in the background for a while after. → *Expect:* progress reaches 100% and the new phone boots to a home screen resembling the old layout.
6. **Restore and verify each critical app by hand.** Open banking, messaging, email, and photos one at a time. Re-login where prompted, re-approve 2FA. Confirm messages and photos actually appear. → *Expect:* each critical app opens signed in with your real data visible, not an empty first-run screen.
7. **Move your phone number / eSIM.** Physical SIM: swap the tray. eSIM: use the carrier's eSIM transfer in Settings or the carrier app. Make a test call and send a test text. → *Expect:* the new phone shows signal and your number; a test call and text both go through.
8. **Confirm the new phone is complete before touching the old one.** Photos, contacts, messages, 2FA, apps, phone number all verified present. → *Expect:* a deliberate "yes, everything is here" check across all of the above.
9. **Wipe the old phone.** ⚠️ *Irreversible:* this erases the old phone permanently. Only after step 8 passes. Sign out of your account first (iPhone: turn off Find My / sign out of iCloud; Android: remove Google account) to release the activation lock, then Settings > Erase All Content and Settings. → *Expect:* the old phone reboots to the "Hello / welcome" first-time setup screen, holding none of your data.

## Decision points

- Old phone is broken or lost → skip device-to-device; restore from the most recent cloud backup instead, and expect to re-login more apps by hand.
- Switching platforms (iPhone to Android or back) → the native transfer does a partial job; use the vendor's switch app, and know that paid apps and some data (iMessage, app purchases) do not cross platforms.
- Not enough cloud storage for a backup → back up to a computer instead, or free space first (`digital/free-up-storage-space`).

## Failure modes & recovery

- **F1 Transfer stalls partway:** keep both phones awake, close, and charging; if truly stuck, restart the transfer. Device-to-device is resumable more often than it looks.
- **F2 App shows empty after restore:** many apps sync in the background; give it time on WiFi, then force-close and reopen. If still empty, re-login manually.
- **F3 Locked out of an account (lost 2FA):** this is why step 3 exists. Recover via the account's backup codes or provider recovery flow before you wipe the old phone, not after.
- **F4 Activation lock on the wiped phone:** you erased before signing out of the cloud account. Sign out remotely from the account website (Find My / Google) to release it.

## Verification

The new phone shows your contacts, messages, photos, signed-in apps, working 2FA, and your phone number with a successful test call and text; the old phone has been erased to its first-time setup screen only after all of that was confirmed.

## Variations

- `carrier-store`: staff can run the transfer for you, but do the 2FA and account-sign-out steps yourself so nobody else touches your credentials.
- Family / child phone: after transfer, set up parental controls and a separate account rather than cloning an adult's logins.

## Safety & privacy

Medium risk because it touches identity and money: accounts, 2FA, and a device full of personal data. The two hard rules: never wipe the old phone until the new one is verified complete, and sign out of your cloud account before erasing so the phone is not activation-locked. If you sell or hand on the old phone, the wipe (not just deleting apps) is what protects your data.
