---
name: debug-a-404-or-routing-error
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You determine whether a 404 comes from the client router, application server, reverse proxy, CDN, or storage layer, then fix the route and verify the expected response.

## Preconditions

- You know the exact URL, HTTP method, expected handler, and environment where the 404 occurs.
- You can inspect route definitions, proxy rules, deployment artifacts, and logs.
- You have a safe way to run the app locally or in staging.

## Steps

1. **Capture the exact failing request.** Record URL, method, headers that influence routing, query string, and whether the failure happens on refresh or navigation. → *Expect:* a reproducible request rather than a paraphrased path.
2. **Identify which layer returns the 404.** Run `curl -i "https://example.com/path"` and inspect `Server`, CDN headers, body shape, and request ID. → *Expect:* evidence pointing to CDN/proxy/app/client router.
3. **Check application route registration.** Search for the route with `rg "path|router|GET /path|/path" .` and list registered routes if the framework supports it. → *Expect:* the intended method and path are present or clearly missing.
4. **Check path normalization.** Compare trailing slash, base path, locale prefix, case sensitivity, and URL encoding. → *Expect:* the request path matches the route definition exactly.
5. **Check proxy and deployment mapping.** Inspect Nginx, ingress, CDN, serverless, or static hosting rewrite rules. → *Expect:* the request is forwarded to the correct service or static artifact.
6. **Add or correct the route.** Fix the route definition, rewrite rule, static fallback, or link target. → *Expect:* local or staging requests now hit the expected handler.
7. **Add a route test.** Use a framework integration test or `curl` smoke test that asserts the path and method. → *Expect:* the test fails before the fix and passes after it.

## Decision points

- 404 happens only on browser refresh for a single-page app → configure static hosting fallback to `index.html`.
- 404 happens only behind CDN → inspect cache rules, origin path, and stale negative caching.
- `GET` works but `POST` returns 404 → check method-specific routes and gateway allowed methods.
- Route exists locally but not in production → verify deployed artifact, branch, build output, and base path config.

## Failure modes & recovery

- **F1 Wrong layer debugged:** detect app logs have no request → move investigation to CDN, load balancer, or DNS.
- **F2 Stale 404 cached:** detect `Age` or cache headers on 404 → purge CDN path or invalidate the route.
- **F3 Base path mismatch:** detect app mounted under `/api` or `/app` → align client links and proxy prefixes.
- **F4 Missing static artifact:** detect route maps to a file absent from build output → fix build config and regenerate assets.

## Verification

`curl -s -o /dev/null -w '%{http_code}' "https://example.com/path"` returns the expected status, usually `200`, and the route integration or smoke test exits 0.

## Variations

- `Next.js/React SPA`: distinguish server route 404 from client-side refresh fallback.
- `Rails/Django/Laravel`: use framework route listing commands to confirm method and path.
- `Kubernetes ingress`: inspect ingress path type, rewrite target, and service backend.
- `static hosting`: configure clean URL or history API fallback rules.

## Safety & privacy

Low risk for local and staging route fixes. Be careful when changing shared proxy or CDN rules because a broad rewrite can shadow other paths. Do not paste authenticated URLs with tokens into tickets or logs.

