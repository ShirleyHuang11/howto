---
name: measure-latency-and-cost
domain: ai
subdomain: evals
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

You measure latency, token use, and estimated cost for an LLM workflow under realistic load. The result is a budgeted performance report with percentiles, not just averages.

## Preconditions

- A representative request set and runnable app endpoint.
- Token counting or provider usage metadata.
- Current provider pricing for the model and any embeddings, rerankers, or tools.

## Steps

1. **Define the workload.** Choose request mix, concurrency, and sample size that match expected traffic. → *Expect:* a load plan with at least 100 requests or enough for stable percentiles.
2. **Instrument every call.** Log `request_id`, model, input tokens, output tokens, start time, end time, retries, and errors. → *Expect:* each request has complete telemetry.
3. **Run a controlled benchmark.** Execute `python bench.py --concurrency 5 --requests eval_requests.jsonl`. ⚠️ *Data leaves your control:* benchmark prompts sent to external APIs must be sanitized. → *Expect:* a results file with one row per request.
4. **Compute percentiles and cost.** Report p50, p90, p95, p99 latency and cost per request using provider pricing. → *Expect:* a table by route, model, and request type.
5. **Separate retries and failures.** Count 429s, 5xx errors, timeouts, and retry-added latency. → *Expect:* reliability metrics appear beside latency and cost.
6. **Set budgets.** Define pass thresholds such as `p95 < 4s`, `error_rate < 1%`, and `$ per 1k requests < budget`. → *Expect:* a clear pass/fail benchmark result.

## Decision points

- Latency high from output length → cap max tokens or improve prompt concision.
- Latency high from retrieval/tools → parallelize independent calls or cache stable results.
- Cost above budget → use a smaller model for easy cases, batch calls, or reduce context.

## Failure modes & recovery

- **F1 Pricing drift:** detect cost mismatch with invoice → update pricing config and rerun reports.
- **F2 Warm-cache bias:** detect benchmark faster than production → include cold-cache and cache-hit scenarios separately.
- **F3 Rate limits:** detect many 429s → lower concurrency, request higher limits, or add backoff.
- **F4 Missing usage metadata:** detect null token counts → add tokenizer fallback or provider response parsing.

## Verification

The benchmark writes complete telemetry for every request, reports p50/p95/p99 latency, token totals, error rate, and estimated cost. The run passes only when all configured budgets are met and no request has missing cost or latency fields.

## Variations

- `streaming`: measure time to first token and time to final token separately.
- `batch API`: measure wall-clock job time and cost per completed item.
- `self-hosted`: include GPU utilization and queue time.

## Safety & privacy

Benchmarks can burn money quickly. Use explicit request caps, separate test keys, sanitized prompts, and current pricing. Never load-test a production dependency without permission.
