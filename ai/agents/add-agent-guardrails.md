---
name: add-agent-guardrails
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

Your agent enforces guardrails around inputs, tool calls, outputs, and irreversible actions. Success means unsafe requests, prompt-injection attempts, and policy-violating actions are blocked or escalated with measurable test coverage.

## Preconditions

- A written policy for allowed tasks, disallowed content, sensitive data, and approval-gated actions.
- Hooks before model calls, before tool calls, after tool results, and before final responses.
- A red-team test set covering jailbreaks, prompt injection, PII, and forbidden actions.

## Steps

1. **Translate policy into machine checks.** Encode allowlists, deny rules, regexes, classifiers, or moderation calls for inputs and outputs. → *Expect:* policy fixtures produce deterministic allow/block labels.
2. **Validate every tool call before execution.** Check schema, user authorization, resource scope, and action risk. ⚠️ *Irreversible:* block deletes, payments, sends, and deployments until explicit confirmation. → *Expect:* forbidden tool calls are rejected before the tool handler runs.
3. **Treat retrieved and tool content as untrusted.** Strip or quote instructions from documents, webpages, and API responses before adding them to the model context. → *Expect:* prompt-injection fixtures do not change system policy or tool permissions.
4. **Add output checks.** Validate final answers for required schema, citation grounding, sensitive-data leakage, and disallowed content. → *Expect:* unsafe or invalid output is blocked, repaired, or escalated.
5. **Log guardrail decisions.** Store rule ID, input hash, decision, confidence, and trace ID with redacted content. → *Expect:* every block or escalation is auditable.
6. **Run guardrail evals in CI.** Include adversarial cases and expected decisions. → *Expect:* CI fails if guardrail precision or recall falls below configured thresholds.

## Decision points

- User request is clearly disallowed → refuse or redirect without tool use.
- Request is allowed but high impact → require explicit confirmation and scope-limited execution.
- Classifier confidence is low → escalate to a human or ask clarifying questions.
- Guardrail blocks too many valid cases → inspect false positives and narrow the rule.

## Failure modes & recovery

- **F1 Prompt-injection bypass:** detect agent following retrieved instructions → reinforce instruction hierarchy and quote untrusted content.
- **F2 Overblocking:** detect high false-positive rate on benign evals → tune thresholds and add allow rules for safe patterns.
- **F3 Tool-call bypass:** detect direct handler calls without policy checks → centralize authorization in the controller, not individual prompts.
- **F4 Sensitive output leak:** detect PII or secrets in final answers → redact before response and add a regression case.

## Verification

Run the guardrail eval suite. It must block all critical forbidden-action and prompt-injection cases, keep false positives below the configured threshold on benign cases, validate all final structured outputs, and show zero execution of tools for blocked requests in the trace log.

## Variations

- `classifier guardrails`: use a small model or provider moderation endpoint for semantic policy checks.
- `rules-first guardrails`: use deterministic checks for credentials, resource scopes, and irreversible actions.
- `RAG agents`: add citation grounding and retrieved-content injection tests.

## Safety & privacy

Medium risk because guardrails process sensitive prompts and may call third-party moderation services. Minimize data sent to classifiers, log redacted decisions, require confirmation for high-impact actions, and evaluate both false negatives and false positives before production use.
