---
name: set-resource-limits-on-a-pod
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You set CPU and memory requests and limits for a Kubernetes workload so scheduling is predictable and runaway containers are constrained.

## Preconditions

- `kubectl` is installed and points at the intended cluster and namespace.
- You know the workload name and container name: `kubectl get deploy,statefulset -n <namespace>`.
- Metrics are available from `kubectl top pod -n <namespace>` or another monitoring system.

## Steps

1. **Inspect current resource settings.** Run `kubectl get deploy <name> -n <namespace> -o jsonpath='{range .spec.template.spec.containers[*]}{.name}{": "}{.resources}{"\n"}{end}'`. → *Expect:* each container's current `requests` and `limits` are visible, or empty resource maps show they are unset.
2. **Measure normal usage.** Run `kubectl top pod -n <namespace> --containers | grep <name>` and check recent CPU and memory percentiles in monitoring. → *Expect:* observed usage gives a baseline for request and limit values.
3. **Choose conservative values.** Set requests near normal steady usage and limits above expected bursts, for example `requests.cpu: 250m`, `requests.memory: 512Mi`, `limits.cpu: 1`, `limits.memory: 1Gi`. → *Expect:* values fit node capacity and leave headroom for traffic spikes.
4. **Edit the workload manifest.** Add resources under the target container in YAML, then apply with `kubectl apply -f k8s/deployment.yaml`. → *Expect:* `deployment.apps/<name> configured` and no schema validation errors.
5. **Wait for the rollout.** Run `kubectl rollout status deploy/<name> -n <namespace> --timeout=5m`. → *Expect:* the rollout reports successfully completed.
6. **Check pod placement and restarts.** Run `kubectl get pods -n <namespace> -l app=<app> -o wide` and `kubectl describe pod <pod> -n <namespace> | grep -A8 -E 'Limits|Requests'`. → *Expect:* new pods are running and show the requested resources.
7. **Watch for throttling or OOM.** Run `kubectl top pod -n <namespace> --containers` and inspect events with `kubectl get events -n <namespace> --sort-by=.lastTimestamp | tail -40`. → *Expect:* no `OOMKilled`, `Evicted`, or repeated restart events after the change.

## Decision points

- Pod stays `Pending` → requests may exceed available node capacity; lower requests or scale node capacity before retrying.
- Container is CPU-throttled but healthy → raise CPU limit or remove CPU limit if your cluster policy allows it.
- Container is `OOMKilled` → increase memory limit after checking for leaks and abnormal traffic.
- Multi-container pod → set resources on every long-running container, including sidecars.

## Failure modes & recovery

- **F1 Unschedulable pod:** detect `0/<n> nodes are available: Insufficient cpu/memory` in events → reduce requests or add capacity, then reapply.
- **F2 Crash after rollout:** detect `CrashLoopBackOff` or high restart count → inspect logs, raise limits if the process is being killed, or roll back with `kubectl rollout undo deploy/<name> -n <namespace>`.
- **F3 OOMKilled:** detect `Last State: Terminated Reason: OOMKilled` → raise memory limit and investigate memory growth.
- **F4 Admission denied:** detect policy errors such as `must specify limits` or forbidden ratios → adjust values to match namespace LimitRange and ResourceQuota.

## Verification

`kubectl rollout status deploy/<name> -n <namespace> --timeout=5m` exits 0, `kubectl get pods -n <namespace> -l app=<app>` shows all pods `Running`, and `kubectl describe pod <pod> -n <namespace>` shows the intended CPU and memory requests and limits.

## Variations

- `Helm`: update `values.yaml`, render with `helm template`, then deploy with `helm upgrade --install <release> <chart> -n <namespace>`.
- `Kustomize`: add or patch `resources` in an overlay and run `kubectl apply -k overlays/<env>`.
- `OpenShift`: use `oc` equivalents and check project quotas with `oc describe quota`.

## Safety & privacy

Medium risk because incorrect limits can prevent scheduling or kill healthy processes. Change one workload at a time, avoid copying production values into public notes if they reveal capacity, and get review for critical services before applying production limits.
