---
name: generate-an-image-from-a-prompt
domain: ai
subdomain: multimodal
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You generate an image from a prompt, save its provenance, and verify that it satisfies format, safety, and task-specific quality requirements.

## Preconditions

- Access to an image-generation model or API and permission to generate the requested content.
- A written prompt, target size, style constraints, and intended use.
- Storage for generated assets and metadata.

## Steps

1. **Write a concrete prompt and constraints.** Include subject, composition, medium, aspect ratio, text requirements, and exclusions. → *Expect:* a prompt that can be reviewed before generation.
2. **Check policy and rights.** Confirm the prompt does not request disallowed content, private likenesses, protected logos, or copyrighted style imitation beyond your policy. → *Expect:* the generation request is approved or revised.
3. **Generate a small batch.** [BRANCH: hosted API | local diffusion model] Request 2-4 candidates with fixed size and saved seed when supported. ⚠️ *Data leaves your control:* prompts and reference images sent to hosted APIs may be retained according to provider settings. → *Expect:* image files and metadata are returned.
4. **Validate technical outputs.** Check file exists, dimensions, MIME type, color mode, and file size. → *Expect:* each output matches the requested technical constraints.
5. **Score against the brief.** Use a human rubric, vision model judge, or CLIP-style similarity where appropriate. → *Expect:* each candidate has an accept/reject score.
6. **Inspect text and sensitive details.** If the image contains words, faces, medical, legal, or brand-sensitive content, review manually. → *Expect:* problematic candidates are rejected or regenerated.
7. **Save provenance.** Store prompt, model, parameters, seed, timestamp, reviewer, and final file hash. → *Expect:* accepted image is traceable and reproducible as far as the generator allows.

## Decision points

- Output must match exact layout or text → use image editing, typography tools, or post-processing rather than relying only on generation.
- Brand or legal use → require human approval before publication.
- Generated images fail the rubric → revise prompt with concrete visual constraints and regenerate a small batch.
- Sensitive input images are required → prefer approved local tools or a provider with suitable data controls.

## Failure modes & recovery

- **F1 Wrong dimensions:** detect image size mismatch → request supported dimensions or resize/crop with explicit rules.
- **F2 Garbled text:** detect misspelled or unreadable text → add text in a design tool after generation.
- **F3 Policy rejection:** detect API safety refusal → revise the prompt to a permitted request.
- **F4 Poor prompt adherence:** detect low rubric score → add concrete constraints, reference-free descriptions, or use image editing with masks.

## Verification

The generation passes only if selected output files exist, dimensions and MIME type match the spec, metadata includes prompt and model parameters, and the accepted image meets the project rubric threshold with any required human approval recorded.

## Variations

- `hosted image API`: easiest setup, but review prompt and image data handling.
- `local diffusion`: better for private drafts and custom control, but requires GPU and model management.
- `image editing workflow`: use masks or control images when exact placement matters.

## Safety & privacy

Medium risk from content policy, likeness, copyright, and data-transfer issues. Review prompts and references before sending them to external APIs, avoid generating deceptive real-person imagery, and require human approval for public or commercial use.
