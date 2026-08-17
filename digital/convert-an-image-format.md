---
name: convert-an-image-format
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

Save an image in a different file format such as JPG, PNG, HEIC, GIF, or WebP.

## Preconditions

- The image is available on your device.
- You know the format required by the app, website, or recipient.

## Steps

1. **Open the image.** Open the file in an editor, photo app, preview app, or trusted converter. → *Expect:* the image is visible.
2. **Choose export or save as.** Select `Export`, `Save as`, `Download as`, or format options. → *Expect:* a format dropdown or file-type menu appears.
3. **Select the new format.** Choose the required format, such as JPG for photos or PNG for transparency. → *Expect:* the selected extension or format is shown.
4. **Set quality if offered.** Choose a quality level that balances file size and clarity. → *Expect:* the estimated file size or quality setting is visible.
5. **Save the converted file.** Use a new name or location to avoid confusing it with the original. → *Expect:* a new file with the target extension is created.
6. **Open the result.** View the converted file in the target app or a file viewer. → *Expect:* the image displays correctly.

## Decision points

- Need transparency → use PNG or WebP, not JPG.
- Need small photo file → use JPG or WebP with moderate quality.
- Need maximum compatibility → use JPG for photos and PNG for graphics.

## Failure modes & recovery

- **F1 Transparency lost:** detect a white or black background → convert from the original to PNG or WebP.
- **F2 File too large:** detect upload limit failure → export again with lower quality or smaller dimensions.
- **F3 Unsupported format:** detect the recipient or site cannot open it → convert to JPG or PNG.

## Verification

The converted file has the desired extension and opens correctly in the target app or upload form.

## Variations

- `windows`: Paint and Photos support Save as or export options.
- `mac`: Preview uses File > Export.
- `web`: use only trusted converters for non-sensitive images.

## Safety & privacy

Online converters may upload your image to a third party. Avoid using them for IDs, documents, medical images, private photos, or confidential work.
