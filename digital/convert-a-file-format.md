---
name: convert-a-file-format
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min-20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A file is converted to the needed format while preserving the content quality required for its next use.

## Preconditions

- The original file, an app that can open it, and knowledge of the target format requested by the recipient, website, printer, or device.
- A backup copy if the original is important.

## Steps

1. **Open the original in its native app.** Use the program that created the file when possible, such as Word for DOCX or Photos for HEIC. → *Expect:* the file displays correctly before conversion.
2. **Look for export or save-as.** Choose File > Export, Save As, Download, or Share, depending on the app. → *Expect:* the app shows a list of output formats.
3. **Pick the target format.** [BRANCH: document | image | audio/video] Documents often become PDF; images become JPG, PNG, or TIFF; media becomes MP4, MP3, or WAV. → *Expect:* the chosen extension matches the requirement.
4. **Choose quality settings.** For documents, embed fonts if offered; for images and video, balance quality against file size. → *Expect:* the estimated size and quality settings are visible before saving.
5. **Save as a new file.** Keep the original untouched and put the converted file beside it with a clear name. → *Expect:* both original and converted files exist.
6. **Use a converter only when needed.** If the app cannot export the format, use a trusted offline converter or reputable service, avoiding sensitive files online. → *Expect:* the converter produces a downloadable file in the target format.
7. **Open the converted file.** Use the recipient's likely app or a common viewer to check layout, fonts, images, sound, or playback. → *Expect:* the converted file opens without errors and looks or plays as intended.
8. **Send or upload the converted copy.** Upload the new file, not the original, and keep both until the recipient confirms it works. → *Expect:* the destination accepts the file type and size.

## Decision points

- Recipient needs editing → send DOCX, XLSX, PPTX, PSD, or another editable format rather than PDF or JPG.
- Recipient needs reliable viewing or printing → PDF is usually safer than editable formats.
- File contains private or regulated data → use built-in export or offline conversion instead of a web converter.

## Failure modes & recovery

- **F1 Formatting shifts:** detect moved text, missing fonts, or broken page breaks, recover by exporting to PDF with fonts embedded or sharing the original app format.
- **F2 File too large:** detect upload or email rejection, recover by lowering image/video quality, compressing the PDF, or splitting the file.
- **F3 Unsupported format:** detect an app cannot open the result, recover by converting to a more common format or asking the recipient for the exact requirement.
- **F4 Quality loss:** detect blurry images or muffled audio, recover by reconverting from the original with higher quality settings.

## Verification

The converted file opens in a common viewer, contains the expected content, and is accepted by the target service or recipient.

## Variations

- Google Docs, Sheets, and Slides: use File > Download to choose formats such as PDF, DOCX, XLSX, or PPTX.
- macOS Preview: exports images and PDFs to common formats with quality controls.
- Command-line tools: `ffmpeg`, `pandoc`, and ImageMagick are useful when exact batch conversion is needed.

## Safety & privacy

Converters can copy uploaded files, strip metadata unpredictably, or add watermarks. Keep originals, avoid online converters for sensitive data, and verify the output before deleting anything.
