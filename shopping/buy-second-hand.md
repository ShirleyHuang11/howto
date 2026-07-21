---
name: buy-second-hand
domain: shopping
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

A used item is bought from a marketplace, thrift store, or private seller at a fair price, inspected before money changes hands, and the transaction completed safely.

## Preconditions

- A defined want with a known new-price reference point. The new price anchors what "a good used price" means.
- A venue: online marketplace (eBay, Facebook Marketplace, Vinted, local classifieds), a thrift store, or a known seller.
- For in-person deals: a safe meeting plan (see step 5).

## Steps

1. **Search with variants and set a price ceiling.** Try synonyms, brand names, and common misspellings; sort by newest for local classifieds. Decide your maximum before messaging anyone, based on the new price and the condition tier you will accept. → *Expect:* a shortlist with asking prices you can compare against your ceiling.
2. **Evaluate the listing before contact.** Photos of the actual item (not stock photos), specific defects mentioned, seller history and ratings where the platform has them. A price far below market is the main scam signal in either direction of the deal. → *Expect:* a listing where the age, condition, and reason for sale form a coherent story.
3. **Ask the questions the listing dodges.** Age, usage history, defects, original packaging or receipts, and for electronics the specific model number. Request an extra photo of the weak point (laptop screen on, bike drivetrain close-up, garment label). → *Expect:* prompt, specific answers. Evasive answers end the deal at zero cost.
4. **Negotiate briefly and in one round.** A fair counter with a reason ("going rate is X, I can do Y today") lands better than lowball ping-pong. Agree the price, the payment method, and the handover before meeting. → *Expect:* agreed terms in writing in the chat.
5. **Meet safely and inspect before paying.** Daytime, public place (many police stations offer marketplace-exchange zones); bring a friend for high-value items. Test the item for real: power it on, ride it, zip it, check the serial against the listing. ⚠️ *Irreversible:* private sales are almost always final. The inspection is your only warranty, so do not pay before it is done. → *Expect:* the item performs as described in your hands.
6. **Pay by the agreed method and keep the trail.** Cash or an in-person-appropriate transfer (`finance/send-money-to-a-friend` rails, noting its stranger warning: for marketplace goods use the platform's protected payment where it exists, never friends-and-family mode). Save the chat, listing screenshot, and any receipt. → *Expect:* payment made once, records kept, both parties clear.

## Decision points

- Shipping instead of meeting: use only the platform's integrated payment and shipping protection. Off-platform payment requests ("PayPal friends mode", gift cards, crypto) are the single loudest scam tell; decline and report.
- Thrift and charity stores: no negotiation and no returns in most cases, so the inspection step happens in the aisle. Check zips, seams, soles, and plug-in items at the store's test socket.
- High-value categories (phones, bikes) carry stolen-goods risk: check the serial or frame number against the free registries where your country has them, and be suspicious of sellers who cannot answer basic ownership questions.

## Failure modes & recovery

- **F1 Item fails inspection at the meeting:** walk away politely. You owe nothing for a no-sale, and renegotiating on the spot is fine only if the defect is priceable ("it needs a new battery, that is 30 off").
- **F2 Seller no-shows:** one message, thirty minutes, then leave and move on. Repeat no-shows get reported on-platform.
- **F3 Post-purchase discovery of a hidden defect:** private sale remedies are thin, but a polite message sometimes works, and platform-protected purchases have a dispute window. This is why the weak-point photo and the power-on test exist.
- **F4 Suspected scam listing (stock photos, urgency, off-platform push):** report it and disengage. Recovery from a completed scam payment runs through the payment provider and, for real losses, a police report.

## Verification

The item you inspected is the item you took home, it works as described, the price stayed at or under your ceiling, payment went through a protected or in-person channel exactly once, and the chat history documents the terms.

## Variations

- Auction formats (eBay bidding): set your ceiling as a maximum bid and do not chase past it; the ceiling discipline from step 1 is the whole skill.
- `de` classifieds culture (Kleinanzeigen) and `jp` (Mercari) have strong platform-payment norms; `us` Facebook Marketplace is meet-up heavy, which raises the weight of step 5.

## Safety & privacy

Medium risk split between money and meeting. The three protections: inspect before paying, keep payment on protected rails for shipped goods, and meet in public. Share your address only for doorstep pickups you are comfortable with, and prefer a nearby corner otherwise.
