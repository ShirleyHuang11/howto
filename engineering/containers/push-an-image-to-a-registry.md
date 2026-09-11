---
name: push-an-image-to-a-registry
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [engineering/containers/build-a-docker-image]
status: draft
last_verified: 2026-09-11
---

## Goal

You tag and push a container image to a registry with the correct repository, immutable version tag, and verified digest.

## Preconditions

- The image builds and passes its local smoke test.
- You have registry credentials with permission to push to the target repository.
- The registry namespace and tag policy are known.

## Steps

1. **Authenticate to the registry.** Run `docker login REGISTRY.example.com` or a cloud-specific login command. → *Expect:* login succeeds without printing the password in shell history.
2. **Tag the local image.** Run `docker tag myapp:dev REGISTRY.example.com/team/myapp:TAG`. → *Expect:* `docker images REGISTRY.example.com/team/myapp:TAG` shows the tagged image.
3. **Use an immutable tag.** Prefer commit SHA, build number, or release version over only `latest`. → *Expect:* the pushed image can be traced to source.
4. **Push the image.** Run `docker push REGISTRY.example.com/team/myapp:TAG`. → *Expect:* upload completes and prints a digest such as `sha256:...`.
5. **Inspect the remote image.** Run `docker buildx imagetools inspect REGISTRY.example.com/team/myapp:TAG` or registry CLI equivalent. → *Expect:* the remote digest and platform list are visible.
6. **Record the digest for deployment.** Use `REGISTRY.example.com/team/myapp@sha256:...` where deployment immutability matters. → *Expect:* deployment references can be pinned to exact content.

## Decision points

- Registry requires cloud auth → use `aws ecr get-login-password`, `gcloud auth configure-docker`, or `az acr login`.
- Multi-platform image required → push with `docker buildx build --platform linux/amd64,linux/arm64 --push`.
- Push fails with denied permissions → verify repository existence and token scopes before retrying.

## Failure modes & recovery

- **F1 Unauthorized:** detect `denied` or `unauthorized` → log in with the correct account and least-privilege push scope.
- **F2 Wrong repository:** detect image under an unexpected namespace → retag and push to the approved path; remove the mistaken tag if policy requires.
- **F3 Mutable tag drift:** detect `latest` pointing to unexpected digest → deploy by immutable tag or digest.
- **F4 Architecture missing:** detect deployment pull succeeds but runtime fails on platform → publish the required platform manifest.

## Verification

Run `docker push REGISTRY.example.com/team/myapp:TAG` followed by `docker buildx imagetools inspect REGISTRY.example.com/team/myapp:TAG`; push exits 0 and remote inspection shows the expected digest and platform.

## Variations

- `Amazon ECR`: authenticate with `aws ecr get-login-password | docker login --username AWS --password-stdin`.
- `GitHub Container Registry`: use `gh auth token` or a fine-grained token with package write permission.
- `Google Artifact Registry`: configure Docker auth with `gcloud auth configure-docker REGION-docker.pkg.dev`.

## Safety & privacy

Medium risk because pushed images can be consumed by deployments. Do not push images containing secrets or unreviewed code, use least-privilege registry tokens, and avoid overwriting release tags unless the release process explicitly allows it.
