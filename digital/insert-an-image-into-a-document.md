---
name: insert-an-image-into-a-document
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

An image is placed into a document at the intended location with readable size and layout.

## Preconditions

- A document is open.
- The image file is saved locally, available in cloud storage, or accessible through the editor's insert menu.

## Steps

1. **Place the cursor.** Click where the image should appear. → *Expect:* the insertion cursor marks the image location.
2. **Open image insertion.** [BRANCH: Word | Google Docs] In Word, choose Insert > Pictures; in Google Docs, choose Insert > Image. → *Expect:* source options for the image appear.
3. **Choose the image.** Select the file, upload source, or cloud image and confirm insertion. → *Expect:* the image appears in the document.
4. **Resize proportionally.** Drag a corner handle, not a side handle, to fit the image. → *Expect:* the image changes size without looking stretched.
5. **Set wrapping if needed.** Choose inline, square, tight, or break text depending on the layout. → *Expect:* surrounding text flows the way you intend.
6. **Add alt text if the document will be shared.** Use the image options or context menu to describe the image briefly. → *Expect:* the image has a short text description for accessibility.

## Decision points

- Image must stay with a paragraph → use inline placement.
- Text should flow beside the image → use a wrapping option and check margins.
- Image contains private people or locations → confirm it is appropriate to include.

## Failure modes & recovery

- **F1 Image is distorted:** detect: circles look oval or people look stretched → recover by undoing or resizing from a corner handle.
- **F2 Text jumps unexpectedly:** detect: paragraphs move around the image badly → recover by changing wrapping or moving the image.
- **F3 Image fails to upload:** detect: editor shows an upload error → recover by checking file type, size, network connection, or using a smaller copy.

## Verification

The image appears at the intended location, is not distorted, and does not obscure nearby text.

## Variations

- `word`: Picture Format controls size, crop, alt text, and text wrapping.
- `google-docs`: Image options controls size, position, text wrapping, and alt text.

## Safety & privacy

Images may reveal faces, addresses, file metadata, or confidential screens. Use only images you have permission to share.
