---
name: transfer-data-to-a-new-computer
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h-4h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Move your documents, photos, browser data, and application settings to a new computer, then verify the old computer still has an untouched copy until the transfer is proven complete.

## Preconditions

- You can sign in to both computers.
- You have a trusted network, external drive, or vendor migration tool available.
- You know which accounts, apps, and folders matter.

## Steps

1. **Update both computers.** Install pending system updates and restart before starting the transfer. → *Expect:* both computers are on the desktop with no restart pending.
2. **Inventory important data.** Check Desktop, Documents, Downloads, Pictures, Music, Videos, browser profiles, email archives, password manager, project folders, and license keys. → *Expect:* you have a short list of data and apps that must appear on the new computer.
3. **Choose a transfer method.** [BRANCH: Windows PC to Windows PC | Mac to Mac | mixed systems] use OneDrive or an external drive on Windows, Migration Assistant on Mac, or an external drive/cloud storage for mixed systems. → *Expect:* one method is selected and has enough storage or network access.
4. **Back up the old computer first.** Create a current backup with File History, Time Machine, or a full external-drive copy before migration. → *Expect:* the backup tool reports a successful backup from today.
5. **Run the transfer.** Start the selected tool, keep both devices awake and powered, and transfer user files before wiping or selling anything. → *Expect:* the new computer shows copied folders or the migration tool reports complete.
6. **Install missing apps.** Download apps only from official stores or vendor websites, then sign in and restore settings where available. → *Expect:* required apps launch and show your account or expected local data.
7. **Verify critical files.** Open samples from documents, photos, spreadsheets, browser bookmarks, email, and any work folders. → *Expect:* files open correctly and recent items are present.
8. **Keep the old computer unchanged.** Do not erase, trade in, or recycle the old computer until you have used the new one for at least a week. → *Expect:* the old computer remains available as a fallback.

## Decision points

- Work or school computer → follow the organization's migration policy before copying data.
- Passwords and authentication apps are involved → verify password manager and authenticator recovery before relying on the new computer.
- Huge photo or video library → prefer external drive or direct migration over slow cloud download.
- Mixed Windows/Mac transfer → copy standard files, then reinstall apps rather than moving application folders.

## Failure modes & recovery

- **F1 Transfer stalls:** detect no progress for 30 minutes → restart both computers and resume with the same tool or switch to an external drive.
- **F2 Files missing:** detect empty folders or old timestamps → compare against the inventory and copy the missing folders directly from the old computer.
- **F3 App will not open migrated data:** detect error on launch → install the latest app version and import the data through the app's File or Import menu.
- **F4 Cloud sync incomplete:** detect cloud icons still pending → keep the computer on Wi-Fi and power until the sync client says up to date.

## Verification

The new computer contains the inventoried folders, critical files open successfully, required apps launch, browser bookmarks are present, and the old computer plus backup remain available.

## Variations

- Windows: Settings > Accounts > Windows backup can sync some preferences, and OneDrive can move Desktop, Documents, and Pictures.
- Mac: Applications > Utilities > Migration Assistant can transfer from another Mac, Time Machine backup, or startup disk.
- Linux: copy the home directory selectively and reinstall packages from the distribution's package manager.

## Safety & privacy

Medium risk because personal files, passwords, and identity documents may be copied. Use encrypted drives for transfer media and wipe the old computer only after verification and a separate backup.
