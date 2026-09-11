---
name: debug-a-crashlooping-pod
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

You identify why a Kubernetes pod is in `CrashLoopBackOff` and either restore service safely or produce a precise fix plan.

## Preconditions

- `kubectl` is authenticated to the relevant cluster and namespace.
- You know the workload, recent deployment, or alert that surfaced the crash.
- You have permission to read pods, events, and logs.

## Steps

1. **Locate the failing pod.** Run `kubectl get pods -n <namespace> -l app=<app>`. → *Expect:* the pod status shows `CrashLoopBackOff`, `Error`, or rising restarts.
2. **Describe pod state and events.** Run `kubectl describe pod <pod> -n <namespace>`. → *Expect:* container exit reason, exit code, restart count, probes, mounts, and recent events are visible.
3. **Read previous container logs.** Run `kubectl logs <pod> -n <namespace> -c <container> --previous --timestamps --tail=200`. → *Expect:* logs from the crashed process reveal the last error before exit.
4. **Check current logs.** Run `kubectl logs <pod> -n <namespace> -c <container> --timestamps --tail=100`. → *Expect:* logs from the latest restart attempt are visible.
5. **Inspect configuration inputs.** Run `kubectl get deploy <name> -n <namespace> -o yaml` and check referenced ConfigMaps, Secrets, env vars, and volume mounts. → *Expect:* missing keys, bad paths, or changed settings are identifiable.
6. **Compare with the last rollout.** Run `kubectl rollout history deploy/<name> -n <namespace>`. → *Expect:* recent revision timing can be matched to the start of crashes.
7. **Recover safely.** [BRANCH: bad rollout | bad config | resource issue] Use `kubectl rollout undo deploy/<name> -n <namespace>` for a bad image, apply a corrected config for bad configuration, or adjust resource limits for OOM. → *Expect:* a new rollout starts and failing pods are replaced.
8. **Verify stability.** Run `kubectl rollout status deploy/<name> -n <namespace> --timeout=10m` and `kubectl get pods -n <namespace> -l app=<app>`. → *Expect:* pods are ready and restart counts stop increasing.

## Decision points

- Exit code 137 or `OOMKilled` → inspect memory limits and recent memory behavior.
- Exit code 1 with app stack trace → fix application configuration or code.
- Probe failure causes restarts → tune liveness/startup probe separately from app startup logic.
- Image pull or command error → verify image tag, entrypoint, args, and registry credentials.

## Failure modes & recovery

- **F1 Previous logs unavailable:** detect `previous terminated container not found` → reproduce by watching `kubectl logs -f` or use centralized logs.
- **F2 Rollback unavailable:** detect no prior ReplicaSet or rollout history → redeploy the last known-good image tag explicitly.
- **F3 Config missing:** detect `CreateContainerConfigError` or missing secret/config key → restore the key and restart pods.
- **F4 OOM repeats:** detect repeated `OOMKilled` after limit increase → capture heap/profile data in a safe environment and scale down traffic if needed.

## Verification

`kubectl rollout status deploy/<name> -n <namespace> --timeout=10m` exits 0, `kubectl get pods -n <namespace> -l app=<app>` shows ready pods, and `kubectl get pod <pod> -n <namespace> -o jsonpath='{.status.containerStatuses[0].restartCount}'` stays unchanged across two checks several minutes apart.

## Variations

- `Ephemeral containers`: run `kubectl debug -it <pod> -n <namespace> --image=busybox:1.36 --target=<container>` when the cluster permits it.
- `Helm`: recover with `helm rollback <release> <revision> -n <namespace>` if the crash came from a chart release.
- `StatefulSet`: rollbacks and pod deletion affect identity and storage; inspect one ordinal at a time.

## Safety & privacy

Medium risk because recovery actions can roll traffic back or restart production pods. Avoid printing secrets from manifests, use least-privilege cluster access, and confirm with the service owner before rollback if user-visible behavior may change.
