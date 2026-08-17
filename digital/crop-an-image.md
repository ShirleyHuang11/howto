---
name: crop-an-image
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Remove unwanted edges from an image while keeping the important subject.

## Preconditions

- The image is available on your device or in an editing app.
- You know what area should remain visible.

## Steps

1. **Open the image.** Open the file in Photos, Preview, Paint, Gallery, or another image editor. → *Expect:* the image is visible.
2. **Enter crop mode.** Choose `Edit`, `Crop`, or the crop icon. → *Expect:* crop handles or a crop frame appear.
3. **Adjust the crop frame.** Drag the corners or edges around the area to keep. → *Expect:* unwanted edges fall outside the crop frame.
4. **Use aspect ratio if needed.** Select a preset such as square, 4:3, 16:9, or original ratio when required. → *Expect:* the crop frame keeps that shape while resizing.
5. **Apply the crop.** Click or tap `Apply`, `Done`, or the checkmark. → *Expect:* the image preview shows only the selected area.
6. **Save the result.** Choose `Save a copy` or `Export` if you need to preserve the original. → *Expect:* the cropped image is saved.

## Decision points

- The image is evidence or documentation → preserve the original and save a cropped copy.
- The image must fit a profile or form → use the required aspect ratio.
- The cropped area looks blurry → start from a higher-resolution original.

## Failure modes & recovery

- **F1 Subject cut off:** detect missing edges or text → undo and expand the crop frame.
- **F2 Wrong shape:** detect the result does not fit the target → crop again with the required aspect ratio.
- **F3 Original changed unexpectedly:** detect the original is cropped → use undo, revert, version history, or backup.

## Verification

The saved image contains the intended subject and excludes the unwanted edges.

## Variations

- `windows`: Photos and Paint include crop tools.
- `mac`: Preview and Photos include crop tools.
- `mobile-app`: crop appears inside the Edit screen in most photo apps.

## Safety & privacy

Cropping may not erase the original from cloud backups or edit history. For sensitive images, export a new file and remove the original where appropriate.
