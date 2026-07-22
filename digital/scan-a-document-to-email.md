---
name: scan-a-document-to-email
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min-20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A paper document is scanned into a readable PDF and sent to the intended email recipient.

## Preconditions

- A scanner or multifunction printer, the document, and an email account that can send attachments.
- Permission to scan and email the document, especially for IDs, medical records, legal papers, or financial records.

## Steps

1. **Prepare the pages.** Remove staples, smooth folds, align page order, and decide whether the pages are one-sided or two-sided. → *Expect:* pages feed or lie flat without clips or curled corners.
2. **Choose glass or feeder.** [BRANCH: scanner glass | automatic feeder] Use glass for fragile, small, or bound pages; use the feeder for clean loose pages. → *Expect:* the first page is positioned against the corner mark or loaded face-up or face-down as labeled.
3. **Select PDF output.** In the scanner app, printer screen, or computer scan utility, choose PDF for documents and JPEG only for photos. → *Expect:* the preview or settings panel shows PDF as the file type.
4. **Set readable quality.** Use 200 to 300 dpi for normal text, grayscale for forms, and color only when color marks matter. → *Expect:* the estimated file size stays reasonable for email.
5. **Scan the pages.** Start the scan and add pages when prompted, keeping the same orientation. → *Expect:* each page appears in preview without cut-off edges.
6. **Check and save.** Rotate pages, delete blanks, name the file clearly, and save it somewhere you can find. → *Expect:* one PDF opens locally with all pages in order.
7. **Send by email.** [BRANCH: scan-to-email | save-then-attach] Use scan-to-email only if the printer is already configured; otherwise attach the saved PDF from your mail app. → *Expect:* the email draft contains the PDF attachment.
8. **Confirm recipient and send.** Check the address, subject, and attachment before sending. → *Expect:* the sent-mail folder shows the message with the PDF attached.

## Decision points

- File is larger than the mail service limit → lower dpi, switch color to grayscale, compress the PDF, or use a secure file link.
- Document has confidential data → prefer save-then-attach from your own mail account over a shared printer address book.
- Feeder pulls crooked pages → use the glass for the important pages rather than rescanning bad feeder output repeatedly.

## Failure modes & recovery

- **F1 Cut-off scan:** detect missing margins in preview, recover by realigning to the corner mark and scanning with auto-crop disabled.
- **F2 Feeder jam or double feed:** detect a stuck page or skipped page number, recover by removing the stack, fanning pages, and scanning smaller batches.
- **F3 Email bounces:** detect a bounce or attachment-size error, recover by reducing file size or sending a link with recipient access.
- **F4 Wrong page order:** detect reversed or mixed pages in the PDF, recover by reordering in the scan app before sending.

## Verification

The sent email contains a PDF that opens, has every intended page in order, and is readable at normal zoom.

## Variations

- iPhone or iPad: Files and Notes can scan documents with the camera and produce a PDF.
- Android: Google Drive, Files, or the printer maker app can scan to PDF from the camera or scanner.
- Office copier: scan-to-email may require signing in at the device before the address book appears.

## Safety & privacy

Scans can expose signatures, account numbers, addresses, and IDs. Verify the recipient before sending, avoid public shared copiers for sensitive records, and delete local copies when retention is not needed.
