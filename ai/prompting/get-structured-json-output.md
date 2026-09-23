---
name: get-structured-json-output
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You make an LLM return machine-readable JSON that validates against a schema and can be safely consumed by downstream code.

## Preconditions

- A model endpoint that supports JSON mode, tool/function calling, or strict instruction following.
- A JSON Schema or typed model for the desired output.
- A parser and validator such as `jsonschema`, Pydantic, Zod, or Ajv.

## Steps

1. **Define the schema before prompting.** Write required fields, types, enums, nullable fields, and maximum lengths. → *Expect:* `schema.json` validates with `python -m json.tool schema.json`.
2. **Choose the structured-output mechanism.** [BRANCH: tool call | JSON mode | prompt-only] Use native structured output when available; otherwise include the schema and require JSON only. → *Expect:* the request config names the schema or includes the schema text.
3. **Provide one valid example.** Show exactly one compact object that passes the schema. → *Expect:* the example validates locally.
4. **Call the model with low randomness.** Use temperature near 0 for extraction and routing tasks. ⚠️ *Data leaves your control:* if the input contains user data and you call an external API, redact or approve it first. → *Expect:* the raw response contains either a tool-call payload or a JSON object.
5. **Parse and validate before use.** Reject outputs that fail JSON parsing or schema validation. → *Expect:* invalid outputs raise a controlled validation error, not a downstream crash.
6. **Retry with a repair prompt once.** Send the validation error and original output back for correction only if the task is safe to retry. → *Expect:* the repaired output validates or the pipeline returns a typed failure.

## Decision points

- Native schema support is available → prefer it over free-form JSON instructions.
- Validation fails repeatedly → simplify the schema or split the task into smaller calls.
- Output is used for actions or database writes → require validation plus human or policy review for high-impact actions.

## Failure modes & recovery

- **F1 Markdown wrapper:** detect ```json fences around output → strip only known wrappers, then validate.
- **F2 Missing required field:** detect schema error → retry once with the exact validation message.
- **F3 Wrong enum value:** detect value outside allowed set → map only if deterministic, otherwise reject.
- **F4 Prompt injection in fields:** detect instructions inside extracted text → treat field values as data, never executable instructions.

## Verification

Run `python validate_outputs.py --schema schema.json --responses outputs.jsonl`; 100% of accepted responses parse as JSON and validate against the schema, and invalid responses are recorded with a typed error instead of being consumed.

## Variations

- `Anthropic`: use tool use for strict object-shaped outputs when available.
- `OpenAI`: use structured outputs or JSON schema response formats for strict validation.
- `local model`: add grammar-constrained decoding if the serving stack supports it.

## Safety & privacy

JSON validity is not truth. Validate types and constraints, then separately verify factual claims and permissions. Redact sensitive input before external API calls and never execute strings from model output as code, SQL, shell, or policy.
