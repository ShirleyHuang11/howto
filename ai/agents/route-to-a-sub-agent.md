---
name: route-to-a-sub-agent
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

Your orchestrator routes work to specialized sub-agents with clear contracts, scoped tools, and measurable handoffs. Success means each sub-agent receives only the task and permissions it needs and returns a validated result to the main agent.

## Preconditions

- At least two distinct task types that benefit from specialization, such as research, coding, review, or data extraction.
- A router policy, sub-agent prompts, tool permissions, and output schemas.
- Evaluation cases with expected route labels and final outcomes.

## Steps

1. **Define sub-agent responsibilities.** Write a concise contract for each sub-agent: input schema, allowed tools, expected output schema, and stop conditions. → *Expect:* every sub-agent has a machine-readable contract.
2. **Create the routing decision.** Use deterministic rules, a classifier, or a small model call to choose a sub-agent based on task type and risk. → *Expect:* route fixtures produce expected labels with confidence scores.
3. **Scope context and tools per sub-agent.** Pass only relevant user instructions, artifacts, and tool permissions. → *Expect:* a sub-agent cannot call tools outside its allowlist.
4. **Validate the sub-agent response.** Require structured output, citations or artifact references where applicable, and a confidence or completion status. → *Expect:* invalid sub-agent outputs are rejected or repaired before the main agent uses them.
5. **Merge results in the orchestrator.** Combine sub-agent outputs, resolve conflicts, and decide whether another sub-agent or user input is needed. → *Expect:* the main agent trace shows the route, sub-agent result, and merge decision.
6. **Evaluate routing end to end.** Test both route accuracy and final task success. → *Expect:* route accuracy and final success meet configured thresholds.

## Decision points

- Task clearly matches one specialty → route directly.
- Task spans multiple specialties → route sequentially or in parallel, then merge with conflict checks.
- Route confidence is low → ask the main model to clarify or keep the task in the orchestrator.
- Sub-agent requests broader permissions → require policy review before expanding its tool set.

## Failure modes & recovery

- **F1 Wrong route:** detect route-label mismatch or poor final score → add examples or deterministic routing rules.
- **F2 Context loss:** detect sub-agent missing key constraints → include a structured handoff summary with required fields.
- **F3 Permission creep:** detect sub-agent calling broad tools → enforce runtime allowlists, not just prompt instructions.
- **F4 Conflicting sub-agent outputs:** detect incompatible results → route to a critic or ask the user for a decision.

## Verification

Run a routing eval with labeled tasks. The router must meet the configured route-accuracy threshold, each sub-agent call must use only its allowed tools, every sub-agent response must validate against its schema, and final task success must meet the end-to-end threshold on the held-out set.

## Variations

- `deterministic router`: best when task categories are stable and auditable.
- `model router`: useful for fuzzy tasks; require confidence thresholds and evals.
- `parallel sub-agents`: useful for independent research or critique; add merge and conflict-resolution logic.

## Safety & privacy

Medium risk because routing can over-share context or permissions. Minimize handoff data, enforce tool allowlists at runtime, redact private information not needed by the sub-agent, and log route decisions for audit and eval.
