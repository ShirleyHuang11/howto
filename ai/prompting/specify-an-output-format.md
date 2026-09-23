---
name: specify-an-output-format
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

You define an output format that is easy for humans or programs to consume, then verify that model responses conform to it consistently.

## Preconditions

- A clear consumer for the output: human reader, API, database, evaluator, or UI.
- A format choice such as JSON, Markdown table, bullet list, CSV, or tool call.
- Representative cases including missing information and edge cases.

## Steps

1. **Pick the strictest useful format.** Use JSON or tool calls for machines, concise Markdown for humans, and avoid formats that require fragile parsing. → *Expect:* a documented format choice with a consumer named.
2. **Write the format contract.** Define required fields, order, units, allowed labels, and what to output when data is missing. → *Expect:* a validator or checklist can determine conformance.
3. **Include one valid example.** Keep the example short and syntactically valid. → *Expect:* the example passes the same validation as model outputs.
4. **Forbid extra wrapper text.** Tell the model whether prose before or after the output is allowed. → *Expect:* responses start directly with the required structure.
5. **Validate model responses.** Parse the output or run a lint check after every call. → *Expect:* invalid responses are rejected before downstream consumption.
6. **Measure conformance on varied inputs.** Run the format prompt across normal, empty, long, and adversarial cases. → *Expect:* a conformance report with parse and field-completeness rates.

## Decision points

- Output drives automation → require schema validation, not a visual format.
- Human readability matters more than parsing → use Markdown headings or bullets with fixed labels.
- Conformance below 98% → switch to native structured output or simplify the format.

## Failure modes & recovery

- **F1 Extra prose:** detect text before JSON or table → add stricter instruction and parser rejection.
- **F2 Missing fields:** detect absent required keys → retry once with validation error.
- **F3 Wrong units:** detect values in unexpected units → specify units in field names and validate ranges.
- **F4 Ambiguous labels:** detect synonyms for enum values → use a closed enum and examples.

## Verification

Run `python check_output_format.py --format schema.json --responses responses.jsonl --min-parse-rate 0.98`; at least 98% of responses parse and 100% of accepted responses contain every required field with valid enum values and units.

## Variations

- `JSON`: best for programmatic consumption.
- `Markdown`: best for user-facing summaries that still need predictable headings.
- `CSV`: use only when fields cannot contain unescaped commas, newlines, or complex objects.

## Safety & privacy

Format compliance does not prove correctness or safety. Validate content separately, treat model-generated URLs and commands as untrusted, and avoid logging sensitive fields unless required.
