---
name: set-secure-http-headers
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

You configure security-related HTTP response headers and verify they are present on real responses without breaking required browser behavior.

## Preconditions

- Access to the web app, reverse proxy, CDN, or framework middleware that sets response headers.
- A staging URL that serves representative pages.
- Knowledge of whether the app embeds frames, uses cross-origin assets, or serves downloads.

## Steps

1. **Capture the current headers.** Run `curl -sI https://staging.example.com/ | sed -n '1,40p'`. → *Expect:* the current response headers are visible for comparison.
2. **Add baseline security headers.** Set `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`, and `X-Frame-Options` or CSP `frame-ancestors`. → *Expect:* framework/proxy config contains the desired headers.
3. **Choose clickjacking behavior.** If the app should not be framed, use `frame-ancestors 'none'` or `X-Frame-Options: DENY`; if trusted embedding is required, allow only explicit origins in CSP. → *Expect:* framing policy matches product requirements.
4. **Set HSTS carefully.** Start with a modest `max-age`, then increase after HTTPS is confirmed for all subdomains; use `includeSubDomains` only when every subdomain supports HTTPS. → *Expect:* HTTPS-only behavior is enforced without stranding subdomains.
5. **Deploy to staging and inspect browser behavior.** Open representative flows and browser devtools console. → *Expect:* pages load without new blocked-resource errors except intentionally blocked behavior.
6. **Verify headers programmatically.** Run `curl -sI https://staging.example.com/ | rg -i 'strict-transport-security|x-content-type-options|referrer-policy|permissions-policy|content-security-policy|x-frame-options'`. → *Expect:* configured headers appear on the response.
7. **Roll out and monitor.** Deploy through normal CI/CD and check error logs plus frontend monitoring. → *Expect:* production serves the same headers and no spike in browser errors occurs.

## Decision points

- App has a CSP recipe planned → coordinate with `engineering/set-up-a-content-security-policy`.
- Multiple proxies set headers → configure at one authoritative layer or ensure values do not conflict.
- App must be embedded by partners → use CSP `frame-ancestors` with explicit origins, not `*`.
- HSTS preload requested → verify all subdomains first and get security approval.

## Failure modes & recovery

- **F1 Broken embeds:** detect partner iframe failures → adjust `frame-ancestors` to approved origins or revert the frame header.
- **F2 Mixed HSTS outage:** detect HTTP-only subdomain failures → remove `includeSubDomains` until every subdomain supports HTTPS.
- **F3 Missing headers on error pages:** detect `curl -I /missing` lacks headers → set headers at proxy/CDN level for all responses.
- **F4 Duplicate conflicting headers:** detect two different CSP or frame headers → remove duplicates and keep the stricter intended policy.

## Verification

`curl -sI https://staging.example.com/` returns the expected security headers, browser smoke tests pass, and production header checks match staging after deployment.

## Variations

- `Express`: use `helmet()` with explicit configuration.
- `Nginx`: use `add_header ... always;` so headers apply to error responses.
- `CDN`: set headers at the edge when multiple app services need the same baseline.

## Safety & privacy

Medium risk because headers can break embeds, downloads, or resource loading. Test representative flows, avoid wildcard frame permissions, and do not enable HSTS preload without review.
