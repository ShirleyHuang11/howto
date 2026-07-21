---
name: pay-at-a-cashier
domain: daily
subdomain: social
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

Your selected items are paid for at a staffed checkout, you hold the receipt and any change, and you leave the counter with the items bagged.

## Preconditions

- Items to purchase are in hand, a basket, or a cart.
- A payment method the store accepts (card/phone, or cash in local currency).
- The store has staffed checkout lanes (for self-checkout, see Variations).

## Steps

1. **Choose an open lane and join the end of the line.** An open lane has a cashier present and its light on (where used). Respect the queue: stand behind the last person, keep a small gap, and don't crowd the customer paying. → *Expect:* you are the last in a single-file line; anyone arriving after you stands behind you.
2. **Wait and advance with the line.** Place a divider bar behind the previous customer's items if a belt is used. → *Expect:* the line advances; eventually the customer ahead of you is paying.
3. **Place your items on the belt/counter when space opens.** Put a divider before your items; heavy items first, fragile last. → *Expect:* all your items are on the belt, separated from the next customer's by dividers.
4. **Greet the cashier when they address you.** A brief greeting and answering their questions (loyalty card? bags?) is the expected script; declining is fine — "No, thanks." → *Expect:* the cashier scans your items; a running total shows on the display.
5. **Watch the total and any prompts.** → *Expect:* the announced/displayed total is plausible for your items; scanning finishes and the cashier states the total.
6. **Pay.** [BRANCH: tap card/phone on the reader | insert card and enter PIN | hand cash over] For cash, hand notes into the cashier's hand or the tray — count roughly beforehand so you're not searching under pressure. → *Expect:* reader shows "approved", or the cashier counts your cash and the drawer opens.
7. **Receive change and the receipt.** Count large change briefly at the counter — discrepancies are only fixable on the spot. → *Expect:* change matches (amount tendered − total); receipt in hand or offered.
8. **Bag your items and clear the counter promptly.** Step aside if you need time to pack; the next customer is waiting. → *Expect:* you leave the lane with items, receipt, and payment method all in your possession.

## Decision points

- An item won't scan or has no price → the cashier calls for a price check; decide to wait or drop the item.
- Total is higher than expected → ask before paying: "Could you check the price on X?" — after payment it becomes a service-desk trip.
- Card declined → F1; have a fallback method ready.
- Lane closes as you queue ("this lane is closing") → move to the lane the cashier directs you to; arrival order is loosely preserved by custom, not enforced.

## Failure modes & recovery

- **F1 Card declined:** try once more or a second card/cash; if nothing works, apologize, ask them to hold the items ("set aside"), and resolve payment before returning.
- **F2 Wrong change:** state it immediately and politely at the counter with the receipt; cashiers can correct on the spot, and drawers are counted, so honest errors resolve quickly.
- **F3 Forgot an intended item mid-checkout:** either drop it from this trip or ask the cashier to wait *only* if the item is seconds away; otherwise pay and re-queue — holding the line for a store run violates the queue norm.
- **F4 Left the payment card/receipt at the counter:** return immediately to the same cashier; unclaimed cards go to the service desk.

## Verification

You possess: all purchased items (bagged), the receipt listing exactly those items, correct change (if cash), and your own payment card/phone. The lane behind you flows normally — you left nothing on the belt or counter.

## Variations

- Self-checkout: you scan and bag yourself; a weight sensor flags mismatches — place each item in the bagging area immediately after scanning; an attendant approves alcohol and errors.
- `jp`: cash goes in the small tray, not hand-to-hand; change is returned tray-first with the receipt.
- Card-minimum stores: small purchases may require cash or a minimum spend — the sign is usually at the register.

## Safety & privacy

Low risk. Shield the PIN pad with your hand; keep your wallet in sight on the counter, not on the belt; the receipt may show a partial card number — treat it as personal, not litter, if discarding in public.
