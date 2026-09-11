---
name: add-structured-logging
domain: engineering
subdomain: observability
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

You emit machine-parseable logs with consistent fields so production behavior can be searched, filtered, and correlated across requests.

## Preconditions

- The service already writes logs to stdout, stderr, or a configured log sink.
- You know the language logging library and deployment environment.
- You have a safe place to run tests and inspect sample logs.

## Steps

1. **Identify required fields.** Choose stable fields such as `timestamp`, `level`, `message`, `service`, `env`, `request_id`, `trace_id`, and domain-specific IDs. → *Expect:* a short field list exists before code changes.
2. **Select the structured format.** Use JSON lines for containerized services unless the platform requires another format. → *Expect:* each log event can be parsed as one JSON object per line.
3. **Configure the logger.** [BRANCH: Python | Node.js | Go] For Python, configure `structlog` or `python-json-logger`; for Node.js, use `pino` or `winston`; for Go, use `log/slog` or `zap`. → *Expect:* application logs are emitted through one structured logger.
4. **Add request context.** Inject request IDs and trace IDs through middleware, for example from `X-Request-Id` and W3C `traceparent`. → *Expect:* every request log line carries the same correlation identifiers.
5. **Remove ad hoc prints.** Replace `print`, `console.log`, or raw logger strings in touched request paths with structured calls. → *Expect:* logs preserve message meaning and move variable data into fields.
6. **Prevent secret leakage.** Add redaction for headers such as `Authorization`, `Cookie`, API keys, tokens, and passwords. → *Expect:* sample logs contain placeholders instead of secret values.
7. **Run tests and inspect output.** Run the service test suite and a local request such as `curl -fsS http://localhost:<port>/health`. → *Expect:* tests pass and local logs parse as valid JSON.

## Decision points

- Existing platform expects plain text → keep human-readable messages but add key-value fields supported by the log collector.
- High-cardinality values → include request IDs, but avoid indexing raw user input or unbounded payloads as labels.
- Legacy logs consumed by alerts → preserve existing message text during migration or update alerts in the same change.
- Multiple services → standardize field names across services before broad rollout.

## Failure modes & recovery

- **F1 Invalid JSON logs:** detect parser errors in the collector or `jq` failures → ensure exactly one JSON object per line and no extra prefixes.
- **F2 Missing request IDs:** detect logs without `request_id` in request paths → fix middleware ordering and background job context propagation.
- **F3 Secret exposure:** detect tokens or passwords in sample logs → add redaction tests and rotate exposed secrets if needed.
- **F4 Alert breakage:** detect log-based alerts no longer matching → update queries and validate them before deploying widely.

## Verification

`<start-service-command> 2>&1 | head -20 | jq -c . >/dev/null` exits 0 for emitted sample logs, the test suite exits 0, and a request log contains `service`, `level`, `message`, and `request_id` fields.

## Variations

- `Python`: use `structlog` or `python-json-logger` and test with `pytest`.
- `Node.js`: use `pino` with serializers and test with `npm test`.
- `Go`: use standard `log/slog` with JSON handler and test with `go test ./...`.
- `Kubernetes`: write to stdout/stderr and let the node log agent ship records.

## Safety & privacy

Medium risk because logging changes can break alerts or leak sensitive data. Redact secrets by default, avoid logging full request bodies, and coordinate changes with whoever owns dashboards and alert queries.
