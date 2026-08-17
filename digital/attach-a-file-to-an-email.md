---
name: attach-a-file-to-an-email
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Attach a file to an email so the recipient can download or view it.

## Preconditions

- The file exists on your device or cloud storage.
- You know the recipient is allowed to receive the file.

## Steps

1. **Open the draft.** Start a new email or open an existing draft. → *Expect:* the compose window is active.
2. **Choose attach.** Click or tap the paperclip, `Attach`, or `Insert file` control. → *Expect:* a file picker or attachment menu opens.
3. **Select the file.** Browse to the file, select it, and choose `Open`, `Attach`, or `Insert`. → *Expect:* the file name appears in the message as an attachment or upload.
4. **Wait for upload.** Do not send until any progress bar finishes. → *Expect:* the attachment shows complete, with no spinning indicator.
5. **Check size and access.** If the app converts it to a cloud link, confirm the link permissions allow only the intended recipient when possible. → *Expect:* the recipient can access the file without exposing it broadly.
6. **Send the email.** Add the recipient, subject, and body, then click or tap `Send`. → *Expect:* the message appears in Sent with the attachment or file link.

## Decision points

- File is too large → use the mail app's cloud-link option or a secure file-sharing service.
- File contains sensitive data → password-protect, encrypt, or share through an access-controlled link.
- Recipient needs to edit → share a cloud document with edit permission instead of a static attachment.

## Failure modes & recovery

- **F1 Upload not finished:** detect a progress bar or warning → wait, reconnect, or reattach before sending.
- **F2 Attachment blocked:** detect an error about file type → compress it, rename only if allowed, or use approved file sharing.
- **F3 Wrong file attached:** detect the file name or preview is wrong → remove it and attach the correct file.

## Verification

The sent email contains the correct file name, size or link, and access setting for the intended recipient.

## Variations

- `web`: drag a file into the compose window to attach in many webmail apps.
- `mobile-app`: use the paperclip, share sheet, or file icon, then choose from Files, Photos, Drive, or OneDrive.

## Safety & privacy

Attachments can leak personal, financial, medical, or work data. Check recipients and cloud permissions before sending, and avoid sending passwords in the same email as encrypted files.
