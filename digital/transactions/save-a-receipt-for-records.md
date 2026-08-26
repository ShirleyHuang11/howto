---
name: save-a-receipt-for-records
domain: digital
subdomain: transactions
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You save a durable copy of a purchase receipt so you can prove the transaction later for returns, warranties, reimbursement, taxes, or disputes.

## Preconditions

- You can access the store account, email inbox, payment app, or checkout confirmation page that contains the receipt.
- You know what transaction you need to preserve: merchant, date, item, and amount.
- You have a secure storage location such as a cloud drive, password manager document vault, or encrypted local folder.

## Steps

1. **Open the official receipt source.** Sign in to the merchant account or open the original confirmation email; avoid using forwarded screenshots as the primary record. → *Expect:* the receipt page or email shows the merchant name, order number, date, items, taxes, fees, payment method, and total.
2. **Check the receipt details before saving.** Compare the receipt total and date against your card or bank activity. → *Expect:* the merchant, date, and amount match the payment record or the difference is explained by pending authorization timing.
3. **Save a complete PDF copy.** Use the browser print dialog or merchant download button, select `Save as PDF`, and include all pages. → *Expect:* a PDF file opens locally and contains the full order details, not only the visible first screen.
4. **Name the file consistently.** Use a sortable name such as `2026-08-25-merchant-order1234-89.20.pdf`. → *Expect:* the filename identifies the date, merchant, order number, and total without opening the file.
5. **Store it in the right records folder.** Move the PDF to the folder used for receipts, reimbursements, taxes, or warranties. → *Expect:* the file appears in the intended folder and is included in that folder's backup or sync system.
6. **Capture supporting proof if needed.** [BRANCH: physical item, photograph serial numbers, packing slip, and warranty card | service purchase, save the terms, plan name, or service dates shown on the receipt] → *Expect:* supporting files are stored beside the receipt or linked in the same record.
7. **Protect sensitive details.** If you must share the receipt, redact full address, phone number, full card digits, and unrelated items first. → *Expect:* the retained original stays private and any shared copy exposes only what the recipient needs.

## Decision points

- Receipt is for reimbursement or taxes → keep the original full receipt, not only a card statement line.
- Receipt is for a warranty → include model, serial number, retailer, and purchase date if available.
- Receipt contains multiple unrelated purchases → keep the full original, but create a redacted copy for sharing.
- Merchant provides only an in-app receipt → use the app's share/export option or take full-page screenshots as fallback.

## Failure modes & recovery

- **F1 Download omits details:** detect a PDF that lacks item lines, tax, or order number → retry with browser print using "background graphics" enabled or save from the email instead.
- **F2 Receipt link expires:** detect a dead confirmation link → search email for the order number, sign in to order history, or request a duplicate receipt from support.
- **F3 Cloud sync fails:** detect the file only exists on one device → wait for sync confirmation or store a second encrypted copy.
- **F4 Sensitive receipt shared:** detect full address or card digits in a copy sent to someone else → revoke the share link, create a redacted copy, and monitor the exposed account if necessary.

## Verification

A readable PDF or equivalent complete receipt file is stored in the chosen records location, its filename includes date, merchant, order number, and total, and the saved contents match the transaction record.

## Variations

- `mobile-app`: use the app's share, export, or print action; if unavailable, capture scrolling screenshots and store them together.
- `business-expense`: add project, client, or reimbursement category to the filename or folder metadata.
- `warranty`: store product photos, serial number, and warranty terms beside the receipt.

## Safety & privacy

Medium risk because receipts can expose payment, address, and purchase information. Keep originals in private storage, share only redacted copies, and verify the receipt total before relying on it for a claim.
