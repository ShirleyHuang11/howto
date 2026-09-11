---
name: set-up-a-content-security-policy
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [engineering/set-secure-http-headers]
status: draft
last_verified: 2026-09-11
---

## Goal

You deploy a Content Security Policy that blocks unexpected script execution and resource loading while preserving legitimate application behavior.

## Preconditions

- Access to web server/framework header configuration.
- A staging URL and representative browser test flows.
- Inventory of legitimate script, style, image, font, connect, frame, and worker origins.

## Steps

1. **Inventory current resource origins.** Load the app in browser devtools Network tab or run tests while capturing requests. → *Expect:* a list of origins needed by each resource type.
2. **Start with report-only mode.** Set `Content-Security-Policy-Report-Only` with conservative directives such as `default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'`. → *Expect:* violations are reported but not blocked.
3. **Add explicit directives.** Configure `script-src`, `style-src`, `img-src`, `font-src`, `connect-src`, `frame-src`, and `worker-src` based on observed legitimate origins. → *Expect:* the policy avoids broad wildcards and documents each external origin.
4. **Replace unsafe inline scripts.** Prefer nonces or hashes for required inline scripts and remove `unsafe-inline` where possible. → *Expect:* scripts still run with nonce/hash protection.
5. **Collect and triage reports.** Send reports to a report endpoint or security monitoring tool and exercise main flows. → *Expect:* violations are either expected attacks/noise or legitimate resources to explicitly allow.
6. **Switch to enforcement on staging.** Change to `Content-Security-Policy` after report-only is clean. → *Expect:* browser flows pass and unexpected scripts/resources are blocked.
7. **Verify and deploy production gradually.** Run browser tests, then deploy with monitoring. → *Expect:* production serves the enforcing CSP and error rates remain stable.

## Decision points

- App depends on inline scripts → use nonces/hashes before enforcing.
- Third-party tag manager is required → constrain it to documented domains and review tag permissions.
- Reports contain sensitive URLs → sanitize or restrict report collection.
- Legacy browser support matters → test fallback behavior and avoid relying on unsupported directives alone.

## Failure modes & recovery

- **F1 Legitimate scripts blocked:** detect console CSP errors and broken UI → add nonce/hash or explicit origin for the specific script.
- **F2 Policy too broad:** detect `*`, `data:` everywhere, or `unsafe-inline` retained → tighten one directive at a time and retest.
- **F3 Report flood:** detect high-volume duplicate reports → sample reports or filter known browser-extension noise.
- **F4 Header missing on routes:** detect CSP absent on error/static routes → set headers at the reverse proxy or CDN for all responses.

## Verification

`curl -sI https://staging.example.com/ | rg -i '^content-security-policy:'` returns the enforcing CSP header, browser tests exit 0, and an injected inline script test is blocked with a CSP console/report event.

## Variations

- `Nonce-based apps`: generate a per-response nonce and attach it to trusted scripts.
- `Static sites`: prefer build-time hashes for inline assets or move inline code into external files.
- `CDN/header service`: centralize CSP at the edge but keep app-specific origin inventories.

## Safety & privacy

Medium risk because a strict CSP can break production UI and reports may include URLs. Start report-only, avoid broad wildcards, protect report data, and require review before allowing new script origins.
