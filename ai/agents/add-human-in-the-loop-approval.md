---
name: add-human-in-the-loop-approval
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You require explicit human approval before an agent performs irreversible, costly, sensitive, or externally visible actions.

## Preconditions

- An agent runtime with tool metadata and execution hooks.
- A list of actions that require approval.
- An approval UI, CLI prompt, ticket, or API workflow.
- Audit logging for requests, decisions, and executed actions.

## Steps

1. **Classify tool risk.** Label tools as read-only, low-risk write, high-impact write, data export, payment, deletion, deployment, or communication. → *Expect:* every tool has an approval policy.
2. **Define approval payloads.** Include actor, tool, exact arguments, predicted effect, data exposure, cost estimate, rollback option, and expiration time. → *Expect:* approvers can decide without reading raw agent traces.
3. **Block before execution.** Insert an approval gate after argument validation and before the tool call. → *Expect:* approval-required tools cannot run without an approved decision id.
4. **Ask for human approval.** Present the exact action and require approve, reject, or modify. ⚠️ *Irreversible:* for deletion, deployment, payment, access changes, messages, or external data transfer, confirm target and scope before execution. → *Expect:* the runtime records a signed or authenticated decision.
5. **Revalidate after approval.** Ensure arguments, permissions, and resource versions have not changed since the request. → *Expect:* stale approvals are rejected.
6. **Execute and log outcome.** Run the approved tool once, attach decision id, and log result or failure. → *Expect:* audit logs link approval request to tool execution.
7. **Test bypass attempts.** Try prompt injection, direct tool invocation, stale approvals, and modified arguments. → *Expect:* none bypass the approval gate.

## Decision points

- Tool sends data outside the organization → approval should include recipient and exact payload summary.
- Tool cost is variable → require cost ceiling in the approval.
- Approver modifies arguments → create a new approval record for the modified action.
- Approval expires → require a fresh decision before execution.

## Failure modes & recovery

- **F1 Approval bypass:** detect tool execution without decision id → disable the tool and fix the central execution wrapper.
- **F2 Stale approval:** detect resource changed after approval → reject and regenerate request.
- **F3 Vague approval text:** detect approver cannot see exact target → include normalized arguments and impact summary.
- **F4 Replay execution:** detect same approval used twice → make approval tokens single-use.

## Verification

Security tests must prove approval-required tools never execute without a valid single-use approval id, modified arguments invalidate approval, stale approvals fail, and audit logs contain request, approver, decision, execution result, and timestamp.

## Variations

- `cli-agent`: pause with a terminal confirmation for local developer workflows.
- `enterprise-workflow`: route approval to a ticketing or access-review system.
- `two-person-rule`: require two independent approvers for very high-impact actions.

## Safety & privacy

Approval gates are for actions that can harm users, spend money, expose data, or change production. Keep them centralized, make approvals explicit and auditable, avoid leaking unnecessary sensitive data to approvers, and never let model text count as approval.
