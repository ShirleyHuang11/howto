---
name: profile-a-slow-function
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You measure where a slow function spends time, make a targeted improvement, and verify the function is faster without changing its result.

## Preconditions

- The slow function can be called with deterministic representative inputs.
- A focused test or assertion already confirms correctness, or you can add one.
- A profiler or benchmark tool is available for the language.

## Steps

1. **Reproduce the slowness.** Run the function through a focused test, script, or benchmark with representative input. → *Expect:* runtime is measurably slow compared with the target.
2. **Add a correctness guard.** Assert the function output before changing performance-sensitive code. → *Expect:* future speedups cannot silently change results.
3. **Capture a profile.** [Python | Go | Node] run `python -m cProfile`, `go test -bench ... -cpuprofile`, or a Node CPU profile. → *Expect:* profiler output ranks time by function or line.
4. **Identify the dominant cost.** Look for repeated parsing, nested loops, allocations, database calls, serialization, or unnecessary I/O. → *Expect:* one or two hot spots explain most runtime.
5. **Make the smallest targeted change.** Cache within safe scope, reduce algorithmic complexity, batch work, or avoid repeated conversions. → *Expect:* the code path does less work for the same input.
6. **Re-run correctness tests.** Execute the focused correctness test and related edge cases. → *Expect:* outputs remain unchanged.
7. **Re-run the profile or benchmark.** Compare before and after with the same input and environment. → *Expect:* measured runtime improves beyond profiler noise.

## Decision points

- Most time is in database or network calls → profile the query or remote boundary, not just local CPU.
- Hot path is allocation-heavy → measure memory allocations as well as time.
- Input sizes vary widely → profile typical and worst-case sizes separately.
- Micro-optimization complicates code → keep it only if the measured gain matters.

## Failure modes & recovery

- **F1 Benchmark input is unrealistic:** detect production remains slow → rebuild the benchmark from real sanitized shapes.
- **F2 Optimization changes semantics:** detect correctness test failure → revert the optimization and preserve the test.
- **F3 Profiler overhead misleads:** detect different hot spots across runs → repeat samples and compare stable patterns.
- **F4 Cache grows unbounded:** detect memory increase after speedup → add size limits or lifecycle cleanup.

## Verification

The focused correctness test exits 0, and the repeated benchmark or profiler command shows the optimized function faster than the baseline for the same representative input.

## Variations

- `Python`: use cProfile for call-level timing, py-spy for sampling, and line_profiler for line-level detail.
- `Go`: use benchmarks with CPU and memory profiles, then inspect with `go tool pprof`.
- `JavaScript`: use Chrome DevTools, Node inspector, or built-in performance timers with a benchmark harness.
- `database-backed function`: pair application profiling with `EXPLAIN ANALYZE` for slow queries.

## Safety & privacy

Low risk for local profiling. Use sanitized inputs, avoid saving raw customer payloads in benchmark fixtures, and treat profiler artifacts as sensitive if they include arguments or object contents.
