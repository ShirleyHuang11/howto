---
name: deploy-a-web-app-to-production
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min-2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You deploy a tested web application release to production and verify the live service is healthy. The production version, commit, and rollback path are known before traffic is exposed.

## Preconditions

- The target commit has passed required CI checks.
- Production credentials and deployment permissions are available.
- A rollback method exists: previous artifact, image digest, release, or platform rollback.
- Database migrations, if any, have a separate safe plan.

## Steps

1. **Identify the exact release artifact.** Record the commit SHA, image digest, package version, or build artifact ID to deploy. → *Expect:* one immutable release identifier is written in the deployment notes.
2. **Confirm production readiness.** Check CI, monitoring, error budget, and open incidents. → *Expect:* required checks are green and no active incident makes deployment unsafe.
3. **Back up mutable production state.** If the deploy touches database schema, uploaded assets, or configuration, take the relevant backup or snapshot first. → *Expect:* backup job completes and restore instructions are available.
4. **Deploy using the approved mechanism.** [BRANCH: Kubernetes, run `kubectl set image deployment/<app> <container>=<image>@<digest> -n <ns>` | PaaS, run the provider deploy command | VM, deploy the built artifact with the release script] ⚠️ *Irreversible:* production traffic can be affected; confirm the release ID and rollback target before executing. → *Expect:* the deploy command exits 0 or returns a deployment ID.
5. **Watch rollout status.** [BRANCH: Kubernetes, `kubectl rollout status deployment/<app> -n <ns> --timeout=5m` | PaaS, watch deployment logs or release status] → *Expect:* rollout reports complete or healthy.
6. **Run smoke checks against production.** Use `curl -fsS https://<host>/healthz` and one read-only user journey or synthetic check. → *Expect:* health endpoint returns 200 and the smoke check exits 0.
7. **Inspect metrics and logs.** Check error rate, latency, saturation, and application logs for at least one normal traffic window. → *Expect:* metrics remain within normal thresholds and no new error spike appears.
8. **Record the deployment.** Update the release tracker with release ID, time, operator, verification result, and rollback target. → *Expect:* deployment history contains enough detail for incident response.

## Decision points

- Smoke check fails → stop rollout and roll back before debugging in production.
- Migration is required → run `engineering/run-a-database-migration-safely` before or during deployment according to expand/contract order.
- Error rate rises after deploy → roll back if thresholds are breached.
- Deployment platform supports progressive rollout → prefer canary or blue-green for high-traffic services.

## Failure modes & recovery

- **F1 Rollout timeout:** detect `progress deadline exceeded` or platform timeout → roll back to the previous release and inspect pod or deploy logs.
- **F2 Health check returns non-200:** detect `curl` failure or load balancer unhealthy targets → revert release or remove new instances from traffic.
- **F3 Configuration missing:** detect boot errors about required env vars → restore previous config or set the missing variable and redeploy.
- **F4 Database incompatibility:** detect runtime SQL errors after deploy → roll back application code if schema is backward-compatible, or execute the planned down/repair procedure.

## Verification

The deployment command completes, rollout status is healthy, `curl -fsS https://<production-host>/healthz` exits 0 with HTTP 200, and production error/latency dashboards remain within agreed thresholds after release.

## Variations

- `Kubernetes`: verify with `kubectl rollout status`, `kubectl get pods`, and service health endpoints.
- `Heroku/Fly/Render/Railway`: use platform release IDs and rollback commands.
- `VM/systemd`: deploy artifact, restart service, then verify `systemctl is-active <service>` and health checks.
- `container registry`: deploy by immutable digest rather than mutable tags.

## Safety & privacy

High risk because production traffic and data may be affected. Confirm the exact artifact, keep secrets out of logs, take backups before state changes, and do not proceed with irreversible steps unless rollback and ownership are clear.
