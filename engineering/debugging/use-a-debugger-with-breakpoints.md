---
name: use-a-debugger-with-breakpoints
domain: engineering
subdomain: debugging
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

You use breakpoints to inspect live program state at the failing line, understand control flow, and confirm the cause of a bug.

## Preconditions

- The bug can be reproduced locally or in a safe development environment.
- Source maps or debug symbols are available if the code is compiled or bundled.
- You can run the process under a debugger without affecting production traffic.

## Steps

1. **Start from a reliable reproduction.** Run the failing test, script, or local request once without the debugger. → *Expect:* the failure appears with a known command.
2. **Place a breakpoint before the suspected failure.** Set it at the first application frame from the stack trace or just before the bad value is used. → *Expect:* execution pauses before the exception or wrong output.
3. **Run under the debugger.** [Python | Node | Browser] use `python -m pdb script.py`, `node --inspect-brk app.js`, IDE debug launch, or browser DevTools. → *Expect:* the process starts and the debugger attaches.
4. **Inspect inputs and locals.** Print variables, object fields, function arguments, and relevant environment flags. → *Expect:* the value that violates the code’s assumption is visible.
5. **Step over and into selectively.** Step over ordinary library calls and step into application functions that transform the suspicious value. → *Expect:* you identify where correct state becomes incorrect.
6. **Test the hypothesis immediately.** Change only a local variable in the debugger or add a temporary assertion to confirm the suspected cause. → *Expect:* the failure changes in the predicted way.
7. **Remove temporary debugger hooks.** Delete `debugger`, `breakpoint()`, `binding.pry`, or IDE-only changes before finishing. → *Expect:* the codebase has no accidental pause statements.

## Decision points

- Bug is timing-sensitive → prefer trace logging or watchpoints because breakpoints can mask races.
- Process forks or runs in a container → attach to the child process or expose the debug port deliberately.
- Code is minified → rebuild in development mode with source maps.
- State is too large to inspect manually → add conditional breakpoints or watch expressions.

## Failure modes & recovery

- **F1 Breakpoint never hits:** detect process runs past it → confirm code version, route, feature flag, and source map mapping.
- **F2 Debugger changes behavior:** detect bug disappears while paused → switch to logging, sampling profiler, or race detector.
- **F3 Cannot attach to container:** detect refused debug connection → expose the debug port to localhost and bind to `0.0.0.0` only inside the container.
- **F4 Temporary breakpoint committed:** detect `debugger` or `breakpoint()` in search → remove it and add a real test.

## Verification

The reproduction command reaches the breakpoint, the inspected variable or branch explains the failure, and after the fix the same command exits 0 with no `debugger`, `breakpoint()`, or equivalent debug statements remaining in the changed files.

## Variations

- `Python`: use `breakpoint()`, `pdb`, or IDE launch configs; inspect with `p variable`.
- `Node.js`: use `node --inspect` and Chrome DevTools or IDE attach.
- `Browser`: use DevTools breakpoints, conditional breakpoints, and source maps.
- `JVM/.NET`: use IDE debuggers with conditional breakpoints and exception breakpoints.

## Safety & privacy

Low risk in local environments. Never attach a debugger to production without an approved incident process, because pausing threads can break service availability and expose secrets in memory.
