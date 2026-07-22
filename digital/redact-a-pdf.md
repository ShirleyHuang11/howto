---
name: redact-a-pdf
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 15min-45min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A PDF copy is permanently redacted so hidden text, metadata, and sensitive marks cannot be recovered by selection, search, or layer inspection.

## Preconditions

- A PDF editor with a real redaction tool, such as Adobe Acrobat Pro, Foxit PDF Editor, Nitro, or a vetted organization tool.
- A separate original copy kept unchanged for records.

## Steps

1. **Make a working copy.** Duplicate the PDF and add `redacted` to the filename before editing. → *Expect:* the original and working copy are both present.
2. **Open the real redaction tool.** Choose Redact, Mark for Redaction, or Sanitize, not drawing, highlight, comment, or rectangle tools. → *Expect:* the app shows redaction marks as pending edits.
3. **Mark sensitive content.** Select names, account numbers, addresses, barcodes, signatures, headers, footers, and repeated instances found by search. → *Expect:* every sensitive item is covered by a pending redaction mark.
4. **Apply redactions permanently.** Confirm the tool's Apply or Redact command. ⚠️ *Irreversible:* this removes content from the working copy, so confirm you are not editing the only original. → *Expect:* pending marks become permanent solid areas.
5. **Sanitize hidden data.** Remove metadata, comments, attachments, form data, hidden text, and previous revisions if the tool offers it. → *Expect:* the sanitizer reports completion or lists removed data types.
6. **Flatten or save as final.** Save the redacted PDF as a new final file, using PDF/A or print-to-PDF only if your workflow requires flattening. → *Expect:* the final PDF opens as a normal document without editable redaction annotations.
7. **Verify by searching and copying.** Search for redacted words and try selecting across blacked-out areas, then paste into a plain-text editor. → *Expect:* redacted text cannot be found or pasted.
8. **Review visually.** Zoom through every page, including margins and thumbnails, to catch missed small text or page images. → *Expect:* only intended visible content remains.

## Decision points

- You only have a free PDF viewer → do not draw black boxes; use a real redaction-capable tool or ask the organization for one.
- The PDF is a scanned image → OCR may have hidden text, so sanitize and verify copy-paste even if the page looks like a picture.
- The file must be filed in court or with an agency → follow that venue's redaction and metadata rules exactly.

## Failure modes & recovery

- **F1 Black box only:** detect text appears when copied from under the box, recover by reverting to the original and using the redaction tool.
- **F2 Search still finds names:** detect search hits for hidden text, recover by sanitizing OCR text or re-exporting with real redactions applied.
- **F3 Metadata leak:** detect author, path, comments, or attachments in document properties, recover by running sanitize or remove hidden information.
- **F4 Wrong content removed:** detect a needed field is gone after applying, recover from the original copy and redo the working copy.

## Verification

Searching and copy-pasting cannot recover any redacted text, and document properties show no sensitive metadata or attachments.

## Variations

- Adobe Acrobat Pro: Tools > Redact, mark items, Apply, then Sanitize and save.
- Preview on macOS: use its Redact tool on current versions, not shape annotations.
- Microsoft Word export: useful only before PDF creation; after PDF creation, verify the PDF itself.

## Safety & privacy

⚠️ Real redaction removes text; a black box placed over text is only decoration and may leak everything underneath. Keep the original securely, share only the verified final copy, and treat failed redactions as high-risk disclosure.
