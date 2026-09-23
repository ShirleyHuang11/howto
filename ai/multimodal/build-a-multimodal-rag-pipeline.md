---
name: build-a-multimodal-rag-pipeline
domain: ai
subdomain: multimodal
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1d
risk: medium
prerequisites: [ai/data/validate-a-data-schema]
status: draft
last_verified: 2026-09-22
---

## Goal

You build a retrieval-augmented system that can answer questions using text, images, tables, or document pages, and you verify retrieval and answer quality with a labeled eval set.

## Preconditions

- A corpus containing text plus images, slides, scanned pages, charts, or PDFs you are authorized to process.
- Embedding, OCR, captioning, and generation models available through approved local or hosted providers.
- A vector index or hybrid search engine and a labeled set of queries with gold supporting assets.

## Steps

1. **Define supported modalities and questions.** List whether the system must retrieve text chunks, image regions, OCR text, captions, tables, or whole pages. → *Expect:* a scope document and eval query set with gold evidence ids.
2. **Extract modality-specific representations.** Run OCR for text in images, parse PDFs into pages, extract tables, and create captions or summaries for visual assets. → *Expect:* each source asset has text, metadata, and asset references.
3. **Chunk and link evidence.** Create chunks that preserve page, region, image, table, and source-document ids. → *Expect:* every retrievable unit links back to the original asset.
4. **Embed and index.** [BRANCH: text embeddings + image captions | joint multimodal embeddings] Store vectors plus metadata in a vector DB or hybrid index. ⚠️ *Data leaves your control:* hosted embedding APIs receive extracted content or images. → *Expect:* index build completes with expected document and chunk counts.
5. **Implement retrieval and reranking.** Retrieve candidates with hybrid search and optionally rerank with a cross-encoder or vision-language judge. → *Expect:* test queries return ranked evidence with source ids.
6. **Generate grounded answers.** Pass retrieved evidence and asset references to a multimodal-capable model, requiring citations to chunk or asset ids. → *Expect:* answers include citations and decline when evidence is insufficient.
7. **Evaluate retrieval and answer quality.** Measure recall@k for gold evidence, citation precision, answer correctness, and unsupported-claim rate. → *Expect:* metrics meet launch thresholds before users see the system.
8. **Add monitoring.** Log query, retrieved ids, answer citations, latency, token cost, and user feedback without storing unnecessary sensitive data. → *Expect:* production behavior can be audited and drift can be detected.

## Decision points

- Retrieval recall is low → improve chunking, OCR, captions, metadata filters, or reranking.
- Answers cite irrelevant assets → tighten citation validation and answer only from retrieved evidence.
- Images contain critical details not captured by captions → use multimodal embeddings or pass cropped images to the answer model.
- Latency or cost is too high → cache extracted representations and rerank fewer candidates.

## Failure modes & recovery

- **F1 Hallucinated citation:** detect citation id not in retrieved context → reject the answer and regenerate with citation constraints.
- **F2 OCR/caption blind spot:** detect gold visual evidence never retrieved → improve extraction, add image embeddings, or create region-level chunks.
- **F3 Index drift:** detect indexed chunk count or checksum mismatch after corpus update → rebuild index from the versioned corpus and compare manifests.
- **F4 Prompt-injection in retrieved text:** detect instructions inside documents affecting the assistant → isolate retrieved content as untrusted evidence and enforce system rules.

## Verification

The pipeline passes only if index counts match the corpus manifest, retrieval recall@5 on the labeled set is at or above the declared threshold, answer correctness meets the judge or human rubric threshold, every citation id exists in retrieved evidence, and unsupported-claim rate is below threshold.

## Variations

- `caption-mediated RAG`: caption images and index captions with text embeddings; simpler but may miss visual details.
- `joint multimodal embeddings`: embed images and text into a shared space for stronger visual retrieval.
- `document QA`: combine OCR, layout-aware chunking, table extraction, and page-image citations.

## Safety & privacy

Medium risk because multimodal corpora often contain private documents and images. Treat retrieved content as untrusted, redact sensitive data before hosted embedding or model calls, and monitor cost, latency, and prompt-injection attempts.
