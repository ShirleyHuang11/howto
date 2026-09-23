---
name: chain-multiple-prompts
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

Build a multi-step prompt chain where each step has a typed input, typed output, and validation gate before the next model call runs.

## Preconditions

- A task that naturally decomposes, such as classify → extract → draft → verify.
- A model API client and a small orchestration script or workflow runner.
- Schemas for intermediate artifacts, such as Pydantic models or JSON Schema.

## Steps

1. **Draw the chain as data flow.** Name each prompt step, its input fields, output schema, and failure behavior. → *Expect:* a diagram or config listing every step and dependency.
2. **Make intermediate outputs structured.** Use JSON, tool calls, or provider structured outputs rather than prose handoffs. → *Expect:* each step has a schema validator.
3. **Implement one step at a time.** [BRANCH: Anthropic | OpenAI | open model] Call the model, parse the response, validate it, and persist the result before continuing. ⚠️ *Data leaves your control:* redact sensitive fields before any external model call. → *Expect:* every step produces a saved artifact with `status: pass` or `status: fail`.
4. **Add guard checks between steps.** Stop if classification confidence is too low, extraction is incomplete, or policy flags are raised. → *Expect:* invalid intermediate outputs never reach later prompts.
5. **Keep prompts independently testable.** Store fixtures for each step so a change to the drafting prompt does not require rerunning extraction. → *Expect:* unit tests can run each prompt with canned inputs.
6. **Propagate trace IDs and costs.** Log prompt version, model, latency, tokens, and parent artifact ID for every call. → *Expect:* one trace reconstructs the complete chain.
7. **Run end-to-end evaluation.** Compare final outputs against a labeled set and inspect which step caused each failure. → *Expect:* an error report grouped by chain step.

## Decision points

- A step output is not machine-validated → do not feed it to the next step.
- A chain uses more than 3-4 model calls → check whether a single structured prompt is sufficient.
- Early step has low recall → fix it first because downstream prompts cannot recover missing facts.
- Cost exceeds budget → cache stable intermediate outputs or combine low-risk steps.

## Failure modes & recovery

- **F1 Cascading hallucination:** detect unsupported facts in final output → validate extracted facts before drafting.
- **F2 Schema mismatch:** detect parse errors between steps → version schemas and reject incompatible artifacts.
- **F3 Silent retry drift:** detect different outputs after retries → log retry attempts and compare parsed artifacts.
- **F4 Cost explosion:** detect calls per request above plan → add caching and hard per-request call limits.

## Verification

Run the chain on a labeled eval set. Success means every intermediate artifact validates against its schema, no failed step is passed downstream, end-to-end task score meets the threshold, and total model calls plus estimated cost per request stay within the configured budget.

## Variations

- `LangGraph or workflow engine`: use nodes for prompt steps and edges for validation gates.
- `serverless`: persist intermediate artifacts so retries are idempotent.
- `local model`: use stricter parsers and repair prompts because structured adherence may be weaker.

## Safety & privacy

Prompt chains multiply data exposure and failure surfaces. Redact once at the boundary, log only necessary fields, avoid storing raw PII in traces, and require review before enabling actions based on chained outputs.
