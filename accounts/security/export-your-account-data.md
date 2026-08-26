---
name: export-your-account-data
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You request, download, and safely store a copy of your account data for backup, portability, review, or closure.

## Preconditions

- You can sign in and complete 2FA.
- You have enough secure storage for the export.
- You understand that exports may include private messages, files, location history, contacts, purchases, or identity data.

## Steps

1. **Open the data export page.** Look for Download your data, Export data, Privacy, Data portability, Takeout, or Account information. → *Expect:* the provider shows export options or a request form.
2. **Choose data categories deliberately.** Select the account history, files, messages, photos, contacts, receipts, settings, or logs you need. → *Expect:* the export scope matches your purpose without unnecessary sensitive data.
3. **Choose file format and delivery.** Pick common formats such as ZIP, JSON, CSV, MBOX, HTML, or original file formats; choose email link or cloud delivery only if secure. → *Expect:* the provider displays the format and destination.
4. **Submit the export request.** ⚠️ *Irreversible:* confirm the delivery email or storage destination before requesting, because the export may contain highly sensitive data. → *Expect:* the provider confirms the request and gives an estimated completion time.
5. **Wait for the official notification.** Large exports may take minutes to days. → *Expect:* a notification appears in the account or verified email when the export is ready.
6. **Download from the official account page.** Avoid forwarded links; sign in directly and download the archive. → *Expect:* the file downloads completely and matches the provider's expected size or parts.
7. **Verify and store securely.** Open the archive, confirm important data is present, then move it to encrypted storage or a secure backup location. → *Expect:* the export is readable and protected.
8. **Delete temporary copies.** Remove downloads from shared computers, browser download folders, and unencrypted temporary locations. → *Expect:* only the intended secure copy remains.

## Decision points

- Export is for account closure → verify the data before deleting or closing the account.
- Export contains regulated or sensitive data → store it encrypted and limit sharing.
- Provider offers API export and archive export → use the archive for human backup and API for structured migration only if you know the destination.

## Failure modes & recovery

- **F1 Export expires:** detect a download link no longer works → request a fresh export.
- **F2 Archive incomplete:** detect missing files or categories → review selected categories and request another export.
- **F3 File too large:** detect failed download or storage error → choose smaller categories, split archives, or use provider-supported cloud delivery.
- **F4 Cannot open format:** detect unreadable JSON, MBOX, or proprietary files → use standard viewers or request a different format if available.

## Verification

The downloaded export opens successfully, contains the selected data categories, is stored in a secure intended location, and temporary unencrypted copies are removed.

## Variations

- GDPR/UK GDPR and similar privacy laws: providers may label exports as data access or portability requests.
- Email accounts: MBOX exports require a mail client or viewer to inspect messages.
- Cloud photo/file services: original-quality exports can be much larger than expected.

## Safety & privacy

Medium risk because an account export can be a complete copy of your private life. Confirm the destination before requesting, encrypt long-term storage, and do not upload the archive to unknown converters or viewers.
