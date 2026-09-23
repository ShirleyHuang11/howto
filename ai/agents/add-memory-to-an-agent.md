---
name: add-memory-to-an-agent
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

You add memory to an agent so it can use relevant past information while respecting user consent, privacy, and retrieval quality.

## Preconditions

- A clear memory purpose, such as preferences, project facts, or task state.
- Storage for short-term session state and optional long-term memory.
- A retrieval or lookup mechanism for long-term memory.
- Tests for memory write, retrieval, update, and deletion.

## Steps

1. **Classify memory types.** Separate conversation state, user preferences, durable facts, and tool-derived records. → *Expect:* each memory type has retention and access rules.
2. **Define write criteria.** Store only information that is useful later, non-sensitive or approved, and attributable to a source. → *Expect:* the agent does not save arbitrary chat text.
3. **Ask for consent where needed.** For durable personal memory, request user permission and provide deletion behavior. → *Expect:* no long-term personal memory is written without consent.
4. **Store structured records.** Use fields like `{subject, fact, source, confidence, created_at, expires_at}` and optional embeddings. → *Expect:* memory records validate against schema.
5. **Retrieve memory by task.** Fetch only relevant records using filters and semantic search, then cap memory tokens. → *Expect:* prompt memory context fits budget and includes record ids.
6. **Validate before using memory.** Treat memory as stale, partial data; ask the user or re-check tools for high-impact decisions. → *Expect:* stale or low-confidence records do not drive irreversible actions.
7. **Implement update and delete.** Support overwriting corrected facts and deleting records by user, project, or retention rule. ⚠️ *Irreversible:* deleting memory can remove audit context; confirm the target records and keep required compliance logs. → *Expect:* deleted records no longer retrieve.
8. **Evaluate memory usefulness.** Test that relevant memories are retrieved and irrelevant or sensitive ones are not. → *Expect:* memory precision and recall meet thresholds.

## Decision points

- Memory contains sensitive personal data → avoid storing, encrypt it, or require explicit consent and retention limits.
- Memory conflicts with current user input → prefer current input and mark old memory stale.
- Retrieval returns too much context → add type filters and recency or project scopes.
- User asks to forget → delete retrievable memory and confirm what was removed.

## Failure modes & recovery

- **F1 Memory leak across users:** detect another user's record retrieved → enforce tenant and user filters in storage queries.
- **F2 Stale preference:** detect user correction contradicting memory → update or expire the old record.
- **F3 Overcollection:** detect raw conversations saved as memory → replace with explicit structured facts and shorten retention.
- **F4 Prompt injection in memory:** detect stored text instructing the agent → treat memory as data, not policy.

## Verification

Automated tests must prove memory writes validate against schema, user/project filters prevent cross-user retrieval, relevant-memory recall and precision meet thresholds on a labeled set, and deleted records are absent from subsequent retrieval results.

## Variations

- `session-memory`: keep task state in the conversation or server session only.
- `semantic-memory`: embed durable facts for similarity retrieval.
- `tool-backed-memory`: store facts in the source system of record instead of a separate memory DB.

## Safety & privacy

Memory can quietly accumulate sensitive data. Store the minimum useful facts, get consent for durable personal memory, encrypt sensitive records, enforce tenant isolation, provide deletion, and never let memory override system policy or current user intent.
