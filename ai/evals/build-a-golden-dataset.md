---
name: build-a-golden-dataset
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

You create a high-quality golden dataset with carefully reviewed labels for model evaluation and regression testing. The dataset is small enough to maintain and trustworthy enough to gate releases.

## Preconditions

- A task definition, label schema, and source pool of examples.
- At least one qualified human reviewer, preferably two for subjective tasks.
- A versioned storage location for examples, labels, and review notes.

## Steps

1. **Write labeling guidelines.** Define labels, edge cases, examples, and what reviewers should do when uncertain. → *Expect:* reviewers can label the same item consistently.
2. **Select candidate examples.** Stratify by category, difficulty, customer segment, and known failures. → *Expect:* a balanced candidate pool larger than the final golden set.
3. **Label independently.** Have two reviewers label a subset or all items without seeing model outputs when possible. → *Expect:* labels include reviewer id and timestamp.
4. **Measure agreement.** Compute agreement such as Cohen's kappa for categorical labels or correlation for scores. → *Expect:* disagreement hotspots are visible.
5. **Adjudicate conflicts.** Resolve disagreements and document the rationale in an `adjudication_note`. → *Expect:* each golden item has one final label and provenance.
6. **Validate and freeze.** Run schema checks, duplicate checks, and hash the final file. → *Expect:* `golden_v001.jsonl` is valid, versioned, and reproducible.

## Decision points

- Inter-annotator agreement low → revise guidelines before adding more examples.
- Labels depend on current policy → include policy version and update labels only through a new dataset version.
- Dataset grows unwieldy → keep a golden core and move exploratory cases to a larger eval set.

## Failure modes & recovery

- **F1 Label leakage:** detect expected answers in model prompt → separate answer keys and audit prompt construction.
- **F2 Reviewer bias:** detect labels influenced by model names → blind outputs and randomize order.
- **F3 Stale labels:** detect product policy changed → fork a new dataset version and preserve the old one for history.
- **F4 Duplicate near-matches:** detect repeated inputs → deduplicate or mark as intentional variants.

## Verification

The final JSONL validates against schema, has unique ids, records source and label provenance for every item, reaches the required agreement threshold before adjudication, and has a saved SHA-256 hash. A loader can sample 10 rows and reproduce labels without external state.

## Variations

- `classification`: optimize for label balance and clear confusion pairs.
- `rag`: include gold documents and acceptable answer facts.
- `safety`: require expert adjudication for severe policy cases.

## Safety & privacy

Golden data is often copied widely. Remove PII and secrets, document licensing, restrict access for sensitive domains, and avoid putting confidential raw user content into public repositories.
