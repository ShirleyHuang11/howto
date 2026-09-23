---
name: resume-an-interrupted-agent-run
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/agents/log-agent-traces]
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent can resume after a crash, timeout, or user pause without duplicating side effects or losing task state. Success means resumed runs continue from durable checkpoints with idempotent tool behavior and a verifiable final status.

## Preconditions

- Durable storage for run state, scratchpad, trace IDs, pending tool calls, and completed side effects.
- Idempotency support for write tools or a policy to never retry unsafe writes automatically.
- Tests that can interrupt the process at controlled points.

## Steps

1. **Define checkpoint boundaries.** Save state before model calls, before tool calls, after tool results, and at terminal stop reasons. → *Expect:* each checkpoint records run ID, step number, state version, and pending action.
2. **Persist enough state to replay safely.** Store messages or compacted context, scratchpad, tool-call IDs, idempotency keys, completed action receipts, and budget usage. → *Expect:* a resumed controller can reconstruct the next legal action without hidden in-memory state.
3. **Make side-effecting tools idempotent.** Use stable idempotency keys and status queries before retrying after an unknown outcome. ⚠️ *Irreversible:* never repeat sends, purchases, deletes, or deployments unless the external system confirms the previous attempt did not succeed. → *Expect:* interruption after a write does not create duplicate external records.
4. **Implement resume logic.** On restart, load the latest valid checkpoint, verify schema version, reconcile pending side effects, and continue or pause for user confirmation. → *Expect:* corrupted or incompatible checkpoints fail closed.
5. **Record resume events in traces.** Log interruption reason, checkpoint ID, reconciliation result, and resumed step. → *Expect:* a trace shows both pre- and post-resume spans under the same run.
6. **Test interruptions at every boundary.** Kill the process before and after model calls, tool calls, and checkpoint writes. → *Expect:* every injected interruption resumes or stops safely with no duplicate side effects.

## Decision points

- Last checkpoint is before a read-only tool → rerun the tool if still relevant.
- Last checkpoint is during a write with unknown outcome → query status by idempotency key or ask a human.
- Checkpoint schema is old but migratable → migrate and validate before resume.
- Checkpoint is corrupted or missing required state → stop with `resume_failed`.

## Failure modes & recovery

- **F1 Duplicate write:** detect two external receipts for one intended action → disable auto-resume for that tool and require idempotency.
- **F2 Lost context:** detect missing scratchpad or messages → fall back to user-visible summary and ask for confirmation.
- **F3 Corrupted checkpoint:** detect schema validation failure → load previous checkpoint or stop safely.
- **F4 Budget mismatch:** detect stored budget lower than provider usage → reconcile usage before continuing.

## Verification

Run an interruption test matrix that terminates the agent at each checkpoint boundary. After resume, the final task must complete or stop with a typed reason, checkpoint schemas must validate, trace continuity must be preserved, and a fake side-effecting API must show exactly one external write for the intended action.

## Variations

- `durable workflow engine`: use built-in checkpoints and activity idempotency.
- `database-backed controller`: store state rows with optimistic concurrency and schema versions.
- `local CLI agent`: save a JSON state file and require confirmation before resuming writes.

## Safety & privacy

Medium risk because resume can duplicate irreversible work or persist sensitive context. Store only necessary state, encrypt sensitive checkpoints, use idempotency for writes, reconcile unknown outcomes, and stop for human confirmation when safety cannot be proven.
