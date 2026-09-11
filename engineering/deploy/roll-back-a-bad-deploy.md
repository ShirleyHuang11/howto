---
name: roll-back-a-bad-deploy
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 10min-45min
risk: high
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You restore the last known good production version quickly and verify the incident symptoms improve. The rollback is traceable and does not make database or data corruption worse.

## Preconditions

- You know the current bad release and the previous known good release.
- The deployment platform supports rollback or redeploying an older artifact.
- Monitoring identifies the failing service and symptom.
- Any database migrations are understood before rolling code backward.

## Steps

1. **Confirm rollback is the right action.** Compare deploy time with error, latency, or user-impact start time. → *Expect:* the bad release is strongly correlated with the incident.
2. **Check migration compatibility.** Determine whether the bad deploy applied schema or data changes that old code can still use. → *Expect:* a clear answer: rollback code only is safe, or a database recovery step is required.
3. **Select the rollback target.** Identify the previous healthy release ID, image digest, artifact version, or deployment revision. → *Expect:* one immutable rollback target is written in incident notes.
4. **Execute the rollback.** [BRANCH: Kubernetes, `kubectl rollout undo deployment/<app> -n <ns>` or set image to the previous digest | Heroku, `heroku rollback v<N>` | Helm, `helm rollback <release> <revision>`] ⚠️ *Irreversible:* rollback changes live production traffic; confirm the target release and database compatibility before executing. → *Expect:* the platform starts rolling back and returns success or a deployment ID.
5. **Watch rollback status.** Use provider rollout status, such as `kubectl rollout status deployment/<app> -n <ns> --timeout=5m`. → *Expect:* rollback completes and serving instances run the target version.
6. **Run production smoke checks.** Execute `curl -fsS https://<host>/healthz` plus the failing synthetic or read-only user journey. → *Expect:* health checks return 200 and the failing symptom is gone or reduced.
7. **Monitor recovery window.** Watch error rate, latency, queue depth, and user reports for the agreed period. → *Expect:* metrics return to normal thresholds.
8. **Record follow-up work.** Link the incident, bad release, rollback target, and any remaining data repair tasks. → *Expect:* future deploys are blocked until the root cause or mitigation is tracked.

## Decision points

- Old code is incompatible with migrated schema → do not roll back code until a safe forward fix or database repair is planned.
- Rollback fails health checks → redeploy an earlier known good version or scale down the faulty service path.
- Incident is configuration-only → revert the config change rather than the application artifact.
- Data corruption occurred → preserve evidence and take backups before repair.

## Failure modes & recovery

- **F1 Rollback target unavailable:** detect missing image or artifact → redeploy from the saved commit or restore from artifact storage.
- **F2 Rollback does not fix symptoms:** detect errors persist after old version serves traffic → investigate config, dependency, database, or infrastructure changes.
- **F3 Database rollback unsafe:** detect old code expecting removed columns or old data shapes → apply forward-compatible hotfix instead.
- **F4 Rollout hangs:** detect timeout or unhealthy instances → inspect logs, scale previous healthy version manually, or route traffic away.

## Verification

The platform reports the rollback deployment healthy, `curl -fsS https://<production-host>/healthz` exits 0, the running version matches the selected rollback artifact, and the incident metric returns below the alert threshold.

## Variations

- `Kubernetes`: use `kubectl rollout history` and `kubectl rollout undo`, or redeploy by previous image digest.
- `Helm`: `helm history` and `helm rollback` restore chart revisions.
- `PaaS`: use provider release history and rollback commands.
- `database-heavy apps`: prefer forward fixes unless migrations were explicitly reversible and backed up.

## Safety & privacy

High risk because rollback affects live users and can interact badly with data changes. Confirm compatibility, avoid deleting evidence needed for incident review, and keep credentials and user data out of incident notes and chat logs.
