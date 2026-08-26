---
name: sell-a-domain-name
domain: shopping
subdomain: marketplace
locale: [generic]
interface: web
difficulty: advanced
est_time: 1h-2h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You sell a domain name through a safe marketplace or escrow workflow and transfer control only after payment is secured.

## Preconditions

- You control the domain in a registrar account and it is not stolen, disputed, locked by court order, or contractually restricted.
- Access to the registrant email, registrar account, and any two-factor authentication.
- A target price, minimum net proceeds, and preferred transfer method.

## Steps

1. **Confirm ownership and transfer eligibility.** Check registrar status, expiration date, transfer lock, recent registration or transfer restrictions, and contact email access. → *Expect:* the domain is active, controlled by you, and eligible for sale or push.
2. **Research comparable sales and set a floor.** Use marketplace comps, keyword quality, extension, age, traffic, and renewal cost to choose asking price and minimum acceptable net. → *Expect:* a public asking price and private walk-away number.
3. **Choose a protected sale channel.** [BRANCH: fixed-price marketplace | broker | independent escrow] Compare fees, payout timing, transfer support, and buyer verification. → *Expect:* a selected channel that can hold or verify funds before transfer.
4. **Prepare the listing or escrow terms.** Enter exact domain spelling, price, included assets if any, transfer method, buyer fees, and timeline. → *Expect:* sale terms match your intended domain and net proceeds.
5. **Publish or send the transaction invitation.** ⚠️ *Irreversible:* a buyer may rely on these terms; confirm spelling, price, and included rights before posting. → *Expect:* the listing is live or the escrow transaction is open.
6. **Verify buyer payment through the channel.** Wait for the marketplace or escrow service to show funded, paid, or authorized status. → *Expect:* the platform confirms funds are secured according to its rules.
7. **Transfer the domain only through the agreed method.** [BRANCH: same-registrar push | inter-registrar transfer] Unlock only if needed, provide auth code through the platform if required, or push to the buyer's account. ⚠️ *Irreversible:* domain control can be hard to recover; transfer only after protected payment confirmation. → *Expect:* the registrar shows the domain pending transfer or moved to the buyer.
8. **Confirm completion and payout.** Monitor escrow/marketplace release, payout method, and final registrar status. → *Expect:* the domain is no longer in your account and proceeds are paid or scheduled.
9. **Remove old sale listings and records.** End duplicate listings, update DNS if required, and archive receipts for taxes. → *Expect:* the domain is no longer advertised by you as available.

## Decision points

- Domain is within a transfer lock period → use same-registrar account push if allowed or wait until transfer eligible.
- Buyer asks to skip escrow for a discount → decline unless the marketplace itself provides equivalent protection.
- Trademark concern appears → stop and seek legal advice before marketing the domain as associated with a brand.
- Offer is below renewal-cost logic or your floor → counter or walk away.

## Failure modes & recovery

- **F1 Wrong domain listed:** detect a typo or wrong extension in the listing → pause immediately and correct before accepting payment.
- **F2 Unfunded escrow:** detect buyer pressure before escrow is funded → do not unlock or transfer; wait for platform confirmation.
- **F3 Transfer stuck:** detect registrar lock, bad auth code, or email approval failure → recheck WHOIS privacy/contact settings and follow registrar support steps.
- **F4 Chargeback or marketplace dispute:** detect payout hold → provide escrow record, registrar transfer proof, and buyer communications.
- **F5 Trademark complaint:** detect a legal notice or platform removal → suspend sale activity and get qualified advice.

## Verification

The domain has transferred to the buyer or their registrar account, the marketplace or escrow transaction shows complete, and your payout is received or formally scheduled for the agreed net amount.

## Variations

- Premium marketplace: the platform may require nameserver changes to verify ownership.
- Brokered sale: the broker may negotiate privately and coordinate escrow, but you still confirm funded status before transfer.
- Same-registrar push: faster than a transfer but still requires verified payment before account push.

## Safety & privacy

Medium risk because domain control and payment are valuable. Use reputable escrow or marketplace workflows, protect registrar credentials with two-factor authentication, avoid trademark misrepresentation, and never send an auth code before funds are secured.
