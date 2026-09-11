---
name: mock-an-api-for-local-development
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You provide a local mock API that returns realistic responses so developers and tests can run without hitting the real service.

## Preconditions

- The real API contract is known from OpenAPI, GraphQL schema, provider docs, or captured fixtures.
- The application can point to a configurable base URL.
- Example success and error payloads are available or can be created without secrets.

## Steps

1. **Choose the mock boundary.** Decide whether to mock at HTTP level, SDK level, or test-only request interception. → *Expect:* local development and automated tests use the same intended boundary.
2. **Create realistic fixtures.** Store redacted JSON examples for success, validation error, auth error, rate limit, and server error. → *Expect:* fixtures contain no real tokens or personal data.
3. **Implement a local mock server.** [OpenAPI | Node] use Prism with `prism mock openapi.yml` or a small Express/Fastify server returning fixtures. → *Expect:* `curl http://localhost:4010/health` or the mock endpoint returns a valid response.
4. **Make the app endpoint configurable.** Add `API_BASE_URL=http://localhost:4010` to local configuration. → *Expect:* the app calls the mock without code changes.
5. **Simulate error and latency cases.** Add routes, query flags, or scenario headers such as `X-Mock-Scenario: rate_limit`. → *Expect:* developers can reproduce failure handling locally.
6. **Add contract checks.** Validate fixtures against OpenAPI/JSON Schema or generated types in CI. → *Expect:* mocks fail tests when they drift from the contract.
7. **Document the local command.** Add a package script or make target such as `npm run mock-api`. → *Expect:* a fresh checkout can start the mock with one command.

## Decision points

- API has an OpenAPI document → prefer Prism, WireMock, Mock Service Worker, or generated handlers.
- Browser app only needs front-end tests → use MSW to intercept requests in tests and Storybook.
- Behavior is stateful → use a lightweight local service or container instead of static fixtures.

## Failure modes & recovery

- **F1 Contract drift:** detect mock passing while staging fails → validate fixtures against the schema and refresh examples from non-sensitive staging data.
- **F2 Hard-coded localhost:** detect deployed app calling the mock URL → require environment-specific configuration and CI checks for production builds.
- **F3 Missing error case:** detect untested 401, 429, or 500 behavior → add scenario fixtures and tests before changing client logic.
- **F4 Secret fixture:** detect real tokens or customer data in fixtures → remove them, rotate exposed secrets if needed, and replace with synthetic data.

## Verification

Run the mock and contract tests, for example `npm run mock-api` in one terminal and `curl -sS http://localhost:4010/example | jq .`, then `npm test -- api-mock`; `curl` parses as JSON and tests exit 0.

## Variations

- `OpenAPI`: use Prism or WireMock with schema-backed examples.
- `GraphQL`: use MSW GraphQL handlers or Apollo mocks tied to operation names.
- `Python`: use `responses`, `respx`, or a FastAPI mock service.

## Safety & privacy

Low risk when local-only. Keep mock data synthetic or redacted, never commit provider credentials, and make it visually or programmatically obvious when the app is pointed at a mock service.
