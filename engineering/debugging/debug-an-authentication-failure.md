---
name: debug-an-authentication-failure
domain: engineering
subdomain: debugging
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

You determine why a login, token exchange, API request, or session check fails, then fix the authentication path without exposing secrets or weakening access control.

## Preconditions

- You know the failing user or service identity, environment, endpoint, expected auth mechanism, and observed status code.
- You can inspect server logs, identity-provider logs, and client storage in a safe environment.
- You have test credentials or a non-production identity.

## Steps

1. **Classify the failure point.** Identify whether the error occurs at credential submission, OAuth/OIDC redirect, token validation, session cookie use, refresh, or authorization check. → *Expect:* one named stage to investigate.
2. **Capture redacted request and response metadata.** Record status, headers excluding secrets, redirect URL without tokens, request ID, and timestamp. → *Expect:* enough metadata to correlate logs without leaking credentials.
3. **Check server and identity-provider logs.** Search by request ID, subject, client ID, or timestamp. → *Expect:* a concrete error such as invalid audience, expired token, bad signature, missing cookie, or disabled account.
4. **Inspect token claims safely.** Decode JWT headers and claims locally without publishing the token, for example `python -m jwt.cli --no-verify "$TOKEN"` if available or a local decoder. → *Expect:* issuer, audience, expiry, subject, scopes, and key ID match expectations.
5. **Verify clocks and key material.** Check system time, JWKS key ID, client secret version, certificate expiry, and redirect URI registration. → *Expect:* no clock skew, stale key, or mismatched redirect URI remains unexplained.
6. **Fix the root cause.** Update client ID, redirect URI, audience, cookie attributes, scope request, key cache refresh, or token validation config. → *Expect:* the auth flow reaches the intended authenticated state in staging.
7. **Add an automated auth test.** Use a fake identity provider, signed test token, or integration environment to assert accepted and rejected cases. → *Expect:* valid credentials succeed and invalid credentials still fail.

## Decision points

- Status is `401` → focus on authentication proof: token, cookie, signature, expiry, issuer, or audience.
- Status is `403` → authentication may work; inspect roles, scopes, groups, tenant membership, or policy.
- Works in one browser only → inspect cookies, SameSite/Secure attributes, blocked third-party storage, and stale sessions.
- Works locally but fails in production → compare callback URLs, issuer URL, client ID, secret version, and TLS termination.

## Failure modes & recovery

- **F1 Secret leaked during debugging:** detect token or password in logs or shell history → revoke/rotate it and remove the artifact according to policy.
- **F2 Stale JWKS cache:** detect token key ID not found while provider has the key → refresh cache or reduce overly long cache TTL.
- **F3 Redirect URI mismatch:** detect provider error about callback URL → register the exact scheme, host, path, and port.
- **F4 Cookie not sent:** detect missing `Cookie` header in request → fix domain, path, `Secure`, `HttpOnly`, and `SameSite` attributes.

## Verification

An automated auth test exits 0 and a scripted request such as `curl -s -o /dev/null -w '%{http_code}' -H "Authorization: Bearer $TEST_TOKEN" "https://api.example.com/me"` returns `200` for a valid test token and `401` or `403` for invalid credentials as intended.

## Variations

- `OAuth/OIDC`: validate issuer, audience, redirect URI, scopes, nonce/state, and JWKS key ID.
- `session cookies`: inspect cookie domain, `SameSite`, CSRF token, server-side session store, and load-balancer stickiness.
- `API keys`: verify key prefix, active status, environment, rate limits, and permission scope.
- `mTLS`: inspect client certificate chain, SAN, expiry, and trust bundle.

## Safety & privacy

Medium risk because auth debugging touches credentials and access policy. Use test identities, redact tokens and cookies, avoid disabling validation to make tests pass, and require review for changes that broaden access.

