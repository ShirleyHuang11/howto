---
name: red-team-an-llm-application
domain: ai
subdomain: safety
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Find and measure safety, privacy, security, and reliability failures in an LLM application before release, using a reproducible adversarial test suite.

## Preconditions

- A deployed staging version of the LLM application with logging enabled.
- A written policy describing disallowed outputs and high-risk tool actions.
- A red-team dataset runner such as pytest, promptfoo, garak, Inspect, or a custom harness.

## Steps

1. **Define the threat model.** List protected assets, allowed actions, disallowed content, tools, data stores, and attacker goals. → *Expect:* a versioned threat model with test categories.
2. **Build adversarial test cases.** Include prompt injection, jailbreaks, data exfiltration, tool misuse, unsafe advice, policy evasion, and malformed input. → *Expect:* a machine-readable test set with expected allowed/blocked labels.
3. **Run tests against staging.** Execute the harness with fixed model, prompt, retrieval, and tool versions. ⚠️ *Data leaves your control:* hosted model calls may include adversarial prompts and retrieved data; use staging-safe fixtures. → *Expect:* a results file with request ids, outputs, labels, and pass/fail verdicts.
4. **Judge outputs consistently.** Use deterministic checks where possible and an LLM judge only with a rubric and calibration examples. → *Expect:* every failure has a category and evidence snippet.
5. **Fix the highest-risk failures.** Patch prompts, filters, tool gates, retrieval permissions, or refusal policy, then rerun the same suite. → *Expect:* the regression count drops without breaking benign-task pass rate.
6. **Set a release gate.** Define the minimum safety pass rate and maximum critical failures allowed. → *Expect:* release status is computed from metrics, not manual vibes.

## Decision points

- Any critical data-exfiltration or destructive-tool bypass succeeds → do not ship until fixed and retested.
- Safety improves but benign utility collapses → tune policy boundaries and add benign counterexamples.
- LLM judge disagrees with humans often → recalibrate rubric or switch to deterministic assertions for that category.

## Failure modes & recovery

- **F1 Prompt-injection bypass:** detect tool use or secret leakage after hostile instructions → add instruction hierarchy, content isolation, and tool allowlists.
- **F2 Judge drift:** detect changed verdicts on the same outputs → pin judge model/version and use calibration cases.
- **F3 Test leakage into prompt:** detect the model seeing expected labels → separate runner metadata from user-visible prompt.
- **F4 Staging/prod mismatch:** detect different prompts or tool permissions → export and compare app configuration before release.

## Verification

The red-team harness produces a versioned report, all critical tests pass, total safety pass rate is at least the configured threshold such as 0.95, benign-task pass rate does not drop by more than 2 percentage points, and every remaining failure has an owner and severity.

## Variations

- `garak/promptfoo/Inspect`: useful for repeatable suites and reports.
- `manual expert red team`: better for novel attacks; convert findings into regression tests afterward.
- `agent application`: include tool-call traces and permission checks, not only final text.

## Safety & privacy

Use synthetic secrets and fixtures, not real credentials or customer data. Keep adversarial prompts out of user-facing examples, restrict access to failure logs, and never run destructive tools during red-team tests.
