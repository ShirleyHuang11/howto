---
name: benchmark-a-function
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You measure a function’s performance with a repeatable benchmark, compare it to a baseline, and avoid confusing benchmark noise with real improvement.

## Preconditions

- The function can be called with deterministic inputs.
- Dependencies are installed and the benchmark can run outside production.
- You have a baseline commit, saved result, or current implementation to compare against.

## Steps

1. **Define the performance question.** Choose latency, throughput, allocations, or memory as the primary metric. → *Expect:* one metric is named before writing benchmark code.
2. **Prepare representative inputs.** Use small, typical, and worst-case fixtures if behavior changes by size. → *Expect:* benchmark inputs reflect real workload shapes without production data.
3. **Use the language benchmark harness.** [Go | Python | JavaScript] write `BenchmarkXxx(b *testing.B)`, `pytest-benchmark`, or Benchmark.js instead of manual one-off timing. → *Expect:* the harness controls iterations and reports statistical timing.
4. **Exclude setup from the timed region.** Build fixtures before the loop or use reset hooks such as `b.ResetTimer()`. → *Expect:* measured time belongs mostly to the target function.
5. **Run enough samples.** Use commands such as `go test -bench=. -benchmem -count=10`, `pytest --benchmark-only`, or `node benchmark.js`. → *Expect:* results include multiple samples or confidence statistics.
6. **Compare against baseline.** Use `benchstat old.txt new.txt` for Go or the benchmark plugin’s compare feature. → *Expect:* the result reports percentage change and significance where supported.
7. **Keep a regression guard where useful.** Add a CI benchmark threshold only if the environment is stable enough. → *Expect:* CI catches large regressions without failing on normal noise.

## Decision points

- Function is dominated by I/O → benchmark with a local fake or measure an integration path separately.
- Results vary by more than expected → pin CPU governor where possible, reduce background load, and increase sample count.
- Allocation count matters → include memory metrics such as `-benchmem` or heap profiling.
- CI runners are noisy → store benchmarks as informational artifacts instead of hard gates.

## Failure modes & recovery

- **F1 Benchmark measures setup:** detect suspiciously constant runtime across input sizes → move fixture construction outside the timed loop.
- **F2 Dead-code elimination:** detect unrealistically tiny times → consume the function result in a package-level sink or assertion.
- **F3 Noisy machine:** detect wide confidence intervals → rerun on an idle machine and increase sample count.
- **F4 Non-representative input:** detect production still slow after a win → add fixtures matching real traces or payload sizes.

## Verification

The benchmark command, such as `go test -bench=BenchmarkParse -benchmem -count=10 ./pkg/parser`, exits 0 and produces a comparison report showing the target metric for old and new implementations with acceptable variance.

## Variations

- `Go`: use `testing.B`, `b.ReportAllocs()`, and `benchstat`.
- `Python`: use `pytest-benchmark` and compare stored benchmark JSON.
- `JavaScript`: use Benchmark.js, tinybench, or the runtime’s built-in test runner benchmark support when available.
- `Rust`: use Criterion.rs for statistically robust local benchmarks.

## Safety & privacy

Low risk because benchmarks should be local and synthetic. Do not benchmark with raw customer payloads; derive anonymized shapes or generated fixtures, and avoid committing machine-specific absolute timings as universal truth.
