---
name: warm-a-model-to-cut-cold-starts
domain: ai
subdomain: llmops
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You reduce first-request latency by warming model servers, caches, and routes before real users hit them, and you verify the cold-start improvement with timing metrics.

## Preconditions

- A deployed model endpoint or local model server with health checks.
- Metrics for time to first token, total latency, model-load time, and cache status.
- A safe synthetic prompt that does not contain user or proprietary data.
- A scheduler, deployment hook, or readiness probe location for warmup calls.

## Steps

1. **Measure the current cold start.** Restart one replica or use a staging deployment and time the first request, time to first token, and second request. → *Expect:* a baseline showing cold and warm latency difference.
2. **Identify what needs warming.** Check whether delay comes from container startup, weight loading, tokenizer load, JIT compilation, graph capture, retrieval caches, or provider route initialization. → *Expect:* a short list of warmable components.
3. **Create a harmless warmup prompt.** Use a tiny deterministic request such as "Reply with OK." with low `max_tokens`. → *Expect:* warmup cost and token count are minimal and predictable.
4. **Add warmup after readiness but before traffic.** In a deploy hook or startup task, call the local model endpoint until it returns a valid response, then mark the replica ready. → *Expect:* new replicas receive user traffic only after a successful warmup.
5. **Warm periodic idle paths.** If serverless or autoscaled workers go idle, schedule lightweight warmups below your cost budget. → *Expect:* idle replicas stay within the desired warm latency window.
6. **Exclude warmups from user analytics.** Tag requests with `warmup=true` and a synthetic tenant. → *Expect:* dashboards can separate warmup latency and cost from user traffic.
7. **Add failure handling.** If warmup fails, keep the replica out of rotation or retry with backoff. → *Expect:* failed warmups produce alerts instead of slow first-user requests.
8. **Compare before and after.** Re-run the cold-start test across multiple restarts. → *Expect:* p95 first-request latency improves by the target amount without meaningful cost increase.

## Decision points

- Warmup cost exceeds benefit → reduce frequency or warm only high-traffic routes.
- Autoscaling creates many new replicas → warm in parallel but cap warmup concurrency.
- Provider bills every warmup → prefer readiness warmups over periodic pings unless cold starts hurt SLOs.
- Local serving uses CUDA graphs → include the representative shape needed for graph capture.

## Failure modes & recovery

- **F1 Warmup hides unhealthy server:** detect warmup succeeds but real routes fail → warm every supported route or run a realistic smoke prompt.
- **F2 Warmup stampede:** detect many replicas warming at once → add jitter and concurrency limits.
- **F3 Analytics pollution:** detect synthetic requests in product metrics → enforce `warmup=true` filters.
- **F4 Cache mismatch:** detect warmup shape differs from real traffic and latency remains high → warm representative sequence lengths and batch sizes.
- **F5 Unexpected spend:** detect warmup cost above budget → reduce token limits, frequency, or warm only on deploy.

## Verification

Run an automated restart benchmark with at least 10 cold starts before and after warmup. The change passes only when first-request p95 latency drops below the configured target, warmup requests are tagged and excluded from user metrics, warmup error rate is `0`, and added warmup cost stays under the budget.

## Variations

- `vLLM`: warm representative prompt lengths to trigger memory allocation and CUDA graph paths.
- `serverless`: scheduled pings can help, but platform idle policies may still reclaim instances.
- `managed-api`: you may only warm provider routes indirectly with low-cost synthetic calls.

## Safety & privacy

Low risk when warmup prompts are synthetic and tiny. Never use real user prompts for warmup, tag all synthetic traffic, cap warmup frequency, and ensure readiness logic does not route traffic to failed replicas.
