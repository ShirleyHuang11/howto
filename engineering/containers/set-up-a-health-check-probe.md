---
name: set-up-a-health-check-probe
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You add Kubernetes startup, readiness, or liveness probes that accurately reflect container health without causing avoidable restarts.

## Preconditions

- The application exposes a cheap health endpoint or command.
- You can edit the workload manifest and apply it to a non-production or approved environment first.
- You understand startup time and dependency behavior for the service.

## Steps

1. **Choose the probe type.** Use readiness for traffic eligibility, liveness for stuck processes, and startup for slow initialization. → *Expect:* each probe has a clear purpose and does not duplicate another probe unnecessarily.
2. **Test the health command locally.** Run `curl -fsS http://localhost:<port>/healthz` inside a local container or `kubectl exec <pod> -n <namespace> -- curl -fsS http://127.0.0.1:<port>/healthz`. → *Expect:* the check exits 0 when healthy and fails when the app is unavailable.
3. **Add probe YAML.** Add `readinessProbe`, and optionally `livenessProbe` or `startupProbe`, under the container with `httpGet`, `tcpSocket`, or `exec`. → *Expect:* the manifest validates with `kubectl apply --dry-run=server -f k8s/deployment.yaml`.
4. **Tune timings.** Set `initialDelaySeconds`, `periodSeconds`, `timeoutSeconds`, `failureThreshold`, and `successThreshold` from real startup and latency data. → *Expect:* normal startup is not killed and true failures are detected promptly.
5. **Apply the manifest.** Run `kubectl apply -f k8s/deployment.yaml`. → *Expect:* Kubernetes accepts the workload update.
6. **Wait for rollout.** Run `kubectl rollout status deploy/<name> -n <namespace> --timeout=10m`. → *Expect:* pods become available and the rollout completes.
7. **Inspect probe events.** Run `kubectl describe pod <pod> -n <namespace> | grep -Ei 'readiness|liveness|startup|unhealthy|probe'`. → *Expect:* no repeated probe failures are present during normal operation.

## Decision points

- App needs external dependencies to serve traffic → readiness may check dependencies, but liveness should usually check only the process.
- Slow boot → add a `startupProbe` before liveness so Kubernetes does not kill normal initialization.
- Health endpoint is expensive → create a lightweight endpoint that avoids database scans or third-party calls.
- Sidecar mesh present → confirm whether probes need rewrite support or direct application port access.

## Failure modes & recovery

- **F1 Restart storm:** detect liveness failures and rising restarts → disable or relax liveness, then fix the health logic.
- **F2 Never ready:** detect pods running but `0/1 Ready` → check endpoint path, port, scheme, and dependency assumptions.
- **F3 Probe timeout:** detect `context deadline exceeded` → raise timeout slightly or make health handler cheaper.
- **F4 Auth blocks probe:** detect HTTP 401 or 403 in events → exempt the internal health endpoint from authentication or use an exec probe.

## Verification

`kubectl rollout status deploy/<name> -n <namespace> --timeout=10m` exits 0, `kubectl get pods -n <namespace> -l app=<app>` shows all desired pods ready, and `kubectl describe pod <pod> -n <namespace>` has no recent `Unhealthy` probe warnings.

## Variations

- `HTTP`: use `httpGet` with path, port, and optional headers.
- `TCP`: use `tcpSocket` for services that only expose a port-level readiness signal.
- `Exec`: use `exec.command` for local checks, but keep commands fast and dependency-light.

## Safety & privacy

Medium risk because bad probes can remove healthy pods from service or create restart loops. Test outside production first, avoid health endpoints that leak version or dependency secrets, and get review before changing liveness behavior on critical workloads.
