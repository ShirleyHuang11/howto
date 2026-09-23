---
name: evaluate-code-generation
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You measure whether a code-generation model solves real programming tasks by running generated code in a sandboxed test harness. The run ends with a numeric pass rate, saved failures, and a ship/no-ship decision.

## Preconditions

- A callable model endpoint and budget for the eval run.
- A task set with prompts, reference tests, timeouts, and allowed languages.
- A sandbox such as Docker, Firecracker, or a restricted CI runner; never execute generated code on a workstation with secrets.

## Steps

1. **Create a machine-readable task file.** Store each case as JSONL with `id`, `prompt`, `language`, and `tests` or a test file path. → *Expect:* `python -m json.tool` or a JSONL parser reads every row without error.
2. **Build the generation harness.** [BRANCH: Anthropic | OpenAI | open model] Call the model with deterministic settings such as `temperature=0.2`, `max_tokens` high enough for code, and a stop sequence if your wrapper needs one. ⚠️ *Data leaves your control:* prompts sent to an external API may contain proprietary code, so redact secrets and confirm the data policy first. → *Expect:* every task produces a captured completion with model name, parameters, latency, and token counts.
3. **Extract executable code.** Strip Markdown fences, reject multiple files unless the task allows them, and write each solution into a fresh sandbox directory. → *Expect:* each generated artifact has one language extension and no path traversal such as `../`.
4. **Run tests in an isolated container.** Use a command such as `timeout 20s docker run --rm -v "$PWD/run:/work:ro" python:3.12 pytest -q /work/tests.py`. → *Expect:* each task returns `passed`, `failed`, `timeout`, or `runtime_error` plus stdout and stderr.
5. **Compute pass metrics.** Calculate `pass@1`, compile error rate, timeout rate, and median latency; keep per-task failures for debugging. → *Expect:* a summary JSON contains numeric fields like `{"pass_at_1": 0.72, "timeout_rate": 0.01}`.
6. **Compare to a baseline.** Run the same tasks against the previous model, prompt, or release. → *Expect:* the report shows absolute and relative delta for pass rate and cost per solved task.
7. **Set the release gate.** Require a threshold such as `pass@1 >= baseline + 0.03` with no increase in unsafe file/network attempts. → *Expect:* CI exits 0 only when the gate is met.

## Decision points

- Pass rate improves but timeout rate increases → inspect generated algorithms before shipping.
- Many compile errors → tighten formatting instructions or add a parser/repair pass.
- Failures cluster by library version → pin dependencies in the sandbox and rerun.
- Eval tasks overlap with training data → create a fresher held-out set before trusting the score.

## Failure modes & recovery

- **F1 Sandbox escape attempt:** detect generated code opening `/etc`, network sockets, or environment variables → block the run, record the sample, and harden the container profile.
- **F2 Flaky tests:** detect the same solution alternating pass/fail → fix tests, freeze random seeds, and rerun affected cases.
- **F3 Context-length truncation:** detect incomplete functions or API context errors → shorten prompts or use a model with a larger context window.
- **F4 False pass from weak tests:** detect obviously wrong code that passes → add hidden and property-based tests.
- **F5 API rate limits:** detect 429 responses → add exponential backoff and resume from saved completions.

## Verification

Run the eval command in CI and require the summary JSON to validate against your schema, `pass_at_1 >= 0.70` or your documented threshold, `sandbox_violation_count == 0`, and `cost_usd <= budget_usd`. The CI job must fail if any generated solution runs outside the sandbox or if any task lacks a recorded outcome.

## Variations

- `HumanEval/MBPP-style`: use public benchmarks for smoke tests, but do not treat them as product-specific evidence.
- `repo-level coding`: run generated patches against repository tests and static checks instead of single-function tests.
- `open model`: run inference locally with vLLM or TGI and include GPU memory and throughput in the report.

## Safety & privacy

Generated code is untrusted code. Keep secrets out of the sandbox, disable outbound network access unless the task explicitly requires it, log all file and process activity, and review any evaluation that sends proprietary prompts to a third-party model provider.
