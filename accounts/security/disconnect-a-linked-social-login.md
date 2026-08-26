---
name: disconnect-a-linked-social-login
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You remove a "Sign in with Google/Apple/Facebook" style connection without locking yourself out of the account.

## Preconditions

- Access to the account that uses the linked social login.
- Access to the social identity provider account.
- A working email address and password method for the target account, or the ability to create one.

## Steps

1. **Confirm how you currently sign in.** Check whether the account has a local password, passkey, email magic link, or only social login. → *Expect:* you know what login methods exist before disconnecting anything.
2. **Add a fallback sign-in method.** Set a password, passkey, verified email, or backup codes if the service supports them. → *Expect:* at least one non-social login method is active.
3. **Test the fallback in a private window.** Log out or use an incognito window and sign in without the social provider. → *Expect:* you can access the account using the fallback method.
4. **Open connected accounts on the target service.** Look for linked accounts, login methods, social sign-in, or security settings. → *Expect:* the social provider is listed as connected.
5. **Disconnect the provider.** ⚠️ *Irreversible:* confirm the fallback login works before removing the linked login. → *Expect:* the provider disappears from the target service's login methods.
6. **Revoke access from the social provider too.** In Google, Apple, Meta, or other provider settings, remove the app's access. → *Expect:* the target service is no longer listed as an authorized app.
7. **Sign in one more time.** Use the fallback method after disconnecting. → *Expect:* login succeeds without the social provider.

## Decision points

- No fallback login can be added -> do not disconnect until support confirms another recovery route.
- You are disconnecting because the social account is compromised -> secure the social account first, then revoke sessions and linked apps.
- The target service uses hidden relay email -> verify the real account email before changing login methods.

## Failure modes & recovery

- **F1 Lockout after disconnect:** fallback login fails -> use account recovery or support with proof of ownership.
- **F2 Duplicate account created:** signing in by email opens an empty account -> contact support to merge or recover the original social-login account.
- **F3 Provider still shows access:** app remains authorized after disconnecting on the target service -> revoke it directly in provider settings.
- **F4 Email is inaccessible:** password reset goes to an old address -> update and verify the email before disconnecting.

## Verification

The target account no longer lists the social provider as a login method, the provider no longer lists the app as authorized, and a fresh login works without the social provider.

## Variations

- Apple private relay: the account email may be an Apple relay address; verify message delivery before changing it.
- Work SSO: organization-managed login may not be removable by the user.
- Gaming and payment accounts: unlinking can affect purchases, saves, or entitlements; read provider warnings first.

## Safety & privacy

Medium risk because disconnecting the only login method can lock you out. Confirm a working fallback login before removal and revoke access on both sides when finished.
