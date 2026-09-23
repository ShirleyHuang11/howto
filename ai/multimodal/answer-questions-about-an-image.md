---
name: answer-questions-about-an-image
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

You use a vision-capable model to answer questions about an image, with structured output and checks against unsupported visual claims.

## Preconditions

- Images and questions you are authorized to process.
- A vision-capable model through an API or local runtime; you can call a model as in `ai/call-an-llm-api`.
- A validation schema and a labeled question-answer set for quality checks.

## Steps

1. **Define answer boundaries.** Tell the model to answer only from visible evidence and return uncertainty when the image is insufficient. → *Expect:* the prompt prohibits hidden intent, identity guesses, and unsupported claims.
2. **Prepare the image.** Resize or tile high-resolution images while preserving relevant details. → *Expect:* the model receives an image that keeps the question-relevant region readable.
3. **Call the vision model with a schema.** [BRANCH: Anthropic | OpenAI | open model] Request JSON containing `answer`, `evidence`, `confidence`, and `needs_human_review`. ⚠️ *Data leaves your control:* external APIs receive the image and question. → *Expect:* a structured answer is returned.
4. **Validate the response.** Parse JSON, enforce allowed confidence values, and require evidence text. → *Expect:* malformed responses are retried or rejected.
5. **Cross-check sensitive claims.** Block or flag identity, demographic, medical, legal, or safety-critical answers unless the workflow explicitly supports human review. → *Expect:* high-risk answers are routed for review.
6. **Evaluate against labeled examples.** Score exact match, semantic match, refusal accuracy, and evidence quality. → *Expect:* quality metrics are available before deployment.
7. **Log provenance.** Save image checksum, question id, model, prompt version, response, and validation result. → *Expect:* answers can be audited and reproduced.

## Decision points

- Question asks for invisible context or intent → answer with uncertainty rather than guessing.
- Question requires reading small text → add OCR or higher-resolution crop.
- Use is safety-critical → require human review and do not rely solely on model confidence.
- Data cannot leave local infrastructure → use an approved local vision model.

## Failure modes & recovery

- **F1 Unsupported visual claim:** detect answer not grounded in image evidence → regenerate with stricter grounding or mark as unknown.
- **F2 Missed small detail:** detect wrong answer on tiny objects or text → crop, tile, or use OCR before asking.
- **F3 JSON validation failure:** detect malformed output → retry with structured output mode or stricter schema.
- **F4 Overconfident refusal or answer:** detect confidence not matching correctness → calibrate confidence labels on validation data.

## Verification

The workflow passes only if all responses validate against the schema, the labeled set reaches the required accuracy and refusal-accuracy thresholds, and a grounding check confirms every non-unknown answer includes visible evidence.

## Variations

- `general VQA`: answer broad questions with evidence and uncertainty.
- `document image QA`: combine OCR, layout extraction, and vision answering.
- `local VLM`: use when images are private, accepting more model-management work.

## Safety & privacy

Medium risk because images can reveal people, documents, locations, and private spaces. Avoid identity and sensitive-attribute inference, strip metadata, and approve external API use before sending images outside your environment.
