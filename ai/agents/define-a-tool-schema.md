---
name: define-a-tool-schema
domain: ai
subdomain: agents
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

You define a tool contract that an LLM agent can call reliably and your runtime can validate before execution.

## Preconditions

- A specific capability to expose as a tool.
- Knowledge of the tool's side effects, auth scope, and expected outputs.
- A JSON Schema validator or typed runtime such as Pydantic, Zod, or TypeBox.
- Example valid and invalid calls.

## Steps

1. **Name one narrow action.** Use a verb phrase like `search_docs` or `create_calendar_event`, not a vague tool like `do_work`. → *Expect:* the tool name maps to one operational capability.
2. **Write a model-facing description.** State when to use the tool, when not to use it, and what information is required. → *Expect:* a reader can distinguish this tool from neighboring tools.
3. **Define input JSON Schema.** Specify types, required fields, enums, bounds, formats, and `additionalProperties: false`. → *Expect:* invalid extra fields are rejected by the validator.
4. **Define output schema.** Return structured data and status codes rather than prose, including errors the model can recover from. → *Expect:* downstream code can parse every successful and failed result.
5. **Mark risk and approval requirements.** Label the tool as read-only, low-risk write, or high-impact side effect. ⚠️ *Irreversible:* if the tool deletes, sends, purchases, deploys, or changes access, require explicit approval and audit logging before execution. → *Expect:* the runtime knows whether it can auto-run the tool.
6. **Add runtime validation.** Validate arguments before execution and validate tool output before sending it back to the model. → *Expect:* malformed inputs and outputs fail closed.
7. **Test examples.** Run unit tests for valid calls, missing required fields, wrong types, boundary values, and injection-like strings. → *Expect:* tests pass and produce clear validation errors.

## Decision points

- Arguments require natural language blobs → add length limits and clarify accepted content.
- Tool has multiple modes → split into separate tools or use a small enum with different required fields.
- Model keeps misusing the tool → improve description, examples, or schema names.
- Tool touches user data → include consent, user id, and authorization checks outside the model.

## Failure modes & recovery

- **F1 Ambiguous schema:** detect frequent wrong argument combinations → split the tool or add stricter required fields.
- **F2 Extra-field smuggling:** detect unrecognized fields accepted → set `additionalProperties: false`.
- **F3 Unvalidated output:** detect downstream parser errors → validate and normalize tool results before model handoff.
- **F4 Unsafe auto-execution:** detect writes running without approval → mark side-effect level and block until approved.

## Verification

The schema must pass JSON Schema validation tests: all golden valid calls pass, all invalid examples fail, output examples parse against the output schema, and any side-effecting tool is flagged for approval by the runtime.

## Variations

- `pydantic`: define Python models and export JSON Schema for the LLM API.
- `zod`: define TypeScript schemas and infer runtime types.
- `openapi`: generate tool schemas from existing API specs, then simplify descriptions for model use.

## Safety & privacy

A schema is part of the safety boundary, but not the whole boundary. Enforce authorization in code, keep secrets out of schemas and descriptions, constrain free-text fields, and require approval for irreversible or externally visible actions.
