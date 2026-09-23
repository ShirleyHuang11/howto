---
name: run-a-human-eval
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: [ai/evals/build-an-eval-set]
status: draft
last_verified: 2026-09-22
---

## Goal

You collect reliable human judgments on model outputs using clear instructions, blinded presentation, and measurable agreement. The result can calibrate automated judges or make a release decision.

## Preconditions

- An eval dataset and generated outputs to review.
- Reviewer guidelines, rubric, and a labeling tool or spreadsheet.
- Privacy approval for any data shown to reviewers.

## Steps

1. **Write reviewer instructions.** Include task context, rubric, examples, edge cases, and what to do when uncertain. → *Expect:* reviewers can label without asking for hidden context.
2. **Prepare blinded tasks.** Remove model names, randomize order, and avoid showing expected labels unless needed. → *Expect:* reviewers judge outputs, not providers or versions.
3. **Run a pilot batch.** Have reviewers label 10-20 items and discuss disagreements. → *Expect:* confusing rubric language is fixed before full labeling.
4. **Collect full labels.** Assign at least two reviewers for subjective tasks. ⚠️ *Data leaves your control:* external contractors must see only approved, redacted data. → *Expect:* labels include reviewer id, timestamp, and rubric fields.
5. **Measure agreement.** Compute kappa, correlation, or exact agreement by criterion. → *Expect:* reliability is reported, not assumed.
6. **Adjudicate and export.** Resolve conflicts and export final labels as JSONL or CSV for eval code. → *Expect:* each example has a final label and provenance.

## Decision points

- Agreement low → revise rubric and relabel affected examples.
- Reviewers need domain expertise → route to qualified experts rather than general annotators.
- Data is sensitive → use internal reviewers or synthetic/redacted examples.

## Failure modes & recovery

- **F1 Reviewer drift:** detect scores shift over time → insert gold checks and recalibrate reviewers.
- **F2 Unblinded bias:** detect model names or order visible → regenerate tasks with blinding.
- **F3 Ambiguous rubric:** detect many comments or disagreements → rewrite criteria and rerun pilot.
- **F4 Label export errors:** detect ids not matching eval set → validate joins before analysis.

## Verification

The exported label file validates against schema, joins to 100% of eval example ids, records reviewer provenance, and meets the required reliability threshold, such as `kappa >= 0.6` before adjudication for pass/fail labels.

## Variations

- `pairwise`: reviewers pick the better of two blinded outputs.
- `rubric scoring`: reviewers grade multiple dimensions independently.
- `expert review`: fewer examples but higher confidence for specialized domains.

## Safety & privacy

Human evals expose data to people, not just APIs. Use need-to-know access, redaction, confidentiality agreements where appropriate, and special handling for PII, minors, health, legal, or financial content.
