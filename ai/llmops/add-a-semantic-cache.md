---
name: add-a-semantic-cache
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: medium
prerequisites: [ai/llmops/cache-llm-responses]
status: draft
last_verified: 2026-09-22
---

## Goal

You add a semantic cache that reuses answers for meaningfully similar requests while avoiding unsafe cross-user or stale responses. Cache hits are validated with similarity and policy checks.

## Preconditions

- A working exact-response cache or LLM call wrapper.
- An embedding model and vector store approved for the data.
- A labeled set of similar and non-similar request pairs for threshold tuning.

## Steps

1. **Define eligible tasks.** Allow semantic caching only for stable, non-personalized, low-risk tasks such as public FAQ answers or repeated summaries. → *Expect:* a task allowlist exists.
2. **Create embedding records.** Embed normalized prompts plus relevant context identifiers, tenant partition, output schema version, and answer metadata. ⚠️ *Data leaves your control:* hosted embedding APIs receive prompt text; redact or use local embeddings for sensitive data. → *Expect:* each cacheable response has a vector and metadata.
3. **Tune similarity thresholds offline.** Run labeled pairs through the embedding search and choose a threshold that meets precision requirements. → *Expect:* a threshold report with false-positive and false-negative rates.
4. **Check metadata constraints before serving.** Require same tenant or public partition, same task, compatible schema, current source version, and safe age. → *Expect:* semantically close but policy-incompatible entries are rejected.
5. **Validate candidate answers.** Optionally use a cheap verifier or deterministic checks to confirm the cached answer satisfies the new request. → *Expect:* false positives are caught before user response.
6. **Fallback to live generation on miss or uncertainty.** Generate a fresh answer, validate it, then insert it if eligible. → *Expect:* misses still return correct model output and may populate the cache.
7. **Monitor cache quality.** Track hit rate, estimated savings, user corrections, verifier rejects, and sampled false positives. → *Expect:* a dashboard shows quality and savings together.

## Decision points

- False positives cause wrong answers → raise threshold or disable semantic cache for that task.
- Requests include tenant or user-specific facts → partition strictly or avoid semantic caching.
- Source documents change → invalidate entries tied to old source versions.
- Embedding provider is not approved for content → use local embeddings or skip semantic cache.
- Hit rate is low but safe → keep exact cache only.

## Failure modes & recovery

- **F1 Wrong cached answer:** detect user correction or verifier failure → delete entry, raise threshold, and add pair to eval set.
- **F2 Cross-tenant leak:** detect hit from another tenant partition → purge index and enforce metadata filter before vector search results are used.
- **F3 Stale source answer:** detect source version mismatch → include source hashes and invalidate on update.
- **F4 Embedding drift:** detect threshold precision drops after model change → rebuild embeddings and retune threshold.
- **F5 Prompt-injection persistence:** detect malicious instruction cached as answer → validate outputs and block caching for untrusted content.

## Verification

Semantic caching is acceptable when a labeled pair eval shows precision at or above the declared threshold, metadata-filter tests prevent cross-tenant hits, stale-version tests miss as expected, and live integration tests show uncertain matches fall back to the model.

## Variations

- `Redis vector`: useful for low-latency cache lookups with TTL support.
- `Postgres pgvector`: simple when app data already lives in Postgres.
- `local embeddings`: preferred for sensitive prompts.
- `FAQ bots`: best fit when answers are stable and public.

## Safety & privacy

Medium risk because semantically similar is not the same as safe or correct. Partition by tenant, avoid personal data, tune for high precision, include source versions, redact embeddings where needed, and provide a fast purge path.
