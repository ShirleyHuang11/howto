---
name: log-prompts-and-completions
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You log LLM prompts and completions for debugging and evaluation without leaking secrets or retaining data longer than allowed. Logs are queryable, redacted, access-controlled, and tied to traces.

## Preconditions

- A central LLM wrapper or gateway where logging can be applied consistently.
- A privacy policy and retention requirement for prompt and completion data.
- A redaction scanner for PII, credentials, and tenant-sensitive content.

## Steps

1. **Choose the logging level by data class.** Decide whether to log full content, redacted content, hashes only, or metadata only for each environment and tenant. → *Expect:* a policy table maps data class to logging behavior.
2. **Add structured trace metadata.** Log request id, user or tenant pseudonym, feature, model, route, token usage, latency, finish reason, and validation result. → *Expect:* every LLM call has a traceable metadata record.
3. **Redact before storage.** Run prompts and completions through secret and PII detectors before writing content logs. ⚠️ *Data leaves your control:* if logs go to a third-party observability platform, prompt content leaves your infrastructure; confirm approval first. → *Expect:* stored content has redaction markers and raw content is discarded unless explicitly allowed.
4. **Protect log access.** Restrict logs by role, tenant, and environment; enable audit trails for reads and exports. → *Expect:* unauthorized users cannot query sensitive logs.
5. **Set retention and deletion.** Apply TTLs, user deletion workflows, and incident purge procedures. → *Expect:* records expire automatically according to policy.
6. **Sample and link to evals.** Sample safe logs for eval set creation and store consent/provenance for any example promoted to training or eval data. → *Expect:* sampled examples have review status and source trace ids.
7. **Test with known sensitive strings.** Send canary emails, fake API keys, and names through staging. → *Expect:* logs contain redacted values, not raw canaries.

## Decision points

- Logs include regulated or customer data → default to metadata or redacted content only.
- Debugging requires raw content → grant time-limited, audited access with approval.
- Third-party logging is unapproved → keep logs in your controlled storage.
- User requests deletion → delete or anonymize content logs and derived samples.
- Redaction confidence is low → block content logging for that data class.

## Failure modes & recovery

- **F1 Secret leakage:** detect canary key in logs → purge affected logs, rotate real secrets, and fix redaction.
- **F2 Cross-tenant access:** detect tenant filter bypass → disable log access and repair authorization.
- **F3 Retention failure:** detect expired logs still queryable → fix TTL job and backfill deletion.
- **F4 Unusable debugging logs:** detect missing request ids or model tags → enforce required metadata schema.
- **F5 Training contamination:** detect unreviewed logs in training data → remove examples and rebuild dataset.

## Verification

Logging is acceptable when automated tests send sensitive canaries and confirm stored logs redact them, schema tests show required metadata on every call, access-control tests deny unauthorized reads, and retention tests remove records after the configured TTL.

## Variations

- `metadata-only`: safest for regulated workloads and still supports cost and latency debugging.
- `redacted content`: useful for eval mining when redaction quality is validated.
- `self-hosted observability`: keeps data in your control but still needs access controls.
- `third-party tracing`: confirm data-processing terms and disable raw content where needed.

## Safety & privacy

High risk because prompts and completions often contain personal, proprietary, or secret data. Minimize content logging, redact before storage, restrict access, audit reads, honor deletion requests, and never use logs for training without explicit provenance and approval.
