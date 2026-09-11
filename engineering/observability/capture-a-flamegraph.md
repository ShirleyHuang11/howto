---
name: capture-a-flamegraph
domain: engineering
subdomain: observability
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You capture a CPU flamegraph from a running workload and identify the hottest code paths without destabilizing the service.

## Preconditions

- Permission to profile the target process and access to the host, container, or profiling platform.
- A representative workload running long enough to sample.
- Symbols or source maps available where the runtime needs them.

## Steps

1. **Identify the target process and load window.** Run `ps -eo pid,comm,args,%cpu --sort=-%cpu | head` or inspect the container process with `docker top <container>`. → *Expect:* a PID or container name for the hot service process.
2. **Confirm profiling safety.** Check CPU headroom and whether production profiling is allowed; prefer a canary or replica for first capture. → *Expect:* the target has enough headroom and a rollback option if profiling adds overhead.
3. **Install or select the profiler.** [BRANCH: Linux native, use `perf` | JVM, use `async-profiler` | Go, use `go tool pprof` endpoint | Node.js, use `0x` or `clinic flame`] → *Expect:* the profiler command is available on the host or in the runtime.
4. **Capture a bounded sample.** Example Linux command: `sudo perf record -F 99 -p <PID> -g -- sleep 30`. Example Go: `go tool pprof -seconds=30 -http=:0 http://localhost:6060/debug/pprof/profile`. → *Expect:* a 30-second profile file is produced without the service becoming unhealthy.
5. **Render the flamegraph.** For `perf`, run `sudo perf script > out.perf` and `stackcollapse-perf.pl out.perf | flamegraph.pl > flamegraph.svg`; for pprof, use the generated web UI or `go tool pprof -svg profile.pb.gz > flamegraph.svg`. → *Expect:* an SVG or interactive profile view opens with visible stacks.
6. **Record the workload context.** Note commit SHA, traffic level, endpoint, PID/container, sample duration, and profiler used. → *Expect:* the flamegraph can be reproduced or compared later.
7. **Validate the hottest path before optimizing.** Cross-check the top frames with request metrics, traces, or benchmark results. → *Expect:* the suspected bottleneck aligns with observed latency or CPU cost.

## Decision points

- Production host has low CPU headroom → profile a canary, staging environment, or shorter interval first.
- Stacks are mostly `[unknown]` → install debug symbols, enable frame pointers, or use runtime-specific profilers.
- Workload is not representative → rerun during realistic traffic before changing code.
- Hot path is garbage collection or allocation → capture heap/allocation profiles as a follow-up.

## Failure modes & recovery

- **F1 Permission denied:** detect `perf_event_open` or ptrace errors → use approved elevated access, adjust `kernel.perf_event_paranoid`, or profile inside an authorized environment.
- **F2 Missing symbols:** detect unreadable or unknown frames → install symbol packages, enable frame pointers, or rebuild with profiling-friendly flags.
- **F3 Service impact:** detect latency or healthcheck degradation during capture → stop profiling immediately and reduce sampling duration/frequency.
- **F4 Empty profile:** detect zero samples or idle stacks → capture during load or verify the PID/container target.

## Verification

The profiler command exits 0, `flamegraph.svg` or a pprof profile file exists and is non-empty (`test -s flamegraph.svg`), and the top stack frames correspond to the target service code or runtime activity.

## Variations

- `Go`: expose `net/http/pprof` behind an internal-only endpoint and use `go tool pprof`.
- `JVM`: use `async-profiler` with `./profiler.sh -d 30 -f flamegraph.html <PID>`.
- `Kubernetes`: use an ephemeral debug container or approved profiling sidecar instead of installing tools into the app image.

## Safety & privacy

Medium risk because profilers can add overhead and stack traces may reveal file paths, function names, or tenant identifiers. Capture bounded samples, store artifacts in restricted locations, and avoid profiling production without an approved window and rollback path.
