---
name: curate-instruction-tuning-data
domain: ai
subdomain: finetuning
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

You curate instruction-tuning examples that teach the desired assistant behavior without contradictions, privacy leaks, or low-value filler. The output is a balanced, validated dataset ready for formatting.

## Preconditions

- Candidate examples from approved sources, synthetic generation, or human authoring.
- A behavior spec covering task scope, tone, refusal boundaries, and output formats.
- Review tools for quality labels, PII scanning, and duplicate detection.

## Steps

1. **Write inclusion criteria.** Define what a good instruction, context, and answer look like for the target product. → *Expect:* reviewers can accept or reject rows using a written rubric.
2. **Sample across real task types.** Include common cases, edge cases, safety boundaries, languages, and difficult examples. → *Expect:* a coverage table shows counts by category.
3. **Review answer quality.** Keep examples where the target answer is correct, concise, grounded, and follows the requested format. → *Expect:* each accepted row has a quality label or reviewer ID.
4. **Remove harmful or contradictory rows.** Drop examples that reward hallucination, policy violation, hidden chain-of-thought disclosure, or inconsistent style. → *Expect:* rejected rows have rejection reasons.
5. **Redact sensitive content.** Remove secrets, unnecessary PII, and proprietary text without training rights. → *Expect:* scanners and spot checks find no high-confidence secrets.
6. **Balance the dataset.** Avoid letting one template, source, or label dominate unless production traffic truly does. → *Expect:* category distribution is within target ranges.
7. **Create a curation report.** Save source counts, acceptance rate, rejection reasons, and known limitations. → *Expect:* another engineer can understand what behavior the dataset teaches.

## Decision points

- Synthetic examples are much cleaner than real traffic → mix with real held-out evals to avoid synthetic style overfit.
- Safety examples are rare → deliberately author boundary cases and refusals.
- Reviewers disagree often → revise rubric before scaling annotation.
- Dataset contains copyrighted or private material → remove it unless rights are explicit.

## Failure modes & recovery

- **F1 Contradictory supervision:** detect similar instructions with different desired answers → adjudicate and remove conflicts.
- **F2 Low-diversity templates:** detect high near-duplicate clusters → downsample or generate varied cases.
- **F3 Hidden PII:** detect names, emails, account IDs, or secrets → redact and rescan.
- **F4 Bad refusal data:** detect refusals for harmless prompts or compliance with unsafe prompts → relabel safety cases.
- **F5 Reviewer drift:** detect acceptance criteria changing over time → recalibrate on shared examples.

## Verification

The curated dataset passes schema checks, PII/secret scanning, duplicate thresholds, coverage minimums for required categories, reviewer agreement on calibration rows, and a random audit where accepted examples meet the written rubric at the required rate.

## Variations

- `domain expert data`: require expert review for correctness before inclusion.
- `synthetic data`: validate generated examples against a human-reviewed rubric and deduplicate aggressively.
- `multilingual tuning`: track language and locale separately and verify native-speaker quality.

## Safety & privacy

Instruction-tuning data defines model behavior. Do not train on unreviewed logs, private content, copyrighted material without rights, or examples that reward unsafe compliance. Keep rejected safety examples available for evals, not training targets.
