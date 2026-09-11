---
name: diagnose-high-cpu-usage
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You determine which process, thread, endpoint, job, or function is consuming CPU and verify that mitigation or a fix reduces usage.

## Preconditions

- You have access to the affected host, container, profiler, or observability dashboard.
- Profiling is allowed for the environment being inspected.
- The service version and traffic pattern are known.

## Steps

1. **Confirm CPU saturation.** Check metrics, `top`, `htop`, `kubectl top pod`, or cloud monitoring. → *Expect:* CPU usage is high for a specific process, pod, host, or time window.
2. **Correlate with workload.** Compare CPU spikes with deploys, cron jobs, traffic, queue depth, or a specific endpoint. → *Expect:* at least one candidate trigger is identified.
3. **Capture a CPU profile.** [Go | Node | Python | JVM] use `pprof`, inspector CPU profile, `py-spy`, `perf`, or Java Flight Recorder. → *Expect:* a profile file or flame graph shows hot functions.
4. **Look for tight loops and retry storms.** Inspect hot frames for unbounded loops, regex backtracking, polling without sleep, serialization, compression, or excessive retries. → *Expect:* the expensive code path is named.
5. **Mitigate immediate impact if needed.** Reduce concurrency, disable a feature flag, pause a job, or scale out through the approved operational path. → *Expect:* user impact or saturation decreases.
6. **Fix and add a guard.** Optimize the hot function, bound retries, add indexes, cache safely, or reject pathological input. → *Expect:* code has a test or benchmark preventing regression.
7. **Verify under representative load.** Run a load test, benchmark, or production-safe canary check. → *Expect:* CPU usage falls and latency or queue depth improves.

## Decision points

- CPU spike started after deploy → compare profiles before and after or roll forward with a targeted fix.
- CPU is high but app throughput is low → inspect lock contention, busy waits, or retry loops.
- One endpoint dominates → reproduce with its payload and add endpoint-level benchmark or rate limit.
- Profiling production is too risky → reproduce in staging with captured synthetic workload.

## Failure modes & recovery

- **F1 Profile missing symbols:** detect anonymous or minified frames → install symbols, enable source maps, or build with profiling metadata.
- **F2 Sampling too short:** detect profile dominated by startup noise → profile during the spike for a longer window.
- **F3 Mitigation hides root cause:** detect CPU drops after restart but later returns → keep the profile and continue root-cause analysis.
- **F4 Profiling overhead hurts service:** detect latency worsens during profiling → reduce profiling duration or move to staging.
- **F5 Retry storm:** detect repeated failed calls in logs → apply backoff, circuit breaking, or pause the caller.

## Verification

A CPU profile or load-test report after the fix shows the previous hot function consuming less CPU, and service metrics show CPU below the alert threshold for the agreed window while tests or benchmarks exit 0.

## Variations

- `Go`: use `go tool pprof` from `net/http/pprof` or saved profiles.
- `Node.js`: capture CPU profiles with inspector or clinic tools and verify event-loop delay.
- `Python`: use `py-spy`, Scalene, or cProfile depending on deployment access.
- `Kubernetes`: correlate `kubectl top`, pod restarts, HPA events, and container CPU limits.

## Safety & privacy

Medium risk because live profiling and mitigation can affect users. Keep profiling windows short, avoid dumping sensitive request payloads, and get operational approval before pausing jobs or changing production capacity.
