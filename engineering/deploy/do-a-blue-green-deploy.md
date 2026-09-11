---
name: do-a-blue-green-deploy
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-3h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You deploy a new version into an idle production-equivalent environment, verify it, then switch traffic from the old environment to the new one. The old environment remains available for quick rollback until the release is stable.

## Preconditions

- Two environments or target groups exist: blue and green.
- Both environments can access required production dependencies safely.
- Database changes are compatible with both old and new versions.
- Traffic can be shifted by load balancer, DNS, service mesh, or platform routing.

## Steps

1. **Identify active and idle environments.** Check which color currently receives production traffic. → *Expect:* one environment is active and the other is idle or receiving no user traffic.
2. **Deploy the new artifact to the idle color.** [BRANCH: Kubernetes, deploy to the inactive namespace or deployment label | load balancer, register new target group instances | PaaS, deploy to the inactive app] → *Expect:* idle environment runs the new version while users stay on the old version.
3. **Run internal health checks on the idle color.** Probe its private URL or target group health endpoint with `curl -fsS`. → *Expect:* health endpoint returns 200 before any traffic switch.
4. **Run smoke and compatibility checks.** Test read-only production-like requests and background workers if applicable. → *Expect:* checks exit 0 and logs show no new startup errors.
5. **Switch traffic atomically or progressively.** Change load balancer weights, service selector, or route mapping to send production traffic to the new color. ⚠️ *Irreversible:* live traffic moves to a new environment; confirm health checks and rollback route before switching. → *Expect:* routing status shows the new color as active.
6. **Verify live traffic on the new color.** Check response headers, version endpoint, logs, or metrics to confirm traffic is served by the new version. → *Expect:* live requests report the new version and error rates remain normal.
7. **Keep the old color warm during the observation window.** Do not tear it down until stability criteria are met. → *Expect:* rollback remains a routing switch, not a rebuild.
8. **Retire or reset the old color.** After approval, scale down or mark old as idle for the next deploy. → *Expect:* deployment inventory shows the new color active and old color idle.

## Decision points

- Shared database has incompatible migration → use expand/contract before blue-green traffic switching.
- DNS controls traffic → account for TTL and prefer load balancer routing when possible.
- Stateful sessions are local to instances → drain or externalize sessions before switching.
- New color fails smoke tests → fix it while traffic remains on the old color.

## Failure modes & recovery

- **F1 Idle color cannot reach dependencies:** detect health or connection failures → fix networking, secrets, or allowlists before switching traffic.
- **F2 Traffic split goes to both colors unexpectedly:** detect mixed version responses → inspect load balancer weights or service selectors.
- **F3 Error spike after switch:** detect 5xx or latency alerts → switch routing back to the old color immediately.
- **F4 Old color removed too soon:** detect rollback requires rebuild → restore the previous artifact and lengthen future observation windows.

## Verification

After the switch, `curl -fsS https://<host>/healthz` exits 0, a version endpoint or response header shows the new release, production metrics remain healthy, and the old color is still available until the observation window ends.

## Variations

- `AWS ALB`: use blue and green target groups with listener rule or weighted routing.
- `Kubernetes`: switch a Service selector or use progressive delivery tooling.
- `Cloud Foundry/Heroku-style PaaS`: map and unmap routes between apps.
- `DNS`: use low TTLs, but expect propagation delay and less precise rollback.

## Safety & privacy

High risk because production traffic is rerouted. Confirm the idle environment uses production-safe secrets, avoid writing test data through live integrations, and keep the old environment intact until rollback is no longer needed.
