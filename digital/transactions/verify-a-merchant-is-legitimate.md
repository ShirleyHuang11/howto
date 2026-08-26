---
name: verify-a-merchant-is-legitimate
domain: digital
subdomain: transactions
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You decide whether an online merchant is safe enough to buy from before entering payment or identity information.

## Preconditions

- You have the merchant website, product page, ad, email, or marketplace listing you are evaluating.
- You know the approximate fair price for the item or service.
- You have not yet submitted payment, full identity documents, or account passwords to the merchant.

## Steps

1. **Inspect the domain carefully.** Check spelling, top-level domain, age cues, and whether the link came from an ad, email, or social post. → *Expect:* the domain either matches the known brand exactly or is identified as a separate seller.
2. **Check secure connection and checkout ownership.** Confirm the browser shows HTTPS and payment forms are on the merchant, platform, or known processor domain. → *Expect:* no password or card fields appear on a suspicious or misspelled host.
3. **Verify business identity.** Look for a real legal name, physical address, customer-service channel, return policy, privacy policy, and terms. → *Expect:* the merchant provides enough accountable contact information to pursue support or claims.
4. **Compare external reputation.** Search independent reviews, complaint databases, marketplace feedback, and recent scam reports using the merchant name plus domain. → *Expect:* reputation signals are consistent with a real business or reveal unresolved fraud patterns.
5. **Evaluate price and urgency.** Compare the offer against normal market prices and note countdown timers, fake scarcity, or unrealistic discounts. → *Expect:* the deal is plausible or flagged as too risky.
6. **Check payment protections.** Prefer credit card, trusted wallet, or marketplace checkout; avoid wire, crypto, gift card, friends-and-family transfer, or off-platform payment. → *Expect:* the payment path includes chargeback or buyer-protection options.
7. **Decide before sharing sensitive data.** [BRANCH: legitimacy confirmed, proceed with a protected payment method | unresolved red flags, abandon or buy from a reputable seller] ⚠️ *Irreversible:* do not enter payment or identity data until red flags are resolved. → *Expect:* you have a buy or walk-away decision supported by evidence.

## Decision points

- New store with no track record → buy only low-risk items with strong payment protection, or avoid.
- Price is far below market → assume counterfeits, non-delivery, or bait-and-switch until proven otherwise.
- Seller pushes off-platform payment → walk away because buyer protection is usually lost.
- Brand site differs from advertised site → navigate from the brand's official search result instead of the ad link.

## Failure modes & recovery

- **F1 Fake storefront:** detect stolen product photos, no real address, and too-good pricing → do not buy; report the ad or domain.
- **F2 Counterfeit marketplace seller:** detect brand complaints or mismatched seller identity → choose an authorized retailer or listing with authentication.
- **F3 Phishing checkout:** detect login or card form on a lookalike domain → close the page, do not submit, and change passwords if entered.
- **F4 Hidden subscription:** detect trial language or recurring billing in terms → avoid checkout or use a virtual card with limits after confirming cancellation terms.

## Verification

Before checkout, the merchant has a verified domain or accountable seller profile, plausible pricing, clear return and contact information, no unresolved scam red flags, and a protected payment method is available; otherwise the purchase is abandoned.

## Variations

- `marketplace`: evaluate seller rating, account age, completed-sale history, return policy, and platform protection.
- `social-commerce`: be more skeptical of sellers operating only through direct messages or comments.
- `high-value`: verify authorized-dealer status or use escrow, authentication, or in-person inspection.

## Safety & privacy

Medium risk because fake merchants can steal money and identity data. Do not enter payment information until the merchant is verified, avoid irreversible payment methods, and keep screenshots of claims and policies if you proceed.
