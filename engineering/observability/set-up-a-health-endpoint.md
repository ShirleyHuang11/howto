---
name: set-up-a-health-endpoint
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

You add a lightweight health endpoint that load balancers, uptime checks, and orchestration probes can use to determine service health.

## Preconditions

- You can edit the service code and route configuration.
- You know which dependencies are required for serving traffic.
- The service has tests and a way to run locally.

## Steps

1. **Define health semantics.** Decide whether `/health` checks process liveness, readiness, or deep dependency health. → *Expect:* the endpoint's meaning is documented and unambiguous.
2. **Implement a cheap route.** Add `GET /health` or `/readyz` that returns JSON such as `{"status":"ok"}` and HTTP 200 when healthy. → *Expect:* the route avoids expensive queries and external calls unless readiness requires them.
3. **Add dependency checks carefully.** For readiness, check only critical dependencies with short timeouts and clear failure status. → *Expect:* dependency failure returns non-2xx and a safe, non-secret reason.
4. **Keep authentication appropriate.** Allow internal probes to reach the endpoint, but do not expose sensitive details publicly. → *Expect:* probes can call the route without credentials or with a dedicated low-privilege mechanism.
5. **Add tests.** Test healthy response and at least one failed dependency branch. → *Expect:* tests assert status code and response body without requiring live external services.
6. **Run locally.** Start the service and run `curl -fsS -o /dev/null -w '%{http_code}\n' http://localhost:<port>/health`. → *Expect:* the command prints `200`.
7. **Wire probes or monitors.** Configure Kubernetes readiness probes, load balancer health checks, or uptime monitors to call the endpoint. → *Expect:* platform health checks report passing after deployment.

## Decision points

- Endpoint is for liveness → do not require database or third-party availability.
- Endpoint is for readiness → include critical dependencies needed to serve traffic, with strict timeouts.
- Public internet can reach it → return minimal information and no version, hostname, or dependency details.
- Multiple components exist → expose separate `/livez` and `/readyz` endpoints.

## Failure modes & recovery

- **F1 Probe cannot reach endpoint:** detect connection refused or 404 → verify route path, port, base path, and network policy.
- **F2 Health check flaps:** detect alternating pass/fail → remove slow dependencies or add timeout and caching.
- **F3 Sensitive details exposed:** detect dependency URLs or stack traces in response → replace with generic statuses and log details server-side.
- **F4 False healthy:** detect endpoint returns 200 during real outage → add the missing critical readiness dependency or synthetic transaction.

## Verification

`curl -fsS -o /dev/null -w '%{http_code}' http://localhost:<port>/health` returns `200`, the health endpoint tests exit 0, and the deployed platform health check reports healthy.

## Variations

- `Kubernetes`: map `/livez` to `livenessProbe` and `/readyz` to `readinessProbe`.
- `Load balancers`: configure expected status code and timeout in the cloud load balancer target group.
- `gRPC`: implement the standard gRPC Health Checking Protocol instead of HTTP.
- `Serverless`: use provider-native health or synthetic checks when no always-on container exists.

## Safety & privacy

Medium risk because health endpoints can control traffic routing and reveal internals. Keep responses minimal, use short dependency timeouts, and test probe behavior before production rollout.
