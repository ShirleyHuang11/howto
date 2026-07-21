---
name: export-your-data
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [have-account-access]
status: draft
last_verified: 2026-07-20
---

## Goal

You hold a complete, openable copy of your data from an online service (email, photos, documents, social account), extracted in a portable format, verified as readable, and stored somewhere durable.

## Preconditions

- You are logged in to the account you want to export, on a device with enough free disk space for the archive (check the estimated size first).
- A stable connection. Large exports can take hours and will resume poorly on flaky mobile data.
- Somewhere to put the result: an external drive or a backup location (see `digital/back-up-your-files`).

## Steps

1. **Find the account's export tool.** Look under Settings for "Export", "Download your data", "Takeout", or "Data & privacy". Most large platforms have a dedicated page. → *Expect:* a page listing which data categories you can include.
2. **Select scope and format deliberately.** Include what you actually want; deselect noise. Prefer open formats when offered (MBOX for mail, JSON or CSV for records, original-resolution for photos). → *Expect:* a summary showing selected categories and a chosen file type.
3. **Choose delivery and size chunking.** [BRANCH: download link by email | deliver to a linked cloud drive] Set a per-file split (2 GB is a safe default) so a single corrupt part does not sink the whole archive. → *Expect:* a confirmation that the export job has started.
4. **Wait for the job to finish.** Exports are queued and can take minutes to days depending on volume. → *Expect:* an email or on-page notice that the archive is ready, usually with a link that expires (often 7 days).
5. **Download every part before the link expires.** Verify each file's size matches what the page claims; a truncated download is the most common silent failure. → *Expect:* all parts on disk, sizes matching, no browser "failed" entries.
6. **Verify the archive opens.** Unzip it and open a sample from each category: a few emails, some photos at full resolution, one document. Do not trust an unopened zip. → *Expect:* sample files open correctly and look complete.
7. **Store it safely and record what it is.** Move the verified archive to your backup destination; encrypt it if it contains personal data. Name the folder with the service and date. → *Expect:* archive filed, dated, and included in your backup rotation.

## Decision points

- Leaving a platform permanently → export first, verify it opens, and only then delete the account (deletion is covered by that service's own flow, not this one).
- Export offers only a proprietary format → take it anyway, but also screenshot or PDF the handful of records you most need to read without the original app.
- Archive exceeds your free disk → export categories separately, or deliver straight to cloud storage with room.

## Failure modes & recovery

- **F1 Download link expired:** re-request the export; the job must usually be re-run from scratch, so start the re-download promptly this time.
- **F2 Zip is corrupt or won't extract:** re-download that part (the split in step 3 is why only one part is affected); if it persists, re-run the export with a smaller chunk size.
- **F3 Photos exported as low-resolution copies:** you picked a "storage saver" tier; look for an "original quality" option, or export from the source device instead.
- **F4 Export missing recent items:** the job snapshotted before your latest changes; re-run after the platform finishes indexing, typically a day.

## Verification

A dated archive of the selected data sits in your backup location, every part downloaded at full size, and you have personally opened a sample from each category and confirmed it is readable outside the original service.

## Variations

- `web`: desktop browser is far more reliable than mobile for multi-gigabyte downloads.
- Email specifically: MBOX imports into most desktop mail clients; keep one client that can open it so the archive stays useful.

## Safety & privacy

Medium risk: the archive concentrates your personal data into one file that is easy to lose or leak. Encrypt it before it leaves your control, delete the copy from any shared or public computer's Downloads folder, and never leave it sitting in an email inbox as your only copy.
