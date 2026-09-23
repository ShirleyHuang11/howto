---
name: measure-instruction-following
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You quantify how reliably a model follows explicit instructions, constraints, and refusal rules. The result is a scored eval with reproducible checks and failure examples.

## Preconditions

- A labeled instruction-following set with prompts and expected constraints.
- A model endpoint, local model server, or batch inference runner.
- Validators for constraints that can be checked programmatically, such as JSON Schema, regex, exact counts, or tool-call assertions.

## Steps

1. **Define instruction categories.** Include format constraints, multi-step ordering, refusal boundaries, citation requirements, and "do not mention" constraints. → *Expect:* each eval item has a `category` and at least one checkable `assertion`.
2. **Write deterministic validators.** Implement checks such as `jsonschema.validate(output, schema)`, `len(items) == 5`, `forbidden not in output.lower()`, or required tool-call names. → *Expect:* validators return structured booleans and error messages for every item.
3. **Generate model outputs.** [BRANCH: Anthropic | OpenAI | open model] Run at low temperature and record parameters. ⚠️ *Data leaves your control:* if prompts contain customer data, redact or use a local model. → *Expect:* every item has exactly one output, or a retry log explaining the missing result.
4. **Score each assertion separately.** Do not collapse multiple instructions into one vague label; record pass/fail by assertion. → *Expect:* output rows include `item_id`, `assertion_id`, `passed`, and `reason`.
5. **Aggregate by category.** Compute overall adherence, category adherence, and strict item pass where all assertions pass. → *Expect:* a report contains metrics such as `strict_item_pass_rate` and `format_pass_rate`.
6. **Inspect high-impact failures.** Sample failures from each category and label whether they are prompt ambiguity, model weakness, or validator bug. → *Expect:* a triage file contains representative failing prompt/output pairs.
7. **Gate releases.** Set thresholds such as `strict_item_pass_rate >= 0.90` and no regression larger than 2 percentage points. → *Expect:* the eval command exits nonzero when thresholds are missed.

## Decision points

- Format failures dominate → add structured-output mode or a repair-and-validate loop.
- Safety/refusal failures occur → block release and run adversarial follow-up tests.
- Validator disagrees with human review → fix the validator before comparing models.
- One category regresses while overall score improves → do not average it away; gate that category separately.

## Failure modes & recovery

- **F1 Ambiguous instruction:** detect human reviewers disagreeing on expected behavior → rewrite the eval item or split it into separate cases.
- **F2 Regex too brittle:** detect valid outputs failing due to harmless phrasing → replace with parsing or semantic checks.
- **F3 JSON parse failure:** detect invalid JSON where structured output was required → use schema-constrained decoding or a repair retry counted separately.
- **F4 Prompt injection bypass:** detect model following text that says to ignore higher-priority instructions → add hierarchy-specific checks and block the release.
- **F5 Rate limit 429:** detect provider throttling → back off, checkpoint completed outputs, and resume.

## Verification

The run passes only when every output is present, every assertion has a recorded boolean result, the summary JSON validates against the eval schema, `strict_item_pass_rate >= 0.90`, and each safety/refusal category is at or above its separate threshold.

## Variations

- `structured output`: validate with JSON Schema or Pydantic models.
- `agent tool use`: assert exact tool names, argument schemas, and tool-call ordering.
- `human preference overlay`: add reviewer labels for borderline cases, but keep deterministic validators as the release gate.

## Safety & privacy

Instruction-following evals often include adversarial or sensitive prompts. Keep test data access controlled, avoid storing real PII, and treat safety-category failures as release blockers rather than ordinary quality bugs.
