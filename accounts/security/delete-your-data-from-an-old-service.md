---
name: delete-your-data-from-an-old-service
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You remove personal data from an old online service, close or deactivate the account where appropriate, and keep proof of the request.

## Preconditions

- You can sign in or recover access to the service.
- You have downloaded anything you need to keep, such as receipts, photos, contacts, or records.
- You understand whether deletion is immediate, delayed, or only deactivation.

## Steps

1. **Sign in directly to the service.** Use the official website or app and avoid links from old emails unless you verify the destination. → *Expect:* your account settings are accessible.
2. **Download required records.** Export invoices, messages, photos, health records, tax documents, or purchase history before deletion. → *Expect:* needed records are stored somewhere you control.
3. **Remove sensitive content manually.** Delete saved cards, addresses, profile details, API keys, connected devices, and public posts if the service allows it. → *Expect:* the account contains less sensitive data before closure.
4. **Find the deletion path.** Look for Account, Privacy, Data, Delete account, Close account, or Contact privacy team. → *Expect:* you reach a deletion, erasure, or closure workflow.
5. **Submit the deletion request.** Confirm the account identifier and choose permanent deletion rather than marketing unsubscribe if that is your goal. ⚠️ *Irreversible:* confirm exports and obligations first because deletion may erase access permanently. → *Expect:* the service accepts the request or sends a confirmation email.
6. **Complete verification.** Click confirmation links, enter codes, or respond to the privacy team's identity check. → *Expect:* the request status becomes confirmed or processing.
7. **Revoke external access.** In Google, Apple, Facebook, password manager, or device settings, remove the old service's connected-account permissions. → *Expect:* the service no longer has delegated access.
8. **Record the outcome.** Save confirmation numbers, screenshots, dates, and stated deletion windows. → *Expect:* you have evidence if the account or data reappears.

## Decision points

- You need receipts for taxes or warranty → export records before deletion and store them securely.
- Service offers only deactivation → remove sensitive data manually and submit a privacy-law deletion request where available.
- Account has a subscription → cancel billing first and confirm no balance or contractual obligation remains.

## Failure modes & recovery

- **F1 Cannot log in:** use account recovery or contact support with proof of ownership.
- **F2 Deletion email never arrives:** check spam, resend, and confirm the account email is current.
- **F3 Service refuses deletion for legal retention:** ask what data is retained, why, and when it will be deleted.
- **F4 Account remains visible after deadline:** reopen the ticket with confirmation evidence and escalate to the privacy contact or regulator if applicable.

## Verification

The service confirms deletion, closure, or processing with a reference number or email, billing is canceled if applicable, and a later sign-in attempt shows the account is closed or pending deletion.

## Variations

- `us-california`: residents may have deletion rights under CCPA/CPRA for covered businesses.
- `eu-uk`: GDPR/UK GDPR erasure rights may apply, subject to legal retention exceptions.
- `financial-health-services`: providers may legally retain records even after closing online access.

## Safety & privacy

Medium risk because deletion can remove records you may later need and account data may include identity or payment details. Export important records and cancel subscriptions before confirming permanent deletion.
