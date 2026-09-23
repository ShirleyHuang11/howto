---
name: prompt-for-step-by-step-reasoning
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

You prompt the model to solve a task in explicit, checkable steps when the user needs an auditable procedure, while keeping final outputs concise and valid.

## Preconditions

- A task where intermediate steps are useful to users or validators.
- A desired step format, such as numbered actions, plan-execute-check, or evidence table.
- Test cases with expected final answers or valid plans.

## Steps

1. **Decide which steps should be visible.** Request only user-useful steps, not unrestricted private reasoning. → *Expect:* the prompt names the allowed step type, such as assumptions, calculation rows, or cited evidence.
2. **Define the step schema.** Require fields like `step`, `action`, `evidence`, and `check`. → *Expect:* each response can be parsed into discrete steps.
3. **Require a final answer separately.** Add a final field or heading after the steps. → *Expect:* downstream code can extract the final answer without reading all steps.
4. **Add self-check criteria.** Tell the model to verify arithmetic, citations, or constraints before finalizing. → *Expect:* responses include a visible check or pass/fail status.
5. **Evaluate both process and result.** Score final correctness and validate that steps follow the schema. → *Expect:* a report with final-answer accuracy and step-validity rate.
6. **Trim unnecessary verbosity.** Cap the number of steps or words per step. → *Expect:* outputs stay within a user-readable token limit.

## Decision points

- User only needs an answer → use hidden reasoning and return concise justification instead.
- Steps expose sensitive inference or policy → omit private reasoning and show evidence-backed summary only.
- Step validity is high but answers are wrong → add tools, calculators, or retrieval checks.

## Failure modes & recovery

- **F1 Endless step list:** detect outputs over token budget → cap steps and require final answer.
- **F2 Invalid process:** detect missing checks or evidence → validate step schema and retry once.
- **F3 Correct steps, wrong final:** detect mismatch between work and answer → add a consistency check from steps to final.
- **F4 Revealed sensitive reasoning:** detect disallowed hidden rationale → constrain visible steps to evidence and actions.

## Verification

Run `python eval_step_prompt.py --prompt step_prompt.md --cases step_eval.jsonl --max-output-tokens 800`; at least 95% of outputs must parse into the step schema, final-answer accuracy must beat the direct baseline, and no output may exceed the token budget.

## Variations

- `math`: include calculation rows and numeric final answer.
- `planning`: use plan, risk, next action, and verification fields.
- `RAG`: use evidence id, claim, and support status per step.

## Safety & privacy

Visible step-by-step output can expose sensitive assumptions or internal policies. Show only steps that help the user verify the answer, and avoid storing long reasoning traces for private user data.
