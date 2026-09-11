---
name: document-an-api-with-openapi
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Create or update an OpenAPI document that accurately describes API paths, schemas, authentication, errors, and examples, then validate it programmatically.

## Preconditions

- Endpoint behavior is implemented or designed.
- The repository has a location for API specs or generated docs.
- An OpenAPI validator such as `redocly`, `swagger-cli`, or `openapi-generator` is available.

## Steps

1. **Locate the canonical spec.** Find `openapi.yaml`, `openapi.json`, or the framework's generated spec. → *Expect:* there is one source of truth to update.
2. **Add path operations.** Document method, path parameters, query parameters, request body, responses, and tags. → *Expect:* every public endpoint has an operation ID and response status list.
3. **Define reusable schemas.** Put shared request, response, and error objects under `components.schemas`. → *Expect:* repeated shapes are referenced instead of copied inconsistently.
4. **Document authentication.** Add `components.securitySchemes` and operation-level security requirements. → *Expect:* docs show exactly which credentials or scopes are needed.
5. **Include examples.** Add realistic success and error examples with fake data. → *Expect:* generated docs are useful without exposing real customer records.
6. **Validate the spec.** Run `npx @redocly/cli lint openapi.yaml` or `npx swagger-cli validate openapi.yaml`. → *Expect:* the validator exits 0.
7. **Compare spec to implementation.** Run contract tests or generated client tests against a local server. → *Expect:* documented requests and responses match actual behavior.

## Decision points

- Spec is generated from code → update annotations/types and inspect generated diff.
- Spec is hand-written → lint and contract-test it to prevent drift.
- Endpoint is internal → still document auth, errors, and examples for maintainers.
- Breaking schema change → coordinate with API versioning.

## Failure modes & recovery

- **F1 Invalid schema reference:** detect validator error for `$ref` → fix component names and paths.
- **F2 Docs claim wrong status:** detect contract test mismatch → update implementation or spec before release.
- **F3 Missing auth documentation:** detect generated client omits auth → add security schemes and requirements.
- **F4 Sensitive example data:** detect real emails, tokens, or IDs → replace with `.example` or `.test` fake values.

## Verification

`npx @redocly/cli lint openapi.yaml` or the repository's OpenAPI validation command exits 0, and API contract tests against the documented examples pass.

## Variations

- `FastAPI`: inspect `/openapi.json` and validate the generated spec in CI.
- `Spring`: use springdoc-openapi annotations and generated spec diffing.
- `Stoplight/Redoc`: publish generated docs only after lint passes.

## Safety & privacy

Low risk, but docs can leak data or create client commitments. Use fake examples, document auth accurately, and review breaking changes before publishing external specs.
