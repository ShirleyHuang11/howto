---
name: call-a-rest-api
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Call a REST API safely from code or the terminal, inspect the response, and handle status codes without leaking credentials.

## Preconditions

- The API base URL, endpoint path, method, and authentication method are known.
- You have a non-production credential or test token.
- `curl` or an HTTP client library is installed.

## Steps

1. **Set environment variables.** Store values outside shell history, for example `export API_BASE_URL='https://api.example.com'` and `export API_KEY='replace-me'`. → *Expect:* commands can reference variables without hardcoding secrets.
2. **Build the request explicitly.** Use `curl -sS -X GET "$API_BASE_URL/v1/widgets" -H "Authorization: Bearer $API_KEY" -H "Accept: application/json"`. → *Expect:* the API returns an HTTP response instead of a local shell error.
3. **Capture status and body separately.** Run `curl -sS -o /tmp/api-body.json -w '%{http_code}\n' ...`. → *Expect:* you can distinguish HTTP errors from malformed JSON.
4. **Validate the body.** Run `jq . /tmp/api-body.json`. → *Expect:* JSON parses or the parse failure is visible.
5. **Implement the client call.** Use timeouts, explicit headers, and structured error handling in the application HTTP library. → *Expect:* network failures and non-2xx responses do not crash unpredictably.
6. **Add a test with a mocked server.** Assert method, path, headers, payload, timeout, and response parsing. → *Expect:* tests fail if the request contract changes unexpectedly.

## Decision points

- API requires a body → send `-H 'Content-Type: application/json' --data '{"name":"demo"}'`.
- Response is paginated → follow pagination links or cursor fields until completion.
- API is unstable or remote in tests → use a mock server or recorded fixture.
- Credential is production-scoped → stop and obtain a narrower test credential.

## Failure modes & recovery

- **F1 401 Unauthorized:** detect status `401` → check token value, auth scheme, and expiration.
- **F2 403 Forbidden:** detect status `403` → verify scopes and account/resource permissions.
- **F3 Timeout:** detect client timeout or connection reset → add bounded retries for safe methods and increase observability.
- **F4 Invalid JSON:** detect `jq` parse error → inspect content type and upstream error page.

## Verification

`curl -sS -o /tmp/api-body.json -w '%{http_code}' "$API_BASE_URL/v1/widgets"` returns the documented 2xx status for valid credentials, `jq . /tmp/api-body.json` exits 0, and the client unit test exits 0.

## Variations

- `Python`: use `requests` or `httpx` with `timeout=...` and `response.raise_for_status()`.
- `Node.js`: use built-in `fetch` or `undici` with an `AbortSignal` timeout.
- `Postman/Insomnia`: store secrets in environment variables, not in exported collections.

## Safety & privacy

Low risk for read-only test calls, higher for write endpoints. Do not paste real tokens into source files, redact headers in logs, and prefer sandbox credentials while developing.
