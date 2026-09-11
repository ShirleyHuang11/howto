---
name: validate-a-request-payload
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

Reject invalid API payloads before business logic runs, returning structured errors that clients can fix.

## Preconditions

- The endpoint request schema and business invariants are defined.
- A validation library or framework middleware is available.
- Tests can send HTTP requests to the endpoint.

## Steps

1. **Define the schema at the boundary.** Specify required fields, types, enums, string lengths, and array limits. → *Expect:* unknown or malformed input has a single validation path.
2. **Validate content type and body size.** Require `Content-Type: application/json` for JSON endpoints and enforce a maximum body size. → *Expect:* non-JSON or oversized requests fail before parsing deeply.
3. **Parse and validate before side effects.** Run schema validation before database writes, queue publishes, or external API calls. → *Expect:* invalid payloads leave no persistent state.
4. **Add business-rule checks.** Validate cross-field rules such as `start_at < end_at` after type validation. → *Expect:* semantically invalid requests return a client error.
5. **Return structured errors.** Include field paths and stable error codes, not stack traces. → *Expect:* clients can highlight the exact fields to fix.
6. **Test invalid cases.** Cover missing required field, wrong type, unknown enum, too-long value, and cross-field violation. → *Expect:* each case returns the documented `400` or `422` response.
7. **Keep server-side validation authoritative.** Do not rely on frontend validation alone. → *Expect:* direct API calls are still protected.

## Decision points

- Invalid syntax or wrong content type → return `400 Bad Request`.
- Semantically invalid but parseable payload → return `422 Unprocessable Content` if that is the project's convention.
- Unknown fields could be dangerous → reject them or strip them consistently.
- Validation schema is shared with clients → generate types from the same source where possible.

## Failure modes & recovery

- **F1 Mass assignment:** detect clients setting protected fields like `role` → whitelist accepted fields and add tests.
- **F2 Stack trace leak:** detect validation response exposing internals → replace raw exceptions with structured errors.
- **F3 Partial side effect:** detect invalid request that still created data → move validation before side effects and wrap writes in a transaction.
- **F4 Inconsistent clients:** detect frontend accepts what backend rejects → share schema or update generated client types.

## Verification

`pytest -q tests/test_payload_validation.py` or `npm test -- payload-validation` exits 0, and `curl -sS -o /tmp/invalid.json -w '%{http_code}' -H 'Content-Type: application/json' --data '{"bad":true}' "$BASE_URL/v1/resource"` returns the documented validation status with field-level errors.

## Variations

- `Express`: use Zod, Joi, or Ajv middleware before route handlers.
- `FastAPI`: use Pydantic models and assert generated OpenAPI matches expected schemas.
- `Rails`: use strong parameters plus model validations, keeping authorization separate.

## Safety & privacy

Medium risk because bad validation can corrupt data or expose internals. Reject protected fields, cap body sizes, redact sensitive values in validation logs, and avoid returning raw exception messages.
