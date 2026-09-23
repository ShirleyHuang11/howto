---
name: caption-an-image-with-a-model
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

You generate accurate, bounded captions for images and verify that the caption format and quality are suitable for downstream search, accessibility, or labeling.

## Preconditions

- Image files or URLs you are authorized to process.
- Access to a vision-capable model through an API or local runtime; you can call a model as in `ai/call-an-llm-api`.
- A caption style guide and a small gold set for evaluation.

## Steps

1. **Define the caption contract.** Specify length, language, whether to mention uncertainty, and fields such as `caption`, `visible_text`, and `safety_notes`. → *Expect:* a JSON Schema or equivalent output contract.
2. **Prepare images safely.** Resize to the model's supported limits, strip unnecessary metadata, and keep originals unchanged. → *Expect:* each input has a processed copy and checksum.
3. **Call the vision model.** [BRANCH: Anthropic | OpenAI | open model] Send the image plus instruction to return schema-conformant JSON. ⚠️ *Data leaves your control:* if using an external API, confirm the image is allowed to leave your environment. → *Expect:* an API response containing a caption candidate.
4. **Validate structured output.** Parse JSON and validate against the schema. → *Expect:* invalid captions are retried or rejected automatically.
5. **Check hallucination-prone fields.** Ask the model to avoid identities, hidden intent, or invisible details unless explicitly visible. → *Expect:* captions describe observable content and mark uncertainty.
6. **Evaluate on a gold set.** Compare against human captions with task metrics such as human judge pass rate, CLIPScore, or retrieval success. → *Expect:* a score report for the captioning prompt and model.
7. **Store caption provenance.** Save model name, prompt version, image checksum, timestamp, and validation result. → *Expect:* every caption can be traced and regenerated.

## Decision points

- Captions are for accessibility → prioritize concise visible content and avoid speculation.
- Captions are for retrieval → include salient objects, setting, visible text, and domain terms.
- Evaluation finds hallucinated details → tighten the prompt and add rejection checks for unsupported claims.
- Images contain people or sensitive scenes → require privacy and safety review before bulk processing.

## Failure modes & recovery

- **F1 JSON parse failure:** detect invalid JSON → retry with stricter schema instructions or function/structured output mode.
- **F2 Hallucinated identity:** detect named people not provided by metadata → block identity claims and regenerate.
- **F3 Missed visible text:** detect OCR-relevant text absent from captions → add an OCR pass or explicit visible-text field.
- **F4 Oversized image:** detect API image-size error → resize or compress while preserving readability.

## Verification

The captioning run passes only if 100% of outputs parse and validate against the schema, at least the configured quality threshold is met on the gold set, and a spot-check script finds no prohibited identity or invisible-attribute claims.

## Variations

- `Anthropic/OpenAI`: use a current vision-capable model with structured JSON instructions.
- `open model`: use a local VLM such as LLaVA-style or Qwen-VL-style models when data cannot leave your environment.
- `batch labeling`: add deduplication and human review for low-confidence or high-impact images.

## Safety & privacy

Medium risk because images may contain faces, homes, documents, or private context. Remove metadata, avoid identity inference, follow consent rules, and review external API use before sending images out.
