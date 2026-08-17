---
name: watermark-your-images
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Add a visible or metadata watermark to images so viewers can identify ownership, origin, or permitted use.

## Preconditions

- You own or have rights to distribute the images.
- You know whether the watermark should be visible, metadata-only, or both.

## Steps

1. **Choose watermark type.** [BRANCH: visible | metadata | both] use visible marks for deterrence and metadata for attribution that does not alter the image. → *Expect:* the watermark goal is clear.
2. **Create a working copy.** Duplicate the original image before editing. → *Expect:* the unwatermarked original remains available.
3. **Place the watermark.** Add your name, logo, copyright notice, or content label in a consistent corner or repeated pattern. → *Expect:* the mark is readable but does not hide essential content.
4. **Set opacity and size.** Adjust contrast so the watermark survives casual cropping or reposting without ruining the image. → *Expect:* the image remains usable.
5. **Add metadata if needed.** Enter creator, copyright, license, contact, and usage terms in the editor's metadata fields. → *Expect:* attribution travels with files that preserve metadata.
6. **Export and test.** Save a distribution copy and upload or message it to yourself to see whether the platform strips metadata or compresses the watermark. → *Expect:* the intended mark remains visible or metadata loss is known.

## Decision points

- The image is for sale or licensing → use both visible proofs and separate registration or contract records.
- The watermark would expose personal information → use a business name, site, or alias instead.
- The image documents evidence → preserve an unedited original with timestamp and hash.

## Failure modes & recovery

- **F1 Metadata stripped:** detect fields disappear after upload → recover by using a visible watermark or platform-specific attribution.
- **F2 Watermark cropped out:** detect the mark sits at an easy edge → recover by repositioning or using a subtle repeated pattern.
- **F3 Original lost:** detect only watermarked copies remain → recover from backup before further edits.

## Verification

The exported copy contains the intended visible watermark or metadata, and the original image remains unchanged in a separate file.

## Variations

- `mobile-app`: photo apps can add text overlays but may not preserve metadata.
- `portfolio`: use subtle visible attribution and keep originals offline.
- `ai-images`: label generated or AI-assisted images when required by platform, client, or policy.

## Safety & privacy

Low risk, but watermarks can reveal legal names, locations, or business identities. Keep originals private and avoid falsely watermarking images you do not own.
