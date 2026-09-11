---
name: warm-up-a-cache-after-deploy
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You pre-populate important caches after a deploy so first real users do not pay cold-start latency or trigger avoidable backend load.

## Preconditions

- The new version is deployed and serving health checks.
- A list of cacheable high-traffic routes, keys, or queries is available.
- Warming requests are safe, idempotent, and do not mutate user data.
- Monitoring exists for cache hit rate, latency, and backend load.

## Steps

1. **Confirm the deploy is healthy.** Run `curl -fsS https://app.example.com/healthz`. → *Expect:* exit 0 and a healthy response before warming begins.
2. **Select the warm-up set.** Use top routes, product IDs, search queries, or API keys from recent traffic, excluding private or user-specific resources. → *Expect:* a bounded list of URLs or cache keys to warm.
3. **Throttle the warm-up job.** Set concurrency and rate limits so warming does not overload the app or database. → *Expect:* a documented limit such as `10` concurrent requests or `50` requests per second.
4. **Run the warm-up requests.** For URLs, run `xargs -n1 -P10 curl -fsS -o /dev/null < warmup-urls.txt`; for a script, run `python scripts/warm_cache.py --limit 1000 --concurrency 10`. → *Expect:* requests complete with 2xx/3xx responses and no mutation side effects.
5. **Watch backend saturation.** Check database CPU, queue depth, and error rate while warming. → *Expect:* metrics remain below alert thresholds.
6. **Measure cache effect.** Query cache metrics or repeat a representative request with timing, such as `curl -fsS -o /dev/null -w '%{time_total}\n' https://app.example.com/popular-page`. → *Expect:* hit rate increases or latency drops on repeated requests.
7. **Stop on error spikes.** If 5xx, timeouts, or database saturation appears, halt the warm-up job and let traffic warm naturally. → *Expect:* error rate returns to baseline.

## Decision points

- Cache keys are user-specific → do not prewarm them unless using synthetic non-user fixtures.
- Cache invalidation happened globally → warm only the highest-value subset first.
- Backend is near saturation → reduce concurrency or delay warming until capacity is higher.
- CDN and app cache both exist → warm CDN through public URLs and app cache through internal safe endpoints if available.

## Failure modes & recovery

- **F1 Warm-up causes 5xx:** detect elevated error rate or failed `curl` responses → stop the job, reduce concurrency, and retry a smaller set.
- **F2 Private data cached publicly:** detect user-specific content in shared cache → purge affected keys/CDN paths and fix cache-control headers before warming again.
- **F3 Cache misses remain high:** detect hit rate unchanged → verify the warm-up URLs match cache keys and that responses are cacheable.
- **F4 Rate limited by CDN or app:** detect 429 responses → lower request rate and use authenticated internal warming only when approved.

## Verification

The warm-up command exits 0, representative URLs return `200`, cache hit-rate metrics increase for the warmed namespace, and backend error rate stays below alert threshold during the run.

## Variations

- `CDN`: use provider cache prefetch or public `curl` requests and verify with cache headers such as `CF-Cache-Status` or `X-Cache`.
- `Redis`: populate keys through a safe script and verify with `redis-cli EXISTS <key>` or application metrics.
- `Search`: warm common queries through read-only API calls and verify query latency percentiles.

## Safety & privacy

Medium risk because warming can amplify load or leak data through shared caches. Warm only idempotent public or synthetic resources, keep concurrency bounded, never include real user tokens in warm-up files, and purge immediately if private content is cached incorrectly.
