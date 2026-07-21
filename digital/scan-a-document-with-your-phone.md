---
name: scan-a-document-with-your-phone
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

A paper document is captured as a clean, cropped, readable multi-page PDF using the phone's built-in scanner, saved with a name you can find again, not a crooked photo in the camera roll.

## Preconditions

- A phone with a native scan tool: iPhone Notes or Files, Android Google Drive scan, or the built-in camera's document mode on newer phones.
- The document flat on a surface with even light and a background that contrasts with the paper (dark table for white pages).

## Steps

1. **Open the native scanner, not the plain camera.** iPhone: Notes > new note > camera icon > Scan Documents, or Files > three-dot menu > Scan. Android: Google Drive > + > Scan. → *Expect:* a viewfinder that highlights the page edges automatically rather than a normal photo screen.
2. **Set up the shot for clean edge detection.** Lay the page flat, fill most of the frame, and keep the phone parallel to the page (shoot straight down, not at an angle). Even light, no hard shadow from your own hand. → *Expect:* a colored overlay snaps to all four corners of the page.
3. **Capture, letting auto-detect fire.** Most scanners shoot automatically when the page is steady and squared; otherwise tap the shutter. → *Expect:* the page captures and the app shows a cropped, de-skewed preview, not the whole tabletop.
4. **Fix the crop if the corners are wrong.** Drag the corner handles to the actual page edges. This is the step people skip, and it is what separates a scan from a photo. → *Expect:* the crop outline sits exactly on the paper edges with no table showing and no text cut off.
5. **Add more pages for a multi-page document.** Keep shooting; each page appends. Scan them in reading order. → *Expect:* a running page count that matches the number of physical pages you have fed.
6. **Choose the right filter.** Black-and-white/document filter for text (smaller, sharper, more legible); color only when color matters (photos, highlighted forms, ID cards). → *Expect:* text looks crisp and high-contrast; the file is not a heavy full-color photo of text.
7. **Save as PDF and name it meaningfully.** Finish/Save, keep the format as PDF for a multi-page document. Rename from the default "Scan 2026-07-20" to something findable like `tax-2025-receipt-electric.pdf`. → *Expect:* a single PDF with all pages in order, under a searchable name, in a folder you will look in.
8. **Verify before you rely on it.** Open the PDF and read the smallest text on the most important page. → *Expect:* every page present, right-side up, in order, and fully legible.

## Decision points

- Document will be signed or filled digitally → keep it as a PDF (not a JPG); PDF is what signing and upload tools expect.
- Glossy or laminated page with glare → tilt the light source or the page, not the phone, to move the reflection off the text; scan in matte, indirect light.
- Very long or bound document → scan two facing pages at a time only if the tool de-skews each; otherwise flatten and shoot one page per capture.

## Failure modes & recovery

- **F1 Edges not detected:** increase contrast between paper and surface (white page on a dark table), improve lighting, and hold the phone squarely above. Auto-detect fails on low contrast.
- **F2 Text blurry in the saved PDF:** the phone moved during capture or focus missed. Steady the phone (or brace elbows), tap to focus on the text, and reshoot that page.
- **F3 Page skewed or trapezoidal:** you shot at an angle. Re-crop with the corner handles, or reshoot straight down; the de-skew only fixes so much.
- **F4 File is huge:** you used the color filter on a text document. Re-save with the black-and-white/document filter to shrink it dramatically.

## Verification

Opening the saved PDF shows every page cropped to the paper edges, upright, in order, and legible down to the smallest important text, under a filename you can find by searching.

## Variations

- `dedicated-app`: third-party scanners (Adobe Scan, Microsoft Lens) add OCR (searchable text) and cloud sync; the capture technique is identical.
- ID cards / receipts: use the app's card or receipt preset for the right aspect ratio and auto-crop; scan both sides of an ID as two pages.

## Safety & privacy

Low risk, but scans often contain sensitive data (IDs, bank statements, medical forms). Check where the scan saves: if the scanner auto-uploads to a cloud folder, know which one and who can see it. Delete scans from shared or temporary folders after you have used them, and avoid emailing sensitive PDFs unencrypted.
