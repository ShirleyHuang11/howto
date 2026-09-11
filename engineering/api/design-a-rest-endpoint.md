---
name: design-a-rest-endpoint
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

Design a REST endpoint with clear resource semantics, request and response schemas, status codes, authorization, and automated contract checks.

## Preconditions

- The product behavior and owning resource are defined.
- Existing API naming, authentication, and error conventions are known.
- You can run API tests locally.

## Steps

1. **Name the resource path.** Use nouns and hierarchy, for example `POST /v1/accounts/{account_id}/invoices`. → *Expect:* the path describes a resource, not an RPC verb.
2. **Choose the HTTP method.** Use `GET` for reads, `POST` for create/actions, `PATCH` for partial updates, and `DELETE` for deletion. → *Expect:* clients can infer idempotency and caching behavior.
3. **Define request and response schemas.** Specify required fields, types, examples, and stable IDs. → *Expect:* invalid payloads can be rejected before business logic runs.
4. **Define status codes and errors.** Use `201` with `Location` for create, `400` for validation, `401` for missing auth, `403` for forbidden, and `404` when appropriate. → *Expect:* each failure mode maps to a predictable response.
5. **Specify authorization.** Check caller permissions against the resource scope, not just authentication. → *Expect:* cross-tenant requests are rejected.
6. **Handle idempotency where needed.** For payment, order, or retryable creates, accept an `Idempotency-Key` header. → *Expect:* retried requests do not create duplicate side effects.
7. **Write contract tests first.** Exercise success, validation failure, auth failure, and forbidden scope. → *Expect:* tests describe the endpoint behavior before or alongside implementation.
8. **Document the endpoint.** Add OpenAPI or equivalent docs with examples. → *Expect:* generated docs and clients match implemented behavior.

## Decision points

- Operation does not fit CRUD → model it as a subresource or action endpoint, for example `POST /invoices/{id}/void`.
- Create operation is retry-prone → require idempotency keys.
- Response may grow large → include pagination from the first version.
- Field may become sensitive → omit it by default and add explicit scopes.

## Failure modes & recovery

- **F1 Verb-shaped URL:** detect paths like `/createInvoice` → rename to resource-oriented paths before release.
- **F2 Ambiguous errors:** detect every failure returning `500` or generic `400` → add structured error codes and tests.
- **F3 Authorization gap:** detect users accessing another tenant's resource → add resource-scope checks and regression tests.
- **F4 Duplicate create:** detect repeated objects after client retry → add idempotency handling.

## Verification

API contract tests exit 0, and `curl -s -o /dev/null -w '%{http_code}' -X POST "$BASE_URL/v1/accounts/$ACCOUNT_ID/invoices" ...` returns the documented success code for a valid request and documented error codes for invalid and unauthorized requests.

## Variations

- `JSON:API`: follow its envelope, relationship, and error object conventions.
- `OpenAPI-first`: update the spec before implementation and generate server/client stubs.
- `Internal APIs`: still define auth and compatibility rules, even if docs are private.

## Safety & privacy

Medium risk because API shape becomes a compatibility contract. Review authorization, avoid returning sensitive fields, document deprecation paths, and require tests for tenant isolation.
