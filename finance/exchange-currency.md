---
name: exchange-currency
domain: finance
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

You obtain foreign currency (as cash, or spending power on a card) at close to the real exchange rate, with the true cost of fees understood, and without being skinned at an airport desk.

## Preconditions

- Knowledge of the interbank ("mid-market") rate for your pair, from a rate site or search; this is the honest benchmark every offer is measured against.
- A card that either has no foreign-transaction fee or a low one, checked in advance.
- A rough plan for how much cash you actually need versus what you will put on a card.

## Steps

1. **Look up the mid-market rate.** Search the currency pair to get the real rate before anyone quotes you one. This is your yardstick. → *Expect:* a benchmark rate written down.
2. **Understand the fee-versus-rate trick.** A "0% commission" desk still profits by giving you a worse rate; a fair-rate provider may charge a visible fee. Judge only the final amount of foreign currency per unit of yours. → *Expect:* you can compute the effective rate of any offer, ignoring the "no fee" label.
3. **Check your card's foreign-transaction terms.** Many cards add 1-3% on foreign spend; some add nothing. A no-FX-fee card at the network rate usually beats cash exchange. → *Expect:* your card's foreign-spend fee known as a percentage.
4. **Decline "pay in your home currency" prompts.** ⚠️ *Irreversible:* at foreign terminals and ATMs, dynamic currency conversion offers to bill in your home currency at a padded rate. Always choose to be charged in the local currency. → *Expect:* the terminal charges in local currency; your bank does the conversion at the network rate.
5. **Get cash the cheap way, not the airport way.** Avoid airport and hotel exchange desks; their rates are the worst you will see. Prefer a bank ATM at the destination (choosing local-currency billing) or a pre-ordered rate from home. → *Expect:* an effective rate within a small margin of mid-market, not 10%+ worse.
6. **Split cash and card deliberately.** Carry enough local cash for small vendors, transit, and tips; put larger and card-friendly spending on the no-FX card. → *Expect:* a cash amount sized to genuine cash-only needs, not your whole trip.
7. **Keep the receipt and check the posted amount.** For cash exchange keep the slip; for card spend, verify the converted amount when it posts. → *Expect:* posted amounts match the expected rate within the disclosed fee.

## Decision points

- Airport arrival with zero local cash → withdraw a small amount from a bank-brand ATM to get moving, then do the bulk elsewhere; never exchange a large sum at the airport desk.
- Exotic or restricted currency (import controls, low availability) → order ahead or exchange on arrival at a bank; your home banks may not stock it or will charge heavily.
- Leftover foreign cash at trip end → spend it down or convert before leaving; buying back home is another spread you pay.

## Failure modes & recovery

- **F1 ATM offers a conversion rate:** it is doing DCC; decline the offered rate and choose "charged in local currency" so your bank converts instead.
- **F2 Surprise ATM operator fee:** foreign ATMs may add a flat fee; withdraw a larger amount fewer times to amortize it, within safety limits for carrying cash.
- **F3 Card declined abroad:** the issuer flagged unfamiliar-country activity; set a travel notice or expect a verification prompt, and carry a backup card on a different network.
- **F4 Counterfeit or short-changed cash:** count notes before leaving any desk; use bank-affiliated exchanges, not street changers offering rates that are too good.

## Verification

You hold local currency and/or card spending power obtained at an effective rate within a few percent of the mid-market benchmark, you declined every home-currency conversion prompt, and no exchange happened at an airport or hotel desk.

## Variations

- `eu`/`us`: no-foreign-transaction-fee travel cards are common and usually beat cash exchange outright.
- Cash-heavy destinations: some economies remain cash-first; size your cash to local reality rather than assuming cards are accepted everywhere.

## Safety & privacy

Medium risk: you carry cash and expose card details at foreign terminals. Use ATMs attached to real banks, shield the PIN, split cash between pockets and bag, and monitor the account after the trip for skimming. The single most common overcharge is accepting dynamic currency conversion.
