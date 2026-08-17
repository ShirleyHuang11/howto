---
name: upscale-an-old-photo
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Improve the usable resolution of an old photo while preserving the original file and avoiding misleading edits.

## Preconditions

- You have the original scan or highest-quality digital copy available.
- You have permission to process the people shown in the photo.

## Steps

1. **Preserve the original.** Make a copy before editing and keep the untouched file in a safe folder. → *Expect:* the original can be restored at any time.
2. **Choose a tool.** [BRANCH: local editor | AI web service] prefer local tools for family, identity, or sensitive images; use web services only when acceptable. → *Expect:* privacy risk is understood.
3. **Set conservative enhancement.** Choose moderate upscaling and avoid aggressive face reconstruction unless the goal is clearly cosmetic. → *Expect:* the image improves without changing identity-defining features.
4. **Run the upscale.** Process the copy and save the output with a new filename that marks it as enhanced. → *Expect:* both original and enhanced files exist.
5. **Compare closely.** Check eyes, teeth, hands, clothing patterns, text, and background details for invented artifacts. → *Expect:* artificial changes are accepted, reduced, or rejected.
6. **Export for use.** Save a high-quality version for printing or sharing and keep notes about the tool used. → *Expect:* recipients can distinguish restoration from original evidence.

## Decision points

- The photo is evidence, archive material, or identity documentation → do not replace the original and label enhancements clearly.
- The tool invents faces or text → lower enhancement strength or use a non-generative resize.
- The image includes living private people → get permission before uploading to a cloud service.

## Failure modes & recovery

- **F1 Changed likeness:** detect a face looks like a different person → recover by reverting to the original or using lower-strength enhancement.
- **F2 Fake detail:** detect new text, jewelry, wrinkles, or objects → recover by labeling the result as AI-enhanced or discarding it.
- **F3 Original overwritten:** detect only the edited file remains → recover from backup and restart with a copy.

## Verification

The enhanced file is larger or clearer, the untouched original still exists, and any invented or uncertain details are either absent or clearly disclosed.

## Variations

- `mobile-app`: duplicate the photo before using one-tap enhancement.
- `print`: match export size to the print dimensions and inspect at 100 percent zoom.
- `genealogy`: keep the original scan, date, source, and enhancement notes together.

## Safety & privacy

Medium risk because AI upscalers can alter faces and create false historical details. Treat enhanced photos as restorations, not proof of what was present.
