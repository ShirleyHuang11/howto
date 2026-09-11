---
name: inspect-a-core-dump
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

You load a crash core dump with matching binaries and symbols, identify the crashing thread and stack, and produce a concrete root-cause hypothesis or fix.

## Preconditions

- You have the core file, the exact executable build, shared libraries or container image, and matching debug symbols if available.
- You are allowed to inspect the dump; core files may contain secrets, request bodies, and personal data.
- Debuggers are installed: `gdb` for Linux native binaries, `lldb` for macOS, or language-specific tools for managed runtimes.

## Steps

1. **Preserve the dump read-only.** Copy it to a restricted working directory with `chmod 600 core.*`. → *Expect:* only the investigating user can read the dump.
2. **Confirm executable and architecture.** Run `file ./app core.*` and, on Linux, `readelf -n ./app | grep -A4 'Build ID'`. → *Expect:* the core and binary architectures match, and the build ID is recorded.
3. **Install or point to symbols.** Add symbol paths, for example `gdb -ex 'set debuginfod enabled on' ./app core.1234` or configure `/usr/lib/debug/.build-id`. → *Expect:* stack frames include function names instead of only raw addresses.
4. **Open the dump in the debugger.** Run `gdb ./app core.1234` or `lldb -c core.1234 ./app`. → *Expect:* the debugger loads the program, core, and shared libraries without fatal mismatch warnings.
5. **Inspect the crashing thread.** In `gdb`, run `info threads`, `thread apply all bt full`, and `frame 0`. → *Expect:* the signal, crashing instruction, and top stack frames are visible.
6. **Inspect local state safely.** Print relevant variables with `p variable`, inspect memory near pointers with `x/16gx address`, and avoid dumping whole buffers unless necessary. → *Expect:* invalid pointer, assertion state, race symptom, or input condition is narrowed.
7. **Map the stack to source.** Use `list`, `info line *0xADDRESS`, or `addr2line -e ./app 0xADDRESS`. → *Expect:* file and line references for the crashing frames.
8. **Reproduce or guard the fault.** Add a failing test, sanitizer run, or defensive check that exercises the suspected path. → *Expect:* the crash or assertion is reproduced before the fix and passes after it.

## Decision points

- Binary build ID does not match the core → retrieve the exact artifact or container from the deployment that produced the dump.
- Stack is corrupted → inspect registers, disassembly, sanitizers, and nearby heap metadata instead of trusting every frame.
- Crash is in a shared library → install symbols for that library and check ABI/version mismatches.
- Dump contains sensitive data → restrict access, avoid broad string extraction, and rotate exposed secrets if discovered.

## Failure modes & recovery

- **F1 Missing symbols:** detect `??` frames or unknown source lines → install debug packages, enable `debuginfod`, or fetch the exact unstripped artifact.
- **F2 Wrong executable:** detect debugger warnings about exec mismatch → match build ID, image digest, or release artifact before continuing.
- **F3 Optimized-out locals:** detect `<optimized out>` in frames → use registers, disassembly, logs, or reproduce with a debug build.
- **F4 Huge or inaccessible core:** detect storage or permission errors → compress securely, inspect on the host that generated it, or configure smaller core filters for next reproduction.

## Verification

`gdb -batch -ex 'thread apply all bt' ./app core.1234` exits 0 and prints a stack containing named project functions, and the follow-up regression test or sanitizer command exits 0 after the fix.

## Variations

- `systemd-coredump`: use `coredumpctl list`, then `coredumpctl debug <PID-or-EXE>`.
- `macOS`: use `lldb -c core ./app` and `image lookup --address`.
- `Go`: inspect panic stacks first; use core dumps only when `GOTRACEBACK=crash` produced one.
- `containers`: extract the exact image with matching libraries and run the debugger inside or against that filesystem.

## Safety & privacy

Medium risk because core dumps can contain credentials, customer data, and encryption material. Store them in restricted locations, do not paste broad memory dumps into tickets, and delete or archive them according to incident-retention policy.

