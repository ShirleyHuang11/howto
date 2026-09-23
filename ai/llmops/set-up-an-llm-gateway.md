---
name: set-up-an-llm-gateway
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: high
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You put LLM traffic behind a gateway that centralizes authentication, routing, logging, rate limits, budgets, and safety policy. Applications call the gateway instead of talking directly to every provider.

## Preconditions

- One or more approved LLM providers or local model endpoints.
- Service identity, tenant identity, and network controls for applications using the gateway.
- Policies for logging, data residency, routing, budget, and retention.

## Steps

1. **Define the gateway API contract.** Support chat/messages, embeddings if needed, streaming, model aliases, metadata tags, and error schemas. → *Expect:* client teams can call a stable internal endpoint.
2. **Configure provider credentials securely.** Store provider keys in a secrets manager and map model aliases to provider endpoints. → *Expect:* no application service stores raw provider keys.
3. **Add authentication and authorization.** Require service tokens or mTLS and authorize models by app, tenant, data class, and environment. → *Expect:* unauthorized model access returns a controlled 403.
4. **Implement policy middleware.** Enforce token limits, rate limits, budgets, logging level, redaction, and provider allowlists before forwarding. ⚠️ *Data leaves your control:* forwarding to hosted providers sends prompt content outside your infrastructure; enforce data-class policies first. → *Expect:* disallowed requests fail before provider calls.
5. **Add routing and fallback.** [BRANCH: static aliases | rules router | failover] Route by model alias, task, sensitivity, or availability with logged route reasons. → *Expect:* each request records selected provider and fallback path.
6. **Support streaming and cancellation.** Proxy streaming events and propagate client disconnects to upstream providers. → *Expect:* long responses can be canceled and traced.
7. **Instrument observability.** Emit request ids, latency, token usage, cost, errors, policy decisions, and provider request ids. → *Expect:* dashboards and alerts cover gateway traffic.
8. **Run conformance tests.** Test auth, policy denial, normal calls, streaming, fallbacks, cost tags, and error mapping. → *Expect:* every client-visible behavior has an automated test.

## Decision points

- Apps need provider-specific features → expose safe extensions without breaking the common contract.
- Data class forbids a provider → block route even if the model alias points there.
- Gateway becomes a bottleneck → horizontally scale stateless workers and isolate streaming capacity.
- Provider outage occurs → fail over only to approved equivalent providers or return structured failure.
- Teams bypass gateway → rotate provider keys and enforce network egress controls.

## Failure modes & recovery

- **F1 Provider key leak:** detect key in app config or logs → rotate key and move access behind gateway.
- **F2 Policy skipped on streaming path:** detect streaming route lacks redaction or limits → use shared middleware for all paths.
- **F3 Incorrect error mapping:** detect clients retry bad requests → preserve retryable flag and provider category.
- **F4 Gateway outage:** detect all LLM traffic fails → deploy multiple instances and health-check dependencies.
- **F5 Tenant budget bypass:** detect missing tenant tag → reject requests without required metadata.

## Verification

The gateway is ready when integration tests prove direct provider keys are not needed by clients, unauthorized routes are denied, allowed requests succeed, streaming cancellation propagates, budget and rate limits trigger, and observability records include request id, route, usage, and policy decision.

## Variations

- `LiteLLM or similar proxy`: faster setup for common providers with routing and budgets.
- `custom gateway`: best when policy, tenant isolation, or data residency requirements are specific.
- `service mesh`: enforce egress and mTLS outside the gateway application.
- `local-only`: route to self-hosted models for sensitive data classes.

## Safety & privacy

High risk because the gateway sees all prompts and controls where data goes. Store secrets in a manager, enforce provider allowlists by data class, redact logs, cap spend, audit policy changes, and require review before adding external providers or raw-content logging.
