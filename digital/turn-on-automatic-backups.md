---
name: turn-on-automatic-backups
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Automatic backups are enabled for important files or a device, and a restore test proves the backup can actually recover data.

## Preconditions

- You know what must be backed up: photos, documents, desktop folders, app data, messages, or whole device.
- You have a backup destination with enough space: cloud account, external drive, network storage, or platform backup.
- You can keep the device powered and connected long enough for the first backup.

## Steps

1. **Choose cloud, local, or both.** [BRANCH: cloud backup | local drive backup | both] Use cloud for off-site protection and local drive for fast restore. → *Expect:* you know where backup copies will live.
2. **Open the backup settings.** Use OS settings, phone backup settings, cloud client, or backup software from a trusted provider. → *Expect:* a backup status page shows destinations and included data.
3. **Select what to include.** Add Documents, Desktop, Photos, key project folders, phone photos, messages, and app data that would hurt to lose. → *Expect:* included folders match your real priorities.
4. **Exclude disposable or risky items.** Skip caches, downloads, temporary files, and huge re-downloadable media unless you truly need them. → *Expect:* backup size fits the destination.
5. **Turn on automatic schedule or continuous sync.** Choose hourly, daily, when connected to power, or continuous depending on the tool. → *Expect:* settings show automatic backup enabled and a next run or active sync.
6. **Secure the backup.** Enable encryption for drives and use strong account protection for cloud backups. → *Expect:* the backup destination requires your account or password to access.
7. **Run the first backup now.** Keep the device awake, powered, and online until the initial run finishes. → *Expect:* status changes from running to completed, synced, or backed up.
8. **Perform a restore test.** Restore one small file to a temporary folder and open it. → *Expect:* the restored file opens and matches the original.
9. **Set a recurring check.** Add a monthly or quarterly reminder to verify last backup time and storage space. → *Expect:* backup health will be checked before a crisis.

## Decision points

- [BRANCH: computer | phone] Computers usually need folder selection; phones usually need account backup plus photo backup.
- Sensitive files in cloud backup → use provider security settings, encryption features, or local encrypted backup.
- Cloud quota is too small → upgrade storage, reduce included folders, or add a local drive.
- Backup destination is always plugged in → protect against ransomware with version history or periodic offline copies.

## Failure modes & recovery

- **F1 First backup never completes:** detect stuck progress; recover by connecting power, stable Wi-Fi, and enough storage, then restart backup.
- **F2 Important folder omitted:** detect missing file during restore test or folder review; recover by adding the folder and running backup again.
- **F3 Backup account locked out:** detect failed cloud login; recover by securing recovery email, phone, 2FA, and recovery codes.
- **F4 Restore fails:** detect missing, corrupt, or unreadable restored file; recover by trying another date/version and fixing the backup tool before relying on it.

## Verification

Backup status shows a recent successful automatic run, the selected important data is included, and at least one file has been restored and opened successfully.

## Variations

- `mobile-app`: enable photo/video backup separately from device settings if the platform separates them.
- External drive: leave it connected for scheduled backups, or set a reminder to connect it weekly.
- Family devices: each device needs its own automatic backup status, not just a shared cloud account.

## Safety & privacy

Medium risk because failed backups are often discovered after data loss. Encrypt backups, protect cloud accounts with 2FA, and test restores instead of trusting green checkmarks alone.
