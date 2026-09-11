---
name: run-a-container-locally
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: low
prerequisites: [engineering/containers/build-a-docker-image]
status: draft
last_verified: 2026-09-11
---

## Goal

You start a container locally with the right ports, environment, and volumes, then verify the process is healthy and reachable.

## Preconditions

- Docker or Podman is installed.
- The image exists locally or can be pulled.
- Required environment variables and ports are known.

## Steps

1. **Pull or build the image.** Run `docker image inspect myapp:dev >/dev/null || docker build -t myapp:dev .`. → *Expect:* the image exists locally.
2. **Choose port mappings.** Map host to container ports, for example `-p 8080:3000`. → *Expect:* the host port is free and matches the URL you will test.
3. **Pass non-secret configuration.** Use `-e APP_ENV=local` for simple values and an env file for local-only settings. → *Expect:* required configuration is visible to the container.
4. **Start the container with a name.** Run `docker run --rm --name myapp-local -p 8080:3000 --env-file .env.local myapp:dev`. → *Expect:* logs show the application started and is listening.
5. **Check the process state.** In another terminal, run `docker ps --filter name=myapp-local`. → *Expect:* the container appears with status `Up`.
6. **Smoke test the service.** Run `curl -f http://localhost:8080/health` or the app's local endpoint. → *Expect:* `curl` exits 0 and returns the expected health payload.
7. **Stop and clean up.** Press Ctrl-C for foreground runs or `docker stop myapp-local`. → *Expect:* the container exits and no named local container remains.

## Decision points

- Container exits immediately → inspect logs with `docker logs myapp-local` or run an interactive shell if available.
- Host port is occupied → choose another host port while keeping the same container port.
- App needs a database → start dependencies with Compose or a dedicated container network.

## Failure modes & recovery

- **F1 Port conflict:** detect `bind: address already in use` → find the process or choose a different host port.
- **F2 Missing environment:** detect errors for unset variables → supply a local env file and keep secrets out of the image.
- **F3 Health endpoint fails:** detect `curl` non-zero or 5xx → inspect logs and verify the app is listening on `0.0.0.0`, not only `127.0.0.1`.
- **F4 Permission denied on volume:** detect write errors inside the container → align UID/GID or chown the mounted directory.

## Verification

Run `docker run -d --name myapp-local -p 8080:3000 myapp:dev`, then `docker ps --filter name=myapp-local --filter status=running` and `curl -f http://localhost:8080/health`; the container is running and `curl` exits 0.

## Variations

- `Podman`: replace `docker` with `podman`; rootless runs may need adjusted port and volume permissions.
- `CLI container`: verify with a command exit status instead of a health URL.
- `Compose`: use `docker compose up` when multiple services are required.

## Safety & privacy

Low risk for local use. Do not pass production secrets into local containers, avoid binding sensitive host directories, and remove containers that contain local test data when finished.
