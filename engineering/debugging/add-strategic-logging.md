---
name: add-strategic-logging
domain: engineering
subdomain: debugging
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

You add focused logs that explain a failure or important state transition without leaking secrets or flooding production.

## Preconditions

- The project has an existing logging library or structured logging pattern.
- You know the request, job, or code path that needs visibility.
- Log access and retention rules are understood for the target environment.

## Steps

1. **Define the question the log must answer.** Write the exact unknown, such as which branch was taken or which external status code was returned. → *Expect:* each planned log has a purpose.
2. **Use the existing logger.** Follow current patterns such as `logger.info("payment_authorized", extra={...})` or `log.Info("payment_authorized", "order_id", id)`. → *Expect:* logs are structured consistently with the codebase.
3. **Choose the lowest useful level.** Use debug for noisy development details, info for important state transitions, warning for recoverable unusual states, and error for failures needing attention. → *Expect:* production log volume remains bounded.
4. **Include correlation fields.** Add request ID, job ID, tenant ID, or trace ID plus safe business identifiers. → *Expect:* one request or job can be followed across services.
5. **Redact sensitive values.** Omit or hash tokens, passwords, session cookies, full card numbers, and raw personal data. → *Expect:* logs reveal behavior, not secrets.
6. **Exercise the path locally.** Run the failing test, curl request, or job command with logs visible. → *Expect:* the new log line appears exactly where expected.
7. **Remove or downgrade temporary noise.** Keep only logs that provide durable operational value. → *Expect:* the final change is reviewable and not chatty.

## Decision points

- Need one-time debugging only → use temporary local logs and remove them before merge.
- Need production observability → add structured logs with stable event names and bounded cardinality.
- High-cardinality fields such as raw URLs or user input → normalize, truncate, or exclude.
- Errors already have traces → add context fields rather than duplicate stack traces.

## Failure modes & recovery

- **F1 Secret leakage:** detect tokens or personal data in captured logs → remove the field, rotate exposed credentials if necessary, and purge logs if policy requires.
- **F2 Log flood:** detect large volume or cost spike → lower level, sample, or log only on state changes.
- **F3 Unsearchable message:** detect free-form strings without fields → convert to structured key-value logging.
- **F4 Missing correlation:** detect isolated logs that cannot be tied to a request → propagate request or trace IDs.

## Verification

The focused reproduction command emits the expected structured log event with safe correlation fields, existing tests still exit 0, and searching the changed files shows no logged secret names or raw credential values.

## Variations

- `OpenTelemetry`: prefer spans and attributes for request flow; keep logs linked by trace ID.
- `JSON logs`: use stable event names and key-value fields so log queries can aggregate them.
- `frontend`: avoid logging personal input to analytics; use browser console logs only temporarily.
- `serverless`: include invocation IDs and keep log volume low because cold starts and retries can multiply output.

## Safety & privacy

Medium risk because logs often reach shared systems and long retention. Treat logs as production data, redact aggressively, avoid raw payloads, and get review before adding logs around authentication, payment, health, or personal data flows.
