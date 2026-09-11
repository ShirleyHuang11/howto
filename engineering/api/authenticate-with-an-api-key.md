---
name: authenticate-with-an-api-key
domain: engineering
subdomain: api
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

Authenticate API requests with an API key while keeping the key secret, scoped, rotatable, and verifiable.

## Preconditions

- The provider supports API-key authentication and documents the required header or query parameter.
- You can create or obtain a least-privilege key for the environment.
- A secret manager or local `.env` workflow exists.

## Steps

1. **Create a scoped key.** In the provider console, create a key limited to the needed environment, resource, and permissions. → *Expect:* the console shows a new key and scope metadata.
2. **Store the key securely.** Save it in a secret manager or local `.env` ignored by version control, for example `API_KEY=...`. → *Expect:* the key is available to the app but absent from tracked files.
3. **Send the key in the documented location.** Prefer headers, for example `curl -H "X-API-Key: $API_KEY" "$API_BASE_URL/v1/widgets"`. → *Expect:* the API accepts the request with a 2xx status.
4. **Validate missing-key behavior.** Repeat the request without the header. → *Expect:* the API returns `401` or the provider's documented authentication error.
5. **Redact logs.** Configure request logging to omit `Authorization`, `X-API-Key`, and query strings that may contain secrets. → *Expect:* logs show redacted values.
6. **Add configuration checks.** Fail startup if the required key is absent in environments that need it. → *Expect:* misconfigured deployments fail fast with a clear error.
7. **Document rotation.** Record where the key is created, stored, and consumed. → *Expect:* another engineer can rotate it without searching the codebase.

## Decision points

- Provider allows query-string keys → avoid them unless required because URLs leak into logs.
- Key grants broad production access → request narrower scopes or separate environment keys.
- Multiple services use the same key → split keys per service for attribution and rotation.
- User-delegated access is required → use OAuth2 instead of an API key.

## Failure modes & recovery

- **F1 Key committed to git:** detect secret scanning alert → revoke the key immediately, create a replacement, and remove the secret from history if needed.
- **F2 401 after deploy:** detect authentication failures → check secret name, deployment environment, and header format.
- **F3 Over-permissioned key:** detect key can access unrelated resources → rotate to a least-privilege key.
- **F4 Logs expose key:** detect raw header or URL in logs → purge accessible logs where possible, rotate the key, and redact logging.

## Verification

`curl -sS -o /tmp/auth-ok.json -w '%{http_code}' -H "X-API-Key: $API_KEY" "$API_BASE_URL/v1/widgets"` returns a documented 2xx status, while the same request without the key returns the documented authentication failure status.

## Variations

- `Bearer token`: use `Authorization: Bearer $API_KEY` when documented by the provider.
- `Serverless`: store the key in platform secrets and redeploy or restart to apply it.
- `CI`: pass the key through encrypted CI secrets and mask it in job logs.

## Safety & privacy

Medium risk because leaked keys can grant service access. Use least privilege, never store real keys in source, rotate on exposure, and restrict who can read production secrets.
