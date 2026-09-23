---
name: deduplicate-a-document-corpus
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Remove exact and near-duplicate documents or chunks from a corpus so retrieval returns diverse, current, and authoritative sources.

## Preconditions

- A corpus with stable document IDs and source metadata.
- Text extraction output or chunks available for comparison.
- Rules for which copy is canonical when duplicates differ.

## Steps

1. **Normalize text for comparison.** Strip boilerplate, collapse whitespace, and standardize obvious formatting without changing the stored source. → *Expect:* each document has a normalized comparison string.
2. **Find exact duplicates.** Hash normalized text with SHA-256 or equivalent and group matching hashes. → *Expect:* exact duplicate groups are listed.
3. **Find near duplicates.** Use MinHash, SimHash, embedding similarity, or shingles to identify highly similar documents or chunks. → *Expect:* candidate groups have similarity scores.
4. **Select canonical records.** Prefer the newest, most authoritative, highest-quality, or user-approved source according to documented rules. → *Expect:* each duplicate group has one canonical ID and zero or more suppressed IDs.
5. **Mark before deleting.** Add `duplicate_of` or suppression metadata and test retrieval behavior before removing anything. → *Expect:* suppressed copies no longer crowd top results.
6. **Delete only when safe.** ⚠️ *Irreversible:* physical deletion can remove audit history; confirm backups, retention policy, and canonical mapping first. → *Expect:* only approved duplicate IDs are deleted or excluded.
7. **Re-evaluate retrieval diversity.** Measure duplicate rate in top results before and after deduplication. → *Expect:* fewer repeated sources with no recall loss.

## Decision points

- Documents differ by version date → keep latest and preserve older version if legally required.
- Near-duplicate similarity is high but metadata differs → manual review before suppression.
- Duplicate is across tenants or permissions → do not merge access scopes accidentally.
- Retrieval diversity improves but recall drops → keep duplicates suppressed at display time rather than deleted.

## Failure modes & recovery

- **F1 False duplicate:** detect different obligations or facts grouped together → raise similarity threshold and review.
- **F2 Canonical mistake:** detect old or unofficial source kept → update precedence rules and remap group.
- **F3 Access leak through merge:** detect metadata combined across tenants → deduplicate only within authorization boundaries.
- **F4 Lost provenance:** detect missing source lineage after suppression → store `duplicate_of` and original IDs.

## Verification

Run a deduplication report. Success means exact duplicate groups are identified by hash, near-duplicate groups above the threshold have canonical mappings, no canonical record violates access boundaries, top-k duplicate rate on eval queries decreases by the target amount, and recall@k does not fall beyond the allowed delta.

## Variations

- `chunk-level dedupe`: suppress repeated boilerplate chunks while keeping documents.
- `document-level dedupe`: keep one canonical document and map duplicates to it.
- `legal archive`: never delete; mark duplicates and filter them from retrieval.

## Safety & privacy

Deduplication can accidentally merge data across tenants or delete records needed for audit. Keep provenance, deduplicate within access boundaries, back up before deletion, and prefer suppression metadata until the policy is proven.
