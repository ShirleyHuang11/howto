---
name: open-a-bank-account
domain: finance
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

A current/checking account is open in your name at a bank you chose deliberately, with the card, online access, and any direct deposits or payments pointed at it.

## Preconditions

- Identity documents per your country's rules: government ID or passport, proof of address (utility bill, lease, registration certificate), and in some countries a tax or residence number.
- Basic clarity on what you need the account for: daily spending, salary deposit, savings, or a local account after moving countries. The use case picks the bank.

## Steps

1. **Choose the bank on fees and fit, not proximity nostalgia.** Compare three candidates on: monthly fee and how to waive it, ATM network, foreign transaction fees if you travel, app quality, and branch access if you value it. Online-only banks win on fees; branch banks win when you need a human. → *Expect:* one chosen bank and a named account type, with its fee schedule actually read.
2. **Gather the exact document list from the bank's site.** Newcomers: check which proofs of address are accepted before showing up; this is the step that fails immigrants and students most often, and some banks explicitly accept alternatives (employer letters, university letters). → *Expect:* every listed document in hand, originals where required.
3. **Apply online or book a branch appointment.** Online flows verify identity by document photo and a selfie or video call; branch flows do it at the desk. Answer the regulatory questions (occupation, source of funds, tax residency) accurately. They are legally required, not curiosity. → *Expect:* an application submitted and an account number issued, sometimes instantly, sometimes after a review of days.
4. **Complete the security setup the moment access arrives.** Set the online banking credentials from the bank's official app or site, enable the strongest offered 2FA, and store everything in your password manager (`accounts/enable-two-factor-authentication` applies in full). → *Expect:* you can log in, see the empty account, and the recovery paths point at you.
5. **Activate the card when it arrives and set the PIN.** Follow the mailed or in-app activation; test with one small purchase or an ATM balance check (`daily/errands/use-an-atm`). → *Expect:* a working card with a PIN only you know.
6. **Point your money at the account.** Salary: give the account details to payroll. Recurring payments: move them over deliberately, one list, one session (`finance/pay-a-bill-online` for each). Fund it with an initial transfer. ⚠️ *Irreversible:* typos in account numbers on inbound transfers are painful to unwind, so copy-paste details from the app rather than retyping. → *Expect:* a test deposit lands, and the payment list shows what moved and what remains.
7. **If this replaces an old account, run both in parallel for one full billing cycle.** Watch what still hits the old account, migrate the stragglers, then close the old one properly rather than leaving it to rot (`accounts/delete-an-account` logic applied to banking: get written confirmation of closure). → *Expect:* a clean cutover with no bounced payment in the gap.

## Decision points

- Student, newcomer, or credit-history-free: look for the accounts designed for exactly that (student accounts, basic accounts with a legal right to open in the EU, secured products in the US). The standard rejection is a product mismatch, not a personal verdict.
- Joint account: both parties present with documents; agree beforehand on either-to-sign vs both-to-sign, because changing it later is paperwork.
- Savings alongside: opening the linked savings account in the same session costs five minutes and is the cheapest commitment device banks offer.

## Failure modes & recovery

- **F1 Application rejected or stuck in review:** ask for the reason. Address-proof mismatches and name-spelling differences across documents cause most of it; fix the document and reapply, or try a bank with lighter requirements.
- **F2 Card never arrives:** report after the stated window; banks reissue routinely. Check the mailing address on file first, especially after a move.
- **F3 Locked out during setup:** use the bank's official recovery flow only, and never a phone number from a search ad. The callback rule from `daily/social/answer-a-phone-call` applies doubly to anything claiming to be your bank.
- **F4 Surprise fees in month one:** read the statement line, then either satisfy the waiver condition (minimum balance, salary deposit) or downgrade to the free tier. Fee creep is a product question, not a moral one.

## Verification

You can log in with 2FA, the card works, a test deposit arrived, the fee waiver condition is understood and met, and either no old account exists or it survived a full parallel cycle and was closed with confirmation.

## Variations

- `us`: expect a credit check for some account types and ChexSystems history checks; `de`: Anmeldung usually precedes everything; `uk`: proof-of-address culture is strict and newcomer alternatives are worth asking for explicitly; `jp`: residence card and sometimes a hanko, with foreigner-friendly banks well known in expat guides.
- Fully digital banks (N26, Monzo, Chime class): steps 2 through 5 compress into one app session; the parallel-run advice in step 7 still applies when migrating.

## Safety & privacy

Medium risk concentrated in identity handling and impersonation. Documents go only into the bank's own channels, credentials only into its official app, and unexpected "bank" contact gets the hang-up-and-call-back treatment every single time.
