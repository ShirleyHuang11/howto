---
name: sell-clothes-on-poshmark
domain: shopping
subdomain: marketplace
locale: [generic]
interface: mobile-app
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [accounts/log-in, have-payment-method]
status: draft
last_verified: 2026-08-25
---

## Goal

You list clothing on Poshmark with accurate sizing and condition details, accept a profitable offer, and ship within the platform's seller-protection rules.

## Preconditions

- A Poshmark account with payout details set up.
- Clean clothing, shoes, or accessories ready to photograph.
- A printer or QR-code label option, packaging, and access to USPS or the supported carrier.

## Steps

1. **Inspect and prep the garment.** Check seams, stains, odors, missing buttons, pilling, and fabric care tags. → *Expect:* every flaw is known before listing.
2. **Measure key dimensions.** Record bust/chest, waist, hips, inseam, rise, length, sleeve, heel height, or bag dimensions as relevant. → *Expect:* buyers can compare the item to their own fit needs.
3. **Research Poshmark comps.** Search sold listings for brand, size, style name, and condition. → *Expect:* a likely sale range and minimum acceptable payout.
4. **Photograph the item.** Use daylight or bright neutral light, show front/back, tag, fabric, flaws, and modeled or flat-lay views if available. → *Expect:* photos accurately show color, scale, and condition.
5. **Create the listing.** Enter brand, category, size, condition, original price if known, listing price, and style keywords. → *Expect:* the listing draft is searchable and complete.
6. **Write the description.** Include measurements, fabric, care, condition, flaws, smoke/pet disclosures if relevant, and what is included. → *Expect:* the description reduces fit and condition disputes.
7. **Publish and share the listing.** ⚠️ *Irreversible:* confirm price, size, and flaw disclosure before publishing because offers may arrive immediately. → *Expect:* the item appears in your closet.
8. **Evaluate offers by net proceeds.** Use Poshmark's fee estimate and shipping discounts before accepting or countering. → *Expect:* any accepted price is above your minimum.
9. **Ship after the sale notice.** Use the Poshmark-provided label, package cleanly, include only agreed items, and drop off promptly. ⚠️ *Irreversible:* confirm the sale is in the app before mailing. → *Expect:* tracking starts and the order shows shipped.
10. **Monitor acceptance and payout.** Respond to any case with photos and measurements from the original listing. → *Expect:* funds become redeemable after buyer acceptance or platform auto-acceptance.

## Decision points

- Item has a hidden flaw → disclose it and price lower rather than hoping the buyer misses it.
- Offer includes a shipping discount → calculate the seller-paid discount before accepting.
- Color photographs inconsistently → describe the color plainly and include a tag or daylight photo.
- Buyer asks for extra off-platform payment → decline and keep the sale in Poshmark.

## Failure modes & recovery

- **F1 Fit dispute:** detect buyer complaint about size → provide listed measurements and tag photos in the case.
- **F2 Undisclosed flaw case:** detect buyer photo of a missed stain or tear → accept the return if valid and relist accurately after inspection.
- **F3 Label or package mismatch:** detect overweight or wrong package limits → use the platform's upgraded label process before shipping.
- **F4 Lowball bundle offer:** detect a bundle price below your minimum → counter using your floor and fee math.
- **F5 Delayed shipment warning:** detect a reminder or cancellation risk → ship immediately or cancel honestly if unavailable.

## Verification

The Poshmark order shows shipped with platform tracking, accepted or auto-accepted, and the redeemable payout meets or exceeds your minimum with no open case.

## Variations

- `us`: Poshmark commonly uses prepaid USPS labels; check current weight and package rules before shipping.
- Luxury items: photograph authenticity markers and use any required platform authentication flow.
- Bundles: calculate one combined payout after discounts and seller fees before accepting.

## Safety & privacy

Medium risk because money and addresses are involved. Do not transact off-platform, disclose flaws, avoid sharing personal contact details, and confirm the in-app sale before shipping.
