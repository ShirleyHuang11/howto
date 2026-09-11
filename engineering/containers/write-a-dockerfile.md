---
name: write-a-dockerfile
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

You create a Dockerfile that builds reproducibly, runs the application as a non-root process, and exposes a checkable container entrypoint.

## Preconditions

- The application can build and run locally outside a container.
- The runtime version, start command, listening port, and required build artifacts are known.
- Docker or a compatible builder is installed.

## Steps

1. **Choose a specific base image.** Pin a maintained runtime family such as `node:22-bookworm-slim`, `python:3.12-slim`, or a digest when release reproducibility matters. → *Expect:* the Dockerfile does not use an ambiguous `latest` tag.
2. **Create a `.dockerignore`.** Exclude `.git`, local dependencies, build output not needed as input, logs, secrets, and test caches. → *Expect:* `docker build` sends a small context without secret files.
3. **Install dependencies before copying volatile source.** Copy lockfiles first, run `npm ci`, `pip install -r requirements.txt`, or equivalent, then copy the application. → *Expect:* dependency layers are cacheable.
4. **Use multi-stage builds when useful.** Build assets or binaries in a builder stage and copy only runtime artifacts into the final image. → *Expect:* compilers and dev dependencies are absent from the runtime image.
5. **Run as a non-root user.** Create or use an unprivileged user and set `USER app`. → *Expect:* `docker run --rm IMAGE id -u` prints a non-zero UID.
6. **Set the runtime command and port.** Add `EXPOSE 3000` and `CMD ["node", "server.js"]` or the correct exec-form command. → *Expect:* the container starts without requiring an interactive shell.
7. **Build and smoke test.** Run `docker build -t app:test .` then `docker run --rm -p 3000:3000 app:test`. → *Expect:* the image builds and the service answers on the expected port.

## Decision points

- App needs native compilation → keep build tools in a builder stage only.
- Runtime writes files → create and chown a specific writable directory instead of writing throughout the image.
- Distroless or scratch image desired → confirm debugging and certificate needs before adopting it.

## Failure modes & recovery

- **F1 Missing files:** detect `COPY failed` or runtime `file not found` → inspect `.dockerignore` and build context.
- **F2 Dependency cache broken:** detect full reinstall on every source edit → copy lockfiles separately from application code.
- **F3 Root-only behavior:** detect permission errors after setting `USER` → chown only required runtime directories.
- **F4 Wrong architecture:** detect `exec format error` → rebuild for the target platform with `docker buildx build --platform`.

## Verification

Run `docker build -t app:test . && docker run --rm app:test <health-or-version-command>`; the build exits 0 and the container command exits 0, or a service smoke test such as `curl -f http://localhost:3000/health` succeeds.

## Variations

- `Node.js`: prefer `npm ci --omit=dev` in the runtime stage.
- `Python`: use wheels or a virtual environment copied from a builder stage.
- `Go/Rust`: compile a static or slim binary in a builder stage and copy only the binary plus certificates.

## Safety & privacy

Medium risk because images can leak secrets or fail in deployment. Never bake `.env`, SSH keys, cloud credentials, or package registry tokens into layers; use build secrets for private dependency fetches and runtime secrets for execution.
