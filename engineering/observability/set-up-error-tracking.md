---
name: set-up-error-tracking
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

You capture unhandled exceptions and important handled errors in an error-tracking service with release, environment, and user-safe context.

## Preconditions

- You have an error-tracking project such as Sentry, Rollbar, Bugsnag, or a managed APM product.
- You have a DSN or ingest token stored in a secure secret manager.
- The application has a deployable release identifier such as a git SHA or semantic version.

## Steps

1. **Create or choose the project.** In the tracking service, create a project for the app and environment. → *Expect:* a DSN or ingest endpoint is available.
2. **Store the DSN securely.** Add it as `ERROR_TRACKING_DSN` in the environment secret store, not in source code. → *Expect:* the runtime can read the variable and the repository contains no secret value.
3. **Install the SDK.** [BRANCH: Python | Node.js] Run `pip install sentry-sdk` or `npm install @sentry/node`. → *Expect:* dependency metadata updates and the package manager exits 0.
4. **Initialize early in startup.** Configure DSN, environment, release, sample rate, and PII settings before request handlers run. → *Expect:* startup succeeds and the SDK reports enabled only when the DSN exists.
5. **Capture request context safely.** Add framework integration middleware and scrub headers, cookies, tokens, and sensitive form fields. → *Expect:* captured events include route, release, and trace context without secrets.
6. **Send a controlled test event.** Trigger a non-production test exception or call the SDK capture method in a guarded admin/debug path. → *Expect:* a test issue appears in the error-tracking project.
7. **Deploy and verify source maps or symbols.** For compiled frontend or native code, upload source maps or debug symbols during CI. → *Expect:* stack traces resolve to readable source files and line numbers.

## Decision points

- Frontend app → configure source map upload and hide public source maps when appropriate.
- Backend app → initialize before framework routes and worker queues start.
- Privacy-sensitive service → disable default PII capture and explicitly allow only safe identifiers.
- High-volume errors → set rate limits and grouping rules before production rollout.

## Failure modes & recovery

- **F1 No events arrive:** detect empty project after test error → verify DSN, network egress, environment gating, and SDK initialization order.
- **F2 Events contain secrets:** detect tokens, cookies, or request bodies in event payloads → add scrubbers and rotate exposed credentials if necessary.
- **F3 Unreadable stack traces:** detect minified or missing source frames → upload source maps or debug symbols with the release name.
- **F4 Alert noise:** detect excessive duplicate issues → tune sampling, ignore rules, or grouping fingerprints.

## Verification

A controlled test exception from the target environment appears in the error-tracking project with the expected `release` and `environment`, and the application test suite such as `pytest` or `npm test` exits 0.

## Variations

- `Sentry`: use DSN plus release uploads through `sentry-cli`.
- `Rollbar`: configure access token, environment, and person tracking policy.
- `Bugsnag`: configure API key, release stage, and app version.
- `OpenTelemetry collector`: route exception events through OTLP when your organization standardizes there.

## Safety & privacy

Medium risk because error events can include customer data and secrets. Use environment secrets, disable unnecessary PII, scrub request data, and restrict project access to engineers who need production diagnostics.
