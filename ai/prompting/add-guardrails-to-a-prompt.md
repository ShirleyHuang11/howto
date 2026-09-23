---
name: add-guardrails-to-a-prompt
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

You add guardrails that prevent unsafe, unsupported, or malformed outputs while preserving useful answers for allowed requests.

## Preconditions

- A prompt or workflow with known risk categories.
- Policy rules for allowed, disallowed, and escalate-to-human behavior.
- Test cases covering benign requests, boundary cases, and violations.

## Steps

1. **List risks and allowed behavior.** Define what the model may answer, must refuse, and should escalate. → *Expect:* a policy table with categories and example requests.
2. **Add guardrail instructions.** Put safety, privacy, grounding, and format constraints ahead of style instructions. → *Expect:* the prompt has explicit rules for refusal and safe completion.
3. **Add output validation.** Use schema checks, citation checks, regex constraints, or classifiers outside the model. → *Expect:* invalid outputs are blocked or retried before delivery.
4. **Test benign and adversarial cases.** Include normal requests so guardrails do not overblock. → *Expect:* a confusion matrix for allow, refuse, and escalate labels.
5. **Add action gates for tools.** Require code-level authorization before sending emails, spending money, modifying data, or calling external systems. → *Expect:* tool calls fail closed when permission is missing.
6. **Tune thresholds and messages.** Make refusals brief, specific, and helpful when safe alternatives exist. → *Expect:* allowed pass rate and violation block rate meet targets.

## Decision points

- Guardrail is about external actions → enforce in code, not only in text.
- Overblocking exceeds target → add more benign examples and narrower refusal triggers.
- Safety classifier and model disagree → route high-risk disagreement to human review.

## Failure modes & recovery

- **F1 Overrefusal:** detect safe requests blocked → split broad policy categories into specific triggers.
- **F2 Underblocking:** detect disallowed answers provided → add tests and server-side validation.
- **F3 Tool bypass:** detect generated unauthorized action → deny at the tool gateway.
- **F4 Vague refusal:** detect unhelpful generic refusals → add safe alternatives and escalation wording.

## Verification

Run `python eval_guardrails.py --cases guardrail_cases.jsonl --min-block-rate 0.98 --min-allow-rate 0.90`; disallowed cases must be blocked at least 98%, benign cases allowed at least 90%, and no unauthorized tool call may execute.

## Variations

- `content safety`: combine prompt rules with moderation or policy classifiers.
- `RAG`: add groundedness and citation validation.
- `agents`: add permission checks and dry-run summaries before actions.

## Safety & privacy

Medium risk because guardrails often protect users and systems from harm. Keep private data out of logs where possible, review failures, and require human approval for high-impact or irreversible actions.
