---
name: sign-and-verify-a-jwt
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [engineering/store-secrets-safely]
status: draft
last_verified: 2026-09-11
---

## Goal

You issue JSON Web Tokens with explicit claims and verify signature, algorithm, issuer, audience, and expiry before trusting them.

## Preconditions

- A maintained JWT library is available for the application language.
- Signing keys or secrets are stored in a managed secret store.
- Issuer, audience, token lifetime, and key-rotation approach are defined.

## Steps

1. **Choose an algorithm deliberately.** Prefer asymmetric `RS256`/`ES256` for multi-service verification; use `HS256` only when all verifiers can safely share one secret. → *Expect:* the algorithm is fixed in config and not accepted from untrusted input.
2. **Create minimal token claims.** Include `iss`, `aud`, `sub`, `iat`, `exp`, and `jti` where replay tracking is needed; avoid sensitive personal data. → *Expect:* tokens contain only required claims and a short expiry.
3. **Sign with managed keys.** Load the signing key from the secret manager or KMS, not source files. → *Expect:* signing succeeds without printing the key.
4. **Verify with strict options.** Configure the JWT library to require the expected algorithm, issuer, audience, and expiration. Example Node: `jwt.verify(token, publicKey, { algorithms: ['RS256'], issuer, audience })`. → *Expect:* invalid signature, wrong audience, wrong issuer, and expired tokens are rejected.
5. **Add key IDs for rotation.** Set `kid` in the header and publish or configure a JWKS/public-key lookup for verifiers. → *Expect:* verifiers can select the correct key without trying every key blindly.
6. **Write positive and negative tests.** Test valid token, expired token, wrong audience, `alg: none`, wrong key, and tampered payload. → *Expect:* only the valid token passes.
7. **Run integration verification.** Call a protected endpoint with a valid and invalid token using `curl`. → *Expect:* valid token returns 2xx and invalid token returns 401/403.

## Decision points

- Multiple services verify tokens → use asymmetric signing and JWKS.
- Token revocation is required → use short expiries plus server-side session/revocation state.
- Claims include authorization roles → verify roles server-side and keep token lifetime short.
- Third-party identity provider signs tokens → fetch keys from its JWKS and pin issuer/audience.

## Failure modes & recovery

- **F1 Algorithm confusion:** detect library accepts `none` or unexpected algorithms → set explicit `algorithms` allowlist.
- **F2 Expired valid sessions:** detect widespread 401s after clock drift → sync clocks and allow small clock tolerance.
- **F3 Key rotation outage:** detect verifiers missing new `kid` → publish new public key before signing with it.
- **F4 Sensitive claims leaked:** detect PII in tokens → stop issuing those claims and rotate affected tokens where possible.

## Verification

JWT unit tests exit 0, tampered/expired/wrong-audience tokens are rejected, and `curl` to a protected endpoint returns 2xx with a valid token and 401 or 403 with an invalid token.

## Variations

- `OAuth/OIDC`: validate ID/access tokens with the provider's issuer, audience, and JWKS.
- `HS256`: rotate shared secrets carefully because every verifier can also sign tokens.
- `KMS-backed signing`: call KMS for signing and expose only public keys to verifiers.

## Safety & privacy

Medium risk because weak verification can grant unauthorized access. Never log full tokens, avoid long-lived bearer tokens, keep private keys in managed storage, and pin algorithms and audiences.
