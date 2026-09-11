---
name: build-and-push-a-docker-image-in-ci
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You configure CI to build a container image from the repository and push it to a registry with traceable tags. The pushed image can be pulled and inspected by digest.

## Preconditions

- A working `Dockerfile` or container build file exists.
- Registry credentials or workload identity are available in CI secrets.
- The application build and tests pass before image publication.

## Steps

1. **Choose registry and tag scheme.** Use immutable tags such as the full commit SHA and optional release tags; avoid relying only on `latest`. → *Expect:* a tag plan like `registry.example.com/app:${GIT_SHA}`.
2. **Add registry authentication to CI.** [BRANCH: GitHub Container Registry, use `docker/login-action@v3` with `GITHUB_TOKEN` | Docker Hub/ECR/GCR, use provider credentials or OIDC] → *Expect:* CI logs show successful registry login without printing secrets.
3. **Build the image after tests pass.** Run `docker build -t "$IMAGE:$GIT_SHA" .` or use BuildKit/buildx. → *Expect:* the build exits 0 and produces a local image ID.
4. **Label the image with source metadata.** Add OCI labels such as `org.opencontainers.image.revision=$GIT_SHA` and `org.opencontainers.image.source=$REPO_URL`. → *Expect:* `docker inspect` shows the commit label.
5. **Push immutable tags.** Run `docker push "$IMAGE:$GIT_SHA"` and push release tags only for release events. → *Expect:* the registry returns a digest like `sha256:...`.
6. **Scan the image when tooling is available.** Run a scanner such as `trivy image --exit-code 1 --severity HIGH,CRITICAL "$IMAGE:$GIT_SHA"` according to policy. → *Expect:* the scan exits 0 or blocks the push/deploy with actionable findings.
7. **Pull and inspect the pushed image.** Run `docker pull "$IMAGE:$GIT_SHA"` in CI or a follow-up job. → *Expect:* pull succeeds and the digest matches the pushed digest.

## Decision points

- Registry supports OIDC → prefer short-lived identity over static passwords.
- Multi-architecture images are required → use `docker buildx build --platform linux/amd64,linux/arm64 --push`.
- Vulnerability policy blocks critical CVEs → scan before deployment and fail on configured severities.
- Image is for PR validation only → build without pushing, or push to a short-retention preview registry path.

## Failure modes & recovery

- **F1 Registry login fails:** detect `unauthorized` or `denied` → verify registry URL, token scope, and repository/package permissions.
- **F2 Build context too large:** detect slow uploads or disk exhaustion → add `.dockerignore` entries for caches, test outputs, and local files.
- **F3 Push succeeds but deploy pulls old image:** detect mutable tag drift → deploy by digest or immutable commit SHA tag.
- **F4 Secret leaked into image layer:** detect secret in `docker history` or scanner output → use BuildKit secrets and rotate the exposed credential.

## Verification

CI exits 0, the registry contains the image tagged with the commit SHA, and `docker pull <image>:<sha>` followed by `docker inspect <image>:<sha>` shows the expected `org.opencontainers.image.revision` label and digest.

## Variations

- `GitHub Actions`: `docker/build-push-action@v6` can build, cache, label, and push with BuildKit.
- `GitLab CI`: use Docker-in-Docker or Kaniko depending on runner policy.
- `AWS ECR`: use OIDC or `aws-actions/amazon-ecr-login`, then push to the account registry.
- `Kubernetes deploy`: pass the immutable image digest to manifests or Helm values.

## Safety & privacy

Medium risk because published images may be deployed by downstream systems. Do not bake secrets into layers, use least-privilege registry credentials, prefer immutable tags or digests, and keep private images in private registries.
