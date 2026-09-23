---
name: add-a-planning-step
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

You add an explicit planning phase so an agent decomposes work, identifies tool needs and risks, and can be evaluated before it acts.

## Preconditions

- An agent or workflow that performs multi-step tasks.
- Tool schemas and risk labels.
- Example tasks with expected substeps or success criteria.
- A place to store plan state and updates.

## Steps

1. **Define the plan schema.** Use fields like `goal`, `steps`, `needed_tools`, `risks`, `approval_required`, and `done_criteria`. → *Expect:* plans validate as JSON before execution.
2. **Generate a plan before tools.** Ask the model for a concise plan and risk assessment before any side-effecting action. [BRANCH: planner model | same model | deterministic workflow] → *Expect:* every non-trivial task has a plan trace.
3. **Validate the plan.** Check that tools exist, risky steps are marked, and done criteria are measurable. → *Expect:* invalid plans are revised before acting.
4. **Gate risky steps.** If the plan includes deletion, deployment, payment, messaging, or data export, require approval before those steps. ⚠️ *Irreversible:* confirm target, scope, rollback, and user approval before executing high-impact steps. → *Expect:* the runtime blocks risky actions until approval is recorded.
5. **Execute step by step.** After each action, update plan status from tool results rather than model assumptions. → *Expect:* plan state reflects completed, pending, blocked, or failed steps.
6. **Revise when observations differ.** Allow bounded replanning when a tool fails or the environment changes. → *Expect:* revised plans retain original goal and explain changed steps.
7. **Evaluate plan quality.** Score plan validity, tool choice, risk marking, and task completion on golden tasks. ⚠️ *Data leaves your control:* hosted planning calls receive user goals and context; redact sensitive details. → *Expect:* plan-quality metrics meet threshold before enabling autonomous execution.

## Decision points

- Task is simple and read-only → skip detailed planning but still track done criteria.
- Plan includes unknown tools → reject and ask for a revised plan using available tools.
- Plan omits approval for risky action → block execution and repair the plan.
- Replanning repeats without progress → stop and ask for human help.

## Failure modes & recovery

- **F1 Decorative plan:** detect plan not used during execution → bind loop state to plan step ids.
- **F2 Missing risk:** detect side-effecting tool in a low-risk step → derive risk from tool metadata, not model text alone.
- **F3 Overplanning:** detect latency overhead on trivial tasks → route simple tasks around the planner.
- **F4 Goal drift:** detect revised plan changes user objective → require user confirmation for changed goal.

## Verification

Automated evals must confirm plans parse against schema, every selected tool exists, all side-effecting tools are marked approval-required, and golden multi-step tasks complete with plan steps updated from actual observations.

## Variations

- `plan-and-execute`: generate the full plan once, then execute with limited replanning.
- `rolling-plan`: keep only the next few steps for uncertain environments.
- `human-approved-plan`: require a human to approve the plan before any tools run.

## Safety & privacy

Planning improves transparency but is not authorization. Enforce tool permissions in code, redact sensitive task context sent to hosted models, store plan traces carefully, and require approval for irreversible, costly, or externally visible steps.
