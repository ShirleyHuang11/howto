---
name: connect-an-agent-to-an-api
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent can call an external API through a typed, permission-aware tool wrapper. Success means valid requests execute, invalid or unauthorized requests are rejected, and responses are validated before the model uses them.

## Preconditions

- API documentation, credentials, rate limits, and a staging or sandbox account if writes are involved.
- A tool-calling agent runtime and a JSON Schema or typed model library.
- A test harness that can mock HTTP responses and assert outgoing requests.

## Steps

1. **Choose the smallest useful API surface.** Expose task-specific operations, not the whole API, such as `lookup_order(order_id)` instead of arbitrary HTTP. → *Expect:* the tool list contains only the endpoints needed for the workflow.
2. **Define input and output schemas.** Validate identifiers, enums, pagination, date ranges, and result fields. → *Expect:* malformed arguments fail locally with validation errors.
3. **Implement authentication and request signing outside the model.** Store credentials in environment or secret management and never expose them in prompts. ⚠️ *Data leaves your control:* API calls send user or business data to the external service; redact and minimize fields first. → *Expect:* traces contain no API keys and requests include only required fields.
4. **Add rate limits, retries, and timeouts.** Respect API `429` and `Retry-After`, cap retries, and set request deadlines. → *Expect:* transient API failures recover or fail with typed errors within the time budget.
5. **Validate and normalize API responses.** Parse JSON, check status codes, verify expected fields, and convert provider-specific errors into tool errors. → *Expect:* the model receives normalized, schema-valid data only.
6. **Gate state-changing calls.** For creates, updates, sends, or deletes, require user confirmation and idempotency keys. ⚠️ *Irreversible:* confirm the exact external account, target record, and action before executing. → *Expect:* destructive or user-visible actions do not run without approval.

## Decision points

- API action is read-only → allow execution with scoped credentials and logging.
- API action changes state → require confirmation, idempotency, and staging tests.
- API returns large result sets → paginate and summarize before adding to model context.
- API data includes PII → redact before model calls unless the task explicitly requires it.

## Failure modes & recovery

- **F1 Schema drift:** detect response validation failures after API changes → update schema and add contract tests.
- **F2 Rate limit:** detect `429` or quota headers → back off, reduce concurrency, or cache reads.
- **F3 Unauthorized call:** detect `401` or `403` → refresh credentials or narrow permissions; do not ask the model to fix secrets.
- **F4 Prompt injection from API data:** detect API text containing instructions → quote it as data and ignore embedded commands.

## Verification

Run contract tests with mocked `200`, `400`, `401`, `429`, malformed JSON, and state-changing responses. Valid reads must return normalized schema-valid data, invalid inputs must fail before HTTP, `429` must retry according to policy, secrets must not appear in traces, and write calls must remain pending until explicit confirmation is supplied.

## Variations

- `OpenAPI`: generate typed clients but still hand-curate which operations become agent tools.
- `GraphQL`: expose narrow query/mutation tools with variable validation and depth limits.
- `internal API`: use service-to-service auth and staging environments for evals.

## Safety & privacy

Medium risk because user data may be sent to external systems and write endpoints can create lasting side effects. Use least-privilege credentials, redact logs, require confirmation for writes, honor rate limits, and keep model-visible API data minimal and validated.
