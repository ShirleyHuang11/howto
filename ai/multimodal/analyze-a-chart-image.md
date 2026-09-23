---
name: analyze-a-chart-image
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

Extract the chart type, axes, visible series, and key numerical claims from an image so the result can be checked against a schema and a small human-labeled answer set.

## Preconditions

- A vision-capable model endpoint or a local chart parser/OCR stack.
- Chart images with permission to process them and a small gold set of expected labels or values.
- A JSON Schema validator such as `jsonschema` and basic image metadata tooling such as Pillow.

## Steps

1. **Normalize the chart image.** Resize only if needed, preserve aspect ratio, and keep a lossless or high-quality copy: `python -c "from PIL import Image; im=Image.open('chart.png'); print(im.size, im.mode)"`. → *Expect:* the input dimensions and mode are recorded, and the readable copy is available.
2. **Define the extraction schema.** Require fields such as `chart_type`, `title`, `x_axis`, `y_axis`, `series`, `data_points`, `uncertainties`, and `source_text`. → *Expect:* `jsonschema.Draft202012Validator.check_schema(schema)` completes without an exception.
3. **Run vision extraction.** [BRANCH: Claude/OpenAI vision API | local OCR plus plot digitizer] Send the image with an instruction to output only JSON conforming to the schema. ⚠️ *Data leaves your control:* if using an external API, redact or crop sensitive labels before upload. → *Expect:* the model returns a parseable JSON object rather than prose.
4. **Validate and coerce cautiously.** Parse with `json.loads()`, validate against the schema, and reject invented values marked with high confidence but absent from visible labels. → *Expect:* schema validation passes and unknown or estimated values are explicitly marked.
5. **Compare against the gold set.** For labeled charts, compute exact-match accuracy on categorical fields and tolerance-based numeric accuracy, for example `abs(pred - gold) / max(abs(gold), 1) <= 0.05`. → *Expect:* at least 90% of required fields match and numeric values are within tolerance on the test charts.
6. **Store the structured result with provenance.** Save the JSON next to the image hash and model version. → *Expect:* a reproducible record exists with `image_sha256`, `model`, `prompt_version`, and validated extraction output.

## Decision points

- Numeric accuracy below threshold → use a plot digitizer/OCR pass or ask a human reviewer before relying on values.
- Chart has tiny labels, log axes, stacked bars, or dual axes → require human review or a specialized parser.
- Sensitive chart labels appear in the image → crop, blur, or run a local model instead of sending to a hosted API.

## Failure modes & recovery

- **F1 OCR label drift:** detect mismatched axis labels or garbled text → increase image resolution, crop the plot region, or run dedicated OCR.
- **F2 Hallucinated data point:** detect values not visible in the chart or absent from the legend → reject the field and require `uncertainties`.
- **F3 JSON parse failure:** detect `json.loads()` error → retry once with a stricter JSON-only instruction and then fail closed.
- **F4 Axis-scale mistake:** detect poor numeric accuracy on log or percentage axes → add explicit scale detection and tolerance tests.

## Verification

The extraction JSON parses, validates against the schema, includes image/model provenance, and scores at least 0.90 required-field accuracy with numeric values within 5% relative error on the labeled chart test set.

## Variations

- `hosted vision model`: simplest path; add redaction and request logging controls.
- `local OCR + plot digitizer`: better for confidential images; requires more preprocessing and chart-specific heuristics.
- `spreadsheet-backed chart`: prefer recovering the original data table instead of inferring pixels.

## Safety & privacy

Charts can contain proprietary metrics, patient data, or financial data. Crop unnecessary context, hash images for traceability, avoid sending confidential images to third-party APIs without approval, and treat extracted numerical claims as untrusted until programmatically checked or reviewed.
