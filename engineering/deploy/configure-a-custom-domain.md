---
name: configure-a-custom-domain
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You point a custom domain at the deployed service and verify DNS, routing, and HTTPS work. The service responds correctly on the new hostname without breaking the existing hostname.

## Preconditions

- You control DNS for the domain.
- The application or hosting provider supports custom domains.
- The current service hostname is healthy.
- You know whether the target is an apex domain, subdomain, or both.

## Steps

1. **Confirm the canonical hostname.** Decide whether users should use `example.com`, `www.example.com`, or another subdomain. → *Expect:* one canonical hostname and any redirects are defined.
2. **Add the domain in the hosting platform.** Enter the hostname in the provider's custom domain settings or CLI. → *Expect:* the provider returns required DNS records such as CNAME, A, AAAA, or TXT validation.
3. **Create DNS records.** Add a CNAME for subdomains or A/AAAA/ALIAS records for apex domains according to provider instructions. → *Expect:* DNS zone contains the exact records requested by the provider.
4. **Verify DNS propagation programmatically.** Run `dig +short <hostname>` or `dig +short CNAME <hostname>` from a shell. → *Expect:* output matches the provider target or expected IPs.
5. **Wait for provider validation.** Refresh the domain status in the hosting console or CLI. → *Expect:* domain status changes to verified, active, or ready.
6. **Enable or confirm HTTPS.** Ensure a certificate is issued for the hostname. → *Expect:* TLS status is active and certificate common names or SANs include the hostname.
7. **Test the new hostname.** Run `curl -I https://<hostname>` and `curl -fsS https://<hostname>/healthz` if available. → *Expect:* HTTP status is 200 or the intended redirect, and health returns 200.
8. **Configure redirects.** Redirect alternate hostnames to the canonical host with 301 or provider routing. → *Expect:* `curl -I https://<alternate-host>` shows the expected `Location` header.

## Decision points

- Apex domain needed → use provider-supported A/AAAA, ALIAS, or ANAME records; CNAME at apex is not standard DNS.
- Existing production DNS present → lower TTL before changes and keep rollback records noted.
- HTTPS validation fails → check CAA records and required TXT records.
- Multiple environments share a domain → use separate subdomains such as `staging.example.com`.

## Failure modes & recovery

- **F1 DNS points to wrong target:** detect `dig` output mismatch → correct the DNS record and wait for TTL.
- **F2 Certificate not issued:** detect browser or `curl` TLS error → verify domain ownership records and CAA allows the certificate authority.
- **F3 Redirect loop:** detect repeated 301/302 responses → align app-level and provider-level canonical host rules.
- **F4 Old hostname broken:** detect existing URL returns error → restore previous routing or keep both hostnames attached.

## Verification

`dig +short <hostname>` resolves to the provider target, `curl -I https://<hostname>` returns 200 or the intended redirect, and `curl -fsS https://<hostname>/healthz` exits 0 when the app exposes a health endpoint.

## Variations

- `Cloudflare`: orange-cloud proxy changes observed IPs; verify origin and edge TLS modes.
- `Vercel/Netlify/Render/Fly`: add domain in platform first, then copy exact DNS records.
- `Kubernetes ingress`: configure host rules and certificate issuer annotations.
- `AWS Route 53`: use ALIAS records for apex domains pointing at AWS load balancers or CloudFront.

## Safety & privacy

Medium risk because DNS mistakes can take production offline. Confirm the zone and hostname before changing records, avoid exposing internal origin hostnames when not intended, and keep previous DNS values for rollback until the new domain is stable.
