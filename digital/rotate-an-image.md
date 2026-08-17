---
name: rotate-an-image
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Turn an image to the correct orientation.

## Preconditions

- The image file is available on your device.
- You know whether it needs to turn left, right, or 180 degrees.

## Steps

1. **Open the image.** Open the file in Photos, Preview, Paint, Gallery, or another image viewer. → *Expect:* the image appears on screen.
2. **Find rotate.** Look for a curved arrow, `Rotate`, or edit menu. → *Expect:* a rotation control is visible.
3. **Rotate the image.** Click or tap rotate left or rotate right until the image is upright. → *Expect:* the preview changes orientation.
4. **Save the image.** Choose `Save`, `Done`, or `Save a copy` depending on whether you want to replace the file. → *Expect:* the image stays in the corrected orientation after closing and reopening.

## Decision points

- You need to keep the original unchanged → use `Save a copy`.
- Text appears mirrored rather than rotated → use flip or mirror tools instead.
- The image is part of a batch → use a file manager or photo app batch rotate feature.

## Failure modes & recovery

- **F1 Rotated wrong direction:** detect the subject is sideways or upside down → rotate again or undo.
- **F2 Orientation resets later:** detect the image opens sideways in another app → export a new copy to bake in the rotation.
- **F3 Quality warning appears:** detect the editor warns about recompression → save a copy and keep the original.

## Verification

The image opens upright in the target app or viewer after saving.

## Variations

- `windows`: File Explorer and Photos can rotate many images.
- `mac`: Preview uses rotate buttons and saves automatically unless duplicated.
- `mobile-app`: rotate is usually inside Edit > Crop/Rotate.

## Safety & privacy

Rotation is low risk, but edited images may sync to cloud photo libraries. Use a copy if the original must remain untouched.
