---
name: buy-a-gift-within-a-budget
domain: shopping
subdomain: buying
locale: [generic]
interface: web
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-08-25
---

## Goal

You buy a suitable gift that arrives on time, respects the recipient's preferences, and stays within a fixed all-in budget.

## Preconditions

- You know the recipient, occasion, delivery deadline, and any relevant sizes, allergies, restrictions, or preferences.
- You have a total budget including tax, shipping, wrapping, cards, and delivery fees.
- You have a valid shipping address or pickup plan.

## Steps

1. **Define constraints.** Write the budget, delivery deadline, recipient preferences, and items to avoid. → *Expect:* a clear shopping brief.
2. **Generate a short candidate list.** Choose three to five gifts that fit the person's interests and practical constraints. → *Expect:* options are relevant, not generic filler.
3. **Check total delivered cost.** For each candidate, include tax, shipping, wrapping, personalization, and delivery fees. → *Expect:* each option has an all-in cost.
4. **Verify timing and returnability.** Confirm delivery date, pickup availability, gift receipt, exchange policy, and whether personalized items are final sale. → *Expect:* late or hard-to-return options are flagged.
5. **Pick the best fit under budget.** Choose the option with the best recipient fit that stays within the all-in cap. → *Expect:* one selected gift and one backup.
6. **Enter recipient and message carefully.** Use the correct address, name spelling, gift note, and hide prices if desired. → *Expect:* checkout preview shows recipient-facing details correctly.
7. **Place the order after final review.** ⚠️ *Irreversible:* confirm total, arrival date, recipient address, and personalization before paying. → *Expect:* order confirmation shows the gift, total, and delivery estimate.
8. **Track delivery.** Save tracking and set a reminder to confirm arrival before the occasion. → *Expect:* you can intervene if shipment stalls.

## Decision points

- Best gift exceeds budget → choose the backup or reduce extras before increasing spend.
- Delivery misses the occasion → switch to pickup, digital gift, local florist, or printable card.
- Recipient may need to exchange it → prioritize gift receipt and easy returns over a slightly lower price.
- Personalization is uncertain → avoid irreversible custom text unless spelling and details are confirmed.

## Failure modes & recovery

- **F1 Wrong address:** detect address mismatch on confirmation → contact merchant immediately to change or cancel.
- **F2 Late shipment:** detect tracking will miss deadline → arrange local replacement or digital backup.
- **F3 Budget creep:** detect add-ons pushing total over cap → remove wrapping, rush shipping, or extras.
- **F4 Unusable gift:** detect allergy, duplicate item, or wrong size → use gift receipt or exchange policy.

## Verification

The gift order confirmation shows the selected item, recipient address, estimated arrival on or before the deadline, and final total at or below the all-in budget.

## Variations

- `digital`: verify the recipient's email and delivery time before sending.
- `international`: include customs, duties, address format, and restricted items.
- `local-pickup`: confirm pickup person, hours, and whether the recipient will be notified.

## Safety & privacy

Medium risk because recipient address and payment data are exposed. Use trusted merchants, double-check private messages and addresses, and avoid gifts that reveal sensitive personal information unintentionally.
