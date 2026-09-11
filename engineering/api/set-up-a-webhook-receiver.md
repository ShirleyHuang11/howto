---
name: set-up-a-webhook-receiver
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Expose an HTTPS endpoint that receives provider webhooks, verifies authenticity, stores events idempotently, and processes them reliably.

## Preconditions

- Provider webhook documentation and signing secret are available.
- The application has a public HTTPS URL or local tunnel for development.
- A database table or queue exists for event processing.

## Steps

1. **Create the receiver route.** Add a `POST /webhooks/provider-name` endpoint with raw-body access if signatures require it. → *Expect:* the route accepts provider test requests.
2. **Verify the signature first.** Validate timestamp and HMAC or provider SDK signature before parsing trusted fields. → *Expect:* invalid signatures return `400` or `401` and produce no side effects.
3. **Parse and validate the event.** Check event ID, type, API version, and required payload fields. → *Expect:* malformed events are rejected cleanly.
4. **Persist idempotently.** Insert the provider event ID into a table with a unique constraint before processing. → *Expect:* duplicate deliveries do not duplicate side effects.
5. **Return quickly.** Acknowledge valid receipt with `2xx` after durable storage, then process asynchronously if work is slow. → *Expect:* provider retries are minimized.
6. **Handle unknown event types.** Store and acknowledge harmless unknown events while alerting if needed. → *Expect:* new provider event types do not break delivery.
7. **Test with provider tooling.** Use the provider CLI or dashboard to send a signed test event. → *Expect:* the app records the event and processing result.

## Decision points

- Processing takes more than a few seconds → enqueue a job and return after durable insert.
- Provider requires raw request body → disable JSON body mutation for that route.
- Event ordering matters → store sequence or timestamp and process with ordering rules.
- Local development → use a tunnel such as `ngrok` or provider CLI forwarding.

## Failure modes & recovery

- **F1 Signature mismatch:** detect every webhook failing verification → confirm raw body handling, secret, timestamp tolerance, and header name.
- **F2 Duplicate delivery:** detect repeated provider event IDs → make insert idempotent and skip already-processed events.
- **F3 Slow acknowledgement:** detect provider retrying timeouts → move work to a queue and respond faster.
- **F4 Poison event:** detect job repeatedly failing on one payload → dead-letter it with event ID and sanitized error context.

## Verification

A signed test webhook from provider tooling returns `2xx`, `SELECT count(*) FROM webhook_events WHERE provider_event_id = '<test-id>';` returns 1 after duplicate delivery, and invalid-signature tests return non-2xx with no stored event.

## Variations

- `Stripe`: use `stripe listen` locally and verify with `stripe.webhooks.constructEvent`.
- `GitHub`: validate `X-Hub-Signature-256` with the shared secret.
- `Serverless`: ensure raw body access is configured before framework JSON parsing.

## Safety & privacy

Medium risk because forged webhooks can trigger business actions. Verify signatures before trust, store only needed payload data, redact secrets, and use least-privilege processing credentials.
