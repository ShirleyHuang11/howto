---
name: dispute-a-card-charge
domain: finance
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h
risk: medium
prerequisites: [accounts/log-in, have-bank-account]
status: draft
last_verified: 2026-07-20
---

## Goal

An incorrect, fraudulent, or undelivered-goods charge on your card is formally disputed, and the dispute is tracked to a credit or a justified rejection.

## Preconditions

- The charge is visible on your statement (note date, merchant string, amount).
- You attempted merchant resolution first for non-fraud cases (this is required by most issuers), or the charge is outright fraud.
- Evidence gathered: receipts, order confirmations, correspondence, photos.

## Steps

1. **Classify the charge.** [BRANCH: fraud (you never transacted) → skip to step 3 | merchant error (wrong amount, duplicate, goods not delivered/not as described) → step 2] Decode the merchant string first — many "unknown" charges are legitimate with unfamiliar billing names; search the string before crying fraud. → *Expect:* a confident classification.
2. **Attempt merchant resolution and document it.** Contact merchant support, state the problem, request a refund; save the ticket/emails and give them the stated response window. → *Expect:* either a refund (done — verify it posts, skip to step 7) or a documented refusal/non-response, which the dispute will require.
3. **For fraud: freeze the card immediately.** In the banking app: lock/freeze the card, then request a replacement. → *Expect:* card locked; further charges impossible.
4. **Open the dispute with the issuer.** Banking app/site → the transaction → "Dispute charge", or call the number on the card. Provide the classification, the story, and upload the evidence from steps 1–2. → *Expect:* a dispute case number and a stated timeline.
5. **Answer follow-up requests promptly.** Issuers may mail/message questionnaires; missing their deadlines forfeits the dispute. → *Expect:* every issuer request answered within its window; case shows "under review".
6. **Track the provisional credit.** Many issuers credit the amount provisionally during investigation. → *Expect:* a provisional credit line on the statement (not guaranteed in all jurisdictions).
7. **Receive the outcome.** ⚠️ *Irreversible:* a resolved-in-your-favor dispute can still be reversed if the merchant provides counter-evidence — keep your evidence until the final resolution notice, not just the first credit. → *Expect:* written resolution: permanent credit, or rejection with reasons.
8. **If rejected and you disagree: escalate.** Request the merchant's counter-evidence, rebut in writing, and if the issuer won't move, complain to the financial regulator/ombudsman for your jurisdiction. → *Expect:* an escalation case with its own timeline.

## Decision points

- Amount is trivial (a few dollars) and it's a one-off billing error → weigh the hour of effort; but *any* unrecognized small charge can be a card-testing probe — treat repeated small unknowns as fraud (step 3).
- Subscription you forgot vs. unauthorized charge → forgotten subscriptions are not fraud; cancel the subscription and request a goodwill refund instead — false fraud claims can close your account.
- Merchant is insolvent (undelivered goods, company folded) → go straight to the dispute; the merchant-resolution step is moot but say so in the filing.

## Failure modes & recovery

- **F1 Dispute window missed:** windows are commonly 60–120 days from the statement; outside it, appeal to the issuer's goodwill and the merchant directly — the formal right has lapsed.
- **F2 Provisional credit reversed:** the merchant supplied evidence; obtain it (you are entitled to it), rebut point by point per step 8.
- **F3 Replacement card breaks autopays:** update card-on-file at each recurring biller — list them from the last 3 statements before the old number dies.

## Verification

The dispute case shows final resolution; a permanent credit for the full disputed amount appears on a statement (or you accepted a reasoned rejection); and for fraud cases, the compromised card is dead and its recurring billers migrated.

## Variations

- Debit cards: same flow, weaker protections and slower money return in many jurisdictions — the case for using credit cards online.
- `us`: Fair Credit Billing Act gives ≥60 days from statement for billing errors; `uk`: Section 75 makes the card issuer jointly liable for £100–£30k credit purchases — cite it explicitly.

## Safety & privacy

Medium risk. Never share the full card number in dispute correspondence (issuers use the last 4); beware follow-up scam calls "from the fraud department" — hang up and call the number on the card (`daily/answer-a-phone-call` rule 5).
