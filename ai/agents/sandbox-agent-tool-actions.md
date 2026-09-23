---
name: sandbox-agent-tool-actions
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

Your agent runs tool actions inside a controlled sandbox that prevents unintended filesystem, network, credential, or production-state access. Success means tests prove disallowed actions fail closed while allowed actions still complete.

## Preconditions

- A list of tools the agent can call and the resources each tool should access.
- A sandbox mechanism such as containers, microVMs, restricted subprocesses, browser contexts, mocked APIs, or scoped cloud credentials.
- Test cases for allowed and forbidden tool behavior.

## Steps

1. **Classify tool action risk.** Label tools as read-only, local write, external write, destructive, networked, or credentialed. → *Expect:* every tool has a risk label and an allowed-resource list.
2. **Run tools with least privilege.** Use isolated containers, read-only mounts, temp workdirs, egress allowlists, and scoped service accounts. → *Expect:* a tool process cannot read outside allowed paths or reach blocked hosts.
3. **Mock or stage external services.** [BRANCH: local mock | staging API | recorded fixture] Point side-effecting tools at non-production endpoints by default. ⚠️ *Irreversible:* production writes require explicit approval, backups, and a rollback plan. → *Expect:* test actions affect only sandbox or staging resources.
4. **Enforce time, memory, and output limits.** Kill tools that exceed configured limits and truncate large outputs before returning them to the model. → *Expect:* runaway fixtures terminate with a bounded error envelope.
5. **Validate tool outputs before trust.** Treat tool output as untrusted data; parse against schemas and strip instructions embedded in results. → *Expect:* prompt-injection strings in tool output are not executed as developer instructions.
6. **Audit all denied and allowed actions.** Log sandbox policy, resource target, decision, and trace ID. → *Expect:* an audit query can show why a forbidden action was blocked.

## Decision points

- Tool needs production credentials → require human approval and a scoped, short-lived token.
- Tool only reads local fixtures → run in a read-only sandbox with no network.
- Tool output includes executable instructions or prompt-injection text → pass it as quoted data, not policy.
- Sandbox blocks legitimate work → add the narrowest missing permission and a regression test.

## Failure modes & recovery

- **F1 Credential escape:** detect access to environment variables or metadata services → remove inherited env, block metadata IPs, and rotate exposed credentials.
- **F2 Filesystem escape:** detect reads outside allowed roots → use read-only bind mounts and path canonicalization.
- **F3 Network exfiltration:** detect blocked-host attempts → enforce egress allowlists and inspect DNS logs.
- **F4 Tool output injection:** detect model following instructions from retrieved/tool text → add output quoting and instruction hierarchy tests.

## Verification

Run a sandbox test suite where an allowed read succeeds, an out-of-scope file read fails, a blocked network call fails, a long-running command is killed, and a prompt-injection payload in tool output is treated as data. The audit log must contain each allow/deny decision with trace IDs and no production resource writes.

## Variations

- `containers`: practical default for CLI tools and code execution with mounts and egress controls.
- `browser automation`: use isolated profiles, blocked downloads, and test accounts.
- `cloud tools`: use separate projects/accounts, IAM least privilege, and short-lived credentials.

## Safety & privacy

High risk because unsandboxed tools can delete data, leak secrets, or mutate production systems. Default to deny, scope credentials narrowly, block unmanaged network egress, require approval for production writes, and treat all tool outputs as untrusted inputs.
