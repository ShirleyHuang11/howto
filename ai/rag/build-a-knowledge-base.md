---
name: build-a-knowledge-base
domain: ai
subdomain: rag
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

You ingest trusted documents into a versioned, searchable knowledge base that a RAG system can retrieve from with measured quality.

## Preconditions

- Approved source documents and permission to process them.
- A storage location for raw documents, parsed text, chunks, embeddings, and index metadata.
- A parser for your document types and an embedding model.
- A labeled retrieval eval set or a plan to create one.

## Steps

1. **Inventory sources.** Record owner, URL or path, document type, update cadence, access level, and retention rule. → *Expect:* a source manifest with one row per collection.
2. **Freeze a corpus version.** Assign a corpus revision id and store immutable raw inputs or content hashes. → *Expect:* every parsed output can be traced back to a source hash.
3. **Parse documents.** Extract text, headings, tables, and metadata with a parser suited to each format. → *Expect:* parsed records include `doc_id`, `section`, `text`, and source location.
4. **Chunk with metadata.** Split by semantic boundaries and token budget, preserving headings and source offsets. → *Expect:* chunks have stable `chunk_id`s and fit the chosen embedding model limits.
5. **Filter and redact.** Remove duplicates, boilerplate, secrets, and disallowed PII before embedding. → *Expect:* a scan report shows zero known secret patterns and documented PII handling.
6. **Embed and index chunks.** [BRANCH: hosted embeddings | local embeddings] ⚠️ *Data leaves your control:* hosted embedding APIs receive chunk text; use only approved data or run locally. → *Expect:* vector index count equals active chunk count.
7. **Run retrieval evaluation.** Query the index with labeled examples and compute recall@k, MRR, latency, and failed queries. → *Expect:* metrics meet your launch threshold or produce a remediation list.
8. **Publish metadata and refresh policy.** Store corpus revision, parser version, chunker version, embedding model, and index build time. → *Expect:* operators can reproduce or roll back the index.

## Decision points

- Documents contain sensitive customer data → require approval, redaction, encryption, or local-only processing.
- Retrieval fails by section boundaries → change chunking to preserve headings or parent-child chunks.
- Duplicate or stale docs dominate results → canonicalize sources and add freshness ranking.
- Eval labels are missing → create a small human-labeled set before trusting the knowledge base.

## Failure modes & recovery

- **F1 Bad parsing:** detect empty or garbled chunks → inspect parser output by file type and replace the parser for failing formats.
- **F2 Source drift:** detect indexed docs no longer matching source hashes → rebuild affected documents.
- **F3 Permission leak:** detect restricted documents returned to unauthorized users → enforce access metadata at retrieval time.
- **F4 Low retrieval quality:** detect recall@k below threshold → adjust chunking, embeddings, hybrid search, or reranking.

## Verification

A build job must prove raw source hashes are recorded, parsed chunks validate against schema, vector index count equals active chunks, access metadata is present on every chunk, and retrieval recall@5 on the labeled eval set meets the configured threshold.

## Variations

- `docs-site`: crawl public pages and preserve canonical URLs.
- `internal-wiki`: enforce per-user authorization filters during retrieval.
- `pdf-heavy`: use layout-aware extraction and table-specific handling before chunking.

## Safety & privacy

Knowledge bases can amplify data exposure. Ingest only authorized sources, preserve access controls in metadata, redact secrets before embedding, document what is sent to third-party APIs, and require review before deleting or replacing a production index.
