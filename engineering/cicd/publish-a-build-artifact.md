---
name: publish-a-build-artifact
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [engineering/cicd/set-up-a-ci-pipeline]
status: draft
last_verified: 2026-09-11
---

## Goal

You configure CI to build a distributable artifact, store it with the CI run or artifact registry, and verify that the downloaded artifact matches the expected contents.

## Preconditions

- The project has a deterministic build command and output directory or file.
- CI already installs dependencies successfully.
- You know retention requirements and whether artifacts are public, internal, or secret-bearing.

## Steps

1. **Build locally and identify outputs.** Run `npm run build`, `go build ./cmd/app`, `mvn package`, or the project command. → *Expect:* a known artifact path such as `dist/`, `target/app.jar`, or `build/app`.
2. **Clean before building in CI.** Ensure the CI job starts from a clean checkout and does not package stale output. → *Expect:* artifacts come only from the current commit.
3. **Add the CI build step.** Run the same build command after dependency installation. → *Expect:* CI creates the artifact path on a green build.
4. **Upload the artifact.** [GitHub Actions | GitLab CI] use the provider artifact feature with an explicit name and path. → *Expect:* the CI run shows a downloadable artifact.
5. **Set retention and access.** Configure retention days and ensure artifact visibility matches project policy. → *Expect:* artifacts are retained long enough and not broader than intended.
6. **Verify artifact contents.** Add a step such as `test -f dist/app.js` or `tar -tf release.tar.gz | rg '^app/'`. → *Expect:* required files exist before upload.
7. **Download from a completed run.** Use the CI UI or CLI to download the artifact and inspect it. → *Expect:* the downloaded artifact contains the expected current build output.

## Decision points

- Artifact contains secrets or `.env` files → stop and remove them from build output before publishing.
- Build output is very large → split artifacts, reduce debug assets, or use an artifact registry.
- Artifact is needed for deployment → include checksum, version, commit SHA, and immutable naming.
- Multiple platforms are built → include OS/architecture in artifact names.

## Failure modes & recovery

- **F1 Empty artifact:** detect upload warning or zero-byte download → verify build path and working directory.
- **F2 Stale files included:** detect files from previous builds → add clean steps and build into a fresh directory.
- **F3 Secret accidentally packaged:** detect credentials in artifact scan → delete the artifact if possible, rotate secrets, and fix packaging rules.
- **F4 Artifact expires too soon:** detect consumers cannot download it → adjust retention or publish to a registry with approved access.

## Verification

The CI build job exits 0, uploads a named artifact, and a download-and-inspect step or manual CLI check confirms required files and checksum, for example `sha256sum release.tar.gz` matches the value printed during CI.

## Variations

- `GitHub Actions`: use `actions/upload-artifact` and optionally `actions/download-artifact`.
- `GitLab CI`: use `artifacts: paths:` and `expire_in`.
- `Docker image`: publish to a container registry and verify by digest with `docker pull image@sha256:<digest>`.
- `language package`: publish to an internal package registry only after signing or checksum verification if policy requires it.

## Safety & privacy

Medium risk because artifacts may outlive the CI run and be shared. Never package secrets, private keys, local `.env` files, or customer data. Keep artifact permissions and retention aligned with the repository's confidentiality level.

