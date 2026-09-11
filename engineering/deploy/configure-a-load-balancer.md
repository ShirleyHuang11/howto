---
name: configure-a-load-balancer
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You configure a load balancer to distribute traffic across healthy application instances and remove failed instances automatically.

## Preconditions

- At least two application instances serving the same version and reachable on a private network.
- A health endpoint such as `/healthz` that returns 200 only when the instance can serve traffic.
- Access to the cloud, Kubernetes, or proxy configuration that owns external traffic.
- DNS control for the public hostname or an existing listener to update.

## Steps

1. **Inventory backend targets.** List instance private IPs, ports, and health URLs; for Kubernetes run `kubectl get endpoints,svc -n <namespace>`. → *Expect:* every intended backend has an address and the serving port is known.
2. **Verify each backend directly.** Run `for h in 10.0.1.10 10.0.1.11; do curl -fsS "http://$h:8080/healthz"; done`. → *Expect:* every backend returns success before being added.
3. **Create or update the target group.** [BRANCH: AWS ALB | GCP Load Balancing | Nginx upstream | Kubernetes Service] Add each backend on the application port and set the health check path to `/healthz`. → *Expect:* the target group contains all intended backends with the correct protocol and port.
4. **Configure listener rules.** Route `HTTPS:443` for the hostname/path to the target group and keep HTTP redirect behavior explicit. → *Expect:* the listener shows one deterministic rule for the app route.
5. **Set load-balancing and draining policy.** Use round-robin or least-connections as appropriate, and set connection draining/deregistration delay long enough for in-flight requests. → *Expect:* draining is enabled and the timeout is documented.
6. **Attach TLS certificate and security controls.** Select the certificate for the hostname and restrict inbound traffic to required ports. → *Expect:* port 443 is open publicly, backend ports are private, and the certificate matches the hostname.
7. **Wait for health checks to pass.** Use the provider status page or CLI such as `aws elbv2 describe-target-health --target-group-arn <arn>`. → *Expect:* every expected target is `healthy`.
8. **Send traffic through the load balancer.** Run `curl -fsS -o /dev/null -w '%{http_code}\n' https://app.example.com/healthz`. → *Expect:* `200` from the public endpoint.

## Decision points

- Health endpoint checks dependencies → use it for readiness; use a lighter liveness check only for process restarts.
- Stateful sessions exist → prefer external session storage; use sticky sessions only as a temporary compatibility measure.
- Long-lived connections exist → increase idle timeout and verify WebSocket or streaming behavior.
- Blue/green deployment planned → create separate target groups and switch listener weights gradually.

## Failure modes & recovery

- **F1 All targets unhealthy:** detect target health `unhealthy` or HTTP 503 → test direct backend health, security groups, health check path, and expected status code.
- **F2 Partial traffic failure:** detect intermittent 5xx only through the load balancer → compare per-target logs and remove the bad target from rotation.
- **F3 TLS hostname mismatch:** detect browser warning or `curl` certificate error → attach the correct certificate and verify SNI configuration.
- **F4 Backend overload:** detect high latency and 5xx during traffic → reduce per-target load, add instances, or tune connection limits and keep-alive.

## Verification

The provider reports all intended targets `healthy`, and `curl -fsS -o /dev/null -w '%{http_code}\n' https://app.example.com/healthz` returns `200` for at least three consecutive attempts.

## Variations

- `AWS ALB`: use target groups, listener rules, security groups, and `aws elbv2 describe-target-health`.
- `Kubernetes`: use `Service` plus `Ingress`; verify with `kubectl describe ingress` and controller events.
- `Nginx`: define an `upstream` block and reload after `nginx -t`; health checks require Nginx Plus or external checking.
- `HAProxy`: use `backend` servers with `check`; verify through the stats socket or stats page.

## Safety & privacy

Medium risk because routing errors can drop production traffic or expose backend ports. Keep backend networks private, avoid permissive security groups, do not paste certificate private keys into tickets, and get review before changing production listener rules.
