---
name: dispute-an-atm-error
domain: finance
subdomain: optimize
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You report an ATM error, such as cash not dispensed or a wrong amount posted, and preserve the evidence needed for the bank to investigate and credit the account.

## Preconditions

- You know the ATM location, date, time, bank or network, requested amount, and account or card used.
- You have retained any receipt, on-screen error photo, or transaction alert.
- You can access your bank or card issuer by app, website, or phone.

## Steps

1. **Move to a safe place and record facts immediately.** Note ATM address, machine ID if visible, date, time, requested amount, cash received, and any error message. → *Expect:* you have a timestamped fact record while memory is fresh.
2. **Keep the receipt and do not retry repeatedly.** Save any paper receipt and avoid multiple withdrawals that could create more confusing transactions. → *Expect:* there is one clear disputed transaction or a documented sequence.
3. **Check account activity.** Open the bank or card app to see whether the transaction is pending, posted, reversed, or absent. → *Expect:* you know the current account impact.
4. **Contact the card issuer or account bank.** Use the app dispute flow, secure message, or phone number on the card; report an ATM error. → *Expect:* the bank opens a claim or gives instructions for submitting one.
5. **Provide precise evidence.** Give location, ATM owner, machine ID, transaction amount, actual cash received, receipt details, and whether the ATM belongs to your bank. → *Expect:* the claim record contains enough information for ATM balancing.
6. **Ask about provisional credit and timeline.** Record claim number, expected investigation date, and whether a temporary credit will be issued. → *Expect:* you know when money should be credited or when the bank will decide.
7. **Follow up after ATM balancing.** If the bank requests more information or denies the claim, ask for the ATM audit result and submit your receipt or photos. → *Expect:* the case status is updated with evidence or appeal path.

## Decision points

- ATM did not dispense cash but account was debited → report immediately and avoid a second withdrawal at that machine.
- ATM dispensed partial cash → dispute only the missing amount and state cash actually received.
- ATM is owned by another bank or independent operator → file with your card issuer; they coordinate with the ATM owner.
- You are traveling and need cash → use a different ATM or branch after documenting the error.

## Failure modes & recovery

- **F1 Receipt lost:** detect no paper proof → use app transaction timestamp, location data, and written notes as evidence.
- **F2 Claim denied after balancing:** detect denial stating cash was dispensed → request the audit details and appeal with timing, receipt, and any camera/location evidence.
- **F3 Duplicate withdrawal attempts:** detect multiple pending debits → document each attempt separately and dispute only failed or short-dispensed transactions.
- **F4 Foreign ATM language or fee confusion:** detect unexpected fees but correct cash dispensed → distinguish fee complaint from cash-dispense error before disputing.

## Verification

The bank has opened an ATM-error claim for the correct transaction, you have the claim number and timeline saved, and the account is either credited for the missing amount or awaiting a documented investigation outcome.

## Variations

- `credit-union`: shared-branch or network ATM claims may require both network and account details.
- `international`: currency conversion and foreign ATM owner fees can complicate the disputed amount.
- `cash-deposit-atm`: record envelope or deposit confirmation details and dispute missing deposit credit.

## Safety & privacy

Medium risk because cash and account access are involved. Leave unsafe ATM areas first, never share PINs, use official bank contacts, and preserve evidence without posting card or receipt details publicly.
