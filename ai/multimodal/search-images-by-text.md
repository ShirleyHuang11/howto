---
name: search-images-by-text
domain: ai
subdomain: multimodal
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Build text-to-image semantic search where queries return relevant images with measurable recall on a labeled evaluation set.

## Preconditions

- An image corpus you are allowed to index and show in search results.
- A multimodal embedding model such as CLIP/SigLIP or a hosted image-text embedding API.
- A vector index such as FAISS, pgvector, Milvus, or a hosted vector database.

## Steps

1. **Create the catalog manifest.** Store image ids, paths or object URLs, captions/metadata, license, and visibility rules. → *Expect:* every searchable image has a stable id and access policy.
2. **Generate image embeddings.** [BRANCH: local CLIP/SigLIP | hosted multimodal embeddings] Embed normalized images in batches. ⚠️ *Data leaves your control:* hosted embedding APIs receive image content and metadata. → *Expect:* one vector per allowed image and no vectors for excluded assets.
3. **Build the vector index.** Insert image ids and vectors with metadata filters. → *Expect:* index count equals the number of allowed image embeddings.
4. **Embed text queries.** Use the paired text encoder or provider text embedding model. → *Expect:* query vectors have the same dimension as image vectors.
5. **Search and filter.** Retrieve top `k` by cosine or inner product, then enforce access filters and remove duplicates. → *Expect:* each query returns ranked image ids plus similarity scores.
6. **Evaluate retrieval quality.** Use labeled query-to-image relevance pairs and compute Recall@K and nDCG@K. → *Expect:* Recall@10 meets the launch threshold, such as `>= 0.85`.

## Decision points

- Recall is low for fine-grained objects → add captions, domain-specific embeddings, or reranking.
- Results violate permissions → move access filtering into the query path and add tests with private images.
- Query language differs from captions → use multilingual embeddings or translate queries before embedding.

## Failure modes & recovery

- **F1 Embedding dimension mismatch:** detect insert or query errors → rebuild index with one model/version.
- **F2 Private image leakage:** detect forbidden ids in results → enforce metadata filters before returning results and re-run access tests.
- **F3 Duplicate near-identical results:** detect repeated assets in top K → cluster or diversify by perceptual hash.
- **F4 Index drift:** detect manifest count and index count diverge → run a reconciliation job and re-embed missing images.

## Verification

For the labeled evaluation set, the search service returns only permitted image ids, vector dimensions match the configured model, index count equals the manifest count, and Recall@10 is at least 0.85 with nDCG@10 reported.

## Variations

- `FAISS`: good local baseline; add your own persistence and access filtering.
- `pgvector`: useful when metadata and permissions live in Postgres.
- `hosted vector DB`: easier scaling; verify deletion, tenant isolation, and billing limits.

## Safety & privacy

Images may reveal people, documents, homes, or proprietary assets. Index only permitted content, store deletion tombstones, enforce access filters after every retrieval, and avoid external embeddings for confidential corpora unless approved.
