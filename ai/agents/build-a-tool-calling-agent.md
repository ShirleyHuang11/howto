---
name: build-a-tool-calling-agent
domain: ai
subdomain: agents
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

You build an agent that can call approved tools, validate tool inputs and outputs, and stop with a verifiable final answer.

## Preconditions

- An LLM API or local model that supports structured tool calls or JSON actions.
- A small set of safe tools with schemas, timeouts, and permissions.
- Test tasks with expected tool calls and final results.
- Logging for model messages, tool calls, tool results, and errors.

## Steps

1. **Define the agent boundary.** Specify allowed tasks, allowed tools, forbidden actions, and when to ask a human. → *Expect:* a policy file or system prompt that names the boundary clearly.
2. **Register tools with schemas.** Provide each tool name, description, JSON schema, timeout, side-effect level, and auth scope. → *Expect:* schemas validate with a JSON Schema validator.
3. **Call the model with tool definitions.** [BRANCH: Anthropic tool use | OpenAI tools | local JSON action model] ⚠️ *Data leaves your control:* external model calls receive user input and tool results; redact sensitive data first. → *Expect:* the model either returns a final answer or a structured tool call.
4. **Validate tool inputs before execution.** Parse arguments, validate schema, enforce permission checks, and reject unknown tools. → *Expect:* invalid calls produce a controlled error message, not tool execution.
5. **Execute tools in a sandboxed wrapper.** Apply timeouts, retries for safe reads, and output size limits. → *Expect:* every tool result is structured and tagged as untrusted data.
6. **Return tool results to the model.** Include only necessary result fields and never treat tool output as instructions. → *Expect:* the next model turn uses the data while following the original system policy.
7. **Stop deterministically.** Cap iterations and require a final answer schema such as `{answer, tool_calls_used, confidence}`. → *Expect:* the loop ends by final answer, human handoff, or max-iteration failure.
8. **Run agent evals.** Test happy paths, invalid arguments, prompt injection in tool output, and unavailable tools. → *Expect:* pass rate and failure reasons are reported automatically.

## Decision points

- Tool has side effects → require explicit user or human approval before execution.
- Tool output contains instructions → ignore them and summarize only data fields.
- Agent exceeds iteration cap → return partial state and ask for clarification or human help.
- Eval shows wrong tool selection → improve tool descriptions or split ambiguous tools.

## Failure modes & recovery

- **F1 Invalid tool arguments:** detect schema validation failure → return a tool error and let the model repair once.
- **F2 Tool hallucination:** detect unknown tool name → reject and remind the model of available tools.
- **F3 Prompt injection via tool output:** detect output asking to ignore instructions → treat as data and keep system policy dominant.
- **F4 Runaway loop:** detect repeated calls or max iterations → stop and surface a controlled failure.

## Verification

The agent test suite must show 100% schema validation on tool inputs and final answers, zero execution of unknown or unauthorized tools, successful completion of the golden tasks above the target pass rate, and controlled failure when tools time out or return malicious text.

## Variations

- `read-only-agent`: allow automatic execution for low-risk information lookup tools.
- `write-capable-agent`: add approval gates and audit logs before side effects.
- `local-model`: use a JSON action format and strict parser when native tool calling is unavailable.

## Safety & privacy

Tools can turn model mistakes into real actions. Keep least-privilege credentials, validate all arguments, cap loops and costs, redact sensitive data sent to external models, and require review before write, payment, deletion, messaging, or deployment tools run.
