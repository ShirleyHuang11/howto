---
name: paginate-through-api-results
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Retrieve all needed records from a paginated API without skipping pages, duplicating work, or ignoring provider rate limits.

## Preconditions

- The API pagination style is documented or visible in responses.
- Authentication is configured.
- The destination processing is idempotent or can resume from a checkpoint.

## Steps

1. **Identify the pagination mechanism.** Look for `next` links, cursor fields, page numbers, or offset parameters. → *Expect:* the client knows exactly which response field drives the next request.
2. **Request a bounded page size.** Use the provider's allowed `limit` or `per_page`, for example `?limit=100`. → *Expect:* each response size is predictable and within API limits.
3. **Loop until no next page exists.** Follow `next_cursor` or `Link: rel="next"` rather than guessing page counts. → *Expect:* the loop stops when the provider indicates completion.
4. **Process each item idempotently.** Upsert by stable external ID or record processed IDs. → *Expect:* rerunning the job does not duplicate downstream data.
5. **Checkpoint progress.** Save the last cursor, page token, or high-water mark after successful processing. → *Expect:* interrupted jobs resume near the failure point.
6. **Handle rate limits inside the loop.** Respect `429` and `Retry-After` before continuing. → *Expect:* the crawler slows down instead of failing permanently.
7. **Test with multiple pages.** Mock at least three pages, including an empty final page or missing next token. → *Expect:* all expected IDs are processed once.

## Decision points

- API uses cursor pagination → persist the cursor only after processing the page.
- API uses offset pagination → avoid concurrent modifications or use a stable sort and time window.
- Full sync is large → partition by date ranges and reconcile counts.
- Data must be exactly once → combine idempotent writes with a durable checkpoint.

## Failure modes & recovery

- **F1 Infinite loop:** detect same cursor repeated → stop on repeated token and alert.
- **F2 Missing last page:** detect item count lower than provider total → check stop condition and `Link` parsing.
- **F3 Duplicate downstream rows:** detect repeated external IDs → change writes to upserts and add a unique constraint.
- **F4 Rate-limit failure:** detect unhandled `429` → integrate backoff before next-page fetches.

## Verification

The pagination unit test with three mocked pages exits 0 and asserts every fixture ID is processed exactly once; a dry run logs final page completion with no next cursor remaining.

## Variations

- `RFC 5988 Link headers`: parse `Link` header values for `rel="next"`.
- `GraphQL`: loop on `pageInfo.hasNextPage` and `endCursor`.
- `Bulk APIs`: prefer provider export jobs when available for very large syncs.

## Safety & privacy

Medium risk because broad pagination can export large datasets. Use least-privilege tokens, cap date ranges for tests, avoid logging full records, and store checkpoints without secrets.
