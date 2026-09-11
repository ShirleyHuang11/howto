---
name: pass-secrets-to-a-container
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

You provide secrets to a container at runtime without baking them into the image, committing them to source control, or printing them in logs.

## Preconditions

- The application names the required secret variables or file paths.
- A local, CI, or orchestrator secret source is available.
- You know whether the app reads environment variables, mounted files, or a secret manager.

## Steps

1. **List required secrets by name only.** Document keys such as `DATABASE_URL` or `API_TOKEN` without values. → *Expect:* the application contract is clear and no secret is exposed.
2. **Remove secrets from build inputs.** Check Dockerfile, Compose file, and `.dockerignore` so `.env`, keys, and credentials are not copied into the image. → *Expect:* secrets are absent from image layers.
3. **Choose a runtime delivery method.** [local | orchestrator] use `--env-file .env.local`, Docker secrets, Kubernetes Secrets, or a cloud secret manager. → *Expect:* the secret value is supplied only when the container runs.
4. **Run the container with secrets.** For local testing, run `docker run --rm --env-file .env.local myapp:dev`. → *Expect:* the app starts and can read required secret names.
5. **Avoid logging values.** Ensure startup validation logs only missing key names, not values. → *Expect:* logs confirm presence without printing the secret.
6. **Verify the image does not contain secrets.** Run `docker history --no-trunc myapp:dev` and scan the build context if tooling exists. → *Expect:* no secret values appear in image history or files.
7. **Rotate if exposure occurred.** ⚠️ *Irreversible:* rotation invalidates the old credential; confirm all dependent deployments can receive the new secret before revoking. → *Expect:* the new secret works and the old one is disabled.

## Decision points

- Secret is needed during build for private dependencies → use BuildKit `--secret`, not `ARG` or `ENV`.
- Secret changes frequently → use an external secret manager and restart or reload containers intentionally.
- Secret is multi-line, such as a private key → mount it as a file when env var escaping is error-prone.

## Failure modes & recovery

- **F1 Secret baked into image:** detect value in `docker history` or filesystem → rotate the secret and rebuild with runtime secret injection.
- **F2 Missing secret at runtime:** detect startup validation failure → provide the secret through the environment, mounted file, or orchestrator configuration.
- **F3 Secret printed in logs:** detect raw token output → remove logging, purge accessible logs where possible, and rotate the secret.
- **F4 Wrong secret version:** detect authentication failures after rotation → verify deployment environment references the current secret name and version.

## Verification

Run `docker run --rm --env-file .env.local myapp:dev <config-check-command>` and `docker history --no-trunc myapp:dev | grep -F "$KNOWN_SECRET_VALUE"`; the config check exits 0 and the grep command finds no secret value.

## Variations

- `Docker Compose`: use `env_file` for local-only values or `secrets` for file-mounted secrets.
- `Kubernetes`: use `Secret` objects or external secret operators, then mount as env vars or files.
- `BuildKit`: pass build-only credentials with `docker build --secret id=name,src=path`.

## Safety & privacy

Medium risk because leaked secrets may grant production access. Use least-privilege credentials, never commit `.env` files with real values, avoid shell history leaks, and rotate immediately if a secret enters an image, repository, ticket, or log.
