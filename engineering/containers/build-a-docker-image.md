---
name: build-a-docker-image
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: [engineering/containers/write-a-dockerfile]
status: draft
last_verified: 2026-09-11
---

## Goal

You build a container image from a Dockerfile, tag it predictably, and verify that the image can start or report its version.

## Preconditions

- A Dockerfile exists at the intended build context.
- Docker, Podman, or BuildKit is installed and can access the container daemon or builder.
- Required build arguments are known and do not include raw secrets.

## Steps

1. **Select the build context and Dockerfile.** Identify the directory sent to the builder and any non-default Dockerfile path. → *Expect:* `docker build` runs from the correct directory.
2. **Choose a deterministic tag.** Use a local tag such as `myapp:dev` or include a commit SHA supplied by CI. → *Expect:* the resulting image can be referenced unambiguously.
3. **Build without leaking secrets.** Run `docker build -t myapp:dev .`; if private credentials are required, use BuildKit secrets such as `--secret id=npmrc,src=$HOME/.npmrc`. → *Expect:* build exits 0 and logs do not show secret values.
4. **Inspect image metadata.** Run `docker image inspect myapp:dev --format '{{.Id}} {{.Config.User}} {{.Config.Entrypoint}} {{.Config.Cmd}}'`. → *Expect:* Docker prints an image id and expected user/command fields.
5. **Run a smoke command.** Use `docker run --rm myapp:dev --version` or the app's health command. → *Expect:* the container exits 0 or stays healthy for a service run.
6. **Record build inputs if needed.** In CI, emit image tag, digest, Dockerfile path, and build platform. → *Expect:* logs identify exactly what was built.

## Decision points

- Building for another architecture → use `docker buildx build --platform linux/amd64` or the target platform.
- Image must be pushed during build → use `docker buildx build --push -t REGISTRY/IMAGE:TAG .`.
- Build depends on network services → replace them with build-time artifacts or fail early with a clear prerequisite.

## Failure modes & recovery

- **F1 Daemon unavailable:** detect `Cannot connect to the Docker daemon` → start Docker Desktop, the daemon, or use the configured remote builder.
- **F2 Missing build arg:** detect empty config or build error for required arg → pass `--build-arg NAME=value` and validate defaults.
- **F3 Secret in layer:** detect credentials in `docker history` or image scan → remove the layer pattern, rotate the credential, and rebuild using secrets.
- **F4 Platform mismatch:** detect `exec format error` when running → rebuild with the deployment platform.

## Verification

Run `docker build -t myapp:dev . && docker image inspect myapp:dev >/dev/null && docker run --rm myapp:dev <smoke-command>`; all commands exit 0 and the smoke command proves the image starts.

## Variations

- `Podman`: use `podman build -t myapp:dev .` and `podman run --rm`.
- `Buildx`: use builders for multi-platform images and provenance.
- `CI`: tag with immutable values such as commit SHA and publish only after tests pass.

## Safety & privacy

Medium risk because build contexts and layers can expose secrets. Keep context small, inspect `.dockerignore`, avoid `ARG` for secret values, and use least-privilege registry credentials.
