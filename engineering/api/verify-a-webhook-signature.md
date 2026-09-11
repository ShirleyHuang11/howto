---
name: verify-a-webhook-signature
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

Verify webhook signatures so only authentic, timely provider events are accepted and processed.

## Preconditions

- The provider's signature algorithm, signed payload format, and header names are documented.
- The webhook signing secret is stored in a secret manager or local ignored environment file.
- Tests can send raw request bodies and custom headers.

## Steps

1. **Preserve the raw request body.** Configure the framework to expose the exact bytes received before JSON parsing. → *Expect:* signature tests use the same byte sequence the provider signed.
2. **Read signature headers.** Capture provider timestamp and signature headers such as `X-Hub-Signature-256` or provider-specific equivalents. → *Expect:* missing headers cause immediate rejection.
3. **Build the signed payload exactly.** Follow provider docs, often `timestamp + "." + raw_body` or just `raw_body`. → *Expect:* locally computed signatures match provider examples.
4. **Compute HMAC with the shared secret.** Use the documented digest, commonly HMAC-SHA256. → *Expect:* valid test fixtures produce the expected hexadecimal or base64 digest.
5. **Compare in constant time.** Use a timing-safe equality helper instead of normal string comparison. → *Expect:* attackers cannot learn valid signatures through timing differences.
6. **Reject stale timestamps.** Enforce a tolerance such as five minutes when the provider includes signed timestamps. → *Expect:* replayed old events fail verification.
7. **Test valid and invalid signatures.** Include changed body, changed timestamp, missing header, and stale timestamp cases. → *Expect:* only the valid fixture reaches event processing.

## Decision points

- Provider offers an official SDK verifier → use it unless raw-body integration makes it unsuitable.
- Multiple active secrets during rotation → try current and previous secrets, then remove old secret after provider cutover.
- No timestamp is signed → rely on idempotency and provider event IDs to reduce replay impact.
- Body parsers mutate whitespace → verify before parsing or use raw-body middleware.

## Failure modes & recovery

- **F1 Raw body mismatch:** detect valid provider events rejected → inspect middleware order and disable body mutation for the route.
- **F2 Wrong secret:** detect all signatures failing after deploy → verify secret name, environment, and rotation state.
- **F3 Replay accepted:** detect old event processed again → enforce timestamp tolerance and event-ID uniqueness.
- **F4 Timing-unsafe comparison:** detect normal equality in code review → replace with `crypto.timingSafeEqual` or equivalent.

## Verification

Signature verification unit tests exit 0 for valid, invalid-body, invalid-header, missing-header, and stale-timestamp fixtures; an invalid signed request returns non-2xx and does not insert a webhook event.

## Variations

- `GitHub`: compute `sha256=` plus HMAC over the raw body and compare to `X-Hub-Signature-256`.
- `Stripe`: use the official webhook construct/verify helper with the raw request body.
- `Node.js`: convert compared strings to equal-length buffers before `crypto.timingSafeEqual`.

## Safety & privacy

Medium risk because failed verification can allow forged actions or block real provider events. Keep signing secrets out of logs, rotate on exposure, allow narrow timestamp tolerance, and verify before trusting any payload field.
