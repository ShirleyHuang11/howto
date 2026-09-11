---
name: cache-api-responses
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You cache safe API responses with clear keys, expiration, and invalidation so the application is faster without serving incorrect or private data.

## Preconditions

- The endpoint is read-only or the cache invalidation behavior is well understood.
- You know whether responses vary by user, tenant, authorization, locale, or query parameters.
- A cache backend is available, such as in-memory LRU, Redis, CDN cache, or framework data cache.

## Steps

1. **Identify cacheable responses.** Choose GET or otherwise idempotent reads whose data can tolerate staleness. → *Expect:* unsafe mutations and user-specific secrets are excluded.
2. **Design the cache key.** Include endpoint name, normalized parameters, API version, tenant or user scope if needed, and locale. → *Expect:* two different users or parameter sets cannot collide accidentally.
3. **Set a TTL and stale policy.** Pick a time such as 60s for volatile data or 1h for stable reference data. → *Expect:* cached entries expire automatically.
4. **Implement read-through caching.** Check the cache first, fetch on miss, validate the response, then store it with TTL. → *Expect:* first request logs `cache_miss`; repeat request logs `cache_hit`.
5. **Add invalidation for writes.** After local mutations, delete the affected keys or bump a versioned namespace. → *Expect:* a write is followed by fresh data on the next read.
6. **Prevent stampedes.** Use request coalescing or a short lock such as Redis `SET key value NX EX 10` around expensive misses. → *Expect:* concurrent misses produce one upstream call, not one per request.
7. **Test hit, miss, expiry, and invalidation.** Use fake timers or a test cache backend. → *Expect:* tests prove values are reused, expire, and refresh after invalidation.

## Decision points

- Response depends on authorization → include user/tenant identity in the key or do not cache.
- Upstream provides `ETag` or `Cache-Control` → honor provider semantics unless product needs stricter freshness.
- Cache backend unavailable → fail open to the upstream for non-critical caches and emit a metric.

## Failure modes & recovery

- **F1 Data leak across users:** detect one user seeing another user's data → disable the cache, purge affected keys, and fix key scoping before re-enabling.
- **F2 Stale after write:** detect UI or tests reading old data after mutation → add invalidation or shorten TTL for that entity.
- **F3 Cache stampede:** detect upstream traffic spikes at expiry boundaries → add coalescing, jittered TTLs, or stale-while-revalidate.
- **F4 Serialization mismatch:** detect parse errors loading cached values → version the cache key and purge old entries.

## Verification

Run the cache tests, for example `npm test -- api-cache` or `pytest tests/test_api_cache.py -q`; the command exits 0 and asserts one upstream call across repeated reads, a fresh call after TTL expiry, and a fresh call after invalidation.

## Variations

- `Redis`: use `GET`, `SET EX`, and key namespaces; avoid `KEYS` in production.
- `CDN`: set `Cache-Control`, `Vary`, and surrogate keys where supported.
- `React/Next.js`: understand framework fetch caching defaults and explicitly set `cache` or `next.revalidate`.

## Safety & privacy

Medium risk because incorrect keys can leak private data or serve stale decisions. Never cache bearer tokens, secrets, payment details, or personalized responses unless the key is scoped to the exact viewer and the TTL is justified.
