---
name: share-a-large-file
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Send a large file by cloud link or transfer service while controlling who can access it and for how long.

## Preconditions

- The file is complete and saved locally or in cloud storage.
- Recipient email address or messaging channel.
- Permission to share the file contents.
- Internet connection suitable for upload.
- Knowledge of any size limit or confidentiality requirement.

## Steps

1. **Check file size and type.** Right-click or inspect file details, then note the extension and size. → *Expect:* you know whether ordinary email attachment limits will fail.
2. **Choose sharing method.** [BRANCH: cloud link | transfer service] Use cloud storage for ongoing collaboration and a transfer service for one-time delivery. → *Expect:* you have selected a service that supports the file size.
3. **Rename clearly.** Use a filename that identifies project, version, and date without sensitive secrets. → *Expect:* the recipient can recognize the file before opening it.
4. **Upload the file.** Place it in the chosen folder or transfer page and wait for upload completion. → *Expect:* the service shows upload complete or the file appears in storage.
5. **Set permissions.** Choose specific people when possible, otherwise set a restricted link with view or download rights only. → *Expect:* the access setting matches the intended recipients.
6. **Set expiry if available.** Add an expiration date for temporary links, especially for personal, financial, legal, or work files. → *Expect:* the link will stop working after the chosen date.
7. **Send the link.** Include file name, size, deadline, and any password in a separate channel if needed. → *Expect:* the recipient receives the link and context.
8. **Confirm access.** Ask the recipient to open or download the file before the deadline. → *Expect:* the recipient confirms successful access.
9. **Clean up access.** Remove the link, revoke broad sharing, or delete the transfer after confirmation. → *Expect:* the file is no longer exposed beyond the intended purpose.

## Decision points

- File will be edited by several people → use cloud storage with named-user permissions.
- File is a one-time delivery → use a transfer service with expiry.
- File contains sensitive data → encrypt it or use a secure portal required by the organization.
- Recipient cannot sign in → use a transfer service or request the correct external-sharing setting.
- File exceeds service limit → compress it, split it, or use a service with higher limits.

## Failure modes & recovery

- **F1 Upload stalls:** detect no progress for several minutes; recover by switching networks or uploading from a wired connection.
- **F2 Recipient denied:** detect "request access" messages; recover by adding the recipient email or changing link scope.
- **F3 Link too open:** detect "anyone with link can edit"; recover by changing to view-only or named recipients.
- **F4 File too large:** detect a size-limit error; recover by compressing, splitting, or choosing a large-file service.
- **F5 Wrong version sent:** detect outdated filename or content; recover by revoking the link and sending the corrected file with version label.

## Verification

The intended recipient can access the correct file, and the sharing settings show only the intended audience, permission level, and expiry.

## Variations

- `google-drive`: use Share, restricted access, and viewer/commenter/editor roles.
- `onedrive-sharepoint`: organization policies may block external links.
- `dropbox`: transfer links can expire separately from shared folders.
- `encrypted-zip`: share the password by phone or a separate message.
- `video-file`: compression may reduce quality, so confirm required resolution first.

## Safety & privacy

Large files often include more metadata than expected. Check file contents, names, comments, and embedded personal data before sharing, and revoke links after the recipient has what they need.
