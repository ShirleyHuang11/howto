---
name: redact-faces-in-images
domain: ai
subdomain: multimodal
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Detect and irreversibly obscure faces in images, then verify that no detectable faces remain before images are shared or stored downstream.

## Preconditions

- Images you are authorized to process and a privacy policy describing redaction requirements.
- A face detector such as RetinaFace, MediaPipe, OpenCV DNN, or a hosted vision service.
- An output format that does not preserve the original face pixels in layers or metadata.

## Steps

1. **Load and normalize images.** Decode, apply EXIF orientation, and preserve a protected original only if policy allows. → *Expect:* a normalized working image exists with dimensions recorded.
2. **Detect faces.** [BRANCH: local detector | hosted vision API] Run a detector with bounding boxes and confidence scores. ⚠️ *Data leaves your control:* hosted detection sends identifiable faces to a third party. → *Expect:* each detected face has a box, confidence, and detector version.
3. **Expand boxes conservatively.** Add margin around each face to cover hairline, ears, and partial profiles. → *Expect:* redaction boxes are larger than raw detections and clipped to image bounds.
4. **Apply irreversible redaction.** Use solid fill, strong blur, or pixelation that cannot be reversed, then flatten the image. → *Expect:* output pixels in redaction regions no longer contain readable facial features.
5. **Strip metadata.** Remove EXIF GPS, camera serials, thumbnails, and original previews. → *Expect:* `exiftool -all= redacted.jpg` or equivalent leaves no sensitive metadata.
6. **Re-run face detection on output.** Detect faces again using the same and, if possible, a second detector. → *Expect:* no face above the configured confidence threshold remains.

## Decision points

- Detector misses partial or small faces → lower threshold, use a second detector, or require manual review.
- Need legal-grade anonymity → prefer solid fill over blur or pixelation.
- Original images must be retained → store them separately with strict access controls and retention limits.

## Failure modes & recovery

- **F1 Missed small face:** detect remaining face on verification pass → expand detection settings and rerun redaction.
- **F2 Reversible blur:** detect recognizable face after blur → switch to solid fill or heavy pixelation.
- **F3 Metadata leak:** detect GPS or embedded thumbnail after export → strip metadata and disable thumbnail preservation.
- **F4 Wrong orientation:** detect boxes offset from faces → apply EXIF orientation before detection and redaction.

## Verification

For every output image, metadata inspection finds no EXIF/GPS/thumbnail data, a second face-detection pass returns zero faces above the configured confidence threshold, and a pixel-difference check confirms every detected input face region was modified.

## Variations

- `solid fill`: strongest privacy and easiest to verify.
- `blur/pixelation`: more visually acceptable but must be strong enough to resist reconstruction.
- `video frames`: track faces across frames and verify sampled frames plus scene changes.

## Safety & privacy

Faces are biometric data. Prefer local detection, strip metadata, avoid retaining originals unless required, and do not claim anonymity if faces, reflections, badges, or other identifiers remain visible.
