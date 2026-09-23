---
name: set-an-agent-stop-condition
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

Your agent stops predictably when it succeeds, reaches a budget, loops, needs approval, or becomes unsafe. Success means every run exits with a typed stop reason that tests and operators can inspect.

## Preconditions

- An agent loop where each model turn, tool call, and observation passes through a controller.
- Access to token, cost, wall-clock, and step counters.
- A way to mark task success, such as a final schema, assertion, or external state check.

## Steps

1. **Define allowed stop reasons.** Use an enum such as `completed`, `needs_user_input`, `approval_required`, `max_steps`, `budget_exceeded`, `loop_detected`, `policy_blocked`, and `tool_failure`. → *Expect:* every terminal run stores exactly one stop reason.
2. **Set hard resource limits.** Configure `max_steps`, `max_tool_calls`, `max_tokens`, `max_cost_usd`, and `max_wall_time_seconds` per task class. → *Expect:* a run that crosses a limit stops before the next model or tool call.
3. **Add a task-specific success predicate.** Validate final JSON, check an external record, or run an assertion like `answer.citations.length >= 2`. → *Expect:* success is based on a programmatic predicate, not the model saying it is done.
4. **Detect loops and repeated failures.** Hash normalized recent actions and stop when the same state/action pattern repeats, such as three identical tool calls. → *Expect:* loop fixtures terminate with `loop_detected`.
5. **Stop before approval-gated actions.** For deletes, payments, deployments, emails, or data exposure, emit `approval_required` with a confirmation summary. ⚠️ *Irreversible:* do not execute the action until the user confirms the exact operation and target. → *Expect:* the action is pending and no external side effect has occurred.
6. **Return a structured run summary.** Include stop reason, steps used, cost, final status, and any pending approval payload. → *Expect:* downstream code can branch on the stop reason without parsing prose.

## Decision points

- Success predicate passes → stop with `completed`.
- Agent asks for missing credentials or ambiguous user input → stop with `needs_user_input`.
- Action is irreversible, costly, or data-exposing → stop with `approval_required`.
- Resource budget is near exhaustion → summarize progress and stop rather than starting another long tool call.

## Failure modes & recovery

- **F1 Infinite tool loop:** detect repeated action hashes → stop and add the repeating trace to diagnostics.
- **F2 Premature success:** detect final answer without passing the success predicate → reject finalization and continue or fail.
- **F3 Budget overspend:** detect model/tool calls after budget exceeded → move budget checks before calls and reserve estimated cost.
- **F4 Ambiguous stop reason:** detect missing or free-text status → enforce the stop-reason enum in the run schema.

## Verification

Run fixtures for success, missing input, repeated tool call, budget limit, and approval-gated delete. Each fixture must terminate within its configured limits, produce a run summary that validates against the stop schema, and show zero external side effects for the approval-gated case.

## Variations

- `LangGraph`: represent stop conditions as terminal nodes and conditional edges.
- `Temporal or durable workflows`: persist stop reason in workflow state before pausing or completing.
- `CLI agents`: return nonzero exit codes for failure stop reasons and JSON summaries for automation.

## Safety & privacy

Medium risk because missing stop conditions can cause runaway spend or unauthorized actions. Put checks in the controller, not only in prompts; require approval for irreversible or data-exposing actions; and store concise summaries rather than full private prompts when possible.
