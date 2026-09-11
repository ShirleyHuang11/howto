---
name: scale-a-deployment
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You change the replica count of a Kubernetes Deployment and verify the service reaches the intended capacity.

## Preconditions

- `kubectl` is authenticated to the intended cluster and namespace.
- You know whether replicas are managed manually, by HPA, or by GitOps.
- The cluster has enough capacity for the requested number of pods.

## Steps

1. **Inspect the current scale state.** Run `kubectl get deploy <name> -n <namespace>` and `kubectl get hpa -n <namespace>`. → *Expect:* current ready replicas and any autoscaler ownership are visible.
2. **Check recent health and capacity.** Run `kubectl top nodes` and `kubectl top pods -n <namespace>`. → *Expect:* nodes have enough CPU and memory headroom for the desired replicas.
3. **Choose the scaling path.** [BRANCH: manual | HPA | GitOps] For manual scaling, use `kubectl scale deploy/<name> --replicas=<count> -n <namespace>`. → *Expect:* Kubernetes reports `scaled`.
4. **Wait for availability.** Run `kubectl rollout status deploy/<name> -n <namespace> --timeout=5m`. → *Expect:* the deployment reaches the new desired state.
5. **Verify pod count.** Run `kubectl get pods -n <namespace> -l app=<app> --field-selector=status.phase=Running`. → *Expect:* the expected number of running pods appears.
6. **Check endpoints.** Run `kubectl get endpoints <service> -n <namespace>` or `kubectl get endpointslice -n <namespace> -l kubernetes.io/service-name=<service>`. → *Expect:* the service has ready endpoints for the new pods.
7. **Confirm traffic behavior.** Run a smoke test such as `curl -fsS https://<service-host>/health`. → *Expect:* the service still returns a successful health response.

## Decision points

- HPA exists → change HPA min/max or target metrics instead of manually fighting the controller.
- GitOps manages manifests → update the replica count in Git and let the reconciler apply it.
- Scaling to zero → confirm background jobs, queues, and external callers tolerate no replicas.
- Pods remain pending → add node capacity or reduce resource requests before increasing replicas.

## Failure modes & recovery

- **F1 HPA overwrites count:** detect replicas changing back automatically → update `minReplicas` or `maxReplicas` instead.
- **F2 Insufficient capacity:** detect pods stuck `Pending` with insufficient resources → scale nodes, lower requests, or choose a smaller replica count.
- **F3 Readiness failures:** detect new pods running but not ready → inspect logs and readiness probe failures before scaling further.
- **F4 Quota exceeded:** detect `exceeded quota` admission errors → request quota or scale another workload down.

## Verification

`kubectl get deploy <name> -n <namespace> -o jsonpath='{.status.readyReplicas}/{.spec.replicas}{"\n"}'` prints `<count>/<count>`, and the service smoke test exits 0.

## Variations

- `HorizontalPodAutoscaler`: run `kubectl patch hpa <name> -n <namespace> --type merge -p '{"spec":{"minReplicas":<min>,"maxReplicas":<max>}}'`.
- `Helm`: update `replicaCount` or autoscaling values and run `helm upgrade`.
- `KEDA`: adjust `minReplicaCount`, `maxReplicaCount`, or trigger metadata in the ScaledObject.

## Safety & privacy

Medium risk because scaling can overload dependencies, increase spend, or reduce availability. Confirm production scaling intent, avoid scaling stateful workloads casually, and ensure logs or screenshots do not expose internal hostnames or customer traffic volumes unnecessarily.
