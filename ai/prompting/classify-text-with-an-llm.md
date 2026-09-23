---
name: classify-text-with-an-llm
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

Classify text into a fixed label set using an LLM, with schema validation, calibrated thresholds, and measured performance on labeled examples.

## Preconditions

- A closed label taxonomy with definitions and examples.
- A labeled development and holdout set representative of production text.
- An LLM API client and a metrics script for accuracy, macro-F1, and confusion matrix.

## Steps

1. **Freeze the label taxonomy.** Define each label, include borderline cases, and add an `unknown` or `needs_review` label if real inputs can be ambiguous. → *Expect:* labels are finite and documented.
2. **Write a constrained classification prompt.** Ask for only the label and optional confidence or rationale in a small JSON object. → *Expect:* the output shape is parseable and labels are enumerable.
3. **Call the model on the dev set.** [BRANCH: Anthropic | OpenAI | open model] Use deterministic settings and record prompt version, model, and raw output. ⚠️ *Data leaves your control:* remove private data or obtain approval before sending production text to an external API. → *Expect:* one prediction row per labeled example.
4. **Validate labels before scoring.** Reject labels not in the taxonomy and count them as invalid predictions. → *Expect:* invalid-label rate is visible in metrics.
5. **Compute classification metrics.** Report accuracy, macro-F1, per-class recall, and a confusion matrix. → *Expect:* weak labels and systematic confusions are identifiable.
6. **Set review thresholds.** Route low-confidence, ambiguous, or high-impact classes to human review instead of forcing a label. → *Expect:* a policy maps confidence bands to accept or review.
7. **Evaluate on holdout before shipping.** Run the final prompt once on untouched data and compare to launch thresholds. → *Expect:* a go/no-go result based on predefined metrics.

## Decision points

- Many examples are truly ambiguous → add `needs_review` rather than pretending labels are clean.
- Macro-F1 is low but accuracy is high → class imbalance is hiding failures; improve minority labels.
- Invalid-label rate is nonzero → use schema constraints or stronger enum instructions.
- Classification triggers enforcement or denial → require stricter thresholds and human review.

## Failure modes & recovery

- **F1 Label drift:** detect new production topics in `unknown` samples → update taxonomy and relabel.
- **F2 Majority-class bias:** detect poor minority recall → add examples and optimize macro-F1.
- **F3 Prompt injection:** detect text asking the model to ignore labels → delimit user text and classify it as data only.
- **F4 Overconfident wrong labels:** detect high confidence in confusion matrix errors → calibrate thresholds using holdout data.

## Verification

Run the classifier on a held-out labeled set. Success means all accepted outputs parse as JSON, `invalid_label_rate == 0`, macro-F1 meets the launch threshold, each critical class meets its minimum recall, and examples below the confidence threshold are routed to `needs_review`.

## Variations

- `moderation`: use conservative thresholds and human review for borderline enforcement.
- `support routing`: optimize per-class recall for urgent categories.
- `local model`: compare against a smaller fine-tuned classifier if latency or privacy matters.

## Safety & privacy

Classification can affect users if used for moderation, eligibility, or prioritization. Log decisions for audit, protect text that may contain PII, defend against prompt injection, and avoid fully automated high-impact decisions without review.
