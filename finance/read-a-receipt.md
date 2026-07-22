---
name: read-a-receipt
domain: finance
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Read a receipt well enough to confirm what you bought, what you paid, whether tax and discounts look right, and how long you have to return or support the purchase.

## Preconditions

- You have the full receipt, not only a card alert or bank transaction.
- You can see the merchant name, date, item list, totals, and any return policy text.
- You have the purchased items nearby if you need to compare names, sizes, or quantities.
- You can contact the merchant if the receipt shows a wrong amount.

## Steps

1. **Identify the merchant and transaction.** Find the store name, location or website, date, time, register, transaction number, and payment method. → *Expect:* you can distinguish this receipt from similar purchases.
2. **Scan every line item.** Match each product or service line to what you actually bought, including size, color, quantity, and unit price. → *Expect:* every item is recognized or marked for review.
3. **Check discounts and coupons.** Confirm sale prices, coupon codes, loyalty discounts, and returns or exchanges were applied to the correct items. → *Expect:* reductions appear near the affected items or in a discount section.
4. **Recalculate the subtotal.** Add the line items after discounts and before tax, shipping, tip, or fees. → *Expect:* your subtotal matches the receipt subtotal or differs by only a rounding cent.
5. **Review tax, fees, tip, and total.** Compare taxable items, service fees, bag fees, delivery fees, and tip to the final total. → *Expect:* the amount charged matches the receipt total.
6. **Find the return window.** Read the return policy, final sale labels, receipt date, and any deadline printed near the bottom or back. → *Expect:* you know the last practical return date and required condition.
7. **Locate the barcode or receipt code.** Find the barcode, QR code, order number, or lookup code used for returns, pickup, warranty, or expense proof. → *Expect:* the merchant can use the receipt to retrieve the transaction.
8. **Decide whether to keep it.** [BRANCH: routine purchase | warranty or expense] discard after return window for routine items; keep or scan receipts for warranties, reimbursements, tax records, or valuable goods. → *Expect:* the receipt is either safely stored or no longer needed.
9. **Spot and document an error.** If any item, tax, coupon, tip, or total looks wrong, circle it and take a photo before contacting the merchant. → *Expect:* you have evidence that shows the exact disputed line.
10. **Request a correction when needed.** Ask the cashier, service desk, or support channel to correct the receipt or refund the difference. → *Expect:* you receive a corrected receipt, refund confirmation, or case number.

## Decision points

- The receipt says final sale → treat the purchase as not returnable unless local law or merchant policy says otherwise.
- The card charge is higher than the receipt total → wait for pending authorization to settle, then dispute only if the posted amount is wrong.
- The receipt is for reimbursement → keep itemized detail, proof of payment, and business purpose together.
- The barcode is faded or missing → save a photo and record the transaction number before the paper becomes unreadable.

## Failure modes & recovery

- **F1 Missing itemized detail:** detect a receipt that shows only a total, recover by asking the merchant for an itemized copy.
- **F2 Wrong quantity or duplicate scan:** detect repeated items or quantities you did not buy, recover by requesting a refund or corrected transaction.
- **F3 Discount not applied:** detect a sale price, coupon, or loyalty offer missing from the receipt, recover by showing the offer and asking for an adjustment.
- **F4 Return deadline missed:** detect that the return date has passed, recover by asking about store credit, warranty service, or manufacturer support.
- **F5 Paper fades:** detect thermal paper becoming pale, recover by scanning or photographing the receipt while it is still readable.

## Verification

The receipt's merchant, date, line items, subtotal, tax or fees, total, return deadline, barcode or code, and any error action are identified.

## Variations

- Restaurant: check tip, service charge, split payments, and adjusted final card total.
- Online order: use the invoice, packing slip, email confirmation, and return portal together.
- Jurisdiction: tax labels, return rights, warranty periods, and receipt requirements vary by country, state, province, and city.
- Business expense: attach category, project, client, and reimbursement notes before submitting.

## Safety & privacy

Low risk, but receipts can reveal card fragments, purchase habits, location, and health or personal items. Store warranty and expense receipts privately, and shred receipts that expose sensitive purchases.
