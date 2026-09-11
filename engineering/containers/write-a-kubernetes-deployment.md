---
name: write-a-kubernetes-deployment
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You write a Kubernetes Deployment manifest that runs a container reliably with explicit replicas, resource requests, probes, configuration, and rollout behavior.

## Preconditions

- The container image exists in a registry reachable by the cluster.
- The app's port, health endpoints, environment variables, and resource needs are known.
- You can validate manifests with `kubectl` against a cluster or schema-aware tool.

## Steps

1. **Create the Deployment skeleton.** Set `apiVersion: apps/v1`, `kind: Deployment`, metadata name, labels, and a matching selector. → *Expect:* selector labels exactly match pod template labels.
2. **Set replicas and rollout strategy.** Choose `replicas: 2` or the environment's minimum and configure rolling update defaults or explicit surge/unavailable values. → *Expect:* rollout can replace pods without dropping all capacity.
3. **Specify the container image and port.** Use an immutable tag or digest and define `containerPort`. → *Expect:* the pod spec identifies exactly what image and port to run.
4. **Add configuration references.** Use ConfigMaps for non-secret values and Secrets for sensitive values. → *Expect:* the manifest contains secret names, not raw secret values.
5. **Define resource requests and limits.** Add CPU and memory requests, plus sensible limits where the platform expects them. → *Expect:* the scheduler has resource data and pods avoid unbounded memory use.
6. **Add readiness and liveness probes.** Use HTTP, TCP, or exec probes against real health endpoints with appropriate delays. → *Expect:* Kubernetes can stop routing to unready pods and restart stuck ones.
7. **Validate the manifest.** Run `kubectl apply --dry-run=server -f deployment.yml` or `kubectl diff -f deployment.yml`. → *Expect:* the API server accepts the schema and references.
8. **Apply in a safe namespace and watch rollout.** Run `kubectl apply -f deployment.yml -n NAMESPACE` then `kubectl rollout status deployment/APP -n NAMESPACE`. → *Expect:* the Deployment creates available pods.

## Decision points

- App has slow startup → tune `startupProbe` or initial delays instead of weakening readiness.
- Single replica is acceptable only for dev → production should usually run at least two replicas or document why not.
- Needs persistent identity or storage → use StatefulSet rather than Deployment.

## Failure modes & recovery

- **F1 Selector mismatch:** detect immutable selector or no pods selected → create a corrected Deployment name or fix before first apply.
- **F2 Unschedulable pods:** detect pending pods with resource or node selector events → adjust requests or scheduling constraints.
- **F3 Probe kills healthy startup:** detect liveness failures during boot → add `startupProbe` or increase initial delay.
- **F4 Secret not found:** detect `CreateContainerConfigError` → create the Secret in the same namespace or fix the reference.

## Verification

Run `kubectl apply --dry-run=server -f deployment.yml && kubectl rollout status deployment/APP -n NAMESPACE --timeout=5m`; validation exits 0 and rollout reports success with available replicas.

## Variations

- `Helm`: template values into a Deployment and verify with `helm template` plus server dry-run where possible.
- `Kustomize`: keep base Deployment generic and patch image, replicas, and config per environment.
- `GitOps`: commit the manifest and verify the controller reports Synced and Healthy.

## Safety & privacy

Medium risk because a bad Deployment can break a shared environment. Never put raw Secret values in YAML, validate context and namespace before applying, and get review before changing production replica counts, probes, or resource limits.
