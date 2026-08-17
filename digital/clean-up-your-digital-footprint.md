---
name: clean-up-your-digital-footprint
domain: digital
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 2h-4h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Reduce unnecessary public and semi-public information about you across accounts, search results, old posts, and data-sharing settings.

## Preconditions

- You can access your main email, password manager, social accounts, and search engine.
- You have time to review before deleting anything permanently.

## Steps

1. **Inventory accounts.** Search your password manager, email, app stores, and browser history for old accounts and profiles. → *Expect:* you have a list of places to review.
2. **Search yourself.** Search your name, usernames, phone numbers, emails, and image results in a private window. → *Expect:* public exposures are listed.
3. **Triage by risk.** Prioritize home address, phone, family links, workplace, old resumes, public photos, and accounts with reused passwords. → *Expect:* the highest-risk items are first.
4. **Update privacy settings.** Limit profile visibility, search indexing, contact discovery, ad personalization, and public friend lists. → *Expect:* active accounts expose less information.
5. **Remove or edit old content.** Delete, unpublish, anonymize, or request removal for posts and profiles that no longer need to be public. ⚠️ *Irreversible:* permanent deletion may remove photos, messages, or purchase records; export needed data first. → *Expect:* unnecessary content is removed or queued for removal.
6. **Close unused accounts.** [BRANCH: delete | deactivate | keep] delete low-value accounts, deactivate uncertain ones, and keep accounts needed for receipts or recovery. → *Expect:* account status matches future need.
7. **Secure what remains.** Change reused passwords, enable multi-factor authentication, and remove stale connected apps. → *Expect:* remaining accounts are harder to abuse.
8. **Track follow-up.** Record removal requests, deletion windows, and accounts that need rechecking. → *Expect:* pending cleanup is not forgotten.

## Decision points

- The account contains purchases, tax records, messages, or creative work → export before deleting.
- Search results expose your address or phone → combine account cleanup with data broker opt-outs.
- Harassment or stalking is involved → preserve evidence before removal and consider professional support.

## Failure modes & recovery

- **F1 Lost data:** detect deleted content was needed → recover from exports, backups, or platform grace periods.
- **F2 Profile reappears:** detect cached or broker-fed search results → recover by requesting cache refreshes and source removal.
- **F3 Account takeover risk:** detect reused passwords during cleanup → recover by changing passwords and enabling multi-factor authentication first.

## Verification

Your inventory shows reviewed accounts, high-risk public exposures are removed or restricted, remaining accounts have unique passwords and MFA where available, and pending removals have follow-up dates.

## Variations

- `job-search`: keep professional profiles public but remove personal contact details.
- `creator`: preserve attribution and portfolio links while removing private metadata.
- `family`: review child, spouse, or household information that exposes shared addresses.

## Safety & privacy

Medium risk because cleanup can delete useful records and can alert platforms or people to changes. Export first, preserve evidence for harassment, and assume screenshots or archives may persist after deletion.
