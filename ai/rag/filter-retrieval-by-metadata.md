---
name: filter-retrieval-by-metadata
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [ai/rag/do-semantic-search]
status: draft
last_verified: 2026-09-22
---

## Goal

Apply metadata filters to retrieval so results match user permissions, tenant boundaries, freshness, language, document type, or other required constraints.

## Preconditions

- Chunks indexed with reliable metadata fields.
- A vector or search database that supports filtered retrieval.
- Test users or fixtures covering allowed and forbidden documents.

## Steps

1. **Define filterable metadata.** Choose fields such as `tenant_id`, `acl_group`, `language`, `doc_type`, `created_at`, and `effective_date`. → *Expect:* a documented metadata schema.
2. **Populate metadata at ingestion.** Validate required metadata before embedding or indexing each chunk. → *Expect:* chunks missing required access metadata are rejected.
3. **Build filters from trusted context.** Use authenticated user and application state, not free-form user prompt text, for authorization filters. → *Expect:* filter objects are generated server-side.
4. **Run filtered retrieval in the database.** [pgvector | hosted vector DB | search engine] Apply filters inside the query, not only after results are returned. → *Expect:* unauthorized chunks cannot appear in the candidate set.
5. **Test deny cases.** Query as users without access to known documents and assert those chunks are absent. → *Expect:* forbidden `chunk_id`s are not returned.
6. **Combine business filters carefully.** Add freshness, language, or document-type constraints without dropping required answer sources unexpectedly. → *Expect:* filter decisions are visible in traces.
7. **Monitor empty-result rates.** Track when filters remove all candidates and whether fallback behavior is appropriate. → *Expect:* empty retrieval is handled as no-answer or broadened only when safe.

## Decision points

- Filter is an authorization rule → never let the model or user override it.
- Filter is a user preference → allow broadening if results are empty and policy permits.
- Required metadata is missing → quarantine the chunk instead of indexing it.
- Filtered recall is low → inspect metadata quality before changing embeddings.

## Failure modes & recovery

- **F1 Post-filter leak:** detect unauthorized candidates in logs before post-filtering → move filter into database query.
- **F2 Missing metadata:** detect chunks with null `tenant_id` or ACL → block ingestion and backfill metadata.
- **F3 Type mismatch:** detect date or boolean filter returning wrong rows → normalize metadata types and add tests.
- **F4 Overfiltering:** detect high empty-result rate → review optional filters and user-facing fallback.

## Verification

Run authorization and metadata-filter tests. Success means forbidden fixture chunks never appear for unauthorized users, required metadata coverage is `100%` for indexed chunks, filtered recall on labeled allowed queries meets threshold, and empty-result behavior matches the configured policy.

## Variations

- `multitenant SaaS`: tenant filter is mandatory and non-overridable.
- `freshness-sensitive docs`: filter by effective date or latest version.
- `multilingual search`: filter by language or retrieve multilingual candidates before reranking.

## Safety & privacy

Metadata filtering is a core privacy control. Treat access metadata as security-critical, generate filters from trusted server context, test denial paths, and log filter traces without exposing sensitive document contents.
