---
name: debug-a-container-that-wont-start
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

You determine why a container exits, fails health checks, or never reaches readiness, then prove the fix with logs and a successful start.

## Preconditions

- The image name, container name, or Compose service is known.
- Docker or Podman access is available.
- You can rebuild or rerun the container locally or in a safe environment.

## Steps

1. **Check the exit state.** Run `docker ps -a --filter name=myapp --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'`. → *Expect:* the container status shows whether it exited, restarted, or never created.
2. **Read recent logs.** Run `docker logs --tail=200 myapp`. → *Expect:* startup errors, stack traces, or missing configuration messages are visible.
3. **Inspect the configured command.** Run `docker inspect myapp --format '{{json .Config.Entrypoint}} {{json .Config.Cmd}}'`. → *Expect:* entrypoint and command match the intended startup process.
4. **Check environment and mounts.** Run `docker inspect myapp --format '{{json .Config.Env}} {{json .Mounts}}'` and redact secrets before sharing. → *Expect:* required variables and volume paths are present.
5. **Override the command for inspection.** Run `docker run --rm -it --entrypoint sh IMAGE` when the image has a shell. → *Expect:* files, permissions, and installed binaries can be inspected interactively.
6. **Fix the smallest cause.** Correct the Dockerfile, Compose file, env var, permissions, or start command. → *Expect:* the build or run configuration changes only the diagnosed issue.
7. **Rerun and health check.** Start the container again and run `docker ps` plus `curl -f http://localhost:PORT/health` if it is a service. → *Expect:* the container stays `Up` and the health check succeeds.

## Decision points

- Exit code is 127 → command or binary is missing; inspect `PATH` and build artifacts.
- Exit code is 126 or permission denied → fix execute bits, ownership, or non-root access.
- Container is running but unhealthy → inspect healthcheck command and application readiness dependencies.

## Failure modes & recovery

- **F1 Crash loop hides logs:** detect rapidly restarting container → run with `--rm` and no restart policy locally to capture the first failure.
- **F2 No shell in image:** detect `exec: "sh": executable file not found` → use a debug variant or inspect with `docker create` plus `docker cp`.
- **F3 Missing configuration:** detect errors for unset env vars → provide local defaults or fail fast with clearer validation.
- **F4 Bind mount masks files:** detect files present in image but missing at runtime → adjust volume mounts or paths.

## Verification

Run `docker run -d --name myapp-debug -p 8080:3000 IMAGE`, then `docker ps --filter name=myapp-debug --filter status=running` and `curl -f http://localhost:8080/health`; the container remains running and the health endpoint exits 0.

## Variations

- `Compose`: use `docker compose logs SERVICE`, `docker compose ps`, and `docker compose run --entrypoint sh SERVICE`.
- `Kubernetes`: use `kubectl describe pod`, `kubectl logs --previous`, and temporary debug containers if enabled.
- `Distroless`: debug through logs, `docker cp`, SBOMs, or a parallel debug image.

## Safety & privacy

Medium risk because logs and environment can contain secrets. Redact env output before sharing, avoid attaching production volumes locally, and do not change restart policies in production without an operational rollback path.
