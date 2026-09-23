---
name: cache-llm-responses
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/llmops/call-an-llm-api]
status: draft
last_verified: 2026-09-22
---

## Goal

You cache deterministic LLM responses so repeated identical requests avoid extra latency and cost. Cache hits are correct for the same model, prompt, parameters, and safety context.

## Preconditions

- An LLM call wrapper you control.
- A cache store such as Redis, SQLite, Postgres, or local disk for development.
- A policy for what prompts and responses may be cached.

## Steps

1. **Define the cache eligibility rules.** Cache only low-risk, repeatable requests; exclude personalized, regulated, time-sensitive, or tool-affecting calls unless reviewed. → *Expect:* a documented allowlist or denylist.
2. **Construct a complete cache key.** Hash model id, system prompt, user prompt, retrieved context ids or hashes, tool schemas, temperature, max tokens, output schema version, and safety policy version. → *Expect:* changing any behavior-affecting input changes the key.
3. **Normalize request fields.** Canonicalize JSON ordering and whitespace where safe, but do not remove meaningful content. → *Expect:* semantically identical structured requests produce the same key.
4. **Store response and metadata.** Save assistant output, finish reason, token usage, provider request id, creation time, TTL, and validator version. ⚠️ *Data leaves your control:* if using external cache infrastructure, cached prompts and outputs may be exposed outside the app boundary; redact or encrypt sensitive values. → *Expect:* cache entries can be audited and expired.
5. **Validate before serving a hit.** Re-run lightweight schema or policy checks before returning cached output. → *Expect:* stale invalid entries are rejected and refreshed.
6. **Measure hit rate and savings.** Log cache hits, misses, latency, token savings, and invalidations. → *Expect:* a dashboard or report shows hit rate and estimated cost saved.

## Decision points

- Temperature is high or task is creative → cache only if exact repeatability is acceptable.
- Prompt includes user-specific data → avoid shared cache or partition by user and tenant.
- Retrieved context changed → include document version hashes or invalidate affected keys.
- Output schema changes → bump schema version and bypass old entries.
- Cache hit rate is low → target repeated prompts or use semantic caching instead.

## Failure modes & recovery

- **F1 Stale answer served:** detect source document version differs → include context hashes and expire affected keys.
- **F2 Cross-user data leak:** detect cache key lacks tenant/user partition → purge cache and add partition fields.
- **F3 Non-deterministic mismatch:** detect different valid answers under same key → lower temperature or disable caching for that task.
- **F4 Invalid cached JSON:** detect validator failure on hit → delete entry and refresh from model.
- **F5 Oversized cache:** detect storage growth beyond budget → add TTL, compression, and eviction policy.

## Verification

Caching is correct when automated tests prove identical eligible requests produce one provider call followed by cache hits, behavior-changing fields produce different keys, schema-invalid cached entries are rejected, and tenant-partition tests cannot read another tenant's cached response.

## Variations

- `Redis`: use TTLs, key namespaces, and optional encryption at the application layer.
- `SQLite`: useful for local development and reproducible eval caching.
- `provider prompt cache`: use provider-side prompt caching for long repeated prefixes when supported.
- `batch jobs`: cache by stable task id and input hash to make retries idempotent.

## Safety & privacy

Medium risk because cached prompts and outputs can contain sensitive data and stale advice. Partition by tenant, encrypt or avoid sensitive cache entries, set TTLs, include policy and context versions in keys, and provide a purge path for user deletion requests.
