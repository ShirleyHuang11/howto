---
name: measure-refusal-rate
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [ai/evals/build-an-eval-set]
status: draft
last_verified: 2026-09-22
---

## Goal

You measure how often a model refuses requests, separating appropriate safety refusals from unnecessary over-refusals. The result protects both safety and user utility.

## Preconditions

- A labeled dataset with allowed, disallowed, and ambiguous requests.
- A refusal detector using rules, classifier, or calibrated LLM judge.
- A policy describing when refusal is required.

## Steps

1. **Label refusal expectation.** Mark each prompt as `should_answer`, `should_refuse`, or `needs_safe_completion`. → *Expect:* policy-aligned labels for all examples.
2. **Generate outputs.** Run the model with fixed prompt and safety settings. ⚠️ *Data leaves your control:* sanitize sensitive prompts before external API calls. → *Expect:* each example has an output and model metadata.
3. **Detect refusal behavior.** Classify outputs as refusal, answer, or safe redirect using a validated detector. → *Expect:* each row has a refusal label and confidence.
4. **Compute rates by class.** Report appropriate refusal rate, over-refusal rate, and under-refusal rate. → *Expect:* safety and helpfulness tradeoffs are visible.
5. **Inspect ambiguous failures.** Review cases where a safe partial answer was expected but the model fully refused or fully complied. → *Expect:* prompt or policy gaps are identified.

## Decision points

- Under-refusal on disallowed content → strengthen safety policy before shipping.
- Over-refusal on allowed content → add safe-completion examples and clarify boundaries.
- Detector uncertain → send the slice to human review.

## Failure modes & recovery

- **F1 Keyword false positive:** detect benign "I can't" phrasing classified as refusal → use semantic detector plus examples.
- **F2 Unsafe compliance:** detect disallowed prompt answered directly → add policy examples and block release.
- **F3 Overbroad policy prompt:** detect many allowed requests refused → narrow safety instructions.
- **F4 Ambiguous labels:** detect reviewer disagreement → add a middle class or adjudicate with policy owner.

## Verification

The eval reports appropriate refusal, over-refusal, and under-refusal rates with per-category breakdown. The model passes only if under-refusal is below the safety threshold, commonly zero for critical disallowed classes, and over-refusal stays below the product threshold.

## Variations

- `customer support`: include escalation instead of refusal for account-specific requests.
- `creative writing`: distinguish refusal from safe transformation.
- `regulated advice`: require disclaimers and professional referral for borderline cases.

## Safety & privacy

Refusal evals often include harmful or sensitive prompts. Keep datasets access-controlled, avoid operational details that enable harm, and use human review for high-impact policy categories.
