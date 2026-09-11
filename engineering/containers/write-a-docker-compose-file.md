---
name: write-a-docker-compose-file
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You create a Compose file that starts a local multi-container stack with explicit services, networks, volumes, and health checks.

## Preconditions

- Docker Compose v2 is available as `docker compose`.
- The required services, ports, environment variables, and persistent data needs are known.
- Images or Dockerfiles exist for app services.

## Steps

1. **Define named services.** Add each process under `services`, such as `web`, `db`, and `redis`. → *Expect:* `docker compose config` recognizes all service names.
2. **Set build or image sources.** Use `build: .` for local app code and pinned image tags such as `postgres:16` for dependencies. → *Expect:* every service has exactly one intended source.
3. **Configure environment safely.** Use local env files or variables such as `POSTGRES_PASSWORD: example-local-only`. → *Expect:* no production secret appears in the Compose file.
4. **Add ports only where needed.** Publish app or database ports with mappings like `"8080:3000"`. → *Expect:* only developer-facing services are reachable from the host.
5. **Persist state with named volumes.** Add `volumes: db-data:` and mount it to the database data directory. → *Expect:* database data survives container recreation.
6. **Add health checks and dependencies.** Use `healthcheck` for databases and `depends_on` with `condition: service_healthy` where supported. → *Expect:* the app waits for dependencies that report healthy.
7. **Validate and start the stack.** Run `docker compose config` then `docker compose up --build`. → *Expect:* config validation exits 0 and all services start.

## Decision points

- Development needs live reload → mount source code into the app container and keep dependency directories container-owned.
- CI needs the stack → create a CI override file with deterministic ports and no interactive behavior.
- Dependency readiness matters → use real health checks, not just `depends_on` startup order.

## Failure modes & recovery

- **F1 Invalid YAML or schema:** detect `docker compose config` errors → fix indentation, keys, or variable substitution.
- **F2 Service starts too early:** detect connection refused from app to db → add health checks and dependency conditions or retry logic.
- **F3 Volume hides built files:** detect missing dependencies after mounting project root → use named volumes for dependency directories or avoid broad mounts.
- **F4 Port collision:** detect bind errors → change the host-side port or stop the conflicting local process.

## Verification

Run `docker compose config && docker compose up -d --build && docker compose ps`; validation exits 0 and `docker compose ps` shows required services running or healthy, followed by a successful app smoke test such as `curl -f http://localhost:8080/health`.

## Variations

- `Podman Compose`: syntax is similar, but networking and rootless volume permissions may differ.
- `Production`: Compose can be used for small deployments, but secrets, scheduling, and rollbacks often belong in an orchestrator.
- `Override files`: use `compose.override.yml` for local-only mounts and ports.

## Safety & privacy

Medium risk because local stacks can expose databases or embed credentials. Bind only necessary ports, use local-only passwords, exclude `.env` from commits when it contains secrets, and avoid mounting sensitive host directories.
