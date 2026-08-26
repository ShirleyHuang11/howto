---
name: avoid-buying-counterfeit-goods
domain: shopping
subdomain: buying
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

You evaluate a product listing before purchase and reject counterfeit-risk listings before money changes hands.

## Preconditions

- The exact product you intend to buy, including model, size, color, or generation.
- Access to the brand's official product page or an authorized-retailer listing for comparison.
- A payment method that supports disputes or chargebacks if you decide to proceed.

## Steps

1. **Identify the exact authentic product.** Open the brand or authorized-retailer page and note the official name, SKU, materials, packaging, warranty terms, and retail price. → *Expect:* a reference record for what a genuine item should look like and cost.
2. **Compare the seller's photos to the official reference.** Check logo placement, stitching, typography, serial-number format, packaging, labels, and included accessories. → *Expect:* either no visible mismatch or a list of specific authenticity concerns.
3. **Check whether the photos are original.** Reverse-search images or look for watermark/crop artifacts that suggest copied catalog photos. → *Expect:* confidence that the seller photographed the actual item, or evidence the photos are reused.
4. **Evaluate the price against the real market.** Compare sold listings and authorized sale prices; treat deep discounts on scarce or luxury goods as a warning sign. → *Expect:* a plausible market range and a decision whether the listing price is suspicious.
5. **Read the seller's return and authenticity policy.** Confirm whether the platform permits returns for counterfeit goods and whether the seller accepts returns without restocking traps. → *Expect:* documented buyer protection before purchase.
6. **Ask for proof only a real seller can provide.** Request a dated photo of the item, serial number if safe, purchase receipt with personal data redacted, or platform authenticity guarantee. → *Expect:* responsive, consistent evidence or a seller who refuses reasonable proof.
7. **Choose the safer purchase path.** [BRANCH: high-value or commonly counterfeited item | ordinary low-risk item] For high-risk goods, buy only through an authorized retailer or a platform with authentication; for low-risk goods, proceed only if all checks are clean. → *Expect:* the chosen seller has acceptable authenticity protection for the item's risk.
8. **Confirm before payment.** ⚠️ *Irreversible:* before placing the order, confirm the item, seller, price, shipping address, return window, and buyer-protection method. → *Expect:* the checkout page matches the listing you vetted and uses a protected payment method.

## Decision points

- Listing uses only stock photos → ask for original photos; walk away if the seller refuses.
- Price is far below the normal used market → assume counterfeit risk unless there is a documented, plausible reason.
- Seller asks for payment outside the marketplace → decline; off-platform payment usually removes buyer protection.
- Serial number is provided → verify it only through the brand or authorized checker; do not rely on seller screenshots.

## Failure modes & recovery

- **F1 Copied authenticity proof:** detect receipt images or serial checks that look generic or edited → request a dated photo tied to the listing; if inconsistent, do not buy.
- **F2 Bait-and-switch listing:** detect photos of a genuine item but vague description like "style" or "inspired" → treat the description as controlling and avoid the purchase.
- **F3 Platform dispute denial:** detect weak buyer protection or final-sale terms → choose a different seller before purchase rather than relying on a later dispute.
- **F4 Counterfeit received anyway:** detect mismatched materials, packaging, or failed brand verification → preserve packaging, photos, and messages; open a counterfeit claim immediately.

## Verification

The listing is either rejected for documented counterfeit risk or purchased only after matching official references, seller evidence, buyer protection, and protected checkout terms.

## Variations

- Luxury goods: prefer platforms with in-house authentication and avoid private-payment deals.
- Electronics: verify model numbers, IMEI/serial status, warranty eligibility, and region locks before purchase.
- Collectibles: require provenance, graded certification where applicable, and clear photos of condition-sensitive details.

## Safety & privacy

Medium risk because counterfeit purchases can lose money and expose payment data. Do not send identity documents to a seller, do not pay by gift card or wire, and preserve all platform messages for dispute evidence.
