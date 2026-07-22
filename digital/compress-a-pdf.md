---
name: compress-a-pdf
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You reduce a PDF file to a practical size while keeping the text, images, forms, and page order readable enough for the recipient or upload site.

## Preconditions

- A PDF file you are allowed to modify and a target size if an upload form gives one.
- A safe place to save a copy so the original stays unchanged.

## Steps

1. **Make a working copy.** Duplicate the PDF and rename it with `compressed` or the target size. → *Expect:* the original file remains untouched and the copy is ready to edit.
2. **Check what is making it large.** Open the PDF and scan for full-page photos, scans, high-resolution images, or embedded graphics. Images usually create most of the file size. → *Expect:* you know whether compression can help a lot or only a little.
3. **Try the built-in export first.** [BRANCH: macOS Preview | Windows print/export | Adobe Acrobat or office app] choose the lowest-friction built-in option such as Export, Save As Reduced Size, or Print to PDF with lower quality. → *Expect:* a second PDF is created with a smaller file size.
4. **Use a trusted tool if built-in export is not enough.** Prefer Adobe Acrobat, your scanner software, or an offline PDF utility from a known vendor. Use online compressors only for non-sensitive files. → *Expect:* the tool offers quality or size settings before saving.
5. **Set the target deliberately.** Choose screen or email quality for casual reading, and higher quality for documents with fine print, signatures, diagrams, or photos that matter. → *Expect:* the output size moves toward the limit without obvious damage.
6. **Open the compressed file and inspect pages.** Zoom into small text, signatures, barcodes, QR codes, tables, and image-heavy pages. → *Expect:* the content is still legible at normal viewing and printing size.
7. **Check forms, links, and page count.** If the PDF had fillable fields, bookmarks, links, or attachments, verify they survived. → *Expect:* page count and important interactive parts match the original.
8. **Keep the best version.** If the file is still too large, run another pass at lower image quality; if it looks bad, go back to the previous copy and use gentler settings. → *Expect:* one compressed PDF meets the upload or sharing requirement.

## Decision points

- File contains scans of text → optical character recognition plus lower image resolution may help more than generic compression.
- File is already small but still over a portal limit → split the PDF or ask for a higher limit instead of making text unreadable.
- PDF contains private, legal, medical, school, or financial information → use offline tools rather than uploading to an unknown website.
- Recipient needs print quality → prioritize readability over hitting an arbitrary tiny size.

## Failure modes & recovery

- **F1 Text turns blurry:** detect: small text smears at 100 percent zoom, recover: recompress from the original with higher quality or OCR the scan.
- **F2 File size barely changes:** detect: output is within a few percent of the original, recover: lower image resolution, remove unused pages, or export images at lower quality.
- **F3 Forms stop working:** detect: fields flatten or cannot be typed into, recover: use Acrobat or the source app's export instead of print-to-PDF.
- **F4 Upload still rejects it:** detect: portal says too large or invalid file, recover: confirm the exact size limit, reduce again, or split into required sections.
- **F5 Sensitive file was uploaded online:** detect: you used a third-party compressor for private content, recover: delete it from the service if possible and use offline compression going forward.

## Verification

The compressed PDF is below the required size, opens without errors, has the same required pages, and remains readable when zoomed into the smallest important text.

## Variations

- `macos`: Preview can export with a Quartz filter, but the default "Reduce File Size" can be too aggressive for scans.
- `windows`: Microsoft Print to PDF can create a new file, but it may flatten forms and links.
- `adobe-acrobat`: "Reduce File Size" and "Optimize PDF" give more control and preserve more PDF features.
- `mobile-app`: Use a scanner or PDF app with export quality settings, then inspect the result on a larger screen if possible.

## Safety & privacy

Do not upload confidential PDFs to random compression sites. Compression can permanently reduce image detail in the copy, so keep the original until the recipient accepts the compressed version.
