---
name: clean-a-scraped-training-corpus
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

You turn a scraped corpus into a lawful, deduplicated, filtered training dataset with measurable quality checks. The final dataset has provenance, license decisions, PII handling, and validation reports.

## Preconditions

- Raw scraped documents with source URLs, timestamps, and crawl metadata.
- A policy for allowed licenses, robots/crawl constraints, personal data, and copyrighted content.
- Tools for text extraction, language detection, deduplication, PII scanning, and schema validation.

## Steps

1. **Preserve raw data separately.** Store the original crawl read-only with manifests and checksums before cleaning. → *Expect:* raw files have stable hashes and are not modified by the cleaning pipeline.
2. **Filter by provenance and rights.** Keep only sources that your policy allows for training; remove disallowed domains, licenses, takedown-listed URLs, and unknown provenance. → *Expect:* each retained record has `source_url`, `license_status`, and `allowed_for_training=true`.
3. **Extract and normalize text.** Remove boilerplate, navigation, ads, broken markup, control characters, and duplicate whitespace while preserving useful structure. → *Expect:* extracted text passes length and character-quality thresholds.
4. **Deduplicate exact and near-duplicate content.** Use hashes for exact duplicates and MinHash or embeddings for near duplicates. → *Expect:* a duplicate report with removed record ids and cluster sizes.
5. **Detect language and content category.** Filter to intended languages and remove spam, malware instructions if disallowed, adult content if out of scope, and low-information pages. → *Expect:* retained records have language and category labels above confidence thresholds.
6. **Scan and redact PII and secrets.** Use pattern detectors and entity recognizers for emails, phone numbers, keys, tokens, addresses, and personal identifiers. → *Expect:* redaction counts by type and zero unredacted high-confidence secrets in a sample.
7. **Validate output schema and split data.** Write JSONL with stable ids, text, metadata, and split labels; split by source to avoid leakage. → *Expect:* `train`, `valid`, and `test` files validate and have no source overlap.
8. **Generate a data card.** Record sources, filters, removal counts, known limitations, and privacy decisions. → *Expect:* a dataset report with counts at each pipeline stage.

## Decision points

- Provenance or license is unknown → exclude until reviewed.
- PII rate is high → stop and review whether the corpus is appropriate for training.
- Near-duplicate rate is high → deduplicate before splitting to prevent eval leakage.
- Language detection disagrees with source metadata → sample-review and tune thresholds.
- Cleaning removes too much task-relevant structure → adjust extraction rules and rerun from raw data.

## Failure modes & recovery

- **F1 Eval leakage:** detect same source or near-duplicate in train and test → split by source/domain before deduped text shards.
- **F2 Secret retention:** detect API-key patterns after redaction → block release and expand secret scanners.
- **F3 License contamination:** detect disallowed source in retained manifest → remove all derived records and rebuild.
- **F4 Boilerplate dominates:** detect repeated navigation text in top n-grams → improve extraction or domain-specific cleanup.
- **F5 Encoding corruption:** detect replacement characters or invalid UTF-8 → re-extract from raw bytes with proper encoding detection.

## Verification

Cleaning succeeds when the pipeline emits a report showing schema validation passes, zero disallowed license records, zero known takedown URLs, no exact duplicate hashes across splits, near-duplicate similarity below the chosen threshold across train/test, and no high-confidence unredacted PII or secrets in automated scans.

## Variations

- `web corpus`: emphasize license, robots metadata, boilerplate removal, and source-level splits.
- `internal docs`: emphasize ACL preservation, PII redaction, and access-controlled storage.
- `code corpus`: scan for secrets, licenses, generated files, vendored dependencies, and repository-level split leakage.
- `multilingual`: keep language-specific quality thresholds and balanced sampling.

## Safety & privacy

Medium risk because scraped data can include personal data, copyrighted material, secrets, and disallowed content. Keep raw access restricted, honor takedowns, document provenance, redact sensitive fields, and require legal/security review before using the corpus for training.
