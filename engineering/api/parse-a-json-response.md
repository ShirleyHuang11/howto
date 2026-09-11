---
name: parse-a-json-response
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

You parse an HTTP JSON response into typed application data, reject malformed or unexpected payloads, and keep useful diagnostics for failures.

## Preconditions

- A reachable API endpoint or captured fixture response.
- A language runtime with a JSON parser and, ideally, a schema validator such as Zod, Pydantic, JSON Schema, or serde.
- A test runner that can exercise success and failure payloads.

## Steps

1. **Capture the expected response shape.** Save a representative response with `curl -sS "$API_URL" | jq . > test/fixtures/response.json`. → *Expect:* `jq` exits 0 and the fixture is valid JSON.
2. **Define the application schema.** [TypeScript | Python] add a schema such as `z.object({ id: z.string(), status: z.enum(["ok", "error"]) })` or a `BaseModel`. → *Expect:* the schema names every field the application actually consumes.
3. **Check the HTTP status before parsing.** Read the status and body separately, for example `const res = await fetch(url); if (!res.ok) throw new ApiError(res.status, await res.text());`. → *Expect:* non-2xx responses produce an error path with status code and body excerpt.
4. **Parse JSON with a single boundary function.** Implement `parseApiResponse(body)` using `JSON.parse` or `await res.json()` inside `try/catch`. → *Expect:* invalid JSON raises a controlled parse error instead of a raw stack trace.
5. **Validate the parsed object.** Run the schema validator immediately after parsing, before business logic touches fields. → *Expect:* missing or wrong-typed fields produce a validation error that includes the field path.
6. **Return typed domain data.** Map the validated payload to the internal object and ignore unneeded remote fields. → *Expect:* callers receive a stable type independent of extra fields in the API response.
7. **Add fixture-based tests.** Test valid JSON, invalid JSON, missing required fields, and a non-2xx response. → *Expect:* each branch is covered by an assertion and the test runner exits 0.

## Decision points

- Response is larger than memory allows → use `engineering/api/stream-a-large-api-response` instead of `await res.json()`.
- API has versioned schemas → include version-specific validators and dispatch on the version field or URL.
- Fields are optional remotely but required internally → set defaults explicitly or fail validation; do not let `undefined` drift downstream.

## Failure modes & recovery

- **F1 Invalid JSON:** detect `SyntaxError`, `JSONDecodeError`, or `jq` parse failure → log request id, status, and a short body excerpt; retry only if the endpoint is known to be flaky.
- **F2 Shape mismatch:** detect schema errors such as missing `id` → update the schema or adapter after confirming the API contract changed.
- **F3 Wrong content type:** detect `Content-Type` not matching `application/json` → treat the response as an upstream error and capture the body for debugging.
- **F4 Numeric precision loss:** detect large identifiers arriving as numbers → request string IDs or parse with a big-number-safe library.

## Verification

Run the targeted parser tests, for example `npm test -- parseApiResponse` or `pytest tests/test_api_parser.py -q`; the command exits 0 and includes passing cases for valid JSON, invalid JSON, and schema mismatch.

## Variations

- `TypeScript`: use `zod`, `valibot`, or generated OpenAPI types plus runtime validation.
- `Python`: use `pydantic.model_validate_json()` or `json.loads()` followed by a Pydantic model.
- `Go`: use `json.Decoder` with `DisallowUnknownFields()` when strict contracts are required.

## Safety & privacy

Low risk because this is local parsing logic. Do not log full response bodies if they may contain tokens, payment data, personal data, or proprietary payloads; keep only redacted excerpts and request identifiers.
