---
name: compare-two-images-for-similarity
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

Compare two images using deterministic visual features or embeddings and return a calibrated similarity decision that passes a labeled threshold test.

## Preconditions

- Image pairs you are allowed to process, plus labels for same/different or near-duplicate decisions.
- A similarity method such as perceptual hash, SSIM, CLIP/SigLIP embeddings, or a domain-specific verifier.
- Python imaging tools and a metrics script for ROC/AUC or precision/recall.

## Steps

1. **Define what similarity means.** Decide whether the task is exact duplicate, near duplicate, same object, same person, or same scene. → *Expect:* the acceptance label and false-positive cost are documented.
2. **Normalize inputs.** Decode, rotate by EXIF, resize consistently, and reject corrupt files. → *Expect:* both images have valid dimensions and a standard color mode.
3. **Compute similarity features.** [BRANCH: perceptual hash for duplicates | SSIM for aligned images | embeddings for semantic similarity] Generate the score and record method version. → *Expect:* each pair gets a numeric score and method metadata.
4. **Calibrate a threshold.** Use labeled pairs to choose a threshold that meets the desired precision or recall. → *Expect:* a threshold is selected from validation metrics, not intuition.
5. **Return structured output.** Include `similar`, `score`, `threshold`, `method`, and `needs_review` for borderline scores. → *Expect:* the JSON output validates against the comparison schema.
6. **Test adversarial cases.** Include crops, compression artifacts, screenshots, watermarks, and visually similar but different items. → *Expect:* known hard negatives stay below the similarity threshold.

## Decision points

- Need exact duplicate detection → use hashes and perceptual hashes before expensive models.
- Need semantic similarity → use multimodal embeddings and calibrate on domain data.
- Comparing faces or biometric identity → perform legal/privacy review and use specialized, consented workflows.

## Failure modes & recovery

- **F1 False match on similar products:** detect high score for different SKUs → add hard negatives and raise threshold.
- **F2 Missed crop/resize duplicate:** detect low score for transformed same image → use crop-resistant features or embeddings.
- **F3 Corrupt input:** detect decoder errors → reject with a typed error instead of returning low similarity.
- **F4 Threshold drift:** detect validation metrics falling after model changes → re-calibrate and version thresholds with the model.

## Verification

On a labeled validation set, the comparison script outputs valid JSON for every pair, achieves the configured metric target such as `precision >= 0.95` at the chosen threshold, and flags scores within a configured margin as `needs_review`.

## Variations

- `perceptual hash`: fast for duplicate and near-duplicate media.
- `SSIM`: useful for aligned render regression checks.
- `embedding similarity`: handles crops and semantic matches better but needs careful threshold calibration.

## Safety & privacy

Image similarity can expose private media relationships or enable biometric matching. Avoid face identity use unless explicitly approved, minimize retained images, and log only hashes or derived scores when raw images are sensitive.
