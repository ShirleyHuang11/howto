---
name: authenticate-with-oauth2
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Authenticate to an API using the correct OAuth2 flow, store tokens safely, refresh access, and verify scopes before using protected resources.

## Preconditions

- The provider's OAuth2 authorization, token, and revocation endpoints are known.
- A client ID is registered and redirect URIs are configured.
- You know whether access is user-delegated or machine-to-machine.

## Steps

1. **Choose the OAuth2 flow.** Use authorization code with PKCE for user login, client credentials for server-to-server access, and device code for limited-input devices. → *Expect:* the selected flow matches the application type and provider policy.
2. **Register redirect URIs exactly.** Configure `https://app.example.com/oauth/callback` and local callback URIs as needed. → *Expect:* provider console accepts the URIs and rejects unregistered redirects.
3. **Request minimal scopes.** Ask only for scopes needed by the feature, such as `read:invoices`. → *Expect:* consent screen and issued token list the intended scopes.
4. **Implement the authorization request.** Include `state` and, for PKCE, `code_challenge` with `S256`. → *Expect:* the callback contains `code` and the original `state`.
5. **Exchange the code server-side.** POST to the token endpoint with the code, redirect URI, client authentication if required, and PKCE verifier. → *Expect:* provider returns access token, expiry, scopes, and optionally refresh token.
6. **Store tokens securely.** Encrypt refresh tokens at rest and keep access tokens short-lived. → *Expect:* tokens are not visible in logs, URLs, or client-side storage unless the flow requires it.
7. **Refresh and revoke deliberately.** Refresh before expiry and revoke tokens when disconnecting an account. → *Expect:* long-running integrations continue without prompting and disconnect stops access.
8. **Test protected calls.** Call the resource API with `Authorization: Bearer $ACCESS_TOKEN`. → *Expect:* valid scope returns 2xx and missing scope returns the documented authorization error.

## Decision points

- Browser-based app with no backend → use authorization code with PKCE, not implicit flow.
- Daemon or cron job → use client credentials if the provider supports app-only access.
- Offline access needed → request refresh-token/offline scope and handle rotation.
- Multi-tenant app → bind tokens to the tenant and provider account ID.

## Failure modes & recovery

- **F1 Redirect URI mismatch:** detect provider error like `redirect_uri_mismatch` → update the registered URI or request parameter exactly.
- **F2 Invalid state:** detect callback state mismatch → reject the callback and restart authorization.
- **F3 Refresh token expired:** detect token endpoint `invalid_grant` → mark the integration disconnected and ask the user to reconnect.
- **F4 Missing scope:** detect `403` or provider scope error → request only the additional needed scope through a new consent flow.

## Verification

An OAuth callback test validates `state`, token exchange returns an access token with expected scopes, `curl -H "Authorization: Bearer $ACCESS_TOKEN" "$API_BASE_URL/v1/me"` returns 2xx, and a test with insufficient scope returns the documented error.

## Variations

- `PKCE`: required for public clients and recommended for authorization-code flows.
- `OIDC`: validate the ID token issuer, audience, expiry, and nonce when using login identity.
- `Client credentials`: no refresh token is usually needed; request a new access token when expired.

## Safety & privacy

Medium risk because OAuth tokens can access user data. Use HTTPS redirect URIs, validate `state`, encrypt refresh tokens, request least privilege, and revoke tokens on disconnect or suspected compromise.
