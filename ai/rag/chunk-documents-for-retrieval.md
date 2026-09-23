---
name: chunk-documents-for-retrieval
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Split documents into retrieval chunks that preserve meaning, fit embedding and generation context limits, and can be evaluated for recall.

## Preconditions

- A document corpus in text, HTML, Markdown, PDF-derived text, or another parseable format.
- A tokenizer for the embedding and generation models.
- A small labeled query set with gold document sections if available.

## Steps

1. **Parse documents into structural blocks.** Preserve headings, page numbers, tables, and source IDs before chunking. → *Expect:* each block has text plus metadata such as `doc_id`, `section`, and `page`.
2. **Choose an initial token window.** Start around 300-800 tokens with 10-20% overlap for prose; use smaller chunks for FAQs and larger chunks for legal or technical sections. → *Expect:* a configured `chunk_size` and `overlap`.
3. **Chunk on semantic boundaries first.** Split by headings, paragraphs, sentences, then tokens only as a last resort. → *Expect:* chunks do not begin or end mid-sentence unless the source block is too large.
4. **Attach retrieval metadata.** Include stable `chunk_id`, `doc_id`, title, section path, page range, and source URI. → *Expect:* every chunk can be traced back to the source.
5. **Filter unusable chunks.** Remove empty, boilerplate-only, or extremely short chunks unless they carry unique facts. → *Expect:* the chunk table has no blank or duplicate boilerplate rows.
6. **Measure size distribution.** Count tokens per chunk and flag chunks exceeding model limits or below a minimum useful size. → *Expect:* a histogram and a list of outliers.
7. **Run a retrieval smoke test.** Embed chunks and test several known queries against gold sections. → *Expect:* gold chunks appear in top results for obvious queries.

## Decision points

- Answers require exact page references → keep page metadata and avoid merging across pages without ranges.
- Tables lose meaning when linearized → serialize with headers repeated or store as structured metadata.
- Chunks are too small and lose context → increase size or prepend section headings.
- Chunks are too large and retrieval is imprecise → reduce size or split by subheading.

## Failure modes & recovery

- **F1 Boundary loss:** detect chunks missing headings or definitions → prepend section path to chunk text.
- **F2 Overlap duplication:** detect near-identical adjacent chunks dominating results → lower overlap or deduplicate.
- **F3 Token overflow:** detect chunks above embedding limit → split with tokenizer-aware logic.
- **F4 Bad PDF text:** detect garbled order or missing tables → improve parsing or use OCR/layout extraction.

## Verification

Run a chunk audit script. Success means `100%` of chunks have stable IDs and source metadata, `0` chunks exceed the embedding token limit, fewer than `2%` are below the minimum token threshold unless allowlisted, and retrieval smoke tests return the gold section in the top 5 for at least `90%` of labeled queries.

## Variations

- `Markdown or docs`: split by headings and include heading paths.
- `PDFs`: preserve page numbers and use layout-aware extraction.
- `code`: chunk by symbols, files, and docstrings rather than prose paragraphs.

## Safety & privacy

Chunking is usually local and low risk, but chunks may expose sensitive text once indexed. Apply redaction before embeddings if using an external provider, and keep source metadata sufficient to delete or update affected chunks later.
