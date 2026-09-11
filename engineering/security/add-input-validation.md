---
name: add-input-validation
domain: engineering
subdomain: security
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

You validate untrusted input at system boundaries so invalid or malicious data is rejected before it reaches business logic, storage, or downstream services.

## Preconditions

- The endpoint, CLI, job, or message consumer receiving untrusted input is identified.
- Existing tests can run locally.
- Expected input schema, size limits, and allowed formats are known.

## Steps

1. **Map every untrusted field.** Inspect request bodies, query params, headers, file uploads, queue messages, and CLI arguments. → *Expect:* a complete list of inputs for the changed boundary.
2. **Choose schema-based validation.** [BRANCH: TypeScript, use Zod/Joi/Yup | Python, use Pydantic/Marshmallow | Java, use Bean Validation | Rails/Laravel, use framework validators] → *Expect:* one maintained validator handles parsing and error reporting.
3. **Define allowlist constraints.** Require types, presence, length, enum values, numeric ranges, URL/email formats, and file MIME/size limits. → *Expect:* the schema rejects malformed and oversized data by default.
4. **Validate before side effects.** Run validation before database writes, API calls, rendering, or command execution. → *Expect:* invalid requests return 400/422 and no side effects occur.
5. **Normalize validated data.** Trim or canonicalize fields only after validation rules are explicit; avoid silently accepting dangerous variants. → *Expect:* business logic receives typed, normalized values.
6. **Add negative tests.** Include missing fields, wrong types, overlong strings, unexpected properties, injection-like strings, and boundary values. → *Expect:* tests assert rejection status and no persistence.
7. **Run tests and a manual bad-request check.** Example: `curl -s -o /dev/null -w '%{http_code}' -X POST "$URL" -H 'Content-Type: application/json' --data '{"amount":"not-a-number"}'`. → *Expect:* the command returns 400 or 422.

## Decision points

- Public API compatibility matters → add validation in warning/report-only mode first if clients may break.
- Data already persisted is invalid → add a cleanup migration before tightening database constraints.
- Free-form text is allowed → constrain length and encoding, not exact content.
- Validation duplicates database constraints → keep both; application validation improves errors, database constraints protect integrity.

## Failure modes & recovery

- **F1 Valid clients rejected:** detect increased 400/422 rates → review logs, adjust schema, or version the API.
- **F2 Validation bypass:** detect another code path writing unchecked data → move validation to a shared boundary or service layer.
- **F3 Poor error leakage:** detect responses exposing stack traces or regex internals → return generic field-level validation errors.
- **F4 Performance regression:** detect slow validation on large payloads → add size limits before parsing and benchmark schemas.

## Verification

The project test command exits 0, negative validation tests pass, and a malformed `curl` request returns 400 or 422 without creating or modifying records.

## Variations

- `GraphQL`: validate custom scalars and resolver inputs, and enforce depth/complexity limits separately.
- `gRPC`: validate generated message fields at service boundaries.
- `File uploads`: validate declared type, sniffed type, extension, size, and storage path separately.

## Safety & privacy

Medium risk because validation changes can break clients. Log only field names and error categories, not full sensitive payloads, and review public API changes before deployment.
