---
name: give-the-model-an-escape-hatch
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

You let the model safely say it cannot answer, needs clarification, or should escalate, and you verify that it uses the escape hatch only when appropriate.

## Preconditions

- A task where inputs may be ambiguous, missing data, unsafe, or outside scope.
- A defined set of escape outcomes such as `clarify`, `insufficient_evidence`, `refuse`, and `escalate`.
- Eval cases covering answerable and unanswerable requests.

## Steps

1. **Define escape categories.** Specify exactly when the model should ask a question, abstain, refuse, or escalate. → *Expect:* each category has triggers and example inputs.
2. **Add the escape output format.** Use a field such as `status` with allowed values `answered`, `clarify`, `insufficient_evidence`, `refused`, or `escalate`. → *Expect:* every output exposes its status.
3. **Require useful next steps.** For clarification or escalation, ask for the missing field or name the review path. → *Expect:* non-answered outputs include a concise reason and next action.
4. **Test answerable cases.** Ensure the escape hatch does not become a default refusal. → *Expect:* answerable cases receive `answered` at the target rate.
5. **Test unanswerable and unsafe cases.** Include missing evidence, ambiguous goals, and disallowed requests. → *Expect:* each case uses the correct escape status.
6. **Tune thresholds.** Adjust instructions and examples until false abstentions and false answers are within limits. → *Expect:* a confusion matrix by status.

## Decision points

- Missing information is easy to ask for → use `clarify`.
- Evidence is absent after retrieval → use `insufficient_evidence`, not a guessed answer.
- Request is unsafe or outside policy → use `refused` or `escalate` depending on severity.

## Failure modes & recovery

- **F1 Guessing:** detect answers for unanswerable cases → strengthen insufficient-evidence rules.
- **F2 Over-abstention:** detect many answerable cases marked unclear → add examples of sufficient context.
- **F3 Vague clarification:** detect questions that do not name missing info → require specific missing fields.
- **F4 Wrong escape type:** detect refusal when clarification would work → define category triggers more sharply.

## Verification

Run `python eval_escape_hatch.py --cases escape_eval.jsonl --min-answerable-answer-rate 0.90 --min-unanswerable-abstain-rate 0.95`; answerable cases must be answered at least 90%, unanswerable cases must abstain or clarify at least 95%, and unsafe cases must not be answered.

## Variations

- `RAG`: use `insufficient_evidence` when retrieved context lacks support.
- `support bot`: use `escalate` for billing, legal, or account-access issues.
- `structured output`: include `status`, `reason`, and `next_action` fields.

## Safety & privacy

An escape hatch reduces hallucination and unsafe compliance, but it must not hide avoidable failures. Track false abstentions, avoid exposing private policy details in refusals, and route high-impact uncertainty to humans.
