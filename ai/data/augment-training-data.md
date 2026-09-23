---
name: augment-training-data
domain: ai
subdomain: data
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

You create additional training examples that improve generalization without corrupting labels, leaking evaluation data, or shifting the dataset away from the real task distribution.

## Preconditions

- A clean training dataset with separate validation/test sets already held out.
- A target failure mode or minority class the augmentation should address.
- Augmentation methods appropriate to the data type, such as text paraphrases, image transforms, audio perturbations, or tabular synthesis.
- Metrics that compare baseline and augmented training runs.

## Steps

1. **Define the augmentation objective.** Name the gap you are trying to fix: class imbalance, robustness to typos, lighting variation, phrasing diversity, or rare intents. → *Expect:* each augmentation maps to a measurable eval slice.
2. **Freeze validation and test data.** Apply augmentation only to the training split. → *Expect:* no augmented derivative of a validation or test example appears in training.
3. **Choose label-preserving transforms.** [BRANCH: text | image | audio | tabular] Use transformations that should not change the true label, such as paraphrase, crop, noise, or unit-preserving perturbation. → *Expect:* transformed examples retain valid labels by design.
4. **Generate augmented examples.** Use deterministic seeds and record source example IDs, transform names, parameters, and generator model if any. ⚠️ *Data leaves your control:* if an external LLM or API generates augmentations from private data, redact or obtain approval first. → *Expect:* every synthetic example has provenance metadata.
5. **Filter low-quality augmentations.** Remove examples that fail schema checks, duplicate existing examples, change labels, contain artifacts, or violate policy. → *Expect:* accepted augmentations pass validation and manual spot checks.
6. **Balance augmentation volume.** Limit synthetic-to-real ratios so generated examples do not dominate the empirical distribution. → *Expect:* class and source distributions are within configured bounds.
7. **Train baseline and augmented models.** Keep architecture, seeds, and training budget comparable. → *Expect:* metric changes can be attributed to augmentation.
8. **Evaluate on untouched real data.** Compare overall metrics, target slices, calibration, and subgroup performance. → *Expect:* augmentation improves the intended slice without hurting core metrics beyond tolerance.

## Decision points

- Augmented examples fail label checks → discard the transform or add human review.
- Validation improves but test or real-world slice worsens → reduce augmentation or make it more realistic.
- Synthetic data dominates training → cap ratio or reweight examples.
- External generator sees sensitive data → switch to local generation or redact inputs.

## Failure modes & recovery

- **F1 Label drift:** detect transformed examples whose true label changes → tighten transform rules and relabel or discard affected examples.
- **F2 Evaluation leakage:** detect augmented training examples derived from validation/test rows → purge and rebuild splits from raw data.
- **F3 Distribution shift:** detect degraded performance on real validation data → reduce unrealistic augmentation.
- **F4 Duplicate inflation:** detect near-duplicates dominating batches → deduplicate by hashes or embeddings.
- **F5 Synthetic bias:** detect subgroup metric regressions → stratify augmentation and audit generated content.

## Verification

Run an augmentation audit that confirms all augmented examples derive only from training IDs, schema validation passes, duplicate or near-duplicate rate is below threshold, synthetic-to-real ratio stays within budget, and the augmented model improves the target eval slice while overall and subgroup metrics remain within allowed regression limits.

## Variations

- `text`: paraphrase, typo injection, back-translation, or templating; verify semantic label preservation.
- `image`: crop, flip, color jitter, blur, or noise; avoid transforms that change the class.
- `tabular`: use SMOTE or generative models cautiously and validate feature constraints.

## Safety & privacy

Medium risk because augmentation can leak private examples to generators or amplify bias. Use only training data, record provenance, review sensitive data before external APIs, and evaluate on untouched real examples before shipping.
