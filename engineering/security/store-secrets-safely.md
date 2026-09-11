---
name: store-secrets-safely
domain: engineering
subdomain: security
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

You move application secrets out of source code and local notes into a managed secret store with least-privilege access and verifiable runtime injection.

## Preconditions

- Admin or maintainer access to the deployment platform and secret manager.
- A list of required secret names, owners, environments, and rotation expectations.
- No real secrets pasted into commits, tickets, or chat.

## Steps

1. **Inventory required secrets.** Search configuration references with `rg 'process\\.env|os\\.environ|getenv|SECRET|TOKEN|PASSWORD' .` and map each variable to an environment. → *Expect:* a table of secret keys and where each is consumed.
2. **Choose the managed storage location.** [BRANCH: cloud, use AWS Secrets Manager, GCP Secret Manager, or Azure Key Vault | platform, use GitHub Actions secrets, Kubernetes Secrets encrypted at rest, or a PaaS secret UI] → *Expect:* each environment has an approved secret backend.
3. **Create secrets with stable names.** Example: `aws secretsmanager create-secret --name prod/payments/stripe-api-key --secret-string "$STRIPE_API_KEY"` or `gh secret set STRIPE_API_KEY --env production`. → *Expect:* the secret appears in the manager and plaintext is not printed in logs.
4. **Grant least-privilege read access.** Bind only the deployment identity or runtime service account that needs the secret. → *Expect:* unrelated users and services cannot read the secret.
5. **Wire runtime injection.** Reference the secret through environment variables, volume mounts, or the platform's secret reference syntax; do not hardcode values in config files. → *Expect:* the running service receives the secret at startup.
6. **Remove unsafe copies.** Delete local `.env` values from shared storage, add `.env` to `.gitignore` if appropriate, and replace examples with placeholders like `STRIPE_API_KEY=replace-me`. → *Expect:* only placeholders remain in repository files.
7. **Run a secret scan and application check.** Run `gitleaks detect --source . --redact` or `trufflehog filesystem . --no-update`, then run the app's smoke test. → *Expect:* no live secrets are detected and the app still authenticates to dependencies.

## Decision points

- Secret already committed → rotate it and consider `engineering/remove-a-secret-from-git-history`.
- Same secret shared across environments → split dev, staging, and production credentials.
- Developers need local access → use a password manager or CLI login flow, not shared plaintext files.
- Secret controls production data → require owner approval before creating or rotating access.

## Failure modes & recovery

- **F1 Runtime cannot read secret:** detect startup errors such as `Missing API key` or `AccessDenied` → fix the service account binding and redeploy.
- **F2 Secret printed in logs:** detect plaintext in CI/app logs → revoke and rotate the secret, then scrub logs where the platform supports it.
- **F3 Wrong environment value:** detect staging calling production or vice versa → rename secrets with environment prefixes and redeploy with corrected references.
- **F4 Scanner false positive:** detect test fixtures flagged as secrets → replace with obvious fake values or add a narrow documented allowlist.

## Verification

`gitleaks detect --source . --redact` exits 0, the deployment identity can read only the needed secret, and the app smoke test exits 0 using the injected environment variable.

## Variations

- `Kubernetes`: use External Secrets Operator or sealed/encrypted secrets instead of committing raw Secret manifests.
- `GitHub Actions`: use environment secrets with required reviewers for production environments.
- `Docker Compose`: load local `.env` files only from developer machines and keep them out of version control.

## Safety & privacy

Medium risk because mishandled secrets can grant production access. Never echo secret values, prefer short-lived credentials where possible, restrict read permissions, and rotate any value that may have been exposed.
