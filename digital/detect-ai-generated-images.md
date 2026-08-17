---
name: detect-ai-generated-images
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Assess whether an image may be AI-generated or manipulated by combining visual inspection, provenance checks, and source verification.

## Preconditions

- You have the highest-resolution version available, not only a compressed repost.
- You understand that detector tools are imperfect and cannot prove authenticity alone.

## Steps

1. **Save the context.** Record where you found the image, the account, caption, date, and any claims attached to it. → *Expect:* the image is tied to its original claim.
2. **Inspect visible details.** Zoom in on hands, teeth, text, reflections, shadows, edges, repeated patterns, and background objects. → *Expect:* possible generation or editing artifacts are noted.
3. **Check provenance.** Look for metadata, content credentials, watermarking, creator statements, or platform labels. [BRANCH: provenance present | provenance absent] verify present claims; treat absence as inconclusive. → *Expect:* you know whether origin evidence exists.
4. **Reverse-search the image.** Use image search or search distinctive caption terms to find earlier versions and related posts. → *Expect:* you identify the earliest credible source you can find.
5. **Compare against real-world facts.** Check whether the place, event, product, uniform, weather, or public figure appearance matches known records. → *Expect:* the image claim is supported, contradicted, or unresolved.
6. **Use detectors cautiously.** If using an AI-image detector, run more than one and record the result as a weak signal, not proof. → *Expect:* detector output is not treated as a final verdict.

## Decision points

- The image could affect public safety, elections, reputation, or legal claims → escalate to stronger verification before sharing.
- The image is artistic or promotional → provenance may matter less than disclosure and licensing.
- The image contains a private person → avoid spreading it while authenticity is uncertain.

## Failure modes & recovery

- **F1 Detector overconfidence:** detect a detector gives a precise score with no evidence → recover by treating it as one weak signal.
- **F2 Repost laundering:** detect many copies with no original source → recover by searching older dates, filenames, captions, and visual matches.
- **F3 Real photo looks synthetic:** detect artifacts caused by compression, blur, HDR, or low light → recover by finding a higher-quality source before judging.

## Verification

Your conclusion includes visual evidence, source/provenance evidence, and an uncertainty label; if those are missing, the image is marked unverified rather than authentic or fake.

## Variations

- `mobile-app`: screenshot search may lose metadata, so prefer opening the original post or file.
- `journalism`: preserve the original URL, upload time, and file hash for audit.
- `marketplace`: inspect product images for duplicated textures and impossible geometry before buying.

## Safety & privacy

Medium risk because false accusations and false reassurance both cause harm. Do not upload private, intimate, medical, or child images to third-party detectors without explicit permission and a clear retention policy.
