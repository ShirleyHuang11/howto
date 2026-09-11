---
name: debug-a-cors-error
domain: engineering
subdomain: debugging
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

You identify why a browser blocks a cross-origin request and configure the server, proxy, or client so the intended origin succeeds while unwanted origins remain blocked.

## Preconditions

- You know the browser origin, target URL, method, request headers, and whether cookies or authorization headers are used.
- You can change the API or gateway CORS configuration in a non-production environment.
- You can inspect browser DevTools network entries and run `curl`.

## Steps

1. **Capture the browser error and request details.** In DevTools, inspect the failed request and any `OPTIONS` preflight. → *Expect:* the console error names the missing or invalid CORS header.
2. **Reproduce the preflight with curl.** Run `curl -i -X OPTIONS "https://api.example.com/resource" -H "Origin: https://app.example.com" -H "Access-Control-Request-Method: POST" -H "Access-Control-Request-Headers: authorization,content-type"`. → *Expect:* a response containing appropriate `Access-Control-Allow-*` headers and a 2xx or 204 status.
3. **Check actual response headers.** Run `curl -i "https://api.example.com/resource" -H "Origin: https://app.example.com"`. → *Expect:* the non-OPTIONS response also includes `Access-Control-Allow-Origin`.
4. **Fix the allowlist precisely.** Add the exact scheme, host, and port for the frontend origin; avoid wildcard origins for credentialed requests. → *Expect:* allowed origins are explicit and unwanted origins remain absent.
5. **Handle credentials correctly.** If cookies are required, set `Access-Control-Allow-Credentials: true`, return a specific origin, and configure cookies with suitable `SameSite=None; Secure` when cross-site. → *Expect:* browser sends credentials only for the intended origin.
6. **Allow required methods and headers.** Include the actual method and request headers in preflight responses, such as `Authorization` and `Content-Type`. → *Expect:* preflight succeeds before the real request is sent.
7. **Add an automated header test.** Use an integration test or smoke script that asserts CORS behavior for allowed and denied origins. → *Expect:* allowed origin passes and disallowed origin fails.

## Decision points

- No `OPTIONS` request appears → the request may be simple; inspect the actual response headers instead.
- Preflight succeeds but real request fails → check actual response status, auth, redirects, and missing CORS headers on error responses.
- Redirect happens during preflight → remove the redirect for `OPTIONS` or point the client at the canonical URL.
- Credentials are needed → do not use `Access-Control-Allow-Origin: *`.

## Failure modes & recovery

- **F1 CORS headers only on success:** detect errors still blocked in browser → add CORS headers to error responses at the gateway or middleware layer.
- **F2 Wildcard with credentials:** detect browser error about wildcard origin and credentials → echo only approved origins and include `Vary: Origin`.
- **F3 Missing allowed header:** detect preflight error naming a request header → add that header to `Access-Control-Allow-Headers` after confirming it is safe.
- **F4 Cached bad preflight:** detect browser still failing after server fix → clear browser cache or lower `Access-Control-Max-Age` while testing.

## Verification

The curl preflight returns 2xx or 204 with the expected `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, and `Access-Control-Allow-Headers`, and a browser or Playwright test can complete the cross-origin request successfully.

## Variations

- `Express`: use the `cors` middleware with an explicit origin function and credentials only when needed.
- `Django`: configure `django-cors-headers` with `CORS_ALLOWED_ORIGINS`.
- `Nginx/API gateway`: ensure headers are added for `OPTIONS` and error responses, not just upstream 200s.
- `S3/static assets`: configure bucket CORS XML/JSON for the exact web origin and methods.

## Safety & privacy

Medium risk because overly broad CORS can expose authenticated APIs to hostile sites. Keep allowlists narrow, avoid wildcard origins with credentials, and do not log authorization headers while debugging.

