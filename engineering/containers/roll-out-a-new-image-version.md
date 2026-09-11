---
name: roll-out-a-new-image-version
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

You deploy a new container image version to a Kubernetes workload and verify the rollout reaches healthy pods.

## Preconditions

- The image has been built, pushed, and scanned in the registry.
- `kubectl` points at the intended cluster and namespace.
- You know the workload, container name, image tag or digest, and rollback path.

## Steps

1. **Confirm the image exists.** Run `docker manifest inspect <registry>/<image>:<tag> >/dev/null` or `crane digest <registry>/<image>:<tag>`. → *Expect:* the command exits 0 and returns image metadata or a digest.
2. **Inspect the current deployment.** Run `kubectl get deploy <name> -n <namespace> -o jsonpath='{.spec.template.spec.containers[*].image}{"\n"}'`. → *Expect:* the currently deployed image is visible for rollback reference.
3. **Update the image.** Run `kubectl set image deploy/<name> <container>=<registry>/<image>:<tag> -n <namespace>`. → *Expect:* Kubernetes reports `deployment.apps/<name> image updated`.
4. **Watch rollout status.** Run `kubectl rollout status deploy/<name> -n <namespace> --timeout=10m`. → *Expect:* the deployment reports successfully rolled out.
5. **Verify pods use the new image.** Run `kubectl get pods -n <namespace> -l app=<app> -o jsonpath='{range .items[*]}{.metadata.name}{" "}{.spec.containers[*].image}{"\n"}{end}'`. → *Expect:* every ready pod lists the new image tag or digest.
6. **Check service health.** Run `kubectl get deploy <name> -n <namespace>` and `kubectl logs deploy/<name> -n <namespace> --since=10m --tail=100`. → *Expect:* desired, current, and available replicas match, with no new startup errors.
7. **Run a smoke test.** Execute `curl -fsS https://<service-host>/health` or the service's smoke-test command. → *Expect:* the endpoint returns success, usually HTTP 200.

## Decision points

- Rollout stalls → inspect `kubectl describe deploy/<name>` and pod events before changing anything else.
- New image fails readiness → roll back with `kubectl rollout undo deploy/<name> -n <namespace>`.
- Tag is mutable → prefer deploying an immutable digest such as `<image>@sha256:<digest>`.
- Canary required → update a canary deployment or use the progressive delivery controller instead of a direct full rollout.

## Failure modes & recovery

- **F1 Image pull failure:** detect `ImagePullBackOff` or `ErrImagePull` → verify registry path, tag, credentials, and pull secrets.
- **F2 CrashLoopBackOff:** detect repeated restarts after new image → read previous logs and roll back if the failure affects availability.
- **F3 Readiness never passes:** detect rollout timeout with unavailable replicas → inspect readiness probe, dependencies, and configuration.
- **F4 Smoke test fails:** detect non-2xx response or failed synthetic check → roll back and open a fix-forward issue with logs.

## Verification

`kubectl rollout status deploy/<name> -n <namespace> --timeout=10m` exits 0, all ready pods report `<registry>/<image>:<tag>` or the target digest, and `curl -fsS https://<service-host>/health` exits 0.

## Variations

- `Helm`: set the tag or digest in values and deploy with `helm upgrade <release> <chart> -n <namespace> --atomic --timeout 10m`.
- `Argo CD`: update Git, wait for sync, then verify `argocd app wait <app> --health --sync`.
- `GitLab CI/GitHub Actions`: let the pipeline apply the manifest and use the CI deployment status as the rollout gate.

## Safety & privacy

Medium risk because a bad image can break live traffic. Keep the previous image reference, avoid leaking private registry URLs in public channels, and confirm production rollouts during an approved deployment window for critical services.
