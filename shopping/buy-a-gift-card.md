---
name: buy-a-gift-card
domain: shopping
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Buy a legitimate gift card that activates correctly and can be given without exposing the balance to theft.

## Preconditions

- You know the recipient's preferred store, platform, or card network.
- You can pay with a normal payment method at a staffed register, kiosk, or trusted website.
- You are not buying the card because someone demanded payment by gift card.

## Steps

1. **Choose the card type.** Pick a store-specific card for a known preference, or a general prepaid card only if the fees are acceptable. → *Expect:* the card matches where the recipient can actually use it.
2. **Inspect the rack card.** Check that packaging is sealed, the scratch-off PIN area is intact, and no sticker covers the barcode or number. → *Expect:* there are no cuts, glue marks, exposed numbers, or mismatched labels.
3. **Prefer a front card from a staffed area.** Avoid cards hanging where anyone could tamper with them unnoticed. → *Expect:* the card came from a supervised rack or from behind the counter.
4. **Take the card to checkout.** Ask the cashier to activate the exact amount you want. ⚠️ *Irreversible:* once activated, many gift cards cannot be refunded, so confirm the brand and value before payment. → *Expect:* the register prints an activation receipt.
5. **Check activation before leaving.** Compare the receipt brand, last digits if shown, and loaded amount with the card. → *Expect:* the activation receipt matches the card in your hand.
6. **Keep the receipt separate.** Put the activation receipt in your wallet or a separate envelope, not inside the gift-card package if mailing. → *Expect:* you can prove purchase if the balance is missing.
7. **Hide the code until gifting.** Do not scratch the PIN or photograph the number unless you are redeeming it yourself. → *Expect:* the card number and PIN remain covered.
8. **Add a note with basics.** Tell the recipient to use the card promptly and keep it until the balance is zero. → *Expect:* the recipient knows not to throw it away after one partial purchase.
9. **Walk away from suspicious demands.** If anyone says to buy gift cards to pay a debt, fine, bill, tax, tech support fee, or emergency, stop and verify independently. → *Expect:* no card is bought for a demand that behaves like a scam.

## Decision points

- The packaging looks opened → choose another card or ask for one from behind the counter.
- The store cannot provide an activation receipt → buy elsewhere.
- The card has purchase or monthly fees → choose a store card or different gift.
- The recipient needs online delivery → use the official retailer site, not a search-ad link.
- Someone is coaching you by phone or text during purchase → leave the checkout line and call a trusted person.

## Failure modes & recovery

- **F1 Tampered card:** detect scratched PIN, extra sticker, or torn package, recover by rejecting it before activation.
- **F2 Activation failed:** detect missing or failed activation receipt, recover by asking the cashier to void or retry before leaving.
- **F3 Wrong brand:** detect the receipt or card brand does not match the intended store, recover by correcting before payment if possible.
- **F4 Drained balance:** detect a zero balance soon after purchase, recover by contacting the card issuer with card and activation receipt.
- **F5 Scam demand:** detect pressure, secrecy, or threats, recover by stopping contact and verifying through an official number.

## Verification

The card is sealed, the activation receipt shows the correct brand and value, and no one except the recipient has seen the PIN.

## Variations

- Digital cards: buy from the retailer's official app or site and check the recipient email twice before sending.
- General prepaid cards: read fees and expiration rules before purchase.
- Holiday racks: inspect more carefully because crowded racks are easier to tamper with.
- Mailed gifts: send the receipt separately or keep a photo of the receipt, not the PIN.

## Safety & privacy

Gift cards are a scammer's demand, never pay taxes/bills/fines with them. Do not share card numbers, PINs, receipt barcodes, or activation codes with anyone except the intended recipient or the official card issuer.
