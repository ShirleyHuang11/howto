---
name: sell-sneakers-on-a-resale-app
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

You list sneakers on a resale app with accurate model, size, and condition information, pass authentication when required, and receive payout after shipment.

## Preconditions

- A resale-app account with payout settings enabled.
- Sneakers, original box and accessories if available, and proof of purchase if useful.
- Packaging suitable for shipping a shoe box without damage.

## Steps

1. **Identify the exact sneaker.** Record brand, model, colorway, SKU/style code, size system, release year, and box label. → *Expect:* the listing matches the exact pair, not just a similar shoe.
2. **Inspect condition and authenticity indicators.** Check soles, uppers, insoles, odor, repairs, replacement laces, box damage, and included accessories. → *Expect:* a condition grade and disclosure list.
3. **Research market prices.** Compare recent sales for the same SKU, size, condition, and box status. → *Expect:* a target ask, lowest acceptable payout, and expected fees.
4. **Photograph the pair.** Show both shoes, all sides, soles, size tags, box label, flaws, and accessories. → *Expect:* photos support authentication and buyer expectations.
5. **Create the app listing.** Select the exact SKU/colorway, size, condition, box status, price, and shipping option. → *Expect:* the app displays the correct product page and payout estimate.
6. **Set price discipline.** Choose ask price or instant-sale bid only if net payout is above your floor. → *Expect:* you know when to accept, counter, or wait.
7. **Publish or accept the sale.** ⚠️ *Irreversible:* confirm SKU, size, condition, payout, and shipping deadline before committing because cancellation can trigger penalties. → *Expect:* the sale or listing is active in the app.
8. **Pack exactly what was sold.** Include matching shoes, box, laces, tags, and accessories promised in the listing; protect the original box inside an outer box. → *Expect:* package contents match the order record.
9. **Ship to the app or buyer address provided.** Use the platform label and scan the package before the deadline. ⚠️ *Irreversible:* verify the order in the app before shipping. → *Expect:* tracking is active and linked to the sale.
10. **Track authentication and payout.** Respond quickly if the app requests more information. → *Expect:* authentication passes or the app explains a specific issue; payout is released after approval.

## Decision points

- Shoes are used or missing the box → price against used/no-box comps, not deadstock comps.
- Authentication confidence is low → do not list as authentic unless you can support it; seek appraisal or avoid selling.
- Instant bid is below your floor → list at your ask instead of accepting immediately.
- Shipping deadline is too soon → do not accept a sale you cannot ship on time.

## Failure modes & recovery

- **F1 Authentication failure:** detect rejection by the app → review the reason, request return if offered, and do not relist without resolving authenticity or condition mismatch.
- **F2 Wrong SKU or size:** detect buyer or app mismatch notice → cancel before shipping if possible; correct the listing.
- **F3 Damaged shoe box in transit:** detect authentication downgrade or buyer complaint → submit packing photos and use stronger outer packaging next time.
- **F4 Seller cancellation penalty:** detect inability to ship by deadline → contact support early; avoid accepting future sales without inventory in hand.
- **F5 Counterfeit accusation:** detect a dispute or hold → provide receipt, SKU photos, box label, and platform communication only.

## Verification

The resale app shows the sneakers shipped with platform tracking, authentication accepted when required, and payout released or scheduled at or above your minimum.

## Variations

- Deadstock: disclose whether shoes were tried on, laced, or missing tags.
- Used sneakers: include sole wear, heel drag, creasing, and odor condition.
- Local sneaker marketplace: meet publicly and verify payment before release instead of relying on app authentication.

## Safety & privacy

Medium risk from counterfeit disputes, chargebacks, and high resale values. Keep proof of purchase and packing photos, transact through the app, and confirm before committing or shipping.
