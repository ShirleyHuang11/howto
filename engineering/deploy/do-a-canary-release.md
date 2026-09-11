---
name: do-a-canary-release
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

You expose a new release to a small portion of production traffic, evaluate objective health metrics, and then either expand or roll back. The release advances only when the canary meets predefined success criteria.

## Preconditions

- The platform can route traffic by percentage, users, region, header, or instance count.
- Metrics exist for error rate, latency, saturation, and business-critical behavior.
- The new and old versions can run side by side safely.
- Rollback can quickly remove the canary from traffic.

## Steps

1. **Define canary success and abort thresholds.** Set metrics such as 5xx rate, p95 latency, crash rate, and domain-specific checks. → *Expect:* a written rule like "abort if 5xx > 1% for 5 minutes".
2. **Deploy the canary version with minimal traffic.** [BRANCH: Kubernetes, use Argo Rollouts/Flagger or a second deployment with 1 replica | service mesh, set 1%-5% weight | feature flag, target internal users first] → *Expect:* only the intended small cohort receives the new version.
3. **Verify the canary is receiving traffic.** Check request logs, metrics labels, or a version endpoint. → *Expect:* canary traffic count is nonzero and within the configured percentage.
4. **Run smoke checks against the canary path.** Use header, route, or user targeting if needed: `curl -fsS -H 'X-Canary: 1' https://<host>/healthz`. → *Expect:* canary health check returns 200.
5. **Observe the first window before expanding.** Watch dashboards and automated analysis for the agreed duration. → *Expect:* canary metrics meet success thresholds.
6. **Increase traffic in controlled steps.** Move to 10%, 25%, 50%, then 100% only after each window passes. ⚠️ *Irreversible:* each increase exposes more real users; confirm current metrics before changing weight. → *Expect:* traffic weights and metrics update at each step.
7. **Promote or roll back.** Promote when the final window passes; set canary traffic to 0 or undo rollout if thresholds fail. → *Expect:* either 100% traffic uses the new version or all traffic returns to the stable version.

## Decision points

- Metrics are missing or unreliable → do not canary beyond internal traffic.
- New version changes database writes → verify backward compatibility and idempotency before user traffic.
- Canary cohort is too small for signal → increase observation time before increasing percentage.
- Automated analysis fails → pause and inspect before overriding.

## Failure modes & recovery

- **F1 Canary receives no traffic:** detect zero request count → fix routing, labels, or flag targeting.
- **F2 Metrics lack version labels:** detect unable to compare old vs new → add release labels before continuing.
- **F3 Abort threshold breached:** detect alert or analysis failure → set canary weight to 0 and keep the stable version serving.
- **F4 Sticky sessions hide impact:** detect uneven user distribution → use user-based targeting or longer windows.

## Verification

Canary dashboards show the configured traffic percentage, canary health checks return 200, abort metrics stay below thresholds at each step, and final promotion shows 100% traffic on the new release with no active canary alert.

## Variations

- `Argo Rollouts`: use `kubectl argo rollouts get rollout <name> --watch` and promote or abort.
- `Flagger`: define metric templates and let Flagger advance or roll back automatically.
- `LaunchDarkly/feature flags`: canary by user segment without deploying a second binary.
- `service mesh`: route weighted traffic through Istio, Linkerd, or Envoy-based controls.

## Safety & privacy

High risk because real users are intentionally exposed to a new version. Keep cohorts limited at first, avoid targeting vulnerable users unintentionally, monitor privacy-sensitive logs carefully, and roll back immediately when abort criteria trigger.
