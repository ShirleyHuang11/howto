---
name: set-up-a-reverse-proxy
domain: engineering
subdomain: deploy
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

You put a reverse proxy in front of an application so public traffic terminates at the proxy, forwards to the correct upstream, and returns healthy responses over HTTPS.

## Preconditions

- A running application on an internal address such as `127.0.0.1:3000` or a private service DNS name.
- DNS for the public hostname points at the proxy host or load balancer.
- Shell access to the proxy host and permission to reload the proxy service.
- A TLS certificate path or an ACME client such as Certbot already available.

## Steps

1. **Confirm the upstream is reachable locally.** Run `curl -fsS http://127.0.0.1:3000/health` from the proxy host. → *Expect:* exit 0 and a healthy response body such as `ok`.
2. **Install the proxy package.** [BRANCH: Nginx | Caddy | Apache] For Nginx on Debian/Ubuntu, run `sudo apt-get update && sudo apt-get install -y nginx`. → *Expect:* `nginx -v` prints a version and `systemctl status nginx` shows the service installed.
3. **Create the site configuration.** Write a server block mapping `example.com` to the upstream, including `proxy_set_header Host $host`, `X-Real-IP`, `X-Forwarded-For`, and `X-Forwarded-Proto`. → *Expect:* the config contains one public `server_name` and one upstream target.
4. **Enable TLS.** [BRANCH: managed certificate | existing certificate] With Certbot, run `sudo certbot --nginx -d example.com`; with existing certs, configure `ssl_certificate` and `ssl_certificate_key`. → *Expect:* the hostname has a valid certificate chain and the proxy listens on port 443.
5. **Validate the proxy config before reload.** Run `sudo nginx -t`. → *Expect:* `syntax is ok` and `test is successful`.
6. **Reload the proxy without dropping connections.** Run `sudo systemctl reload nginx`. → *Expect:* the command exits 0 and `systemctl is-active nginx` prints `active`.
7. **Verify headers and status through the public route.** Run `curl -fsSI https://example.com/health`. → *Expect:* HTTP status is 200 and response headers come from the proxied application path.
8. **Check proxy logs for routing errors.** Run `sudo tail -n 100 /var/log/nginx/error.log`. → *Expect:* no new `connect() failed`, `upstream timed out`, or certificate errors for the hostname.

## Decision points

- Upstream is on the same host → proxy to `127.0.0.1:<port>` and keep the app port firewalled from the internet.
- Upstream is in Kubernetes or another private network → proxy to a stable internal service DNS name, not a pod IP.
- WebSocket or streaming endpoint present → add HTTP/1.1 upgrade headers and disable buffering where required.
- Multiple apps on one host → use one virtual host per `server_name` and avoid catch-all routing to sensitive services.

## Failure modes & recovery

- **F1 Bad gateway:** detect HTTP 502 or `connect() failed` in proxy logs → verify the upstream address, port, process health, and local firewall rules.
- **F2 Redirect loop:** detect repeated 301/302 between HTTP and HTTPS → ensure the app trusts `X-Forwarded-Proto` and only one layer performs canonical redirects.
- **F3 TLS failure:** detect `curl: (60)` or browser certificate warnings → reissue the certificate for the exact hostname and verify the full chain.
- **F4 Client IP lost:** detect all app requests coming from `127.0.0.1` → configure forwarded headers in the proxy and trusted proxy settings in the app.

## Verification

`curl -fsS -o /dev/null -w '%{http_code}\n' https://example.com/health` returns `200`, `sudo nginx -t` exits 0, and the proxy service remains `active` after reload.

## Variations

- `Caddy`: define `example.com { reverse_proxy 127.0.0.1:3000 }`; Caddy obtains and renews certificates automatically.
- `Traefik`: configure routers, services, and middlewares through labels or CRDs; verify with the Traefik dashboard and `curl`.
- `Kubernetes Ingress`: use an Ingress controller instead of host-level Nginx; verify `kubectl describe ingress` and external HTTP status.

## Safety & privacy

Medium risk because proxy mistakes can expose internal services or take the public site offline. Do not route catch-all hosts to admin apps, keep private upstream ports firewalled, avoid logging secrets in query strings, and require review before changing production TLS or routing rules.
