---
name: export-a-document-to-pdf
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

A document is saved as a PDF that preserves layout for sharing, uploading, or printing.

## Preconditions

- The source document is open.
- You know where the PDF should be saved.

## Steps

1. **Review the document first.** Check title, page breaks, images, and final edits. → *Expect:* the document is ready to export.
2. **Open export or download.** [BRANCH: Word | Google Docs] In Word, choose File > Save As or File > Export > Create PDF/XPS; in Google Docs, choose File > Download > PDF Document. → *Expect:* PDF is available as an output format.
3. **Choose the save location.** Select a folder and enter a clear file name ending in `.pdf`. → *Expect:* the save dialog shows the intended PDF name and location.
4. **Save or download the PDF.** Click Save, Export, Publish, or Download. → *Expect:* a PDF file is created.
5. **Open the PDF.** View the exported file in a PDF viewer. → *Expect:* the PDF opens without errors.
6. **Inspect layout.** Check page count, headings, images, links, and any special characters. → *Expect:* the PDF matches the source document closely enough for its purpose.

## Decision points

- Recipient needs editing → send the original editable file as well as or instead of the PDF.
- File includes comments or tracked changes → choose whether to include markup before exporting.

## Failure modes & recovery

- **F1 PDF layout changed:** detect: page breaks, fonts, or images shift → recover by adjusting the source document and exporting again.
- **F2 Wrong file exported:** detect: PDF content is outdated or from another document → recover by reopening the correct source and exporting again.
- **F3 PDF is too large:** detect: upload or email rejects the file → recover by compressing images or using PDF optimization.

## Verification

The PDF exists at the chosen location, opens successfully, and shows the expected content and page count.

## Variations

- `word`: Export options can include or exclude document properties and markup.
- `google-docs`: Downloaded PDFs use the current document state and page setup.

## Safety & privacy

PDF export can preserve comments, metadata, links, or hidden document information depending on settings. Inspect the PDF before sharing.
