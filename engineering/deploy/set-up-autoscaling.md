---
name: set-up-autoscaling
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You configure autoscaling so capacity increases under sustained load, decreases safely when idle, and keeps enough healthy instances available during scaling events.

## Preconditions

- The app is horizontally scalable and does not rely on local-only session state.
- Health checks and readiness checks work through the load balancer or orchestrator.
- Metrics exist for scaling signals such as CPU, request rate, queue depth, or latency.
- Deployment limits, cloud quotas, and budget constraints are known.

## Steps

1. **Confirm the app can scale horizontally.** Check that sessions, uploads, caches, and scheduled jobs do not require a single specific instance. → *Expect:* shared state lives in external services or the scaling plan explicitly excludes non-scalable workers.
2. **Choose the scaling metric.** Use CPU for CPU-bound services, request rate for web fleets, or queue depth for workers. → *Expect:* one primary metric has a target threshold and a measurement window.
3. **Set minimum and maximum capacity.** Choose a minimum that survives one instance failure and a maximum within quota and budget. → *Expect:* `min`, `desired`, and `max` values are recorded and enforceable.
4. **Create the scaling policy.** [BRANCH: Kubernetes HPA | AWS Auto Scaling | GCP MIG] For Kubernetes, run `kubectl autoscale deployment api --cpu-percent=60 --min=2 --max=10 -n <namespace>`. → *Expect:* the autoscaler resource exists with the intended min, max, and metric target.
5. **Ensure scale-out integrates with readiness.** Confirm new instances do not receive traffic until readiness passes. → *Expect:* the load balancer or service endpoints include only ready instances.
6. **Configure scale-in protection.** Set termination grace periods, connection draining, and pod disruption budgets where available. → *Expect:* scale-in removes instances only after draining or graceful termination.
7. **Generate controlled load.** Use a safe test environment or low-risk production canary with a tool such as `hey -z 5m -c 50 https://app.example.com/healthz`. → *Expect:* the scaling metric crosses the threshold and capacity increases.
8. **Observe scale-down.** Stop load and wait for the cooldown or stabilization window. → *Expect:* capacity returns toward minimum without dropping healthy traffic.

## Decision points

- Web app has bursty traffic → prefer request-rate or target-tracking scaling over raw CPU alone.
- Worker queue backs up → scale on queue depth or age of oldest message.
- Cold starts are slow → keep a higher minimum or add scheduled scaling before known peaks.
- Database is the bottleneck → do not scale app replicas blindly; tune the database or connection pool first.

## Failure modes & recovery

- **F1 No scaling occurs:** detect metric above threshold but replica count unchanged → verify metrics pipeline, autoscaler permissions, and max capacity.
- **F2 Thrashing:** detect rapid scale up/down cycles → increase cooldown, stabilization window, or target threshold.
- **F3 New instances fail readiness:** detect replicas created but unavailable → inspect startup logs, image pull errors, secrets, and dependency access.
- **F4 Downstream saturation:** detect more app replicas causing database or API errors → cap max capacity and fix the constrained dependency.

## Verification

During a controlled load test, `kubectl get hpa api -n <namespace>` or the cloud autoscaling status shows desired capacity increasing above minimum, all new instances become ready, and the public health check continues returning `200`.

## Variations

- `Kubernetes HPA`: requires metrics-server or custom metrics; verify with `kubectl describe hpa`.
- `AWS ECS`: use Application Auto Scaling policies on service desired count and verify service events.
- `AWS EC2 ASG`: use target tracking or step policies and verify instance health in the target group.
- `Queue workers`: use queue length per worker or age of oldest message rather than HTTP latency.

## Safety & privacy

Medium risk because bad scaling policies can create outages or surprise cost. Cap maximum capacity, run load tests in staging when possible, avoid logging customer payloads during testing, and get review before enabling aggressive production scale-in.
