---
name: sell-on-ebay
domain: shopping
subdomain: marketplace
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h-2h
risk: medium
prerequisites: [accounts/log-in, have-payment-method]
status: draft
last_verified: 2026-08-25
---

## Goal

You create an accurate eBay listing, choose sale and shipping terms that protect you, and complete the sale only after payment and shipping details are confirmed.

## Preconditions

- An eBay account in good standing with a payout method connected.
- The item, accessories, serial/model details, and packaging materials.
- A scale, tape measure, and access to a carrier drop-off or pickup.

## Steps

1. **Identify the exact item.** Record the brand, model, size, condition, serial or part number when safe to disclose, and everything included. → *Expect:* a fact list you can copy into the listing without guessing.
2. **Research sold prices.** Search eBay sold listings for the same item in similar condition and note shipping prices, not just item prices. → *Expect:* a realistic net price range after fees and shipping.
3. **Choose the listing format.** [BRANCH: auction for uncertain collectibles | Buy It Now for common items with known market prices] Set a private minimum you will not go below. → *Expect:* a selling format and walk-away price.
4. **Create the listing draft.** Enter the correct category, item specifics, condition, title keywords, and an honest description with flaws called out. → *Expect:* eBay shows a complete draft with required item specifics accepted.
5. **Upload clear photos.** Include front, back, sides, labels, accessories, and close-ups of wear or damage. → *Expect:* the photo gallery proves condition without relying on promises.
6. **Set shipping and returns.** Enter measured package weight/dimensions, choose tracked shipping, decide whether returns are accepted, and avoid underpriced shipping. → *Expect:* the buyer-facing total reflects a carrier service you can actually use.
7. **Review fees and payout estimate.** Check eBay's estimated proceeds against your minimum. → *Expect:* the expected payout is above your private floor.
8. **Publish the listing.** ⚠️ *Irreversible:* confirm title, price, shipping, condition, and return terms before listing goes live because buyers can purchase immediately. → *Expect:* the listing is live and visible in your active listings.
9. **Handle buyer questions inside eBay.** Answer factual questions, add photos if needed, and refuse requests to pay or message off-platform. → *Expect:* all material buyer communication remains in eBay messages.
10. **Ship only after eBay says paid.** Buy or upload a tracked label addressed exactly as eBay provides, photograph the packed item, and scan it with the carrier on time. ⚠️ *Irreversible:* do not ship based on screenshots or emails; verify the order status inside eBay first. → *Expect:* tracking is uploaded and the order shows shipped.
11. **Confirm payout and close records.** Save the order number, tracking number, final value fee, shipping cost, and payout amount. → *Expect:* funds are paid out or scheduled by eBay with no open dispute.

## Decision points

- Item is expensive or fraud-prone → require signature confirmation and keep packing photos.
- Sold prices vary widely → use auction only if you can tolerate the final price; otherwise use Buy It Now with offers.
- Buyer asks to change the address after purchase → cancel and ask them to repurchase with the correct address through eBay.
- Shipping estimate is close to your margin → remeasure and reprice before publishing.

## Failure modes & recovery

- **F1 Underpriced shipping:** detect carrier label cost higher than expected → revise the listing before sale; after sale, ship as promised and treat the loss as a pricing error.
- **F2 Off-platform payment request:** detect a buyer asking for email, wire, gift card, or external invoice → decline and keep all payment through eBay.
- **F3 Item-not-as-described dispute:** detect a return or case → respond with listing photos, flaw disclosures, serial numbers, and tracking evidence.
- **F4 Buyer address change scam:** detect a message asking shipment somewhere other than the order address → do not comply; cancel if necessary.
- **F5 Listing removed:** detect an eBay policy notice → read the specific violation, remove prohibited language or category errors, and relist only if permitted.

## Verification

The eBay order shows paid and shipped with valid tracking to the order address, the item is delivered or in carrier possession, and the payout is issued or scheduled above your minimum with no active case.

## Variations

- `us`: keep sale, shipping, and cost-basis records for tax reporting if marketplace income is reportable.
- Auction: schedule the ending time when likely buyers are awake and active.
- Local pickup: use eBay's local pickup flow and confirm payment status before releasing the item.

## Safety & privacy

Medium risk because payment, shipping addresses, and disputes are involved. Keep communication on eBay, ship only to the platform address, hide unnecessary serial numbers in public photos, and confirm before publishing or shipping.
