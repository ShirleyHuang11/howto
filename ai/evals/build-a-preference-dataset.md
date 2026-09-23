---
name: build-a-preference-dataset
domain: ai
subdomain: evals
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

You create a preference dataset of prompts with chosen and rejected responses that can train or evaluate a reward model, DPO run, or ranking system. The finished dataset has validated pairs, reviewer agreement, and documented policy criteria.

## Preconditions

- A prompt sample from the target use case, stripped of unnecessary PII.
- Two or more response sources, such as model variants, prompt variants, or human-written answers.
- A rubric that defines helpfulness, correctness, safety, and style priorities.

## Steps

1. **Sample prompts from real traffic or a task set.** Stratify by domain, difficulty, language, and safety sensitivity. → *Expect:* a prompt manifest with stable IDs and distribution counts.
2. **Generate candidate responses.** [BRANCH: Anthropic | OpenAI | open model] Produce at least two candidates per prompt with recorded model IDs and parameters. ⚠️ *Data leaves your control:* external APIs receive the prompts, so remove secrets and minimize user data. → *Expect:* each prompt has `response_a` and `response_b` plus provenance.
3. **Write the preference rubric.** Make reviewers prefer factual, instruction-following, safe, and concise answers over fluent but wrong answers. → *Expect:* a one-page rubric and labels such as `chosen`, `rejected`, `tie`, and `both_bad`.
4. **Collect independent labels.** Have at least two reviewers label a calibration subset before full annotation. → *Expect:* inter-annotator agreement, such as Cohen's kappa or simple agreement, is computed.
5. **Resolve ties and low-agreement items.** Remove unclear pairs or adjudicate them with a senior reviewer. → *Expect:* no training row contains `tie`, `both_bad`, or unresolved disagreement.
6. **Validate dataset shape.** Save JSONL rows as `{"prompt": "...", "chosen": "...", "rejected": "...", "metadata": {...}}`. → *Expect:* a script parses every row and confirms `chosen != rejected`.
7. **Split by prompt ID.** Put prompts, not individual pairs, into train/validation/test splits to avoid leakage. → *Expect:* no prompt ID appears in more than one split.

## Decision points

- Reviewer agreement below 0.7 → clarify the rubric and relabel a calibration sample.
- Many `both_bad` labels → improve candidate generation before building preferences.
- Sensitive prompts remain after redaction → use a local labeling flow or remove them.
- Preference is mostly style, not correctness → add factuality checks before tuning.

## Failure modes & recovery

- **F1 Label leakage:** detect the same prompt in train and validation → resplit by prompt ID and regenerate manifests.
- **F2 Position bias:** detect reviewers favoring `response_a` disproportionately → randomize display order and store original provenance separately.
- **F3 Low agreement:** detect kappa or agreement below threshold → revise rubric, retrain reviewers, and relabel affected categories.
- **F4 PII exposure:** detect names, emails, tokens, or account IDs in prompts → redact and rerun validation before sending to tools or vendors.
- **F5 Duplicate pairs:** detect identical chosen/rejected text → drop the row or regenerate candidates.

## Verification

Run a validation script that confirms every JSONL row has nonempty `prompt`, `chosen`, and `rejected`, no unresolved labels, no duplicate prompt across splits, `chosen != rejected`, reviewer agreement on the calibration set is at least 0.7, and PII scanners report zero high-confidence findings.

## Variations

- `DPO`: store chosen/rejected pairs directly for supervised preference optimization.
- `reward model`: include scalar reviewer scores or pairwise comparisons depending on trainer requirements.
- `online preference collection`: log implicit preferences only after checking for confounders such as position, latency, and user segment.

## Safety & privacy

Preference data can encode private user needs and reviewer bias. Minimize retained user data, document policy criteria, audit sensitive categories, and do not outsource labeling until contractual and privacy controls match the data sensitivity.
