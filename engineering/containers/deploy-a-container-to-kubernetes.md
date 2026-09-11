---
name: deploy-a-container-to-kubernetes
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: [engineering/containers/push-an-image-to-a-registry]
status: draft
last_verified: 2026-09-11
---

## Goal

You deploy a container image to Kubernetes, wait for rollout, and verify the running workload serves traffic or passes its health checks.

## Preconditions

- `kubectl` is installed and pointed at the intended cluster and namespace.
- The image is pushed to a registry the cluster can pull from.
- Deployment manifests, Helm chart, or Kustomize overlays exist for the workload.
- You have approval to deploy to the target environment.

## Steps

1. **Confirm the target context.** Run `kubectl config current-context` and `kubectl config view --minify --output 'jsonpath={..namespace}'`. → *Expect:* the context and namespace match the approved environment.
2. **Confirm the image reference.** Use an immutable tag or digest such as `registry/team/app@sha256:...`. → *Expect:* the image exists in the registry and matches the tested build.
3. **Preview manifest changes.** Run `kubectl diff -f k8s/` or `helm diff upgrade RELEASE CHART`. → *Expect:* only the intended Deployment, Service, ConfigMap, or Secret references change.
4. **Apply the deployment.** ⚠️ *Irreversible:* production rollout changes live traffic; confirm maintenance window, rollback image, and approval before `kubectl apply -f k8s/` or `helm upgrade`. → *Expect:* the API server accepts the change.
5. **Wait for rollout.** Run `kubectl rollout status deployment/APP -n NAMESPACE --timeout=5m`. → *Expect:* rollout completes successfully.
6. **Inspect pods and events.** Run `kubectl get pods -l app=APP -n NAMESPACE` and `kubectl describe deployment/APP -n NAMESPACE`. → *Expect:* desired replicas are available and no pull, scheduling, or probe errors remain.
7. **Run an external or in-cluster smoke test.** Use `curl -f https://app.example.com/health` or `kubectl run tmp-curl --rm -i --restart=Never --image=curlimages/curl -- curl -f http://SERVICE/health`. → *Expect:* health check exits 0.

## Decision points

- Rollout fails → stop and inspect pods; roll back with `kubectl rollout undo deployment/APP -n NAMESPACE` if live service is impaired.
- Image pull fails → check image reference, registry credentials, and `imagePullSecrets`.
- Database migration required → run and verify migration before shifting application traffic if the release plan requires it.

## Failure modes & recovery

- **F1 ImagePullBackOff:** detect pod status → fix registry auth or image tag, then restart rollout.
- **F2 CrashLoopBackOff:** detect repeated restarts → read `kubectl logs --previous` and roll back if production is affected.
- **F3 Readiness never passes:** detect unavailable replicas → inspect readiness probe path, port, and dependency health.
- **F4 Bad config rollout:** detect new pods failing due to ConfigMap or Secret changes → restore previous config or roll back the Deployment.

## Verification

Run `kubectl rollout status deployment/APP -n NAMESPACE --timeout=5m && kubectl get deployment/APP -n NAMESPACE -o jsonpath='{.status.availableReplicas}'` and a `curl -f` health check; rollout exits 0, available replicas equal desired replicas, and health check exits 0.

## Variations

- `Helm`: use `helm upgrade --install`, `helm status`, and `helm rollback`.
- `Kustomize`: use `kubectl apply -k overlays/ENV` and review `kubectl diff -k` first.
- `Argo CD/Flux`: update Git, wait for sync/health, and verify controller status instead of applying directly.

## Safety & privacy

High risk for production because deployments affect live traffic. Confirm cluster context, namespace, approval, rollback plan, and secret handling before applying; use least-privilege kube credentials and never paste Secret values into logs or tickets.
