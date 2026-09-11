---
name: handle-api-errors-gracefully
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You turn remote API failures into predictable application behavior: retries where safe, clear user-facing messages, structured logs, and no silent data corruption.

## Preconditions

- The API client code path is identifiable and covered by at least one test.
- You know which operations are idempotent and which can create, charge, delete, or mutate data.
- Logs or tracing can record status code, method, endpoint name, and request id without secrets.

## Steps

1. **Classify expected failure categories.** List transport errors, timeouts, 4xx validation/auth errors, 429 rate limits, and 5xx upstream errors. → *Expect:* each category has a documented handling policy.
2. **Normalize errors at the client boundary.** Wrap raw library errors in an `ApiError` containing `status`, `code`, `retryable`, and a redacted message. → *Expect:* callers do not need to inspect library-specific exception types.
3. **Handle client errors without retrying.** For 400, 401, 403, and 404, return a clear branch or raise a non-retryable error. → *Expect:* invalid requests fail fast and do not multiply load.
4. **Retry only safe failures.** Retry idempotent GET/PUT/DELETE or POST requests with idempotency keys on network errors, 408, 429, and 5xx using exponential backoff with jitter. → *Expect:* logs show bounded retry attempts such as 3 tries, then a final failure.
5. **Surface actionable messages.** Map internal errors to user-safe text such as "Service temporarily unavailable" while retaining diagnostic details in logs. → *Expect:* users do not see stack traces or secret-bearing payloads.
6. **Add tests with mocked responses.** Simulate 200, 400, 401, 429, 500, and network timeout responses. → *Expect:* assertions prove retry counts, final error type, and user-facing message.
7. **Add observability fields.** Emit structured logs with endpoint label, status, duration, attempt, and upstream request id. → *Expect:* a failed request can be found in logs without exposing credentials.

## Decision points

- Operation is non-idempotent and has no idempotency key → do not auto-retry; return an explicit uncertain-state error.
- 401 appears after a token refresh → stop retrying and require re-authentication or secret rotation.
- 429 includes `Retry-After` → honor that delay within the caller's maximum wait budget.

## Failure modes & recovery

- **F1 Retry storm:** detect many identical retries or 429s → reduce concurrency, increase backoff, and add circuit breaking.
- **F2 Hidden partial success:** detect timeout after a write request → check the provider by idempotency key or operation id before retrying.
- **F3 Secret leakage in logs:** detect `Authorization`, cookies, or API keys in log output → redact centrally and rotate exposed credentials if logs left trusted storage.
- **F4 Swallowed error:** detect a fallback returning empty data after upstream failure → make the failure explicit unless stale cache behavior is intentional.

## Verification

Run the API client tests, for example `npm test -- api-errors` or `pytest tests/test_api_errors.py -q`; the command exits 0 and verifies no retry on 400, bounded retry on 500, `Retry-After` handling for 429, and redacted logs.

## Variations

- `fetch`: wrap `Response.ok` checks because `fetch()` only rejects on network failures.
- `axios`: use interceptors for normalization but keep retry policy explicit and tested.
- `Python requests/httpx`: set timeouts and catch `Timeout`, `ConnectError`, and HTTP status errors separately.

## Safety & privacy

Medium risk because error handling can duplicate writes or hide outages. Never retry unsafe mutations without idempotency, never log credentials or full personal-data payloads, and require review for payment, deletion, or account-changing API calls.
