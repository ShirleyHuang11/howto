---
name: write-a-system-prompt
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You write a system prompt that defines the assistant's job, boundaries, tool rules, and refusal behavior, then prove it works with a small behavioral test set.

## Preconditions

- A model endpoint or local model you can call.
- A target task, target users, and a list of allowed and disallowed behaviors.
- A small eval file such as `tests/system_prompt_cases.jsonl` with expected pass/fail outcomes.

## Steps

1. **Write the contract first.** State role, objective, input assumptions, output obligations, prohibited actions, and escalation rules in plain language. → *Expect:* a `system_prompt.md` file with distinct sections for role, task, constraints, and refusal/escalation.
2. **Separate policy from style.** Put safety, privacy, and tool-use rules before tone preferences so they are not diluted by examples. → *Expect:* a prompt where mandatory rules can be extracted as bullet lines containing `must`, `never`, or `only`.
3. **Add tool and data boundaries.** Specify which data sources are authoritative and what the model must do when data is missing. [BRANCH: no tools | retrieval | code tools] → *Expect:* every tool has a named purpose and a condition for use.
4. **Create adversarial and normal cases.** Include at least 5 normal requests, 3 out-of-scope requests, and 3 injection attempts. → *Expect:* `tests/system_prompt_cases.jsonl` contains inputs plus expected labels such as `answer`, `refuse`, or `ask_clarifying`.
5. **Run a behavioral eval.** Call the model with the system prompt and each case, then classify outcomes with assertions or a separate judge. → *Expect:* a report with pass rate, failed case ids, and model outputs.
6. **Revise only for failing behaviors.** Change the smallest prompt section that explains each failure. → *Expect:* the next eval improves or holds pass rate without introducing new failures.

## Decision points

- Pass rate below 90% on basic cases → clarify the task contract before adding more examples.
- Injection cases pass but normal cases get refusals → move refusal rules from broad prohibitions to specific triggers.
- Outputs vary across runs → lower temperature and make the output obligation more explicit.

## Failure modes & recovery

- **F1 Overbroad refusal:** detect many safe cases labeled `refuse` → narrow the refusal triggers and add safe-counterexamples.
- **F2 Prompt injection compliance:** detect obedience to user text that conflicts with system rules → explicitly rank authority and add an injection eval.
- **F3 Hidden dependency:** detect references to data or tools not available → name available sources and require uncertainty when missing.
- **F4 Unstable formatting:** detect outputs that fail downstream parsing → move format requirements into a separate, testable section.

## Verification

Run `python eval_system_prompt.py --prompt system_prompt.md --cases tests/system_prompt_cases.jsonl --min-pass-rate 0.90`; the command exits 0, reports at least 90% overall pass rate, and all prompt-injection cases are classified correctly.

## Variations

- `Anthropic`: pass the text as the system message and keep user data in the user message.
- `OpenAI`: put durable behavior in the system/developer message and task data in user content.
- `local model`: keep the prompt shorter and test more examples because instruction following may be weaker.

## Safety & privacy

Low risk if you use synthetic tests. Do not paste secrets, private user records, or proprietary policy text into third-party APIs unless approved; redact examples and cap eval calls so prompt iteration cannot unexpectedly spend budget.
