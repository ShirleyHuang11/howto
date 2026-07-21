---
name: factory-reset-a-device-safely
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: [have-admin-access]
status: draft
last_verified: 2026-07-20
---

## Goal

A device is wiped back to factory state with your data verifiably gone, your accounts deregistered so it is not locked to you (or to a previous owner), ready to sell, recycle, or hand on without leaking your information.

## Preconditions

- A current, verified backup of everything on the device you want to keep (see `digital/back-up-your-files`); the reset destroys local data permanently.
- The account passwords the device is tied to, so you can sign out and disable activation locks.
- Charger connected or a strong battery; a reset interrupted by power loss can brick the device.

## Steps

1. **Back up first and verify the backup opens.** Confirm your files, photos, and app data are safely copied and you have opened a sample. ⚠️ *Irreversible:* the reset erases local data with no undo; do not proceed on an unverified backup. → *Expect:* a verified backup exists off the device.
2. **Deregister and sign out of accounts.** ⚠️ *Irreversible:* leaving activation lock on (Find My / Google account / Samsung account) can render the wiped device unusable to the next owner. Turn off Find My, then sign out of the platform account and any DRM/store accounts. → *Expect:* the device no longer shows a linked owner account or activation lock.
3. **Remove tied hardware and licenses.** Unpair watches and accessories, deauthorize the machine from media/software licenses that count device slots, and note anything using device-bound authentication. → *Expect:* paired devices dropped; license count freed.
4. **Remove physical media and SIM.** Take out the SIM and any memory card so they do not leave with the device. → *Expect:* SIM and cards in your hand, slots empty.
5. **Confirm encryption is on, then reset.** Modern phones and laptops encrypt storage by default, which is what makes a reset actually unrecoverable. Verify encryption is enabled, then run the factory reset / erase-all-content from settings. → *Expect:* a warning listing what will be erased, then the device reboots into a wipe.
6. **Let the wipe finish untouched.** Do not interrupt power or force-restart during the erase. → *Expect:* the device boots to the initial "welcome / set up" screen, as if new.
7. **Verify the clean state.** Walk to (or just short of) the setup screen and confirm no account is pre-filled, no data or apps remain, and no activation lock prompts for a previous owner's credentials. → *Expect:* a genuinely empty device with no trace of your accounts.

## Decision points

- Old spinning hard drive (not SSD) → a settings reset may leave recoverable data; use a full-disk wipe tool or, for highly sensitive drives, physical destruction.
- Selling versus recycling → for recycling you can stop at a verified wipe; for selling, also complete step 2 fully so the buyer is not locked out.
- Device you cannot log into (forgot password, inherited) → use the platform's recovery to prove ownership before reset, or it will lock at the activation screen.

## Failure modes & recovery

- **F1 Device asks for the previous owner's account after reset:** activation lock was left on; the only fix is that owner signing in and removing it remotely, so always do step 2 before wiping.
- **F2 Reset hangs or the device won't boot:** power was interrupted or the OS is corrupt; use recovery mode to reinstall the OS and re-run the wipe.
- **F3 Realized the backup was incomplete after wiping:** local data is gone; recover only what a cloud service still holds. This is why step 1 verifies before step 5 erases.
- **F4 Data still recoverable on an old drive:** a quick format is not a wipe; run a proper erase pass or destroy the drive physically.

## Verification

The device boots to a factory setup screen with no accounts pre-filled, no activation or previous-owner lock, no residual data or apps, SIM and cards removed, and every account that was tied to it has been signed out and deregistered. Your verified backup holds everything you needed to keep.

## Variations

- `mobile-app`: phones bury Find My / activation lock in account settings; turning it off before the reset is the single most-forgotten step.
- Laptops: deauthorize media and software licenses that count installs before wiping, or you burn a license slot on a device you no longer own.

## Safety & privacy

High risk: this step is irreversible and, done wrong, either leaks your data to the next owner or locks the device forever. The two hard rules are verify the backup before wiping and deregister every account (especially activation lock) before the erase. Encryption plus a factory reset is what makes your data truly gone; a mere format on an old drive is not enough.
