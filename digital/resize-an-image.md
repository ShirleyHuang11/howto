---
name: resize-an-image
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

Change an image's pixel dimensions or file size for sharing, uploading, or storage.

## Preconditions

- The image is available on your device.
- You know the required width, height, percentage, or maximum file size.

## Steps

1. **Open the resize tool.** Open the image in an editor that has resize, image size, or export-size controls. → *Expect:* the image is loaded in the editor.
2. **Choose resize settings.** Select pixels, percentage, or a preset size. → *Expect:* width and height fields or size presets are visible.
3. **Keep proportions linked.** Leave aspect ratio, lock, or constrain proportions enabled unless you intentionally want distortion. → *Expect:* changing one dimension updates the other.
4. **Enter the target size.** Type the required width, height, percentage, or export quality. → *Expect:* the preview or file-size estimate updates.
5. **Save a copy.** Export or save under a new name if you need the original size later. → *Expect:* a resized image file is created.
6. **Check the result.** Open file details or properties to confirm dimensions and size. → *Expect:* the numbers match the target or upload requirement.

## Decision points

- Upload rejects the file size → lower image quality or dimensions.
- Image looks stretched → undo and repeat with proportions locked.
- Print quality matters → avoid making the image smaller than the printer's recommended resolution.

## Failure modes & recovery

- **F1 Image becomes blurry:** detect softness or pixelation → resize from the original at a larger target size.
- **F2 File still too large:** detect upload or properties show excess size → reduce quality or dimensions further.
- **F3 Original overwritten:** detect only the small file remains → restore from backup or cloud version history.

## Verification

The saved image has the required pixel dimensions or file size and opens without distortion.

## Variations

- `windows`: Photos, Paint, and many web tools provide resize controls.
- `mac`: Preview uses Tools > Adjust Size and Export quality.
- `mobile-app`: photo editors often resize through Export, Save copy, or Share settings.

## Safety & privacy

Resizing can remove detail needed for records or evidence. Keep the original when accuracy, metadata, or print quality matters.
