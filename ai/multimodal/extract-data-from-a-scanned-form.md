---
name: extract-data-from-a-scanned-form
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

Convert a scanned form into validated structured data with field-level confidence, provenance, and automated checks against required business rules.

## Preconditions

- Permission to process the scanned forms and a retention policy for documents that may contain PII.
- A target schema with required fields, allowed formats, and validation rules.
- OCR or document-understanding tooling, such as a vision LLM, Tesseract, AWS Textract, Google Document AI, or Azure Document Intelligence.

## Steps

1. **Prepare representative scans.** Include clean, skewed, handwritten, low-contrast, and multi-page examples. → *Expect:* a test folder with labeled expected JSON for at least 20 forms.
2. **Define the output schema.** Include fields, types, confidence scores, page numbers, bounding boxes where available, and `needs_review`. → *Expect:* the schema validates with `jsonschema` and encodes every required field.
3. **Preprocess images.** Deskew, rotate, de-noise, and split pages without changing document meaning. → *Expect:* each input produces readable page images and a processing manifest.
4. **Extract fields.** [BRANCH: hosted document AI | vision LLM | local OCR plus rules] Run extraction into the schema. ⚠️ *Data leaves your control:* scanned forms often contain PII; redact unnecessary fields or use local processing unless external transfer is approved. → *Expect:* parseable JSON with field values, confidence, and provenance.
5. **Validate business rules.** Check formats such as dates, totals, IDs, signatures, and cross-field consistency. → *Expect:* invalid or low-confidence fields are marked `needs_review: true`.
6. **Score field accuracy.** Compare extracted values with labeled truth using exact match for identifiers and normalized match for names/addresses. → *Expect:* required fields meet the acceptance threshold, such as `field_f1 >= 0.95`.
7. **Export only validated records.** Send accepted JSON to the downstream system and route review cases separately. → *Expect:* downstream writes contain only records passing schema and business validation.

## Decision points

- Field-level confidence is low → route to human review instead of guessing.
- Handwriting or checkboxes dominate → use a document AI model trained for forms, not generic OCR alone.
- PII is not needed downstream → redact or tokenize before storage.

## Failure modes & recovery

- **F1 Page rotation error:** detect missing header fields or OCR confidence collapse → run orientation detection and retry.
- **F2 Schema mismatch:** detect validation failure → version the schema and add migration code rather than silently dropping fields.
- **F3 Transposed totals:** detect totals that fail arithmetic checks → mark for review and keep page provenance.
- **F4 PII leakage:** detect raw form images in debug logs → disable payload logging and rotate exposed credentials if needed.

## Verification

On the labeled form set, every extraction parses as JSON and validates against the schema, required-field F1 is at least 0.95, identifier exact-match accuracy is at least 0.98, and no `needs_review` record is written to the accepted downstream table.

## Variations

- `Textract/Document AI/Azure`: strong layout extraction; map provider-specific blocks into your stable schema.
- `vision LLM`: flexible for unusual forms; require strict JSON validation and review thresholds.
- `local OCR`: best for sensitive data; expect more custom layout rules.

## Safety & privacy

Forms commonly contain names, addresses, IDs, financial data, or health data. Use least-privilege storage, encrypt files, minimize retention, redact logs, and get approval before sending scans to any third-party processor.
