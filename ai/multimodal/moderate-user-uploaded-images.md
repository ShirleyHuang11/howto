---
name: moderate-user-uploaded-images
domain: ai
subdomain: multimodal
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Block, quarantine, or allow user-uploaded images according to a written policy, with automated labels, confidence scores, and audit logs that can be evaluated against a labeled moderation set.

## Preconditions

- A clear image safety policy with categories such as sexual content, minors, graphic violence, self-harm, hate symbols, private data, and malware/QR abuse.
- A moderation model or API, plus a labeled validation set that represents your product.
- Secure object storage where quarantined uploads are not publicly served.

## Steps

1. **Write the category schema.** Define labels, severity levels, thresholds, and actions: `allow`, `blur`, `quarantine`, `human_review`, or `reject`. → *Expect:* a versioned YAML/JSON policy file exists and has no duplicate category ids.
2. **Validate upload metadata before model calls.** Check MIME type, file size, dimensions, and decodeability with Pillow or ImageMagick. → *Expect:* corrupt, oversized, or unsupported files are rejected before moderation.
3. **Run image moderation.** [BRANCH: hosted moderation API | local safety classifier] Send only the image bytes or a private signed URL with least privilege. ⚠️ *Data leaves your control:* user images sent to an external API may contain faces, documents, or private spaces; disclose this and avoid external processing where policy forbids it. → *Expect:* a structured moderation result with labels and scores is returned.
4. **Apply deterministic thresholds.** Convert labels and scores into an action using the policy file, not ad hoc code paths. → *Expect:* each upload gets exactly one final action and a reason code.
5. **Quarantine before serving.** Store new uploads in a non-public bucket until the action is `allow` or `blur`. ⚠️ *Irreversible:* publicly serving harmful or illegal content can create user harm and legal exposure; confirm moderation passes before publishing. → *Expect:* blocked images never receive a public URL.
6. **Evaluate on labeled images.** Compute precision, recall, and false-negative rate by category. → *Expect:* high-severity categories meet the required recall target, such as `recall >= 0.98` for child-safety and graphic-violence blocks.

## Decision points

- High-severity recall below target → keep quarantine default and improve classifier, thresholds, or human review.
- False positives harm legitimate users → route medium-confidence cases to review instead of hard rejection.
- Jurisdiction or platform policy requires reporting → involve legal/trust-and-safety workflows before automating reports.

## Failure modes & recovery

- **F1 Decoder bypass:** detect files that claim one MIME type but decode as another → sniff content bytes and re-encode accepted images.
- **F2 Model blind spot:** detect false negatives in evals or appeals → add targeted examples and raise thresholds for risky categories.
- **F3 Public-before-moderated race:** detect public URLs created before action is known → change upload flow to private staging first.
- **F4 Missing audit trail:** detect moderation actions with no policy version or model version → reject deployment until logging is complete.

## Verification

A test upload suite produces one policy action per image, blocked fixtures never receive public URLs, and the labeled validation set meets category thresholds, including `recall >= 0.98` for high-severity block categories and `precision >= 0.90` for auto-reject actions.

## Variations

- `hosted moderation API`: faster to integrate; requires privacy review and vendor retention settings.
- `local classifier`: better data control; requires model evaluation and regular updates.
- `human review queue`: necessary for appeals and ambiguous content; add reviewer tooling and access controls.

## Safety & privacy

This is high risk because uploads may include illegal material, faces, IDs, or private locations. Minimize retention, restrict reviewer access, encrypt storage, document data sharing with moderation providers, and fail closed for high-severity categories.
