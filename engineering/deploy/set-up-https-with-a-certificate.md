---
name: set-up-https-with-a-certificate
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

You install or enable a trusted TLS certificate for a service and verify HTTPS works with modern protocol settings. HTTP traffic redirects to HTTPS where appropriate.

## Preconditions

- The domain resolves to the service or load balancer.
- You can change web server, ingress, load balancer, or hosting platform TLS settings.
- Port 443 is reachable from the internet or intended client network.

## Steps

1. **Choose certificate management.** Prefer managed certificates from the hosting platform, load balancer, or Let's Encrypt automation over manually copied certificates. → *Expect:* a clear issuer and renewal mechanism are selected.
2. **Verify domain control.** Complete DNS or HTTP validation required by the certificate authority. [BRANCH: Let's Encrypt HTTP-01, serve `/.well-known/acme-challenge/` | DNS-01, create TXT record] → *Expect:* validation status succeeds.
3. **Issue or attach the certificate.** [BRANCH: certbot with Nginx, `sudo certbot --nginx -d <host>` | Kubernetes, create a cert-manager `Certificate` | cloud load balancer, request and attach managed certificate] → *Expect:* certificate is active and bound to the hostname.
4. **Configure TLS termination.** Ensure the web server, ingress, or load balancer listens on 443 and forwards to the app. → *Expect:* port 443 accepts TLS connections.
5. **Redirect HTTP to HTTPS.** Add a 301 redirect from port 80 unless the service intentionally supports plain HTTP internally only. → *Expect:* `curl -I http://<host>` returns a redirect to `https://<host>/`.
6. **Test certificate details.** Run `openssl s_client -connect <host>:443 -servername <host> </dev/null` or an SSL scanner. → *Expect:* the certificate chain verifies and includes the hostname.
7. **Verify app health over HTTPS.** Run `curl -fsS https://<host>/healthz` or the app's health URL. → *Expect:* HTTP 200 over HTTPS.
8. **Confirm renewal automation.** Run `certbot renew --dry-run`, inspect managed cert renewal status, or check cert-manager conditions. → *Expect:* renewal check succeeds or managed renewal is enabled.

## Decision points

- Service is behind a load balancer → terminate TLS at the load balancer unless end-to-end encryption is required.
- Wildcard certificate needed → use DNS-01 validation.
- Certificate chain fails → install intermediate chain or use managed certs.
- Internal service only → use private CA or service mesh certificates instead of public certificates.

## Failure modes & recovery

- **F1 Domain validation fails:** detect ACME authorization error → fix DNS, HTTP challenge routing, or CAA records.
- **F2 Wrong certificate served:** detect hostname mismatch in `openssl` output → check SNI, virtual host order, and load balancer listener rules.
- **F3 Mixed content in browser:** detect HTTPS page loading HTTP assets → update asset URLs and Content Security Policy.
- **F4 Renewal not configured:** detect expiring certificate or dry-run failure → fix automation before expiry and set monitoring.

## Verification

`curl -fsS https://<host>/healthz` exits 0, `curl -I http://<host>` returns a redirect to HTTPS, and `openssl s_client -connect <host>:443 -servername <host>` reports a valid certificate chain for the hostname.

## Variations

- `Nginx + certbot`: certbot can edit server blocks and install renewal timers.
- `Kubernetes cert-manager`: verify `Certificate` and `Challenge` resources with `kubectl describe`.
- `AWS ACM/CloudFront/ALB`: certificates are managed and attached to listeners or distributions.
- `Cloudflare`: distinguish edge certificates from origin certificates.

## Safety & privacy

Medium risk because TLS mistakes can expose traffic or take the site offline. Protect private keys, use managed renewal when possible, avoid logging sensitive request data during troubleshooting, and keep HTTP open only for redirects or certificate challenges.
