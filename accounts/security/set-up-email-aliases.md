---
name: set-up-email-aliases
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

You create separate email aliases for different account categories so you can filter mail, reduce exposure of your primary address, and disable a leaked alias without changing your main inbox.

## Preconditions

- Access to your email provider account and its settings.
- A provider that supports aliases, plus-addressing, custom domains, or hide-my-email addresses.
- A short list of categories you want to separate, such as banking, shopping, newsletters, and travel.

## Steps

1. **Confirm what kind of alias your provider supports.** Check account settings for aliases, forwarding addresses, custom-domain addresses, or masked email addresses. → *Expect:* you know whether aliases are true alternate addresses, plus-addresses, or relay addresses.
2. **Choose a naming scheme.** Pick labels that are meaningful but not revealing, such as `shop`, `travel`, or random relay names for sensitive accounts. → *Expect:* a written list of aliases and intended uses.
3. **Create the alias in the provider settings.** Add the alias, verify ownership if prompted, and enable receiving mail for it. → *Expect:* the alias appears as active or verified in the account settings.
4. **Send a test message to the alias.** Use a different account or trusted sender to send a short test. → *Expect:* the test message arrives in your main inbox or designated folder.
5. **Create filters for each alias.** Route mail addressed to the alias into a label or folder, and optionally mark low-priority aliases as non-urgent. → *Expect:* future messages to that alias are automatically labeled or moved.
6. **Update accounts gradually.** Change email addresses on selected services one at a time, starting with low-risk accounts before financial or identity accounts. → *Expect:* each service sends a verification email to the alias and shows the alias on its profile page.
7. **Document where each alias is used.** Store the alias map in a password manager note, not in a public spreadsheet. → *Expect:* you can identify which service used an alias if it later receives spam.

## Decision points

- Provider only supports plus-addressing -> use it for filtering, but do not treat it as private because many sites can infer the base address.
- Sensitive account such as banking or healthcare -> prefer a stable alias you control long term, not a temporary relay that might be discontinued.
- Alias starts receiving unrelated spam -> identify the likely source, change that account's address, then disable or filter the alias.

## Failure modes & recovery

- **F1 Alias cannot receive mail:** senders get a bounce or tests never arrive -> recheck spelling, activation status, and whether receiving is enabled.
- **F2 Website rejects the alias format:** a signup form refuses plus signs or relay domains -> use a standard alias address from your provider or a custom-domain alias.
- **F3 Verification goes to spam:** account-change email does not appear in the inbox -> search all mail for the recipient alias and check spam, quarantine, and focused inbox views.
- **F4 Alias reveals too much:** the alias includes your full name or account type -> replace it before using it broadly.

## Verification

At least one alias is active, a test message sent to it arrives in your inbox, and a filter or label shows the alias-specific mail route working.

## Variations

- Gmail: plus-addressing works automatically, but alternate send-as aliases require setup under account settings.
- Outlook/Microsoft: account aliases can be added under Microsoft account sign-in preferences and may also be used for login unless disabled.
- Apple iCloud+: Hide My Email creates relay addresses that forward to your Apple ID inbox.

## Safety & privacy

Medium risk because aliases can protect or expose account identity. Keep the alias map in a password manager, avoid using disposable aliases for critical accounts, and confirm you can receive recovery messages before changing important account emails.
