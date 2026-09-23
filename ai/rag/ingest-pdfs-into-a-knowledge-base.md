---
name: ingest-pdfs-into-a-knowledge-base
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/rag/chunk-documents-for-retrieval, ai/rag/generate-text-embeddings, ai/rag/set-up-a-vector-database]
status: draft
last_verified: 2026-09-22
---

## Goal

Ingest PDFs into a searchable knowledge base with reliable text extraction, page-level metadata, embeddings, and retrieval verification.

## Preconditions

- PDF files and permission to process their contents.
- A PDF parser or OCR pipeline, such as PyMuPDF, pdfplumber, Tesseract, or a managed document extraction service.
- A vector index and ingestion manifest format.

## Steps

1. **Inventory the PDF set.** Record file path, checksum, title, source URI, access metadata, and whether each PDF is digital text or scanned image. → *Expect:* a manifest with one row per PDF.
2. **Extract text with layout metadata.** Use text extraction for digital PDFs and OCR for scanned pages; preserve page numbers and headings where possible. → *Expect:* page-level text with extraction confidence or parser status.
3. **Quality-check extracted pages.** Flag pages with very low text length, OCR confidence, garbled order, or missing tables. → *Expect:* problematic pages are listed for repair or exclusion.
4. **Normalize and chunk text.** Create chunks that include title, section path, and page range in metadata. → *Expect:* each chunk maps back to exact PDF pages.
5. **Embed and index chunks.** [BRANCH: hosted embeddings | local embeddings] Generate embeddings and upsert vectors with PDF metadata. ⚠️ *Data leaves your control:* hosted OCR or embedding APIs receive PDF text or images. → *Expect:* every accepted chunk has a vector record.
6. **Add citation-friendly source links.** Store file URI, page number, and optional bounding boxes if available. → *Expect:* RAG answers can cite a page or source link.
7. **Run retrieval and citation tests.** Query known PDF facts and verify returned chunks cite the right page. → *Expect:* gold pages appear in top results.

## Decision points

- PDF is scanned or image-heavy → use OCR and inspect confidence.
- Tables are important → use a layout-aware parser or store tables separately.
- Access metadata is missing → do not index the PDF until fixed.
- Extraction quality is poor → improve parsing before embedding; embeddings cannot recover missing text.

## Failure modes & recovery

- **F1 Garbled reading order:** detect sentences or columns interleaved → switch parser or layout settings.
- **F2 OCR misses:** detect low-confidence pages or empty text → rescan at higher resolution or manual review.
- **F3 Lost page citations:** detect chunks without page ranges → fix metadata propagation before indexing.
- **F4 Duplicate PDFs:** detect same checksum or near-identical text → deduplicate before embedding.

## Verification

Run an ingestion validation job. Success means every indexed chunk has `pdf_id`, `chunk_id`, source URI, and page range; no chunk exceeds embedding limits; extraction-quality flags are resolved or excluded; and labeled PDF queries return the gold page or chunk in top 5 for at least `90%` of cases.

## Variations

- `born-digital PDFs`: use direct text extraction and preserve outlines.
- `scanned PDFs`: use OCR with confidence thresholds and manual sampling.
- `forms or tables`: extract structured fields separately from prose chunks.

## Safety & privacy

PDFs often contain contracts, financial records, medical data, or personal information. Confirm processing rights, redact or keep OCR and embeddings local for sensitive files, preserve access controls, and avoid indexing pages with unknown permissions.
