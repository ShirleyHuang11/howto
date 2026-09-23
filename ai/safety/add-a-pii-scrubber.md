---
name: add-a-pii-scrubber
domain: ai
subdomain: safety
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

Detect and redact or tokenize personally identifiable information before storage, logging, retrieval, or third-party model calls, with measurable recall on a labeled PII set.

## Preconditions

- A definition of PII for your product and jurisdiction, including direct and quasi-identifiers.
- A labeled PII test set with names, emails, phones, addresses, account numbers, IDs, and edge cases.
- A scrubber stack such as Microsoft Presidio, spaCy/NER plus regex, cloud DLP, or a custom detector.

## Steps

1. **Define PII categories and actions.** Map each category to `redact`, `tokenize`, `hash`, `allow`, or `review`. → *Expect:* a versioned policy file covers every regulated identifier type.
2. **Normalize text before detection.** Canonicalize Unicode, strip zero-width characters, and preserve offsets. → *Expect:* detector offsets map back to the original text.
3. **Run PII detection.** [BRANCH: local detector | cloud DLP | hybrid rules plus NER] Detect entities with type, span, and confidence. ⚠️ *Data leaves your control:* cloud DLP or hosted LLMs receive the text being scrubbed. → *Expect:* a list of detected spans with no overlaps unresolved.
4. **Apply redaction or tokenization.** Replace spans with typed placeholders such as `[EMAIL_1]` while preserving enough structure for the task. → *Expect:* scrubbed text contains placeholders and no raw detected PII spans.
5. **Protect reversible maps.** Store token maps only when needed, encrypted and access-controlled. → *Expect:* the app can recover originals only through an authorized path.
6. **Evaluate recall and leakage.** Compare scrubbed outputs with labeled truth and run regex checks for common identifiers. → *Expect:* high-risk PII recall meets the required threshold.

## Decision points

- Text must be sent to a third-party model → scrub before the call unless user consent and contract terms allow raw data.
- Recall is low for domain identifiers → add custom regex/checksum validators and labeled examples.
- Downstream task needs exact values → tokenize reversibly with strict access controls instead of deleting.

## Failure modes & recovery

- **F1 Missed identifier:** detect raw emails, phone numbers, or IDs after scrubbing → add detector rules and block release until fixed.
- **F2 Offset corruption:** detect malformed replacements or broken JSON → scrub structured fields separately or preserve spans carefully.
- **F3 Over-redaction:** detect loss of useful non-PII terms → tune entity types and confidence thresholds.
- **F4 Token map exposure:** detect reversible map in logs or broad storage → rotate keys, purge logs, and restrict access.

## Verification

On the labeled PII set, scrubbed text validates against expected placeholders, high-risk PII recall is at least 0.99, raw identifier regex scans return zero matches for blocked categories, and reversible token maps are encrypted with access tests proving unauthorized reads fail.

## Variations

- `Presidio/local NER`: strong privacy and extensibility.
- `cloud DLP`: broad built-in detectors; requires third-party data-transfer review.
- `structured JSON`: scrub field-by-field before serializing to prompts or logs.

## Safety & privacy

This is high risk because missed PII may be logged, indexed, or sent to providers. Default to local detection for sensitive data, minimize raw retention, encrypt token maps, and document exactly which data leaves your infrastructure.
