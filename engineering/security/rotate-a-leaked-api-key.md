---
name: rotate-a-leaked-api-key
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: high
prerequisites: [engineering/store-secrets-safely]
status: draft
last_verified: 2026-09-11
---

## Goal

You replace a leaked API key everywhere it is used, verify consumers work with the new key, and revoke the old key so it can no longer be abused.

## Preconditions

- Confirmed key identifier, affected provider, environments, and services.
- Admin access to the provider console and the secret manager.
- Incident owner approval for production key revocation.

## Steps

1. **Freeze unsafe propagation.** Stop sharing the leaked value, restrict ticket visibility, and record where it was found without reposting the secret. → *Expect:* responders know the affected key without spreading plaintext.
2. **Identify every consumer.** Search references by key name, not value: `rg 'STRIPE_API_KEY|PAYMENTS_API_KEY|provider_key_name' .` and inspect secret manager usage/audit logs. → *Expect:* a list of services, jobs, and environments that need the replacement.
3. **Create a replacement key with least privilege.** In the provider console or CLI, create a new scoped key matching only the required permissions. → *Expect:* the new key exists and has a visible key ID or creation timestamp.
4. **Store the new key in the secret manager.** Use the existing secret name or versioned secret path so consumers can read it through normal injection. → *Expect:* the secret backend contains the new version and does not print it in logs.
5. **Deploy or restart consumers.** Roll out the secret update through CI/CD, then check application logs and provider authentication metrics. → *Expect:* consumers authenticate successfully with the new key.
6. **Run functional smoke tests.** Example: `curl -fsS -H "Authorization: Bearer $API_KEY" "$PROVIDER_HEALTH_ENDPOINT"` from the service environment, or run the integration test suite. → *Expect:* requests succeed with 2xx responses or tests exit 0.
7. **Revoke the leaked key.** ⚠️ *Irreversible:* once revoked, workloads still using the old key will fail; confirm the new key is deployed and smoke tests pass first. Revoke or delete the old key in the provider console. → *Expect:* the old key is disabled and provider audit logs show revocation.
8. **Verify old key rejection.** Attempt a harmless request using the old key ID/value from a secure incident terminal if policy permits. → *Expect:* the provider returns 401/403 for the old key while the new key still succeeds.

## Decision points

- Key grants production write access → treat as an incident and review audit logs for abuse before closing.
- Provider supports overlapping keys → deploy the new key before revoking the old one.
- Provider allows only one active key → schedule a short maintenance window and restart consumers immediately.
- Key was committed to git → also run `engineering/remove-a-secret-from-git-history`.

## Failure modes & recovery

- **F1 Unknown consumers:** detect 401s after revocation → temporarily reissue a scoped key, update the missed consumer, and document the dependency.
- **F2 New key lacks permissions:** detect 403s from smoke tests → compare scopes with the old key and add only required permissions.
- **F3 Secret cache delay:** detect old key usage after deployment → restart workers, clear secret caches, or wait for documented propagation.
- **F4 Suspected abuse:** detect unexpected provider activity → disable affected resources, preserve logs, and escalate to security/incident response.

## Verification

The new-key smoke test returns 2xx or the integration suite exits 0, the provider audit log shows the old key revoked, and a test request with the old key returns 401 or 403.

## Variations

- `AWS IAM access keys`: create a second access key, deploy it, then deactivate and delete the old key after CloudTrail review.
- `GitHub tokens`: use fine-grained tokens or GitHub Apps with minimal repository permissions.
- `Payment providers`: validate with a non-mutating endpoint before revoking the old production key.

## Safety & privacy

High risk because revocation can break production and the leaked key may already be abused. Never paste keys into chat, keep incident notes access-limited, verify deployment before revocation, and preserve audit logs for investigation.
