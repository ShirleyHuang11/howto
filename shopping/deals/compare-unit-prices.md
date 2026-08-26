---
name: compare-unit-prices
domain: shopping
subdomain: deals
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You compare two or more package sizes by true cost per usable unit, then buy the option that fits your budget, storage, and usage rate.

## Preconditions

- The product candidates are the same type and close enough in quality to compare.
- You know the final price after discounts, shipping, taxes, deposits, and mandatory fees.
- You know the usable quantity, such as ounces, grams, sheets, doses, loads, servings, or count.

## Steps

1. **List the comparable products.** Open each product page or shelf tag and write down brand, package size, quantity, and displayed price. → *Expect:* a side-by-side list of every candidate you may buy.
2. **Normalize the unit.** Convert every quantity to one unit, such as price per ounce, per gram, per sheet, or per dose. → *Expect:* all candidates use the same denominator.
3. **Use the final payable price.** Add required shipping, taxes, bottle deposits, service fees, and subtract real coupons that apply to that exact item. → *Expect:* each candidate has a realistic checkout price, not just a shelf price.
4. **Calculate unit price.** Divide final payable price by usable units, excluding packaging, water weight when irrelevant, or bundled extras you will not use. → *Expect:* every item has a cost per usable unit.
5. **Check quality and concentration.** For concentrates, detergents, batteries, medications, and supplements, compare active ingredients, dose count, or expected performance rather than container size. → *Expect:* the comparison reflects useful output, not misleading package volume.
6. **Reject false bulk savings.** If the larger package expires, spoils, or takes storage you do not have before you can use it, treat the waste as part of the cost. → *Expect:* an adjusted winner that you can actually use.
7. **Buy the best eligible option.** ⚠️ *Irreversible:* before checkout, confirm the cart total is within your budget and the selected item is the unit-price winner after all fees. → *Expect:* the order or purchase receipt shows the chosen item and final price.

## Decision points

- The lowest unit price requires buying more than you can use → choose the smaller package with the lowest expected waste.
- A coupon applies only to one size → recalculate after coupon instead of assuming the sale tag is best.
- Two options are within a small margin → choose the one with better return policy, freshness date, or storage fit.
- Subscription pricing changes the unit price → include only discounts that remain after the first shipment if you intend to keep subscribing.

## Failure modes & recovery

- **F1 Mixed units:** detect one item priced per pound and another per ounce → convert both before deciding.
- **F2 Hidden fees:** detect a winner losing after shipping or service fees → recalculate using cart totals.
- **F3 Concentration trap:** detect a larger bottle with fewer doses or weaker formula → compare cost per dose or use.
- **F4 Waste turns savings negative:** detect expiration or storage limits → buy the smaller usable quantity.

## Verification

The purchased item has the lowest final cost per usable unit among eligible options, after required fees and realistic waste, and the receipt total stays within the chosen budget.

## Variations

- `grocery`: compare by edible weight or serving, not package size when liquid, bone, or shell weight differs.
- `household`: compare by load, sheet, dose, or battery life where the label provides usable-output units.
- `marketplace`: include delivery fees and minimum-order padding in the unit price.

## Safety & privacy

Medium risk because checkout spends money. Confirm cart total, item size, delivery quantity, and recurring-subscription status before placing the order.
