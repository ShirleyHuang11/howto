---
name: anonymize-a-dataset
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You remove, mask, or transform personal and sensitive fields so a dataset can be used for AI development with reduced re-identification risk.

## Preconditions

- Authorization to process the dataset and a clear purpose for the anonymized copy.
- A data dictionary or profiler that identifies direct and quasi-identifiers.
- A secure workspace; raw data should not leave approved storage.

## Steps

1. **Classify sensitive fields.** Identify direct identifiers, quasi-identifiers, free-text PII, secrets, and regulated attributes. → *Expect:* a column-level sensitivity inventory.
2. **Choose transformations by field type.** Remove direct identifiers, generalize quasi-identifiers, tokenize stable join keys, and redact free text with a PII detector plus manual sampling. → *Expect:* every sensitive field has a documented transformation.
3. **Create a reversible-token plan only if needed.** Store token maps separately with stricter access, or use one-way salted hashes when reversibility is not required. → *Expect:* the anonymized dataset does not contain raw identifiers.
4. **Run the anonymization job.** ⚠️ *Data leaves your control:* if using an external PII detection API, redact locally first or obtain approval because raw text may be sent to a third party. → *Expect:* an anonymized output table or file is produced.
5. **Scan the output for residual PII.** Use regexes, named-entity recognition, secret scanners, and sample review on free text. → *Expect:* no emails, phone numbers, addresses, access tokens, or raw ids are detected above threshold.
6. **Measure utility loss.** Compare row counts, label distribution, missingness, and model baseline performance before and after anonymization. → *Expect:* utility metrics remain within the project tolerance.
7. **Restrict and label the release.** Mark the dataset as anonymized, record methods and residual risk, and apply access controls. → *Expect:* consumers can see the anonymization version and allowed use.

## Decision points

- Dataset contains free text → combine automated PII detection with sampled human review.
- Linkage across tables is required → use stable pseudonymous tokens, not raw ids.
- Strong anonymity is legally required → consult privacy counsel; simple masking may not qualify.
- Utility drops too much → generalize less sensitive fields or create task-specific synthetic features.

## Failure modes & recovery

- **F1 Residual direct identifier:** detect email, phone, account id, or secret in output → stop release, patch detector rules, and regenerate from raw source.
- **F2 Re-identification through quasi-identifiers:** detect unique combinations such as ZIP, birth date, and gender → bucket, suppress, or add k-anonymity checks.
- **F3 Broken joins:** detect no matching rows across tokenized tables → use a consistent keyed hash or mapping service for join keys.
- **F4 Unapproved third-party processing:** detect API logs or network calls containing raw data → revoke the run, report the incident, and rerun locally.

## Verification

The anonymization job passes only if automated scanners find zero direct identifiers, k-anonymity or uniqueness checks meet the declared threshold for quasi-identifiers, row counts match expected filters, and a sampled free-text review records no raw PII leaks.

## Variations

- `structured tables`: use column suppression, bucketing, hashing, and k-anonymity checks.
- `free text`: use local NER plus regex and sampled review.
- `synthetic data`: generate replacement records only after testing that they do not memorize source rows.

## Safety & privacy

High risk because anonymization mistakes can expose people and may be irreversible after sharing. Keep raw data inside approved systems, review external API use, store token maps separately, and do not claim a dataset is anonymous without re-identification testing.
