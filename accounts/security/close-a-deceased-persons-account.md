---
name: close-a-deceased-persons-account
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h-2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You request closure, memorialization, or transfer of a deceased person's account through the provider's official process while preserving necessary estate records.

## Preconditions

- You are the executor, administrator, next of kin, legacy contact, or otherwise authorized requester.
- You have the deceased person's full name, account identifier, email or username, date of death, and any required documents.
- You understand whether the goal is closure, memorialization, data export, subscription cancellation, or asset transfer.

## Steps

1. **Find the provider's official deceased-user process.** Search the provider help center for deceased user, memorialization, estate, next of kin, or account closure. → *Expect:* you locate an official form, mailing address, or support process.
2. **Gather required documents.** Prepare a death certificate and proof of authority such as letters testamentary, letters of administration, court appointment, notarized next-of-kin statement, or legacy-contact access key if required. → *Expect:* documents match the provider's listed requirements.
3. **Decide the requested outcome.** [BRANCH: social account, choose memorialize or close | financial/subscription account, cancel billing or transfer assets through estate process | cloud/email account, request closure or limited data access if legally available] → *Expect:* one requested action is clearly chosen.
4. **Back up estate-relevant records you are authorized to access.** Save invoices, subscription details, account numbers, or provider correspondence without bypassing passwords or privacy law. → *Expect:* necessary estate records are preserved.
5. **Submit the official request.** Upload or mail documents through the provider's official channel. ⚠️ *Irreversible:* confirm the account identifier and requested action before submitting, because closure may permanently delete data or access. → *Expect:* the provider issues a case number, confirmation email, or mailed receipt.
6. **Stop recurring charges.** If the account bills a card or bank account, notify the provider and estate financial institution as appropriate. → *Expect:* future billing is canceled, suspended, or under review.
7. **Track the case to completion.** Respond to document requests and record dates, case numbers, and representative names. → *Expect:* the provider confirms closure, memorialization, transfer, or denial with next steps.
8. **Store final confirmation with estate records.** Keep the closure or memorialization confirmation, cancellation notice, and any refund or transfer records. → *Expect:* the estate file shows the account's final status.

## Decision points

- Account contains financial assets, domain names, royalties, or business records → consult the executor, attorney, or court process before closure.
- Provider offers memorialization → choose it when public profile preservation matters and private data access is not needed.
- You lack legal authority → request guidance from the executor or probate court rather than using the deceased person's password.

## Failure modes & recovery

- **F1 Documents rejected:** detect provider says proof is insufficient → obtain certified death certificate or current court appointment documents.
- **F2 Wrong account targeted:** detect mismatched email, username, or profile → stop and correct the identifier before approving closure.
- **F3 Billing continues:** detect charges after request → contact provider billing and dispute through the estate's card issuer or bank.
- **F4 Data needed after closure:** detect missing records after deletion → use saved exports, invoices, or legal discovery; provider recovery may be impossible.
- **F5 Unauthorized requester denied:** detect denial for lack of authority → have the executor, administrator, or legacy contact submit the request.

## Verification

The provider has issued written confirmation that the deceased person's account is closed, memorialized, transferred, or otherwise resolved, recurring billing has stopped, and the estate file contains the case number and final status.

## Variations

- `us`: estates commonly use certified death certificates and letters testamentary or letters of administration, but probate terminology varies by state.
- Social networks: memorialization may preserve the profile while preventing new logins.
- Financial, healthcare, and government accounts: closure or access usually requires formal estate authority and may not be available through ordinary customer support.

## Safety & privacy

High risk because account closure can permanently delete data, affect estate assets, and expose private communications. Confirm legal authority, account identity, and desired outcome before submitting; do not impersonate the deceased or bypass access controls with stored passwords unless legal counsel and provider rules allow it.
