---
name: stream-a-large-api-response
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

You process a large API response incrementally so memory stays bounded and partial failures are handled without corrupting downstream data.

## Preconditions

- The upstream supports streaming, pagination, NDJSON, server-sent events, or chunked downloads.
- The consumer can process records incrementally or write to a temporary file.
- You can run a memory-aware test or command against a large fixture.

## Steps

1. **Confirm the response format.** Check headers and docs for `application/x-ndjson`, `text/event-stream`, chunked transfer, or paginated JSON. → *Expect:* the stream framing is known before implementation.
2. **Use a streaming client API.** [Node | Python] use `fetch()` with `response.body` or `httpx.stream("GET", url)` instead of reading the whole body. → *Expect:* code consumes chunks or lines incrementally.
3. **Parse at record boundaries.** Buffer incomplete chunks until a newline, SSE event, or parser token is complete. → *Expect:* split chunks do not cause JSON parse errors.
4. **Apply backpressure.** Await writes to files, queues, or databases and avoid unbounded arrays. → *Expect:* memory use remains roughly flat as record count grows.
5. **Write through a temporary destination.** For downloads, write to `file.tmp` and rename only after checksum or count validation succeeds. → *Expect:* interrupted streams do not appear as complete outputs.
6. **Handle cancellation and retry boundaries.** Track cursor, page token, byte range, or last processed id if resumable. → *Expect:* a retry can continue safely or restart from a known clean point.
7. **Test with a large fixture.** Generate or serve a fixture larger than normal memory comfort, such as 100k NDJSON records. → *Expect:* the test completes without loading all records at once.

## Decision points

- API only returns a giant JSON array → use an incremental parser such as `ijson`, `stream-json`, or switch to pagination if available.
- Processing is not idempotent → checkpoint only after downstream writes commit.
- Network drops mid-stream → discard temporary output unless a validated resume mechanism exists.

## Failure modes & recovery

- **F1 Out-of-memory:** detect OOMKilled, heap limit errors, or rising RSS → remove accumulation, lower batch size, and enforce backpressure.
- **F2 Partial record parse:** detect JSON parse errors at chunk boundaries → add a line/token buffer and parser tests with tiny chunks.
- **F3 Corrupt partial file:** detect missing checksum, short byte count, or absent final marker → delete `.tmp` output and retry.
- **F4 Duplicate records after retry:** detect repeated ids downstream → make writes idempotent or resume from the last committed checkpoint.

## Verification

Run a large-stream test such as `pytest tests/test_stream_large_response.py -q` or `npm test -- stream-large-response`; it exits 0, processes the expected record count, and asserts peak memory stays under the configured limit.

## Variations

- `NDJSON`: split on newline and parse one JSON object per line.
- `SSE`: parse `data:` events and stop on documented terminal events.
- `Paginated REST`: loop over `next` links or page tokens and commit each page.

## Safety & privacy

Medium risk because large streams often contain bulk customer or production data. Redact logs, write temporary files to protected storage, clean up partial artifacts, and avoid replaying non-idempotent downstream operations.
