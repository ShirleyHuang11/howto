---
name: set-up-a-vector-database
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/rag/generate-text-embeddings]
status: draft
last_verified: 2026-09-22
---

## Goal

Create a vector database or vector-enabled table that stores embeddings, metadata, and indexes needed for reliable similarity retrieval.

## Preconditions

- Embedding vectors with known dimension and distance metric.
- A selected store, such as pgvector, Qdrant, Weaviate, Milvus, Pinecone, or another hosted vector DB.
- Access credentials and permission to create collections, tables, or indexes.

## Steps

1. **Choose the distance metric.** Match the embedding model recommendation, commonly cosine similarity, dot product, or L2 distance. → *Expect:* one metric is recorded in the index config.
2. **Create the schema.** [pgvector | hosted vector DB] Store `chunk_id`, `doc_id`, text or text pointer, metadata JSON, embedding vector, model version, and timestamps. → *Expect:* the database accepts one complete record per chunk.
3. **Create the vector index.** Use HNSW or IVFFlat where appropriate; for pgvector, create an index matching the metric and dimension. → *Expect:* nearest-neighbor queries use the vector index rather than a full scan.
4. **Add metadata indexes.** Index common filters such as tenant, document type, language, access group, and updated timestamp. → *Expect:* filtered queries stay within latency targets.
5. **Load a small sample first.** Insert 100-1,000 records and run exact or approximate nearest-neighbor queries. → *Expect:* inserts succeed and queries return ranked chunks.
6. **Load the full corpus idempotently.** Upsert by stable `chunk_id` and commit in batches. → *Expect:* rerunning ingestion updates records without duplicates.
7. **Record backup and deletion procedures.** Define how to export, restore, and delete by `doc_id` or tenant. ⚠️ *Irreversible:* deletion from a production vector store may remove retrieval coverage; confirm backups and target filters first. → *Expect:* a tested delete command or API path exists.

## Decision points

- Need relational joins and simple ops → use pgvector.
- Need large-scale managed ANN search → use a hosted vector database.
- Need strict tenant isolation → use separate collections or enforced tenant filters.
- Query latency is high → tune HNSW parameters, add metadata indexes, or reduce candidate set.

## Failure modes & recovery

- **F1 Wrong metric:** detect irrelevant nearest neighbors despite good embeddings → recreate index with the model's intended metric.
- **F2 Dimension mismatch:** detect insert failures → verify embedding model version and collection dimension.
- **F3 Missing tenant filter:** detect cross-tenant results in tests → enforce filters in the query builder and add authorization tests.
- **F4 Slow filtered search:** detect latency spikes with metadata filters → add indexes or pre-partition collections.

## Verification

Run database checks that insert, query, filter, update, and delete test records. Success means vector queries return the known nearest test vector at rank 1, metadata filters exclude unauthorized records, p95 query latency is under the configured target on sample load, and upsert by `chunk_id` produces no duplicates.

## Variations

- `pgvector`: use SQL migrations and explicit vector dimensions.
- `Qdrant or Weaviate`: define collections/classes with payload schemas and HNSW settings.
- `Pinecone or managed DB`: configure namespace, metric, replicas, and metadata filters in the provider console or API.

## Safety & privacy

Vector stores often hold sensitive derived data plus source metadata. Enforce tenant filters, encrypt at rest, avoid storing raw text if not needed, and test deletion paths before ingesting regulated content.
