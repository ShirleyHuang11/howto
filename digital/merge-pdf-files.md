---
name: merge-pdf-files
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You combine multiple PDF files into one correctly ordered PDF with the intended page range, pagination, and readable content.

## Preconditions

- The PDF files you want to combine, stored in one folder if possible.
- A known final order and any page ranges that should be included or excluded.

## Steps

1. **Create a staging folder.** Copy the PDFs into one folder and rename them with leading numbers such as `01-application.pdf`, `02-id.pdf`, and `03-receipt.pdf`. → *Expect:* the file list sorts in the same order as the final packet.
2. **Open the merge tool.** [BRANCH: macOS Preview | Adobe Acrobat | browser or office PDF tool] use a built-in or trusted tool that shows page thumbnails before saving. → *Expect:* thumbnails or a file-order list is visible.
3. **Add files in final order.** Drag files or use Add Files, then confirm the sequence before merging. Order matters because many portals review the first pages first. → *Expect:* the first thumbnail is the intended first page.
4. **Set page ranges if needed.** Include only the pages required from each source, such as pages 2-4 of a statement or only the signature page. → *Expect:* unwanted cover sheets, blank pages, or duplicates are excluded.
5. **Merge into a new file.** Save as a new PDF name that describes the packet and date. Do not overwrite source PDFs. → *Expect:* one combined PDF appears in the staging folder.
6. **Review pagination from start to finish.** Open the merged file, use thumbnails, and check that each section begins where expected. → *Expect:* page count and section order match your plan.
7. **Inspect rotated and scanned pages.** Rotate sideways pages, remove accidental blanks, and confirm scans are not upside down. → *Expect:* every page can be read without turning the screen.
8. **Check size and upload rules.** If the merged file is too large, compress a copy rather than redoing the merge blindly. → *Expect:* the final PDF satisfies the recipient's file-size and format rules.

## Decision points

- Need a subset of a long PDF → use page ranges or extract pages before merging.
- Need bookmarks or table of contents → use Acrobat or a PDF editor with bookmark support, not a simple print-to-PDF merge.
- Confidential documents → avoid unknown online merge sites because the service receives every page.
- Portal requires separate documents → do not merge just for neatness; follow the portal's required upload slots.

## Failure modes & recovery

- **F1 Pages are in the wrong order:** detect: thumbnails or page numbers do not match the intended sequence, recover: reorder files or thumbnails and save a new merged copy.
- **F2 Missing pages:** detect: final page count is lower than expected, recover: check page-range settings and re-add the source file.
- **F3 Duplicate or blank pages:** detect: review shows repeated pages or scanner blanks, recover: delete the bad pages before saving again.
- **F4 Forms or links break:** detect: fillable fields no longer work, recover: merge with a PDF editor that preserves forms or submit separate files.
- **F5 File is too large:** detect: upload fails or file properties exceed the limit, recover: compress the merged copy and recheck readability.

## Verification

The merged PDF opens, its pages appear in the intended order, the page count matches the selected ranges, and the first and last required pages are correct.

## Variations

- `macos`: Preview can merge by dragging thumbnails between open PDFs, then saving a new file.
- `windows`: Browser-based PDF tools, Acrobat, or vendor utilities are common; choose offline tools for sensitive files.
- `ios`: Files and third-party PDF apps can combine documents, but page-range controls vary.
- `android`: PDF utility apps can merge, but verify the output carefully because ad-supported tools may reorder by filename.

## Safety & privacy

Merging is usually reversible if you keep the source PDFs. The privacy risk is in the tool choice: online merge sites receive all uploaded documents, so use offline software for identity, legal, medical, tax, school, or work files.
