---
name: back-up-your-phone
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Create a current phone backup and verify that the important data would be recoverable after loss, damage, or replacement.

## Preconditions

- The phone has enough battery or is plugged in.
- You know the phone passcode and account password.
- You have Wi-Fi for cloud backup or a computer and cable for local backup.

## Steps

1. **Choose backup location.** [BRANCH: cloud | computer] use cloud for automatic recovery, or a computer for local control and large backups. → *Expect:* you know where the backup will be stored.
2. **Check what is included.** Review whether photos, messages, contacts, app data, device settings, and health data are included. → *Expect:* critical categories are either included or handled separately.
3. **Free storage if needed.** Compare available cloud or computer storage with the estimated backup size. → *Expect:* there is enough space to finish the backup.
4. **Connect power and Wi-Fi.** Plug in the phone and connect to a trusted Wi-Fi network unless using a computer cable. → *Expect:* the backup will not fail from battery or cellular limits.
5. **Start the backup.** Use the phone's backup settings or the computer's device-management app. → *Expect:* progress starts or the phone reports a backup is queued.
6. **Keep the phone available.** Leave it locked or idle until the backup completes. → *Expect:* the backup finishes without interruption.
7. **Verify timestamp and size.** Open backup settings and confirm the latest backup date, time, and device name. → *Expect:* the newest backup is from today and belongs to this phone.
8. **Check separate apps.** Confirm chat apps, authenticator apps, banking apps, and photo services have their own backup or transfer plan if needed. → *Expect:* app-specific data is not assumed without evidence.
9. **Set cadence.** Turn on automatic backup or schedule a manual backup before travel, repairs, and phone upgrades. → *Expect:* the next backup will happen without relying on memory.

## Decision points

- Cloud storage is full → upgrade storage, delete unneeded backups, or use a computer backup.
- Photos sync separately → verify photo sync status in the photo app, not only phone backup settings.
- You use authenticator apps → confirm transfer or cloud backup before replacing the phone.
- A computer backup offers encryption → enable it when passwords, health data, or Wi-Fi settings matter.
- The phone is going for repair → back up, verify, then consider signing out or erasing only after recovery is confirmed.

## Failure modes & recovery

- **F1 Not enough storage:** detect backup paused or failed for space, recover by freeing storage or changing destination.
- **F2 Incomplete categories:** detect missing photos or messages in included list, recover by enabling that category or using app backup.
- **F3 Stale backup:** detect last backup older than expected, recover by running a manual backup on power and Wi-Fi.
- **F4 Computer trust failure:** detect the computer does not see the phone, recover by unlocking phone and approving trust prompt.
- **F5 App-specific loss:** detect apps that do not restore from device backup, recover by using each app's export or transfer tool.

## Verification

Backup settings show a completed backup from today for this phone, and your most important data categories are listed as included or separately backed up.

## Variations

- iPhone: iCloud backup and encrypted computer backup include different categories, so read the included-data list.
- Android: manufacturer, Google, and app backups may overlap but are not identical.
- Low storage phones: delete downloaded media after confirming cloud copies.
- Before travel: run a manual backup and verify it before leaving home Wi-Fi.

## Safety & privacy

Backups may contain photos, messages, passwords, health data, and location history. Protect the cloud account or computer account with a strong password and multi-factor authentication.
