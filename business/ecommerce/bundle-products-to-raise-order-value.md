---
name: bundle-products-to-raise-order-value
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Create a product bundle that increases average order value while still giving the customer a clear, fair reason to buy the items together.

## Preconditions

- Access to the ecommerce admin, product catalog, inventory counts, and pricing settings.
- At least two complementary products with reliable stock and known unit costs.
- A target bundle margin and a minimum acceptable gross margin.

## Steps

1. **Choose products that solve one buyer need together.** Pair items customers naturally use in the same session, such as a device plus case or skincare cleanser plus moisturizer. → *Expect:* a bundle concept that is easy to explain in one sentence.
2. **Check inventory and fulfillment constraints.** Confirm every bundled SKU has enough stock and can ship together without special handling surprises. → *Expect:* no component has low stock, restricted shipping, or incompatible fulfillment rules.
3. **Calculate the standalone total and unit cost.** Add current selling prices, product costs, packaging cost, payment fees, and expected shipping subsidy. → *Expect:* a baseline revenue, cost, and gross margin for the unbundled items.
4. **Set the bundle price above your margin floor.** Offer a modest discount only if the bundle remains profitable after fees and shipping. → *Expect:* a bundle price that beats the standalone total and still meets the margin target.
5. **Create the bundle product or offer.** Use the platform's bundle app, kit SKU, or discount rule so inventory decrements correctly for each component. → *Expect:* the admin shows the bundle with all component SKUs linked.
6. **Write the bundle copy around the outcome.** Name what the customer gets, list each included item, and state the savings without exaggeration. → *Expect:* the product page makes the included items and final price unambiguous.
7. **Test the cart and checkout.** Add the bundle, change quantity, apply common discounts, and estimate shipping. ⚠️ *Irreversible:* do not publish until the cart total and inventory behavior are correct. → *Expect:* cart price, taxes, shipping, and inventory changes match the intended rules.
8. **Publish and monitor the first orders.** Watch conversion rate, average order value, refund reasons, and stock levels for the bundle components. → *Expect:* the bundle is live and early orders can be fulfilled without manual correction.

## Decision points

- Bundle margin falls below the floor → reduce the discount, swap a lower-cost component, or do not launch.
- One component has limited stock → make the bundle temporary or exclude that component.
- Existing sitewide discounts stack too deeply → exclude the bundle from other promotions or set a minimum price rule.

## Failure modes & recovery

- **F1 Inventory oversells:** detect component stock going negative → unpublish the bundle, fulfill paid orders first, and correct inventory mapping.
- **F2 Customer confusion:** detect messages asking what is included → rewrite title, images, and bullet list to show every component.
- **F3 Margin leak:** detect payout per order below target → raise price, remove stacking discounts, or adjust shipping subsidy.
- **F4 Fulfillment split:** detect warehouse cannot pick the kit as configured → switch from kit SKU to automatic cart discount or update fulfillment instructions.

## Verification

The bundle is live, adding it to cart charges the intended bundle price, every component SKU decrements correctly, and the calculated gross margin is at or above the stated minimum.

## Variations

- `shopify`: use Bundles, combined listings, or a discount app depending on inventory needs.
- `marketplace`: some marketplaces prohibit synthetic bundles unless all items are packaged together; follow listing policy.

## Safety & privacy

Medium risk because incorrect pricing or inventory can lose money. Confirm the final cart total, discount stacking, and stock behavior before making the bundle visible to customers.
