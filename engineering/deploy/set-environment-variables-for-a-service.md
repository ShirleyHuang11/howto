---
name: set-environment-variables-for-a-service
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You add or update service environment variables in the runtime platform and verify the service reads them correctly. Secrets are stored in the platform's secret manager rather than committed to source control.

## Preconditions

- You know the exact service, environment, variable names, and intended values.
- Sensitive values are available from an approved secret source.
- You can restart, redeploy, or roll the service if required for config changes to apply.

## Steps

1. **Classify each variable.** Separate non-secret config from secrets such as tokens, passwords, private keys, and connection strings. → *Expect:* every key is labeled as secret or non-secret.
2. **Check existing runtime config.** [BRANCH: Kubernetes, `kubectl get deploy <app> -n <ns> -o yaml` and secret references | Heroku, `heroku config -a <app>` | Docker Compose, inspect env files and secrets] → *Expect:* current values or references are known without printing secret plaintext unnecessarily.
3. **Store secrets in the platform secret mechanism.** [BRANCH: Kubernetes, create/update `Secret` or external secret reference | PaaS, set encrypted config vars | cloud, use Secret Manager/Parameter Store] → *Expect:* the secret exists with the expected key name and limited access.
4. **Attach variables to the service.** Update deployment manifests, platform settings, or service config to reference the new keys. → *Expect:* the service spec includes the variable names or secret references.
5. **Roll or restart the service if needed.** [BRANCH: Kubernetes, `kubectl rollout restart deployment/<app> -n <ns>` | systemd, `systemctl restart <service>` | PaaS, config set triggers a release] → *Expect:* new instances start with the updated environment.
6. **Verify the process sees the variables.** Use a safe diagnostic endpoint, application startup log, or container exec that prints only key presence, not secret values. → *Expect:* the app reports config loaded and no missing-variable errors.
7. **Run service health checks.** Execute `curl -fsS https://<host>/healthz` or a platform health command. → *Expect:* health check returns 200 and rollout is healthy.
8. **Remove obsolete variables when safe.** Delete unused keys after confirming no deployed version reads them. → *Expect:* config inventory contains only active keys.

## Decision points

- Variable is a secret → never store it in Git or plaintext CI logs.
- Changing value affects production behavior → schedule with deploy owner and keep rollback value available.
- App reads env only at startup → restart or roll pods after setting it.
- Multiple services share the key → update consumers in a controlled order.

## Failure modes & recovery

- **F1 Service fails to boot:** detect missing env or validation error logs → restore previous value or add the missing key and restart.
- **F2 Secret value printed:** detect plaintext in logs or shell history → rotate the secret and remove exposed logs where possible.
- **F3 Config set but not applied:** detect old behavior after update → restart processes or verify the correct environment/namespace.
- **F4 Wrong environment changed:** detect staging value in production or vice versa → revert immediately and add environment labels to config commands.

## Verification

The platform shows the expected variable names or secret references on the target service, rollout status is healthy, and `curl -fsS https://<host>/healthz` exits 0 with no missing-config errors in logs.

## Variations

- `Kubernetes`: use `Secret`, `ConfigMap`, `envFrom`, and rollout restarts.
- `Heroku`: `heroku config:set KEY=value -a <app>` creates a new release.
- `AWS ECS`: update task definition environment and secrets, then deploy a new service revision.
- `systemd`: use `EnvironmentFile=` with protected permissions and restart the unit.

## Safety & privacy

Medium risk because config changes can break production and secrets can leak. Use secret managers, avoid echoing values, restrict access, keep previous values for rollback, and confirm the target environment before changing production.
