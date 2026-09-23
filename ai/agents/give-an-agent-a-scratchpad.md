---
name: give-an-agent-a-scratchpad
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

Your agent has a bounded scratchpad for task state, assumptions, and intermediate artifacts without exposing hidden reasoning or letting notes override policy. Success means the scratchpad improves continuity and remains schema-valid, size-limited, and safe to persist.

## Preconditions

- An agent loop with a place to load and save per-run state.
- A schema for scratchpad entries, such as facts, todos, tool results, decisions, and user-confirmed constraints.
- A privacy policy for what may be persisted.

## Steps

1. **Define scratchpad scope and schema.** Store task-relevant state like `facts`, `open_questions`, `completed_steps`, and `artifacts`, not private chain-of-thought. → *Expect:* scratchpad content validates against a JSON Schema.
2. **Initialize the scratchpad from trusted context.** Load user instructions, durable state, and prior approved summaries with source labels. → *Expect:* each scratchpad item has `source` and `timestamp` fields.
3. **Update it after model turns and tool calls.** Let the controller write concise summaries of verified facts and next actions. → *Expect:* new entries are derived from tool results or user-visible model output, not hidden reasoning.
4. **Bound size and age.** Enforce maximum entries or tokens, summarize old items, and expire sensitive state. → *Expect:* `count_tokens(scratchpad)` stays below the configured budget.
5. **Protect instruction hierarchy.** Treat scratchpad notes as data; never allow a note to override system, developer, policy, or user instructions. → *Expect:* injection text stored in the scratchpad does not change tool permissions.
6. **Persist only when useful and allowed.** Save run-local scratchpads by default; require explicit retention for cross-session memory. ⚠️ *Data leaves your control:* if stored in external memory or tracing systems, redact PII and secrets first. → *Expect:* persisted scratchpad records contain no secret-pattern matches.

## Decision points

- Task spans multiple steps or resumptions → use a scratchpad.
- Task is single-turn or highly sensitive → keep scratchpad in memory only or disable persistence.
- Scratchpad exceeds token budget → summarize verified state and drop obsolete entries.
- Scratchpad contains user secrets → remove or vault the secret reference instead of storing plaintext.

## Failure modes & recovery

- **F1 Hidden reasoning leak:** detect chain-of-thought style text in persisted notes → store concise conclusions and evidence references only.
- **F2 Stale assumption:** detect scratchpad fact contradicted by a newer tool result → mark old item superseded and keep source timestamps.
- **F3 Scratchpad injection:** detect note instructing the model to ignore policy → quote it as untrusted data and add a guardrail test.
- **F4 Token bloat:** detect context over budget → compact old entries and retain only active facts and todos.

## Verification

Run a fixture where the agent writes facts, updates a todo, stores a malicious note, and resumes from state. The scratchpad must validate against schema, stay under the token budget, preserve source metadata, contain no secret-pattern matches, and fail the injection attempt by keeping tool permissions unchanged.

## Variations

- `run-local scratchpad`: simplest and safest for one workflow execution.
- `durable memory`: useful for long-running agents; add retention, user controls, and audit logs.
- `graph/state-machine agents`: store scratchpad fields as typed state rather than free-form notes.

## Safety & privacy

Medium risk because scratchpads can persist sensitive details or accidental hidden reasoning. Keep entries structured and minimal, label sources, expire sensitive data, redact before external storage, and never let scratchpad content outrank trusted instructions.
