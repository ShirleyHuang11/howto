---
name: debug-a-memory-leak
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You prove whether memory grows without being released, identify the retaining objects or allocations, and verify that a fix stabilizes memory.

## Preconditions

- The service, job, or test can run under a profiler in local, staging, or a safe diagnostic environment.
- You have a workload that reproduces memory growth.
- Production heap dumps or profiles, if used, are approved and handled as sensitive data.

## Steps

1. **Measure baseline memory over time.** Run the workload while recording RSS, heap, or container memory with `ps`, runtime metrics, or dashboard graphs. → *Expect:* memory growth is visible and quantified.
2. **Distinguish leak from legitimate cache growth.** Check cache limits, batch sizes, queues, and warmup behavior. → *Expect:* you know whether memory should plateau.
3. **Capture a profile or heap snapshot.** [Node | Python | Go] use heap snapshots, `tracemalloc`, `pprof`, or the runtime profiler. → *Expect:* a profile shows largest object types or allocation sites.
4. **Compare before and after workload.** Take snapshots at startup and after repeated operations. → *Expect:* retained objects that grow with each iteration are visible.
5. **Find the retaining path.** Inspect references from globals, caches, listeners, goroutines, closures, or pending promises. → *Expect:* one owner explains why memory is not released.
6. **Fix ownership or lifecycle.** Remove stale entries, close resources, unsubscribe listeners, bound caches, or stream instead of buffering. → *Expect:* retained object count stops increasing.
7. **Run a soak verification.** Execute the workload long enough to exceed the previous failure window. → *Expect:* memory plateaus below the configured limit.

## Decision points

- Memory plateaus after warmup → document expected cache size and alert threshold rather than changing code.
- Leak appears only under concurrency → run load with representative parallelism and inspect goroutine/thread/task counts.
- Heap is stable but RSS grows → inspect native allocations, buffers, fragmentation, or runtime memory release behavior.
- Container is killed before profiles are saved → lower workload or raise diagnostic memory limit in staging only.

## Failure modes & recovery

- **F1 Profiling changes timing:** detect leak disappears under profiler → use lower-overhead sampling or production metrics plus staging snapshots.
- **F2 Heap dump contains secrets:** detect request bodies or tokens in snapshots → store securely, restrict access, and delete after analysis.
- **F3 Cache mistaken for leak:** detect bounded growth that stops → set explicit cache max size and monitor it.
- **F4 Native memory leak:** detect RSS growth without managed heap growth → inspect native modules, image libraries, database drivers, or cgo allocations.
- **F5 OOM before diagnosis:** detect `OOMKilled` or exit 137 → reduce workload and capture incremental profiles earlier.

## Verification

The same workload that previously caused unbounded growth now runs for the agreed soak period, memory plateaus below the limit, and the profiler shows the suspected retained objects no longer increase per iteration.

## Variations

- `Node.js`: use Chrome DevTools heap snapshots, `--inspect`, and allocation sampling.
- `Python`: use `tracemalloc`, `objgraph`, or Memray for allocation tracking.
- `Go`: use `net/http/pprof`, `go tool pprof`, and goroutine profiles.
- `Kubernetes`: verify with pod memory metrics and absence of `OOMKilled` restarts.

## Safety & privacy

Medium risk because memory diagnostics can expose live data and profiling can slow services. Prefer staging, restrict heap dump access, redact artifacts before sharing, and do not raise production memory limits as the only fix.
