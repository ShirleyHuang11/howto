---
name: test-a-cli-tool
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

You add automated tests for a command-line tool that verify exit codes, stdout, stderr, file effects, and error handling.

## Preconditions

- The CLI can run from source or as a built binary.
- Tests can use temporary directories and synthetic input files.
- The command’s expected behavior is documented or inferable from current usage.

## Steps

1. **Choose the test level.** Use direct function tests for parsing and subprocess tests for full CLI behavior. → *Expect:* at least one test exercises the real executable entrypoint.
2. **Create an isolated workspace.** Use `tmp_path`, `mktemp -d`, or the framework temp directory helper for input and output files. → *Expect:* test files do not modify the repository or user home directory.
3. **Run the CLI as a subprocess.** [Python | Node] use `subprocess.run([...], text=True, capture_output=True)` or `execa`/`child_process.spawn`. → *Expect:* the test captures exit code, stdout, and stderr.
4. **Assert the successful path.** Check exact exit code `0`, stable output text, and any generated file contents. → *Expect:* the CLI produces the intended user-visible result.
5. **Assert the failure path.** Pass invalid arguments or missing files and assert a nonzero exit code plus useful stderr. → *Expect:* the CLI fails predictably without stack traces for normal user errors.
6. **Avoid brittle environment assumptions.** Set required environment variables explicitly and scrub user-specific variables where needed. → *Expect:* the test behaves the same locally and in CI.
7. **Run the focused CLI tests.** Use `pytest -q tests/test_cli.py` or `npm test -- cli`. → *Expect:* all CLI tests exit 0.

## Decision points

- CLI writes snapshots or formatted output → normalize paths, timestamps, and ANSI color before asserting.
- Command prompts interactively → pass flags for non-interactive mode or provide stdin explicitly.
- CLI relies on network APIs → mock the HTTP boundary or run against a local test server.
- Binary packaging is important → test both source invocation and the packaged executable in CI.

## Failure modes & recovery

- **F1 Test hangs waiting for input:** detect timeout or no output → pass `--yes`, `--no-input`, or explicit stdin.
- **F2 Path differs by platform:** detect failures from `/tmp` versus Windows paths → assert relative paths or normalize separators.
- **F3 ANSI color breaks assertions:** detect escape codes in output → disable color with `NO_COLOR=1` or strip ANSI codes.
- **F4 Non-deterministic output:** detect timestamps, random IDs, or ordering changes → inject fixed clock and sort unordered output before asserting.

## Verification

`pytest -q tests/test_cli.py` or the project’s equivalent CLI test command exits 0, and at least one subprocess assertion verifies exit code, stdout or stderr, and any expected file-system side effect.

## Variations

- `Python`: use `pytest` with `tmp_path` and `subprocess.run`; Click apps can use `CliRunner` for lighter tests.
- `Node`: use `execa` or `child_process.spawn`; set `FORCE_COLOR=0` for stable output.
- `Go`: build the binary in a temp directory with `go build -o` and execute it from tests.
- `Shell`: use Bats for black-box CLI tests.

## Safety & privacy

Low risk when tests use temporary directories and synthetic inputs. Never run CLI tests against real cloud accounts by default, and scrub tokens, home-directory config, and machine-specific paths from captured output.
