---
name: red-team-your-own-prompt
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You systematically attack your prompt with misuse, ambiguity, injection, and edge-case tests, then fix the failures before release.

## Preconditions

- A candidate prompt or LLM workflow.
- A risk taxonomy for the product area.
- A harness that can run many test prompts and record outputs.

## Steps

1. **Define attack categories.** Include prompt injection, policy bypass, malformed input, missing context, privacy leakage, and tool misuse. → *Expect:* a red-team checklist with named categories.
2. **Generate test cases.** Write manual cases and optionally use an LLM to propose more variants. → *Expect:* `redteam_cases.jsonl` contains input, category, expected behavior, and severity.
3. **Run the harness.** Execute all cases against the same prompt and model settings planned for release. ⚠️ *Data leaves your control:* do not send real secrets or private records as attack payloads to external APIs. → *Expect:* a results file with output, pass/fail, and failure reason.
4. **Triage failures by severity.** Mark failures that leak data, enable unsafe actions, or violate policy as blockers. → *Expect:* a prioritized fix list.
5. **Patch prompt and code guardrails.** Fix instruction clarity, validation, permissions, or retrieval filtering depending on root cause. → *Expect:* previously failing cases have targeted mitigations.
6. **Re-run full regression.** Test red-team and benign cases together. → *Expect:* fixes block attacks without damaging normal usefulness beyond tolerance.

## Decision points

- A failure involves tool execution or data access → fix code-level controls before prompt wording.
- Red-team pass rate improves but benign pass rate drops → narrow the guardrail and add safe alternatives.
- New severe category appears → expand the suite and delay release.

## Failure modes & recovery

- **F1 Shallow attacks:** detect only obvious `ignore instructions` cases → add encoded, indirect, and role-play variants.
- **F2 No expected behavior:** detect cases without pass criteria → label each case before running.
- **F3 Fix overfits tests:** detect similar new attacks still pass → generate paraphrases and mutations.
- **F4 Missing audit trail:** detect unlogged outputs → store prompt version, model, case id, and result.

## Verification

Run `python run_redteam.py --cases redteam_cases.jsonl --benign benign_cases.jsonl --max-critical-failures 0 --min-benign-pass-rate 0.90`; there must be zero critical failures and benign pass rate must remain at least 90%.

## Variations

- `agent`: include unauthorized tool calls, destructive actions, and permission escalation.
- `RAG`: include malicious retrieved documents and citation spoofing.
- `structured output`: include payloads that try to break JSON or inject commands into fields.

## Safety & privacy

Medium risk because red-team tests may contain harmful instructions. Use synthetic data, never include real secrets, restrict access to failure logs, and treat discovered severe failures as release blockers.
