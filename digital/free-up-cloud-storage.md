---
name: free-up-cloud-storage
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your cloud storage has usable free space again because the largest files, backups, photos, and trash were reviewed instead of blindly upgraded.

## Preconditions

- You can sign in to the cloud storage account.
- You know which devices, backups, and apps use the account.
- You have another place to keep files before deleting them if they matter.

## Steps

1. **Open storage management.** Go to the provider's storage page for iCloud, Google, Microsoft, Dropbox, or your service. → *Expect:* a usage breakdown appears.
2. **Find the largest categories.** Sort by size or review storage by photos, drive files, mail, backups, and shared items. → *Expect:* one or two categories explain most usage.
3. **Review large files first.** Download, move, or delete videos, archives, duplicate exports, and installers you no longer need. → *Expect:* selected large items are removed or moved.
4. **Check photos and videos.** Delete obvious duplicates and long videos, or move originals to another backed-up location. → *Expect:* photo storage estimate drops or queued deletes appear.
5. **Review device backups.** Remove backups for old phones, tablets, or computers you no longer own. → *Expect:* backup storage no longer includes obsolete devices.
6. **Empty trash and recently deleted.** ⚠️ *Irreversible:* confirm the selected trash items are disposable before permanently deleting them. → *Expect:* storage is actually released after trash clears.
7. **Account for shared albums.** [BRANCH: owner | viewer] if you own shared items they may count against you; if you only view them they may not. → *Expect:* you know which shared content affects your quota.
8. **Decide prune or upgrade.** If needed files still exceed the plan, compare the monthly cost of upgrading with the time cost of ongoing pruning. → *Expect:* you choose a sustainable storage plan.

## Decision points

- Storage is mostly photos → handle videos and duplicate bursts before documents.
- Storage is mostly mail → delete large attachments and empty mail trash or spam.
- You need everything for records → upgrade may be more practical than risky deletion.

## Failure modes & recovery

- **F1 Space does not update:** detect quota unchanged after deletion, recover by emptying trash and waiting for provider recalculation.
- **F2 Deleted a needed file:** detect a missing document, recover from trash, version history, local sync, or another backup before emptying trash.
- **F3 Sync keeps reuploading files:** detect removed files returning, recover by deleting from the synced folder on all devices or changing sync settings.
- **F4 Backup stops after pruning:** detect device backup warnings, recover by freeing more space or increasing the plan before the next automatic backup.

## Verification

The storage dashboard shows enough free space for expected uploads and backups, with trash or recently deleted emptied only for confirmed disposable items.

## Variations

- `icloud`: device backups, iCloud Photos, Messages, and iCloud Drive often share one quota.
- `google`: Gmail, Drive, Photos, and backups can all count against account storage.
- `microsoft`: Outlook attachments, OneDrive files, and PC folder backup can share Microsoft storage.

## Safety & privacy

Cloud files may be the only copy of important records and family photos. Download or back up anything uncertain before permanent deletion, and remember that shared files may affect other people's access.
