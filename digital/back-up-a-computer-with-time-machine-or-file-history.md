---
name: back-up-a-computer-with-time-machine-or-file-history
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 45min-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create an automatic computer backup using Time Machine on Mac or File History on Windows, then verify that files can be restored.

## Preconditions

- You have an external drive with enough capacity for the computer's important files.
- You can connect the drive directly or through a trusted dock.
- You understand that backup drives should be dedicated to backups.

## Steps

1. **Connect the backup drive.** Plug in the external drive and wait for the operating system to recognize it. → *Expect:* the drive appears in Finder, File Explorer, or system backup settings.
2. **Start the backup setup.** [BRANCH: Mac | Windows] open System Settings > General > Time Machine on Mac, or Settings > System > Storage > Advanced storage settings > Backup options/File History on Windows. → *Expect:* the OS shows backup destination options.
3. **Select the backup drive.** Choose the external drive as the backup destination. ⚠️ *Irreversible:* formatting or erasing the drive deletes its existing contents, so confirm it contains nothing you need first. → *Expect:* the drive is assigned to Time Machine or File History.
4. **Enable encryption if offered.** Turn on encrypted backups and store the password in a password manager. → *Expect:* the backup settings show encryption enabled or the password is stored before the first backup proceeds.
5. **Choose included folders.** Confirm Documents, Desktop, Pictures, and other important user folders are included, and exclude only files you can replace. → *Expect:* the backup scope covers critical data.
6. **Run the first backup.** Start the backup and keep the computer awake and connected to power until it finishes. → *Expect:* backup progress completes without errors.
7. **Restore a test file.** Use Time Machine or File History to restore a copy of a harmless file to a temporary folder. → *Expect:* the restored file opens correctly.
8. **Set a backup routine.** Leave automatic backups enabled and connect the drive on a predictable schedule if it is not always attached. → *Expect:* settings show the latest backup time and future backups are automatic or scheduled.

## Decision points

- Laptop rarely stays plugged in → schedule a weekly backup reminder.
- Drive contains old files → copy them elsewhere before allowing the backup tool to erase or repurpose the drive.
- Sensitive files exist → encrypted backup is required.
- One backup is not enough → add cloud or off-site backup for disaster recovery.

## Failure modes & recovery

- **F1 Drive not recognized:** detect missing drive in backup settings → try another cable, port, enclosure, or disk utility check.
- **F2 Not enough space:** detect backup fails for capacity → use a larger drive or exclude replaceable folders.
- **F3 Encryption password lost:** detect password unavailable → create a new encrypted backup and store the new password securely.
- **F4 Restore fails:** detect restored file will not open → rerun backup to a healthy drive and test again.

## Verification

Backup settings show a successful backup from today, encryption is enabled when sensitive data is present, and a test restore opens correctly from the backup.

## Variations

- Mac: Time Machine can back up to local drives and supported network destinations.
- Windows: File History protects user libraries; use system image or other tools if you need full-system recovery.
- Desktop computer: keep the backup drive connected if theft and power risks are acceptable.

## Safety & privacy

Medium risk because backup drives contain private files and may be erased during setup. Encrypt the drive and keep it physically secure.
