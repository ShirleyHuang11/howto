---
name: label-a-dataset
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1d
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You produce a labeled dataset with clear guidelines, measured annotator agreement, audited quality, and a versioned label file ready for training or evaluation.

## Preconditions

- Unlabeled examples sampled from the target distribution.
- A label taxonomy with definitions, edge cases, and allowed multi-label behavior.
- A labeling tool or structured spreadsheet that records annotator, timestamp, item ID, and label.
- Privacy approval if examples contain user or proprietary data.

## Steps

1. **Define the labeling task.** Write the label set, positive and negative examples, tie-break rules, and when to choose `uncertain` or escalate. → *Expect:* annotators can label the same example from the instructions alone.
2. **Sample examples deliberately.** Include random production examples plus rare classes, edge cases, languages, and known failure modes. → *Expect:* the labeling batch represents both normal and difficult cases.
3. **Run a pilot with overlap.** Have at least two annotators label the same pilot items independently. → *Expect:* inter-annotator agreement and confusion cases are measurable.
4. **Revise guidelines from disagreements.** Clarify ambiguous labels and add examples before full labeling. → *Expect:* pilot disagreement rate drops or unresolved ambiguity is documented.
5. **Label the full batch with quality controls.** Include overlap items, gold checks, attention checks where appropriate, and escalation paths. → *Expect:* each item has required labels and quality metadata.
6. **Adjudicate disagreements.** Route conflicting labels to a senior reviewer or consensus process and preserve original labels. → *Expect:* final labels and disagreement history are both available.
7. **Validate label files.** Check allowed label values, one label per required task, no duplicate item IDs, no missing adjudications, and expected class balance. → *Expect:* the label file passes schema and consistency tests.
8. **Version and document the dataset.** Save label guidelines, sampling method, annotator agreement, adjudication rules, and label distribution. → *Expect:* training can cite an immutable label version and data card.

## Decision points

- Agreement is low after the pilot → fix taxonomy or split confusing labels before scaling.
- Class imbalance is extreme → collect or sample more minority-class examples for training or eval.
- Labels require expert judgment → use trained reviewers and smaller batches instead of crowdsourcing.
- Data contains sensitive user content → redact, minimize, or use approved internal annotators only.

## Failure modes & recovery

- **F1 Ambiguous taxonomy:** detect low agreement or frequent `uncertain` → revise definitions and relabel affected items.
- **F2 Annotator drift:** detect agreement dropping over time → add calibration rounds and refresh examples.
- **F3 Duplicate examples across splits:** detect same item ID labeled for multiple splits → deduplicate before final split.
- **F4 Gold-check failures:** detect annotator below quality threshold → review and relabel their items.
- **F5 Privacy exposure:** detect sensitive fields unnecessary for labeling → redact and regenerate batches.

## Verification

Run a label validation script that checks schema validity, duplicate item IDs equal `0`, all required items have final labels, unresolved disagreement count is `0`, annotator agreement meets the configured threshold such as Cohen's kappa or Krippendorff's alpha, and class distribution is reported with no unexpected labels.

## Variations

- `expert-labeling`: slower and costlier, best for medical, legal, safety, or domain-specific labels.
- `crowd-labeling`: useful for simple tasks, requires strong guidelines and quality checks.
- `LLM-assisted`: use a model for suggestions or pre-labeling, but keep human review and measure bias.

## Safety & privacy

Medium risk because labels can encode bias and examples may expose sensitive data. Minimize displayed fields, train annotators on privacy rules, preserve disagreement metadata, and audit subgroup label quality before training.
