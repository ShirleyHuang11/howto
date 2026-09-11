---
name: read-logs-from-a-pod
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You retrieve Kubernetes pod logs for the right container and time window without exposing secrets or losing incident context.

## Preconditions

- `kubectl` is authenticated to the intended cluster and namespace.
- You know enough labels, workload names, or timestamps to narrow the search.
- You have permission to view logs for the namespace.

## Steps

1. **Find the target pod.** Run `kubectl get pods -n <namespace> -l app=<app> -o wide`. → *Expect:* one or more matching pods with status, age, node, and restart count.
2. **Identify containers in the pod.** Run `kubectl get pod <pod> -n <namespace> -o jsonpath='{.spec.containers[*].name}{"\n"}'`. → *Expect:* container names are printed so you can select the application container or sidecar.
3. **Read recent logs.** Run `kubectl logs <pod> -n <namespace> -c <container> --since=30m --timestamps`. → *Expect:* timestamped log lines from the selected container are printed.
4. **Read previous crash logs when needed.** If the pod restarted, run `kubectl logs <pod> -n <namespace> -c <container> --previous --timestamps`. → *Expect:* logs from the terminated container instance are shown, or Kubernetes reports no previous container.
5. **Stream live logs for reproduction.** Run `kubectl logs <pod> -n <namespace> -c <container> -f --tail=100`. → *Expect:* the last 100 lines appear and new lines stream until interrupted.
6. **Capture a bounded artifact.** Run `kubectl logs <pod> -n <namespace> -c <container> --since=1h --timestamps > /tmp/<pod>-logs.txt`. → *Expect:* a local file contains the requested log window for review.
7. **Redact sensitive values before sharing.** Search the artifact with `grep -Ein '(password|token|secret|authorization|cookie)' /tmp/<pod>-logs.txt`. → *Expect:* any sensitive lines are redacted before posting in tickets or chat.

## Decision points

- Multiple pods match → inspect the pod with the restart, node, or time range relevant to the incident.
- Logs are empty → check the correct container name and whether the app logs to stdout/stderr.
- Need all pods for a deployment → use `kubectl logs deploy/<name> -n <namespace> --all-containers --since=30m`.
- Need historical logs after pod deletion → query the centralized logging system instead of Kubernetes pod logs.

## Failure modes & recovery

- **F1 Unauthorized:** detect `forbidden: User cannot get resource pods/log` → request read-only log access for the namespace.
- **F2 Wrong container:** detect `a container name must be specified` or unrelated sidecar logs → rerun with `-c <container>`.
- **F3 Lost crash logs:** detect `previous terminated container not found` → use centralized logs or events because the old container record is gone.
- **F4 Excessive output:** detect terminal flooding or truncated history → add `--since`, `--tail`, or redirect to a file.

## Verification

`kubectl logs <pod> -n <namespace> -c <container> --since=5m --timestamps --tail=20` exits 0 and prints timestamped lines from the expected container, or prints no lines while confirming the container has no recent output.

## Variations

- `stern`: run `stern <app> -n <namespace> --since 30m` to aggregate logs across matching pods.
- `kubetail`: run `kubetail <deployment> -n <namespace>` for multi-pod tailing.
- Cloud logging: use the provider's log explorer for deleted pods and longer retention windows.

## Safety & privacy

Low operational risk, but logs often contain personal data, tokens, request bodies, and internal hostnames. Redact before sharing, prefer bounded time windows, and keep downloaded artifacts in temporary or access-controlled locations.
