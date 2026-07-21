---
name: upload-a-document-to-a-portal
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

A required document is uploaded to the correct portal field in the accepted format, readable quality, and confirmed as received.

## Preconditions

- You can log in to the real portal for the school, employer, bank, insurer, agency, or service.
- The document is available as a clean PDF, JPG, or PNG on your device.
- You know which document category the portal requested.

## Steps

1. **Open the portal from a trusted route.** Type the site address, use a bookmark, or start from the organization's official page. → *Expect:* the portal domain and login branding match the organization.
2. **Read the upload requirements first.** Check allowed file types, maximum size, page count, naming rules, and whether color is required. → *Expect:* you can state the exact limits before selecting a file.
3. **Inspect the document locally.** Open it and zoom to the smallest text, stamps, signatures, and corners. → *Expect:* every page is upright, complete, readable, and not cropped.
4. **Prepare the file to fit the limits.** Rename it clearly, combine pages into one PDF if requested, or compress only enough to meet the size cap. → *Expect:* the file extension and size match the portal's requirements.
5. **Choose the correct upload field.** Match the portal label to the document type, such as proof of address, transcript, ID front, or pay stub. → *Expect:* the selected field name matches the document content.
6. **Upload and wait for completion.** Select the file once, then wait through scanning, processing, or progress bars without closing the tab. → *Expect:* the portal shows the filename with uploaded, complete, or ready status.
7. **Preview the uploaded copy if possible.** Open the portal preview or download-back link. → *Expect:* the portal copy is the same document, not a blank page or wrong file.
8. **Submit or save the upload.** ⚠️ *Irreversible:* some portals lock the upload after final submission, so verify field and file before clicking Submit. → *Expect:* the item changes from draft/uploaded to submitted/received.
9. **Save confirmation.** Download a receipt or screenshot the status page with filename, date, and reference number visible. → *Expect:* proof exists outside the portal.

## Decision points

- [BRANCH: one combined PDF | separate files] Use one combined PDF when the portal asks for "the document"; use separate fields when it asks for front/back or category-specific uploads.
- Portal says image too large → reduce scan resolution or export PDF at smaller size, but re-check legibility afterward.
- Portal rejects password-protected files → save an unprotected copy only for upload, then delete that temporary copy after confirmation.
- Required field is ambiguous → use the portal help text or contact support before uploading private documents to the wrong category.

## Failure modes & recovery

- **F1 Wrong file uploaded:** detect by filename or preview mismatch; recover by deleting/replacing before final submit or contacting support with the confirmation number.
- **F2 Upload spinner never finishes:** detect no progress for several minutes; recover by refreshing only after saving draft, then try a smaller file or different browser.
- **F3 Blurry or cropped scan:** detect unreadable text in preview; recover by rescanning in better light and replacing the file.
- **F4 No confirmation after upload:** detect status still says draft or pending action; recover by pressing the final Save/Submit button and checking messages for receipt.

## Verification

The portal status for the required document shows submitted, received, accepted, or equivalent, with the expected filename and date visible.

## Variations

- `mobile-app`: upload from cloud storage or Files rather than the photo gallery to avoid picking a thumbnail or preview image.
- Identity documents: many portals require front and back as separate uploads, so label filenames clearly.
- Medical or legal portals: do not compress so aggressively that signatures, seals, or handwritten notes become unreadable.

## Safety & privacy

Uploaded documents often contain identity numbers, addresses, financial records, or health information. Use only the real portal, avoid shared computers, delete temporary unprotected copies, and keep confirmation proof in a private folder.
