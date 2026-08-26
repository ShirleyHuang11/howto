---
name: launch-a-new-product
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: advanced
est_time: 2d
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You publish a new ecommerce product with accurate content, inventory, pricing, fulfillment, and launch checks so customers can buy it without avoidable errors.

## Preconditions

- Final product details: title, SKU, variants, dimensions, weight, cost, images, inventory, and legal/compliance requirements.
- Ecommerce admin access and permission to create products.
- Shipping, tax, payment, and return policies already configured.

## Steps

1. **Create the product record in draft.** Add the name, SKU, product type, vendor, status, and sales channels without publishing yet. → *Expect:* a draft product exists in the catalog.
2. **Add accurate variant data.** Enter sizes, colors, bundles, barcodes, weights, inventory quantities, and option names exactly as they should appear to buyers. → *Expect:* each sellable variant has a unique SKU and inventory value.
3. **Upload product media.** Add clear images or videos showing the product, scale, included items, and important details. → *Expect:* the gallery communicates what the buyer will receive.
4. **Write the purchase-critical content.** Add description, specifications, care instructions, compatibility, ingredients/materials, warranty, and restrictions as applicable. → *Expect:* the page answers the main pre-purchase questions.
5. **Set price and margins.** Enter price, compare-at price if truthful, cost, tax category, and any launch discount. → *Expect:* the expected gross margin is known before launch.
6. **Configure fulfillment.** Assign warehouse/location, shipping profile, package weight, delivery promise, and backorder behavior. → *Expect:* checkout can calculate shipping for the product.
7. **Run a test purchase path.** Preview the product, add each key variant to cart, apply intended discounts, and proceed to the payment step without submitting a real order unless using test mode. → *Expect:* product, price, tax, shipping, and inventory behave as intended.
8. **Publish the product.** ⚠️ *Irreversible:* before setting live, confirm price, inventory, shipping, legal claims, images, and sales channels because customers can purchase immediately. → *Expect:* the product page is live and buyable on intended channels.
9. **Monitor the first orders.** Watch analytics, search, payment authorization, inventory decrement, and fulfillment queue for the first hour or first several orders. → *Expect:* orders flow through without catalog or checkout errors.

## Decision points

- Product has regulated claims → get legal/compliance approval before publishing.
- Inventory is limited → cap launch quantity or disable oversell/backorder.
- Variants have different weights or prices → test each variant, not only the default.
- Launch depends on email or ads → publish shortly before campaigns go live and verify the URL.

## Failure modes & recovery

- **F1 Wrong price live:** detect orders at an unintended price → pause the product, correct pricing, and follow store policy for affected orders.
- **F2 Shipping unavailable:** detect checkout saying no rates → assign the product to the correct shipping profile and retest by destination.
- **F3 Variant mismatch:** detect orders for a SKU that does not match the displayed option → unpublish, fix option/SKU mapping, and contact impacted customers.
- **F4 Oversell:** detect inventory below zero or backorders you cannot fulfill → stop sales, update inventory, and offer cancellation or delayed shipment.
- **F5 Rejected sales channel:** detect marketplace disapproval → fix missing attributes or prohibited claims and resubmit.

## Verification

The product is live on the intended sales channel, at least one variant can reach checkout with correct price/shipping/tax, inventory decrements correctly, and no launch-blocking admin errors remain.

## Variations

- Marketplace launch: required attributes and approval reviews may delay publication.
- Digital product: replace shipping setup with file delivery, license terms, and download testing.
- Preorder: clearly label ship date, payment timing, cancellation policy, and inventory cap.

## Safety & privacy

Medium risk because customers can spend money based on the page. Confirm legal claims, price, inventory, fulfillment promise, and customer-data collection before publishing.
