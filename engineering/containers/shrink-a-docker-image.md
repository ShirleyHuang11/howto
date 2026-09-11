---
name: shrink-a-docker-image
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [engineering/containers/build-a-docker-image]
status: draft
last_verified: 2026-09-11
---

## Goal

You reduce a container image size while preserving runtime behavior, security updates, and debuggability appropriate for the service.

## Preconditions

- The image builds and has a working smoke test.
- You can compare image sizes and run the application after each change.
- Build dependencies and runtime dependencies are distinguishable.

## Steps

1. **Measure the current image.** Run `docker images myapp:dev` and optionally `docker history myapp:dev`. → *Expect:* a baseline size and largest layers are visible.
2. **Inspect contents.** Use `dive myapp:dev` or `docker run --rm -it myapp:dev sh` if a shell exists. → *Expect:* obvious caches, build tools, or unused artifacts are identified.
3. **Add or tighten `.dockerignore`.** Exclude `.git`, tests if not needed at runtime, local caches, coverage, logs, and secrets. → *Expect:* build context size decreases in build output.
4. **Use multi-stage builds.** Keep compilers, package managers, and dev dependencies in a builder stage; copy only runtime artifacts. → *Expect:* final image no longer contains build-only tools.
5. **Install production dependencies only.** Use commands such as `npm ci --omit=dev`, `pip install --no-cache-dir`, or package-manager cleanup in the same layer. → *Expect:* dev dependencies and package caches are absent.
6. **Choose a smaller maintained base.** Move to slim, alpine, distroless, or scratch only after compatibility testing. → *Expect:* the app still starts and TLS certificates/timezone needs are satisfied.
7. **Rebuild and compare.** Run `docker build -t myapp:slim .` and compare with `docker images`. → *Expect:* size is lower and smoke tests still pass.

## Decision points

- Native dependencies fail on Alpine → use Debian slim rather than spending time on musl compatibility.
- Need shell debugging in production → avoid distroless or keep a separate debug image.
- Size reduction removes security updates → prefer maintained base images over stale tiny images.

## Failure modes & recovery

- **F1 Runtime library missing:** detect shared library or import errors → copy required runtime packages or use a compatible base.
- **F2 TLS failures:** detect certificate verification errors → install CA certificates in the final image.
- **F3 Broke non-root permissions:** detect write permission errors → chown required directories during build.
- **F4 False savings from cache:** detect local size change but registry digest still huge → push and inspect the actual manifest or compressed size.

## Verification

Run `docker build -t myapp:slim . && docker run --rm myapp:slim <smoke-command> && docker images myapp`; the build and smoke command exit 0 and the new image size is lower than the recorded baseline.

## Variations

- `Node.js`: copy `node_modules` produced by `npm ci --omit=dev` or build standalone output.
- `Python`: build wheels in one stage and install them into a slim runtime without pip caches.
- `Go`: copy a static binary into `scratch` or distroless when certificates and timezone data are handled.

## Safety & privacy

Medium risk because shrinking can remove needed runtime files or hide diagnostics. Make one change at a time, keep the smoke test mandatory, and do not use unmaintained base images solely for a smaller number.
