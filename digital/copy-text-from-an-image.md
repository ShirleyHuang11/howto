---
name: copy-text-from-an-image
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 3min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Extract readable text from a photo, screenshot, or image and copy it for reuse.

## Preconditions

- The image contains visible text.
- You have an OCR-capable app, photo viewer, notes app, browser, or phone camera feature.

## Steps

1. **Open the image.** View the photo or screenshot in an app that supports text recognition. → *Expect:* the text in the image is visible.
2. **Activate text recognition.** Choose `Live Text`, `Copy text`, `Lens`, OCR, or select directly over the text. → *Expect:* recognized words become selectable or highlighted.
3. **Select the text.** Drag selection handles or choose `Select all` for the recognized text. → *Expect:* the intended text is highlighted.
4. **Copy the text.** Click or tap `Copy`. → *Expect:* the text is placed on the clipboard.
5. **Paste into a text field.** Paste into Notes, a document, email, or form. → *Expect:* editable text appears.
6. **Proofread carefully.** Compare the pasted text with the original image. → *Expect:* numbers, names, dates, and punctuation are correct.

## Decision points

- Text is small or blurry → zoom, crop, or retake the image before OCR.
- Text contains codes or account numbers → verify every character manually.
- Image is confidential → use local OCR rather than uploading to an online service.

## Failure modes & recovery

- **F1 Text not recognized:** detect no selectable words → crop closer, improve contrast, or use another OCR app.
- **F2 Characters copied incorrectly:** detect wrong letters, numbers, or spacing → correct manually after pasting.
- **F3 Wrong language detected:** detect nonsensical output → set the OCR language or use an app that supports the language.

## Verification

The pasted text matches the image text closely enough for the intended use, with critical fields manually checked.

## Variations

- `ios`: Photos and Camera support Live Text on compatible devices.
- `android`: Google Lens and many gallery apps support copy text.
- `desktop`: OneNote, Preview-like tools, browsers, and PDF apps may include OCR.

## Safety & privacy

OCR can expose private text to cloud services depending on the tool. Avoid uploading IDs, passwords, medical records, or confidential documents to unknown converters.
