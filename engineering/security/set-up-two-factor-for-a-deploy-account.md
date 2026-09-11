---
name: set-up-two-factor-for-a-deploy-account
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

You enable two-factor authentication for a deploy account or replace it with a safer machine identity, then verify deployments still work without weakening access controls.

## Preconditions

- Owner access to the deploy account, identity provider, and deployment platform.
- Inventory of CI jobs, tokens, SSH keys, and integrations using the account.
- Recovery codes or break-glass process approved before enabling 2FA.

## Steps

1. **Inventory account usage.** Review recent logins, tokens, SSH keys, and CI secrets connected to the deploy account. → *Expect:* every deployment path using the account is known.
2. **Prefer machine identities for automation.** Replace human deploy accounts with service accounts, deploy keys, GitHub Apps, OIDC federation, or platform robot users where supported. → *Expect:* automation does not depend on a shared human login.
3. **Choose phishing-resistant MFA when possible.** Use security keys/WebAuthn; use TOTP only where hardware keys are unavailable. → *Expect:* at least two approved factors are available before enforcement.
4. **Store recovery material securely.** Save recovery codes in an approved password manager or break-glass vault with restricted access. → *Expect:* account recovery is possible without sharing codes broadly.
5. **Enable 2FA in the provider UI.** Follow the identity provider or platform 2FA setup flow for the account. → *Expect:* the provider reports 2FA enabled and recent session prompts are satisfied.
6. **Rotate legacy tokens if required.** Some platforms invalidate or require stronger token scopes after 2FA; create least-privilege replacements and update CI secrets. → *Expect:* CI has current tokens or OIDC configuration.
7. **Run a deployment dry run or staging deploy.** Trigger the normal pipeline. → *Expect:* deployment authentication succeeds without interactive 2FA prompts in automation.

## Decision points

- Account is shared by humans → split into named user accounts plus service identities.
- Platform supports OIDC federation → prefer it over long-lived deploy tokens.
- Enabling 2FA will invalidate tokens → rotate and update CI in the same maintenance window.
- No recovery path exists → create one before enabling 2FA.

## Failure modes & recovery

- **F1 CI starts prompting for 2FA:** detect pipeline auth failure → replace the login-based credential with a token, app, or OIDC role.
- **F2 Lost factor:** detect inability to log in → use stored recovery codes or break-glass admin process.
- **F3 Overbroad replacement token:** detect token with admin scopes → create a least-privilege token and revoke the broad one.
- **F4 Shared account persists:** detect multiple humans using one credential → migrate each person to named accounts and audit access.

## Verification

The provider security page or API reports 2FA enabled for the deploy account, recovery codes are stored in the approved vault, and a staging deployment pipeline exits 0 using non-interactive automation credentials.

## Variations

- `GitHub/GitLab`: prefer deploy keys, GitHub Apps, project access tokens, or OIDC cloud roles over shared users.
- `Cloud providers`: use workload identity federation or service accounts with MFA-required human admin access.
- `PaaS`: use team roles and pipeline tokens scoped to one app/environment.

## Safety & privacy

Medium risk because misconfigured 2FA can lock out deployments. Do not share TOTP seeds in chat, keep recovery codes restricted, and replace shared human accounts with auditable service identities.
