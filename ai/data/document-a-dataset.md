---
name: document-a-dataset
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1h
risk: low
prerequisites: [ai/data/compute-summary-statistics]
status: draft
last_verified: 2026-09-22
---

## Goal

You create a dataset card or README that makes the dataset's source, intended use, limitations, schema, and evaluation suitability clear to humans and agents.

## Preconditions

- The dataset or a representative sample.
- Summary statistics and schema information, such as `ai/data/compute-summary-statistics`.
- Knowledge of collection method, consent or license, update cadence, and allowed uses.

## Steps

1. **Record dataset identity.** Write name, version, owner, creation date, source, license, and contact. → *Expect:* the document clearly identifies this dataset version.
2. **Describe collection and processing.** Include sampling, filters, labeling process, preprocessing, anonymization, and known transformations. → *Expect:* readers can trace how raw data became the released dataset.
3. **Document schema and splits.** List columns, types, units, nullable fields, split logic, row counts, and label distribution. → *Expect:* schema and split information matches machine-readable metadata.
4. **State intended and prohibited uses.** Explain supported tasks, evaluation limits, and contexts where the dataset should not be used. → *Expect:* misuse risks are explicit.
5. **Summarize quality and bias checks.** Include missingness, duplicates, coverage gaps, annotator agreement, and segment-level limitations. → *Expect:* users see both strengths and known weaknesses.
6. **Add privacy and governance notes.** Describe PII handling, retention, access controls, and takedown or deletion contacts. → *Expect:* governance expectations are visible before use.
7. **Validate the documentation against metadata.** Run a script that compares documented row counts, columns, version id, and splits to the actual dataset manifest. → *Expect:* documentation is consistent with the dataset.

## Decision points

- Dataset will be public → include license, consent basis, privacy review, and examples only after redaction.
- Dataset is for internal model evals → emphasize split stability, leakage risks, and update policy.
- Dataset contains human labels → document annotator instructions, quality control, and disagreement handling.
- Dataset has known coverage gaps → state them plainly and add segment metrics where available.

## Failure modes & recovery

- **F1 Stale documentation:** detect row counts or schema mismatch → regenerate stats and update the dataset card before release.
- **F2 Missing license:** detect unknown reuse rights → block sharing until legal basis is clarified.
- **F3 Hidden preprocessing:** detect undocumented filters or label transformations → add pipeline provenance and rerun verification.
- **F4 Overbroad intended use:** detect claims beyond collected evidence → narrow the use statement and list unsupported contexts.

## Verification

A documentation check passes only if the dataset card contains required sections for source, version, schema, splits, intended use, limitations, privacy, and contact, and a metadata comparison script confirms documented row counts and columns match the dataset manifest.

## Variations

- `dataset card`: best for ML datasets shared across teams or publicly.
- `README`: suitable for small internal datasets with a separate machine-readable manifest.
- `model eval set`: include prompt format, grading rubric, leakage exclusions, and frozen-version policy.

## Safety & privacy

Low risk, but documentation can accidentally reveal sensitive source details or examples. Redact sample records, suppress tiny cohorts, and avoid claiming privacy guarantees that were not tested.
