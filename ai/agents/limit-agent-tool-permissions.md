---
name: limit-agent-tool-permissions
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

Your agent receives only the tools and permissions required for the current task. Success means unauthorized tools cannot be called, sensitive scopes are excluded by default, and permission decisions are visible in traces.

## Preconditions

- A tool registry with metadata for required scopes, resource patterns, risk level, and whether the tool is read-only or state-changing.
- User, tenant, or role identity available to the agent controller.
- Tests for allowed and denied tool calls.

## Steps

1. **Inventory tools and scopes.** For each tool, document action type, required credentials, allowed resources, risk level, and approval requirement. → *Expect:* the registry has no tool with missing permission metadata.
2. **Build a per-task tool allowlist.** Select tools based on task intent, user role, and current resource scope. → *Expect:* the model is only shown tools in the computed allowlist.
3. **Enforce permissions at runtime.** Validate every tool call against user authorization, task scope, and tool risk before handler execution. → *Expect:* a forbidden tool call is blocked even if the model requests it.
4. **Use scoped credentials.** Issue short-lived tokens or service credentials limited to the selected resources and operations. ⚠️ *Data leaves your control:* tools that call third-party services may expose user data; grant those scopes only when needed. → *Expect:* credentials fail when used outside their declared scope.
5. **Add approval gates for elevated permissions.** Require explicit approval before adding write, delete, admin, export, or public-send tools. → *Expect:* privilege escalation pauses with a confirmation summary.
6. **Log permission decisions.** Record allowed tools, denied calls, scope checks, and approval events. → *Expect:* traces show why each tool call was allowed or denied.

## Decision points

- Task can be completed with read-only tools → do not grant write tools.
- User lacks role or resource access → deny tool call and explain required permission.
- Agent asks for a broader tool than needed → provide a narrower wrapper instead.
- Elevated permission is genuinely needed → request explicit approval and use short-lived credentials.

## Failure modes & recovery

- **F1 Prompt-only permissioning:** detect handler executes a hidden or denied tool → move enforcement into the tool gateway.
- **F2 Overbroad credentials:** detect token can access unrelated resources → narrow IAM scopes and add credential tests.
- **F3 Tool list leakage:** detect model sees admin tools for normal tasks → compute tool list per request.
- **F4 Permission drift:** detect registry and backend scopes disagree → run periodic permission audits and contract tests.

## Verification

Run permission tests for normal, elevated, unauthorized, and prompt-injection scenarios. The model-visible tool list must match the computed allowlist, denied tools must fail before handler execution, scoped credentials must reject out-of-scope resources, elevated actions must require approval, and traces must include allow/deny decisions.

## Variations

- `role-based access`: map users or tenants to allowed tool scopes.
- `capability tokens`: issue short-lived tokens per run and resource.
- `MCP tools`: expose only selected server tools and enforce authorization inside the MCP server as well.

## Safety & privacy

Medium risk because excessive tool permissions let agents leak data or mutate systems. Enforce least privilege in code, not prompts; hide unavailable tools from the model; scope credentials tightly; and require explicit approval for elevated, third-party, or state-changing actions.
