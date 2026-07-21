---
name: use-cloud-storage
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [have-account-access]
status: draft
last_verified: 2026-07-20
---

## Goal

You have a cloud storage account set up with a folder structure you can navigate, a clear understanding of whether it is syncing or backing up, and sharing permissions set so the right people have exactly the access you intend.

## Preconditions

- A cloud storage account with enough quota for what you plan to keep; check the free tier's limit against your needs.
- The desktop or mobile app installed if you want files to appear locally, or just a browser for web-only use.
- A sense of what goes here versus what stays a true backup (see `digital/back-up-your-files`).

## Steps

1. **Decide sync versus backup, because they are not the same.** Sync mirrors a folder across devices and the cloud; delete a file on one device and it vanishes everywhere. Backup keeps a separate protected copy. Cloud sync alone is not a backup. → *Expect:* you can state which of the two this account is doing for you.
2. **Design a shallow, named folder structure.** A few top-level folders by area (Documents, Photos, Projects, Shared) beat a deep maze. Name for how you will search later. → *Expect:* a top level you can scan in one screen.
3. **Choose what syncs to each device.** Use selective sync so a small laptop is not forced to hold your entire library; keep large archives cloud-only. → *Expect:* each device shows only the folders you chose, with free space intact.
4. **Understand "online-only" versus "available offline."** Files marked online-only download on open and need a connection; mark anything you need on a plane as available offline first. → *Expect:* a test online-only file downloads on open, and an offline-marked file opens with the network off.
5. **Set sharing permissions per item, most restrictive that still works.** Share a specific folder or file, choose view versus edit, and prefer named people over "anyone with the link." → *Expect:* the share dialog shows exactly who has access and at what level.
6. **Check link scope before sending.** ⚠️ *Irreversible:* a public "anyone with the link" share can be forwarded and indexed beyond your control; treat it as posting publicly and set an expiry or restrict to named accounts for anything private. → *Expect:* the link's audience matches your intent; sensitive items are not world-readable.
7. **Confirm sync health and review shares periodically.** Watch the app's sync status reach "up to date," and revisit the shared-items list to revoke access people no longer need. → *Expect:* sync status green; the shared list contains only current, intended recipients.

## Decision points

- Irreplaceable files (photos, records) → keep a real backup in addition to cloud sync, because a synced deletion or ransomware propagates everywhere.
- Collaborating with a team → share the parent folder with edit rights once, rather than re-sharing each new file inside it.
- Sensitive documents → restrict to named accounts, set link expiry, and consider a provider or client that encrypts before upload.

## Failure modes & recovery

- **F1 Deleted a file and it disappeared from every device:** sync propagated the delete; recover it from the provider's trash or version history within its retention window (often 30 days).
- **F2 Sync stuck or conflicting copies appear:** a file was edited in two places at once; open the "conflicted copy," merge by hand, and check that the app is signed in and not paused.
- **F3 Shared more than intended:** open the item's sharing panel, switch from "anyone with link" to named people or revoke the link entirely, then reissue a scoped one.
- **F4 Out of quota, uploads failing silently:** clear large cloud-only archives to another destination or upgrade the plan; verify uploads resume.

## Verification

The account has a shallow named folder structure, you can state whether each device is syncing or holding a backup, selective and offline settings behave as tested, every share shows exactly the intended people and access level with no unintended public links, and the app reports sync as up to date.

## Variations

- `mobile-app`: enable photo backup deliberately and confirm it uploads at full resolution rather than optimized copies.
- Business accounts: admin-managed sharing policies may override personal link settings; check the org defaults before assuming a link is private.

## Safety & privacy

Medium risk: cloud storage centralizes personal files and makes oversharing a single click away. Default to named-person access over public links, review shared items on a schedule, and never rely on sync as your only copy of anything irreplaceable. Store the account password in a manager and turn on two-factor authentication.
