---
name: configure-cors-safely
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You configure Cross-Origin Resource Sharing so approved browser clients can call the API while untrusted origins cannot read credentialed responses.

## Preconditions

- The API routes, frontend origins, credential mode, and deployment environments are known.
- Access to framework middleware, API gateway, or reverse proxy CORS configuration.
- A staging frontend or curl/browser test path exists.

## Steps

1. **List exact allowed origins.** Include scheme, host, and port for production, staging, and local development, such as `https://app.example.com`. → *Expect:* a finite allowlist exists; no wildcard is needed for credentialed requests.
2. **Decide whether credentials are required.** If cookies or HTTP auth are used, set credentialed CORS only for trusted origins; token-only APIs may not need credentials. → *Expect:* `Access-Control-Allow-Credentials` is used only when required.
3. **Configure origin reflection safely.** Compare the incoming `Origin` header to the allowlist before echoing it; never reflect arbitrary origins. → *Expect:* approved origins receive CORS headers and unapproved origins do not.
4. **Set allowed methods and headers narrowly.** Include only required methods and request headers, and handle `OPTIONS` preflight consistently. → *Expect:* preflight requests return the expected CORS headers.
5. **Add `Vary: Origin` where origin-specific headers are returned.** Configure the proxy/framework so caches do not mix responses across origins. → *Expect:* cached responses remain origin-correct.
6. **Test approved and rejected origins.** Run `curl -i -X OPTIONS "$API_URL" -H 'Origin: https://app.example.com' -H 'Access-Control-Request-Method: POST'` and repeat with `https://evil.example`. → *Expect:* approved origin receives allow headers; unapproved origin does not.
7. **Run browser integration tests.** Exercise the frontend call path with credentials if used. → *Expect:* approved browser requests succeed and unapproved origins are blocked by the browser.

## Decision points

- API uses cookies → require exact origins, `SameSite`, CSRF protection, and no wildcard CORS.
- Public unauthenticated API → wildcard may be acceptable only for non-credentialed responses.
- Many tenant origins → store verified tenant origins and match exactly, not by loose suffix.
- CDN caches API responses → ensure `Vary: Origin` or disable caching for credentialed responses.

## Failure modes & recovery

- **F1 Wildcard with credentials:** detect `Access-Control-Allow-Origin: *` plus credentials → replace with exact origin allowlist.
- **F2 Preflight fails:** detect browser CORS error before request body is sent → add correct `OPTIONS` handler and allowed headers.
- **F3 Cache leaks origin headers:** detect wrong origin in cached response → add `Vary: Origin` and purge affected cache.
- **F4 Overbroad regex:** detect `evil-example.com` matching `example.com` → use URL parsing and exact host comparison.

## Verification

An approved-origin preflight returns the expected `Access-Control-Allow-Origin` and methods, an unapproved-origin preflight omits allow headers or returns 403, and browser tests for the trusted frontend pass.

## Variations

- `Express`: use the `cors` middleware with a function-based allowlist.
- `Django/Rails`: use maintained CORS middleware and environment-specific origin settings.
- `API Gateway/CDN`: configure CORS at the edge only if it can enforce exact origin matching and `Vary`.

## Safety & privacy

Medium risk because permissive CORS can expose authenticated API responses to malicious sites. Keep explicit origin allowlists, avoid wildcard credentials, protect cookies with `SameSite` and CSRF controls, and do not log sensitive request bodies while debugging.
