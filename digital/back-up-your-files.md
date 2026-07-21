---
name: back-up-your-files
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [have-admin-access]
status: draft
last_verified: 2026-07-20
---

## Goal

Your important files exist in at least two places besides the original device — one of them off-site — and you have proven you can restore from them.

## Preconditions

- You can name what matters: documents, photos, keys/credentials exports, project folders.
- At least one backup destination available: an external drive, and/or a cloud storage account with enough quota.

## Steps

1. **Inventory what to protect.** List the folders that would hurt to lose; check their total size. Exclude what's re-downloadable (installers, media libraries with accounts). → *Expect:* a short folder list and a size number that fits your destinations.
2. **Adopt the 3-2-1 shape.** 3 copies (original + 2 backups), 2 different media, 1 off-site. [BRANCH: cloud-first (sync tool + external drive) | drive-first (two drives, one stored elsewhere)] → *Expect:* you can say where each of the three copies will live.
3. **Set up the cloud/off-site copy.** Install the sync client (or enable the OS's built-in backup) and point it at the inventory folders. → *Expect:* initial upload running; the client shows progress and finishes with all folders marked synced.
4. **Set up the local copy.** Connect the external drive; use the OS backup tool (Time Machine / File History / rsync script) targeting the same inventory, scheduled automatically — manual copying is a backup plan that stops happening within a month. → *Expect:* first full backup completes; the schedule shows a next run time.
5. **Encrypt what leaves your control.** Turn on the drive's/OS's encryption for the external disk; confirm the cloud provider encrypts at rest (or use an encrypting client for sensitive folders). ⚠️ *Irreversible:* an encrypted backup with a lost password is destroyed data — store the backup password in your password manager *now*. → *Expect:* both destinations encrypted; password stored.
6. **Run a restore test — this is the step everyone skips.** Pick 3 random files, restore them from *each* destination to a temp folder, open them. → *Expect:* all restored files open correctly; you know the restore procedure cold.
7. **Schedule the off-site rotation and a periodic check.** Drive-first setups: swap the off-site drive on a recurring reminder (monthly). All setups: calendar a quarterly 5-minute check that both backups are current. → *Expect:* reminders exist; latest-backup timestamps are recent at each check.

## Decision points

- Sensitive data (tax, medical, keys) → encrypting client before cloud upload, not just provider-side encryption.
- Huge media collections exceed cloud quota → tier them: irreplaceable (photos) to cloud, replaceable media to the local drive only.
- Family devices → each device gets its own backup; a shared drive of manual copies is where family photos go to die.

## Failure modes & recovery

- **F1 Cloud sync silently stopped (quota full, auth expired):** this is why the quarterly check exists — fix the cause, verify it catches up, spot-restore again.
- **F2 External drive not recognized:** try another cable/port; if the drive is failing, replace it *immediately* and re-run the full backup — a backup system with a dead leg is one failure from loss.
- **F3 Ransomware/corruption synced into the backup:** use the destinations' version history (most cloud tools and OS backups keep versions) to restore pre-incident versions — versioning is the reason sync-only is not enough; verify yours keeps ≥30 days.

## Verification

Three current copies exist (original, local drive, off-site/cloud), a random-file restore succeeded from both backup legs within recent memory, the backup password is in the password manager, and automatic schedules show recent successful runs.

## Variations

- `mobile-app`: phone photos — enable the platform's photo backup and verify it's actually uploading (open the cloud gallery from another device).
- Developers: code belongs in remote git; the backup inventory covers what git doesn't (env files, local databases, keys — encrypted).

## Safety & privacy

Medium risk: backups concentrate your most sensitive data — encryption (step 5) is not optional for drives that leave the house. The failure mode that actually loses data is untested backups; step 6 is the core of the recipe.
