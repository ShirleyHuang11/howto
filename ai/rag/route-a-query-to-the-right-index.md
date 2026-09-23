---
name: route-a-query-to-the-right-index
domain: ai
subdomain: rag
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You choose the correct retrieval index or collection for each user query and prove routing improves relevance without leaking data across scopes.

## Preconditions

- Multiple indexes or collections with clear ownership, topic, freshness, and access rules.
- Labeled routing examples mapping queries to allowed indexes.
- A router implementation: rules, classifier, embedding similarity, or LLM router.
- Retrieval and authorization tests for each index.

## Steps

1. **Describe each index.** Record name, topic, allowed users, freshness, language, and example queries. → *Expect:* an index catalog that the router can use.
2. **Create routing labels.** Label historical or synthetic queries with one or more correct indexes and disallowed indexes. → *Expect:* a test set with `query`, `allowed_indexes`, and `gold_indexes`.
3. **Implement a first-pass router.** [BRANCH: deterministic rules | classifier | LLM router] Start with high-precision rules for obvious cases and fall back to a classifier for ambiguity. → *Expect:* each query receives ranked candidate indexes with confidence.
4. **Enforce authorization after routing.** Intersect candidate indexes with the user's permitted indexes before retrieval. → *Expect:* unauthorized indexes are never queried even if the router selected them.
5. **Retrieve and merge results.** Query selected indexes, normalize scores per index, and keep source index metadata. → *Expect:* final results identify which index each chunk came from.
6. **Evaluate routing and retrieval.** Measure routing accuracy, unauthorized-query rate, answer quality, latency, and cost. ⚠️ *Data leaves your control:* hosted LLM routers receive user queries and index descriptions; redact sensitive query fields or use local routing. → *Expect:* routing accuracy beats all-index retrieval or reduces cost while maintaining recall.
7. **Add abstention and fallback.** If confidence is low, query a safe default or ask a clarifying question. → *Expect:* ambiguous eval cases do not silently hit unrelated indexes.

## Decision points

- Indexes have strict tenant boundaries → authorization filters must override router output.
- Queries often span domains → allow multi-index routing with a cap.
- Router confidence is low → ask a clarifying question or search a broad public index only.
- Routing hurts recall → use all permitted indexes with reranking until labels improve.

## Failure modes & recovery

- **F1 Data leak by misroute:** detect restricted index queried for unauthorized user → enforce permission intersection outside the model.
- **F2 Over-narrow routing:** detect gold source in an unqueried index → lower confidence threshold or allow top-n indexes.
- **F3 Router prompt injection:** detect query text telling router to choose a restricted index → ignore user instructions that conflict with policy.
- **F4 Score mismatch across indexes:** detect one index dominating after merge → calibrate scores or rerank merged candidates.

## Verification

The router must achieve the configured routing accuracy on labeled queries, produce zero unauthorized index queries in access-control tests, and maintain end-to-end retrieval recall@5 at or above the baseline while meeting latency and cost budgets.

## Variations

- `tenant-sharded`: route by tenant id before semantic routing.
- `topic-indexes`: classify by product area, documentation set, or language.
- `freshness-routing`: prefer recent incident or changelog indexes for time-sensitive queries.

## Safety & privacy

Routing is a privacy boundary when indexes have different permissions. Do authorization outside the LLM, avoid exposing index names the user cannot access, redact sensitive queries sent to hosted routers, and log routing decisions for audit without storing raw PII unnecessarily.
