---
name: evaluate-function-calling
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/evals/build-an-eval-set]
status: draft
last_verified: 2026-09-22
---

## Goal

You evaluate whether a model chooses the correct tool or function and supplies valid arguments. The eval catches wrong calls, missing calls, unsafe calls, and schema-invalid arguments.

## Preconditions

- Tool schemas in JSON Schema or provider-native tool format.
- Eval examples with expected tool name, required arguments, and cases where no tool should be called.
- A harness that records model tool calls before executing anything.

## Steps

1. **Define expected tool behavior.** For each example, label required tool name, argument constraints, and whether execution is allowed. → *Expect:* every row has a machine-checkable expected call.
2. **Run the model with tools enabled.** Capture raw tool call JSON without executing side effects. ⚠️ *Data leaves your control:* prompts sent to external APIs should not include real secrets or unauthorized user data. → *Expect:* one recorded decision per example.
3. **Validate the schema.** Use `jsonschema.validate(arguments, tool_schema)` for the selected tool. → *Expect:* schema pass/fail is recorded separately from semantic correctness.
4. **Score tool selection.** Compare selected tool to expected tool or expected no-call. → *Expect:* selection precision, recall, and no-call accuracy.
5. **Score arguments.** Check exact fields, normalized values, ranges, and required ids. → *Expect:* argument accuracy by field and whole-call accuracy.
6. **Test safety gates.** Include examples that request unauthorized, destructive, or irrelevant tool use. → *Expect:* forbidden calls are refused or require confirmation.

## Decision points

- Correct tool but bad arguments → improve schema descriptions, examples, or validation feedback.
- Over-calling tools → add no-call examples and require evidence before tool use.
- Unsafe tool call appears → block execution path until authorization and confirmation checks exist.

## Failure modes & recovery

- **F1 Invalid JSON arguments:** detect parser or schema errors → use structured tool calling and stricter schemas.
- **F2 Wrong tool:** detect semantically similar but incorrect tool → clarify tool descriptions and add contrastive examples.
- **F3 Unsafe execution:** detect real side effect during eval → switch to dry-run mocks and audit credentials.
- **F4 Hidden default mismatch:** detect omitted arguments filled incorrectly downstream → score post-normalization and raw arguments.

## Verification

The harness reports tool-selection accuracy, no-call accuracy, schema-valid rate, required-argument accuracy, and forbidden-call count. A release passes only if schema-valid rate is at least 0.99 and forbidden-call count is zero.

## Variations

- `OpenAI tools`: inspect `tool_calls` and validate JSON arguments.
- `Anthropic tools`: inspect `tool_use` blocks and validate input objects.
- `agent framework`: intercept tool calls before executor dispatch.

## Safety & privacy

Never execute destructive or external tools during eval unless they are mocked. Treat tool arguments as untrusted, validate them server-side, and require user confirmation for irreversible or sensitive actions.
