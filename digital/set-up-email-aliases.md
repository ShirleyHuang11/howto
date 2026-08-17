---
name: set-up-email-aliases
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create email aliases so you can separate identities, filter mail, and disable exposed addresses without replacing your main inbox.

## Preconditions

- Your email provider, domain host, or alias service supports aliases.
- You can access account security settings and recovery options.

## Steps

1. **Choose alias strategy.** [BRANCH: provider alias | custom domain | relay service] use provider aliases for simplicity, a custom domain for control, or a relay for disposable forwarding. → *Expect:* the alias source matches your needs.
2. **Create the alias.** Add the alias in the provider settings or relay dashboard and point it to your real inbox. → *Expect:* the alias appears as active.
3. **Send a test message.** Email the alias from another account and confirm it arrives in the main inbox. → *Expect:* forwarding works.
4. **Set filters and labels.** Route mail from the alias to a folder or label and mark the service it belongs to. → *Expect:* alias mail is easy to identify.
5. **Configure sending if needed.** Add send-as settings, verification, SPF, DKIM, or DMARC only when you must reply from the alias. → *Expect:* outgoing mail does not reveal the wrong address.
6. **Record the mapping.** Save which alias belongs to which site in a password manager or account note. → *Expect:* you can disable a leaked alias later.

## Decision points

- You need anonymity from the recipient → a normal alias may still reveal your name, domain, IP context, or billing identity.
- You run a custom domain → configure authentication records before sending mail at scale.
- A site rejects aliases → use a stable provider alias rather than a temporary-looking address.

## Failure modes & recovery

- **F1 Mail not delivered:** detect test message missing → recover by checking forwarding, spam, DNS records, or provider limits.
- **F2 Real address exposed:** detect replies show the main address → recover by fixing send-as identity before replying.
- **F3 Alias spammed:** detect unwanted mail to one alias → recover by disabling that alias and updating the affected account.

## Verification

A test email to the alias reaches the correct inbox, is labeled or filtered, and any reply path uses the intended sender address.

## Variations

- `custom-domain`: use catch-all aliases only if you can handle spam and filtering.
- `work`: follow organization identity and retention policies.
- `shopping`: create one alias per merchant to identify leaks.

## Safety & privacy

Medium risk because aliases affect account recovery and identity. Keep the main mailbox secured with strong authentication, and do not rely on aliases alone for anonymity.
