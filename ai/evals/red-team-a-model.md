---
name: red-team-a-model
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h
risk: high
prerequisites: [ai/evals/build-an-eval-set]
status: draft
last_verified: 2026-09-22
---

## Goal

You test an LLM application against misuse, jailbreaks, prompt injection, data exfiltration, and unsafe tool use. The result is a reproducible adversarial eval with mitigations for confirmed failures.

## Preconditions

- Written safety policy defining allowed and disallowed behavior.
- A sandbox environment with mock tools and no production credentials.
- A red-team prompt set covering policy, privacy, tool, and retrieval attacks.

## Steps

1. **Define attack categories.** Include jailbreaks, indirect prompt injection, sensitive-data extraction, unsafe advice, and unauthorized tool actions. → *Expect:* a labeled attack taxonomy.
2. **Create adversarial cases.** Combine known attacks with product-specific threats and benign controls. → *Expect:* a JSONL set with `attack_type`, `input`, and expected refusal or safe behavior.
3. **Run in a sandbox.** Use mock tools and fake records for any agent actions. → *Expect:* no real emails, payments, deletes, or external side effects occur.
4. **Score policy compliance.** Use deterministic checks for tool calls and a calibrated judge for text safety. ⚠️ *Data leaves your control:* do not send real secrets or user records to external judges. → *Expect:* each case is labeled pass, fail, or needs human review.
5. **Triage severe failures.** Prioritize cases where the model reveals secrets, follows injected instructions, or calls forbidden tools. → *Expect:* a ranked remediation list.
6. **Add regressions for fixes.** Put confirmed failures into the recurring eval suite. → *Expect:* each fixed issue has a permanent test.

## Decision points

- Tool misuse occurs → disable the tool path until authorization checks and confirmation steps are added.
- Prompt injection succeeds through retrieved text → separate instructions from data and ignore untrusted content as instructions.
- Refusal rate on benign controls rises → tune policy prompts to reduce over-refusal.

## Failure modes & recovery

- **F1 Real side effect:** detect a production write or outbound message → revoke credentials, audit logs, and rerun only in sandbox.
- **F2 Prompt-injection bypass:** detect retrieved text changes system behavior → add instruction hierarchy tests and content isolation.
- **F3 Secret leakage:** detect keys, emails, or internal text in output → rotate exposed secrets and tighten context access.
- **F4 Judge blind spot:** detect human reviewers find missed harms → update rubric and require human review for that category.

## Verification

The red-team runner reports zero critical failures, zero real tool side effects, and pass rates above configured thresholds per attack type, such as `prompt_injection_pass_rate >= 0.95` and `secret_leak_failures == 0`.

## Variations

- `rag`: include malicious retrieved documents and citation manipulation.
- `agent`: include unauthorized writes, privilege escalation, and confirmation bypass.
- `code assistant`: include dependency confusion, insecure code generation, and secret extraction.

## Safety & privacy

This is high risk because it intentionally probes harmful behavior. Use fake data, mock tools, isolated credentials, logging, and human review before publishing or sharing attack prompts that could enable abuse.
