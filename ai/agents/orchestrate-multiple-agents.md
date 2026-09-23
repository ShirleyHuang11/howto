---
name: orchestrate-multiple-agents
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You coordinate multiple specialized agents so they divide work, share only necessary context, and produce a result that beats a single-agent baseline.

## Preconditions

- A task class that naturally decomposes into roles, such as research, coding, review, and synthesis.
- Role prompts, tool permissions, and output schemas for each agent.
- An orchestrator process that routes messages and tracks state.
- Eval tasks with single-agent baseline scores.

## Steps

1. **Define roles and authority.** Specify each agent's goal, allowed tools, input schema, output schema, and decision rights. → *Expect:* no two agents have ambiguous ownership of the same final decision.
2. **Choose an orchestration pattern.** [BRANCH: manager-worker | planner-executor-reviewer | debate-and-judge] Pick the simplest pattern that matches the task. → *Expect:* a state diagram or workflow config describes message flow.
3. **Constrain shared context.** Pass task-relevant artifacts, summaries, and schemas rather than full transcripts by default. → *Expect:* each agent receives only the context it needs.
4. **Validate inter-agent outputs.** Parse each agent's output against schema before another agent consumes it. → *Expect:* malformed outputs are rejected or repaired.
5. **Add conflict resolution.** Use a reviewer, judge, or deterministic rule when agents disagree. → *Expect:* disagreements produce a recorded resolution, not blended guesses.
6. **Set global budgets.** Limit total tokens, wall time, tool calls, and per-agent retries. ⚠️ *Data leaves your control:* multiple hosted agents can multiply exposure and cost; redact inputs and cap budgets before running. → *Expect:* orchestration stops before budget overrun.
7. **Evaluate against baseline.** Compare task success, quality, latency, cost, and failure modes against a single-agent implementation. → *Expect:* multi-agent orchestration ships only if it improves the primary metric enough to justify complexity.

## Decision points

- Single-agent baseline is close in quality → avoid multi-agent complexity.
- Agents need the same tool with write access → centralize execution behind one approval gate.
- Disagreements are frequent → improve role definitions or add a judge with explicit rubric.
- Cost is high → reduce agents, share summaries, or run cheaper models for helper roles.

## Failure modes & recovery

- **F1 Context bloat:** detect token use growing with every message → pass artifacts and summaries instead of full transcripts.
- **F2 Responsibility gap:** detect no agent handles a required step → update role ownership and workflow tests.
- **F3 Collusion on wrong answer:** detect agents reinforcing unsupported claims → require source-grounded review and independent evidence.
- **F4 Budget cascade:** detect retries across agents exceeding budget → enforce global caps in the orchestrator.

## Verification

The orchestration eval must show all inter-agent messages validate against schemas, global budgets are enforced, and the multi-agent system improves the chosen success metric over the single-agent baseline by the configured margin without increasing critical failure rate.

## Variations

- `manager-worker`: one planner assigns tasks to specialist workers.
- `reviewer-gate`: executor output cannot ship until an independent reviewer passes it.
- `debate`: multiple agents propose answers and a judge selects using a rubric and evidence.

## Safety & privacy

Multi-agent systems duplicate prompts, data exposure, and tool risk. Give each agent least-privilege tools, avoid sharing sensitive context unnecessarily, log message flow for audit, and keep approval for side effects centralized outside agent-to-agent conversation.
