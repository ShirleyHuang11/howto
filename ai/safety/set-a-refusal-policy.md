---
name: set-a-refusal-policy
domain: ai
subdomain: safety
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Create and enforce a refusal policy so the application consistently declines disallowed requests while still helping with safe alternatives.

## Preconditions

- Product requirements describing allowed users, allowed domains, and prohibited behavior.
- Example prompts for safe, disallowed, and borderline requests.
- A model prompt, policy classifier, or output guard where refusal behavior can be implemented and tested.

## Steps

1. **Write policy categories.** Define disallowed, allowed, and transform/educational cases with examples. → *Expect:* a versioned policy document reviewers can approve.
2. **Specify the refusal style.** Require brief refusals, no procedural harmful detail, and safe redirection where appropriate. → *Expect:* refusal templates or rubric examples exist.
3. **Implement policy checks.** [BRANCH: system prompt | classifier before generation | output moderation] Apply the policy before or during generation. → *Expect:* disallowed prompts produce refusal-shaped outputs.
4. **Create a policy eval set.** Include clear disallowed requests, benign lookalikes, and requests that should be answered safely. → *Expect:* each case has an expected label and rationale.
5. **Run automated evaluation.** Judge label correctness and refusal quality with deterministic checks and calibrated human/LLM grading. → *Expect:* refusal accuracy and helpful-answer accuracy are reported separately.
6. **Add regression gates.** Fail CI or deployment when critical disallowed cases are answered or benign cases are over-refused. → *Expect:* policy regressions block release.

## Decision points

- Model gives harmful details in refusals → tighten refusal template and output moderation.
- Benign educational content is over-refused → add allowed examples and clarify intent boundaries.
- Policy conflicts with jurisdiction or platform rules → escalate to legal/safety owners before release.

## Failure modes & recovery

- **F1 Inconsistent refusal:** detect different outcomes for paraphrases → add paraphrase tests and classifier normalization.
- **F2 Helpful harmful detail:** detect refusal that still includes instructions → output-filter for forbidden procedural content.
- **F3 Over-refusal:** detect safe prompts refused → add safe-completion examples and tune thresholds.
- **F4 Stale policy:** detect rules not matching current product policy → version policies and require owner review.

## Verification

The policy eval suite passes with zero critical disallowed completions, refusal-label accuracy is at least 0.95, benign over-refusal rate is at most 0.05, and every refusal includes an approved safe-redirection pattern when applicable.

## Variations

- `prompt-only`: fast to deploy; pair with evals because behavior may drift.
- `classifier-gated`: clearer control; maintain labeled data and thresholds.
- `regulated domain`: require legal or clinical review for policy categories and examples.

## Safety & privacy

A refusal policy protects users only when it is specific, tested, and updated. Avoid collecting unnecessary sensitive prompts in evals, keep policy decisions explainable to reviewers, and do not let refusal wording provide actionable harmful instructions.
