---
name: do-a-zero-downtime-deploy
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

You release a new application version without dropping active traffic or returning errors during the transition. Old and new versions overlap safely until health checks prove the new version can serve requests.

## Preconditions

- The service has a load balancer, rolling update, blue-green, or canary mechanism.
- The app supports graceful shutdown and readiness checks.
- Database changes are backward-compatible with both old and new code.
- A previous healthy version is available for rollback.

## Steps

1. **Confirm compatibility between versions.** Verify config, API contracts, queues, and database schema work with old and new instances at the same time. → *Expect:* no migration or protocol requires all instances to switch simultaneously.
2. **Set readiness and liveness checks.** Ensure new instances receive traffic only after `/readyz` or equivalent succeeds. → *Expect:* load balancer or orchestrator marks only ready instances available.
3. **Deploy with a rolling or progressive strategy.** [BRANCH: Kubernetes, set `maxUnavailable: 0` and `maxSurge: 1` or higher | PaaS, enable rolling deploy/preboot] ⚠️ *Irreversible:* production traffic will shift; confirm rollback target and monitoring before starting. → *Expect:* new instances start before old healthy instances are removed.
4. **Drain old instances gracefully.** Use termination grace periods and stop accepting new requests before shutdown. → *Expect:* logs show graceful shutdown without killed in-flight requests.
5. **Watch rollout and live health.** Run `kubectl rollout status deployment/<app> -n <ns> --timeout=10m` or provider equivalent while monitoring 5xx and latency. → *Expect:* rollout completes and metrics stay within normal range.
6. **Run synthetic checks during the rollout.** Execute repeated probes such as `for i in $(seq 1 30); do curl -fsS https://<host>/healthz >/dev/null || exit 1; sleep 2; done`. → *Expect:* every probe exits 0.
7. **Complete and record the release.** Confirm all instances run the new version and record the deployed artifact. → *Expect:* instance list shows only the new version and deployment notes include verification.

## Decision points

- Readiness checks are weak → improve them before claiming zero downtime.
- Database migration is not backward-compatible → split into expand, deploy, backfill, contract phases.
- Long-lived connections exist → configure connection draining and test websocket or streaming behavior.
- Error rate increases during rollout → pause or roll back immediately.

## Failure modes & recovery

- **F1 New instances never become ready:** detect readiness probe failures → keep old instances serving, inspect logs, and roll back the rollout.
- **F2 5xx spike during replacement:** detect monitor alert or failed synthetic probes → pause rollout and restore previous version.
- **F3 In-flight requests terminated:** detect client disconnects or shutdown errors → increase grace period and implement graceful shutdown hooks.
- **F4 Schema mismatch:** detect SQL column or type errors from either version → apply compatible migration or roll back code depending on the migration state.

## Verification

During the deploy, repeated `curl -fsS https://<host>/healthz` probes exit 0, orchestrator rollout status completes successfully, and production metrics show no downtime-level 5xx or availability breach.

## Variations

- `Kubernetes`: use rolling updates with readiness probes, PodDisruptionBudgets, and `preStop` hooks.
- `Heroku`: use preboot for web dynos, then verify release health.
- `load balancer plus VMs`: add new instances, pass health checks, drain old instances, then terminate them.
- `queues/workers`: deploy workers with idempotent handlers and drain old workers before stopping.

## Safety & privacy

High risk because the procedure changes live serving capacity. Keep rollback ready, avoid incompatible state changes during the overlap, and ensure logs and monitoring do not expose request bodies or secrets while debugging.
