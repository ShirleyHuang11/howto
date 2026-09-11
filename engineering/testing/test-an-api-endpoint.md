---
name: test-an-api-endpoint
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [engineering/run-the-test-suite]
status: draft
last_verified: 2026-09-11
---

## Goal

Add an automated test for an API endpoint that verifies request validation, response status and body, authentication behavior, and persisted side effects where relevant.

## Preconditions

- The API route and expected contract are known.
- A test client, local server, or HTTP runner is available.
- Test authentication and data stores use disposable credentials and data.

## Steps

1. **Identify the contract.** Record method, path, required auth, request body, response schema, and side effects. → *Expect:* the test has explicit success and failure expectations.
2. **Set up a test client.** [BRANCH: FastAPI | Express | Rails] Use the framework test client or start the app on a local test port. → *Expect:* requests do not hit a production host.
3. **Seed required data.** Create only the user, records, or permissions needed for the endpoint. → *Expect:* the endpoint can run from a known state.
4. **Test the success path.** Send a valid request and assert status code, content type, and response body fields. → *Expect:* the endpoint returns the documented success response.
5. **Assert side effects.** Query the test database or dependency to confirm created, updated, or deleted state. → *Expect:* persisted state matches the response.
6. **Test validation failures.** Send missing or invalid fields. → *Expect:* the endpoint returns the expected 4xx status and error shape.
7. **Test auth behavior.** Send no token or insufficient permissions. → *Expect:* the endpoint returns 401 or 403 without performing the side effect.
8. **Run the endpoint tests.** Execute the targeted test file. → *Expect:* all endpoint cases pass locally and in CI.

## Decision points

- Endpoint calls a third party → mock the provider at the adapter boundary or use a sandbox.
- Endpoint is read-only → focus on filtering, authorization, status, and response schema.
- Endpoint streams or uploads files → assert headers, content length, and stored object metadata.

## Failure modes & recovery

- **F1 Test hits wrong host:** detect requests to staging or production URLs → use framework test clients or enforce localhost base URLs.
- **F2 Auth bypass in test:** detect direct handler calls that skip middleware → use a request path that includes auth middleware.
- **F3 Schema drift:** detect response fields changed unexpectedly → update either the endpoint contract or the test intentionally.
- **F4 Dirty database state:** detect duplicate keys or unexpected rows → wrap tests in transactions or reset tables.

## Verification

Run the endpoint test command, for example `pytest tests/api/test_orders.py -q` or `npm test -- orders.api.test.ts`; it exits 0, includes at least one success case and one auth or validation failure case, and CI passes with the same tests.

## Variations

- `FastAPI`: use `TestClient` or `httpx.AsyncClient` with dependency overrides for test services.
- `Express`: use `supertest` against the app object and a test database.
- `Rails`: use request specs and assert response JSON plus database changes.

## Safety & privacy

Medium risk because API tests can mutate data if pointed at the wrong environment. Use disposable databases, synthetic tokens, localhost or in-process clients, and never log real authorization headers.
