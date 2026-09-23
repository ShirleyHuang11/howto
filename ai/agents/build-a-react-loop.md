---
name: build-a-react-loop
domain: ai
subdomain: agents
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

You implement a reason-act-observe loop that lets an agent use tools iteratively while staying bounded, inspectable, and testable.

## Preconditions

- A model that can emit structured actions or tool calls.
- A set of tools with validated schemas.
- A loop runner with persistent trace logging.
- Golden tasks that require one or more tool calls.

## Steps

1. **Define loop state.** Track user goal, messages, tool calls, observations, iteration count, token use, and stop reason. → *Expect:* each run has a complete trace object.
2. **Prompt for structured actions.** Ask the model to choose either `final_answer` or one allowed tool call with JSON arguments. [BRANCH: native tool calling | JSON action format] → *Expect:* every model turn parses into one known action type.
3. **Validate before acting.** Check tool name, argument schema, authorization, and side-effect policy before execution. → *Expect:* invalid actions produce a recoverable observation instead of executing.
4. **Execute and observe.** Run the tool with timeout and return a concise structured observation to the model. → *Expect:* the next loop turn sees data, error, or approval-needed status.
5. **Bound the loop.** Set max iterations, max tokens, max wall time, and repeated-action detection. → *Expect:* runaway loops stop with a controlled failure.
6. **Separate reasoning from logs.** Store enough decision trace for debugging without exposing hidden chain-of-thought to users. → *Expect:* user-facing output contains final answer and tool summary, not private reasoning traces.
7. **Evaluate loop behavior.** Run tasks that require zero, one, and multiple tool calls plus adversarial tool output. ⚠️ *Data leaves your control:* hosted model calls receive task state and observations; redact sensitive tool outputs. → *Expect:* tests report success, stop reason, and tool-call correctness.

## Decision points

- Tool side effect is requested → pause for human approval before the act step.
- The same tool call repeats → stop or ask the model to revise with the last error.
- Observation is too large → summarize or page results before returning to the model.
- User goal is ambiguous → ask a clarifying question instead of looping.

## Failure modes & recovery

- **F1 Infinite loop:** detect iteration or repeated-call limit → stop with a clear error and trace id.
- **F2 Invalid action JSON:** detect parser failure → give one repair opportunity, then fail.
- **F3 Observation injection:** detect tool output containing instructions → return it as quoted data and keep policy separate.
- **F4 Hidden state loss:** detect missing prior observations → persist loop state after every step.

## Verification

The loop test suite must show all model actions parse into the action schema, invalid actions never execute tools, golden multi-step tasks complete within iteration and token budgets, and adversarial observations do not change allowed-tool policy.

## Variations

- `native-tools`: use provider tool-call messages and let the SDK handle action envelopes.
- `json-react`: require a strict JSON object with `thought_summary`, `action`, and `args`.
- `workflow-agent`: replace free-form looping with a fixed state machine for high-stakes tasks.

## Safety & privacy

Loops magnify small mistakes. Keep strict iteration and cost limits, validate every action outside the model, redact sensitive observations sent to hosted models, and require approval for irreversible or externally visible actions.
