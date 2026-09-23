---
name: extract-structured-data-from-text
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Extract fields from unstructured text into a validated schema with measured field-level accuracy and safe handling of missing or ambiguous values.

## Preconditions

- A representative sample of source documents or messages.
- A JSON Schema, Pydantic model, or equivalent typed schema for the extracted fields.
- Labeled examples for at least the most important fields.

## Steps

1. **Define the extraction schema.** Include field types, required fields, enums, date formats, and how to represent unknown values. → *Expect:* a schema file that rejects malformed records.
2. **Write source-grounded instructions.** Tell the model to extract only facts present in the text and use `null` for missing or ambiguous fields. → *Expect:* a prompt that forbids inference beyond the source.
3. **Request structured output.** [BRANCH: Anthropic | OpenAI | open model] Use tool calling, JSON mode, or constrained decoding where available. ⚠️ *Data leaves your control:* redact or pseudonymize PII before sending source text to a third-party API. → *Expect:* a JSON object matching the target top-level shape.
4. **Parse and validate every response.** Reject invalid JSON, wrong types, extra fields if disallowed, and impossible values. → *Expect:* validation returns either a typed object or a specific error.
5. **Normalize deterministic fields in code.** Convert dates, currencies, units, and casing after extraction rather than asking the model to do all normalization. → *Expect:* canonical values such as ISO dates and decimal currency amounts.
6. **Score against labeled data.** Compute exact match for enums, tolerant match for dates and amounts, and field-level precision, recall, and F1. → *Expect:* a metrics table by field.
7. **Add a repair path for invalid outputs.** Retry once with the validation error and original text, then fail closed if still invalid. → *Expect:* no invalid record enters the downstream system.

## Decision points

- Field is absent in the text → output `null`, not a guessed value.
- Field-level F1 below threshold → add examples or split the document before extraction.
- Dates or units vary by locale → normalize in code with explicit locale assumptions.
- Extraction feeds a high-impact decision → require human review for low-confidence or missing critical fields.

## Failure modes & recovery

- **F1 Hallucinated field:** detect value not supported by source span → require evidence spans or reject unsupported fields.
- **F2 JSON parse failure:** detect parser exception → use structured output or one repair retry.
- **F3 Schema drift:** detect new source format causing many nulls → update labels and schema intentionally.
- **F4 Ambiguous entity:** detect multiple possible values → include all candidates or mark ambiguous according to schema.

## Verification

Run extraction on a labeled holdout set. Success means `100%` of accepted records validate against the schema, critical fields meet `>= 0.90` field-level F1 or the chosen threshold, unsupported-value rate is `0` in sampled evidence checks, and invalid records are quarantined.

## Variations

- `receipts and invoices`: use OCR confidence and deterministic currency/date normalization.
- `contracts`: require evidence spans for every extracted obligation or date.
- `open model`: use grammar-constrained decoding or a JSON repair parser with strict validation.

## Safety & privacy

Source text may contain PII, contracts, or customer data. Minimize fields, redact before third-party calls where possible, encrypt stored raw text, and fail closed when extraction confidence is too low for consequential use.
