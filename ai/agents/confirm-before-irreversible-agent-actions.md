---
name: confirm-before-irreversible-agent-actions
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent pauses for explicit confirmation before irreversible, costly, public, or data-exposing actions. Success means protected actions cannot execute unless the user approves the exact operation, target, and consequences.

## Preconditions

- A registry of tool actions and their risk levels.
- An agent controller that can pause, return a confirmation summary, and resume after approval.
- Audit logging for requested, approved, denied, and executed actions.

## Steps

1. **Classify approval-gated actions.** Mark deletes, payments, purchases, emails, public posts, deployments, permission changes, large paid jobs, and third-party data transfers as gated. → *Expect:* each high-impact tool action has `requires_confirmation=true`.
2. **Generate an exact confirmation summary.** Include action, target, account, data sent, cost estimate, reversibility, and deadline. → *Expect:* the summary is specific enough for a user or reviewer to approve without reading hidden state.
3. **Pause before execution.** Return `approval_required` with an operation ID and do not call the tool yet. ⚠️ *Irreversible:* the external action must not run until the matching operation ID is approved. → *Expect:* traces show zero protected tool executions before approval.
4. **Validate the approval.** Require explicit approval of the exact operation ID and reject vague confirmations or changed parameters. → *Expect:* modified action arguments invalidate the prior approval.
5. **Execute once with idempotency.** Use the approved operation ID as an idempotency key when supported and record the external receipt. → *Expect:* repeated approval submissions do not duplicate the action.
6. **Audit the full lifecycle.** Log request, summary, approver, timestamp, execution result, and receipt. → *Expect:* an audit query reconstructs who approved what and when.

## Decision points

- Action is reversible and low impact → log and execute if policy allows.
- Action is irreversible, costly, public, or sends private data to a third party → require confirmation.
- User approval is vague, conditional, or refers to a different target → ask again with the exact summary.
- Arguments change after approval → generate a new operation ID and require fresh approval.

## Failure modes & recovery

- **F1 Approval bypass:** detect protected tool execution without operation ID → block in the tool gateway and investigate trace.
- **F2 Ambiguous confirmation:** detect approval text without matching ID or exact target → keep action paused.
- **F3 Duplicate execution:** detect repeated approvals causing multiple receipts → use idempotency and executed-operation locks.
- **F4 Incomplete summary:** detect missing cost, target, or data exposure → fail summary validation before asking the user.

## Verification

Run approval-gate tests where a delete, email send, paid job, and third-party export are requested. Each must stop with `approval_required`, include a schema-valid confirmation summary, execute zero protected tools before approval, reject changed arguments after approval, and execute at most once when the exact operation ID is approved.

## Variations

- `chat UI`: present a concise approval card with action, target, and confirm/deny controls.
- `API workflow`: require a signed approval token or operation ID in a resume call.
- `enterprise`: route approvals to role-based reviewers for high-cost or regulated actions.

## Safety & privacy

High risk because these actions may be irreversible, public, expensive, or expose private data. Make approval checks enforceable in code, not just prompts; include cost and data exposure in summaries; require fresh approval for changed arguments; and keep immutable audit logs.
