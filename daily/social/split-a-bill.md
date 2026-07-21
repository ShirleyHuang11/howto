---
name: split-a-bill
domain: daily
subdomain: social
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: low
prerequisites: [daily/social/order-at-a-restaurant]
status: draft
last_verified: 2026-07-20
---

## Goal

A shared bill (meal, taxi, group purchase) is divided and settled such that the venue is paid once, everyone's share is fair *enough*, and no friendship absorbs hidden cost.

## Preconditions

- A bill exists or is imminent for a group of 2+.
- Payment/transfer channels among the group: cash, or a mutually usable payment app.

## Steps

1. **Set the split *method* before or when the bill lands — not after negotiation-fatigue.** [BRANCH: even split (default for similar orders) | pay-for-what-you-had (fair when orders diverged: someone had wine + steak, someone had soup) | one payer, reimbursed later] Someone just naming a method usually settles it: "Even split OK with everyone?" → *Expect:* an agreed method, chosen in seconds, not litigated.
2. **Determine the total including service.** Bill + tip per local custom (`daily/order-at-a-restaurant` variations) — the tip is part of the split, not the payer's private burden. → *Expect:* one number everyone is dividing.
3. **Execute the mechanics.** Even: total ÷ N, rounded *up* to a clean unit. Itemized: each claims their lines, shared plates ÷ their sharers, then proportional tip. Ask whether the venue splits cards ("Can we do two/three cards?") — many do, some don't. → *Expect:* each person's number known; venue's card-splitting policy known.
4. **Pay the venue once, cleanly.** [BRANCH: venue splits cards → each pays their number | one card pays all → others transfer to the payer *now, at the table*, by app] "Now at the table" is the load-bearing phrase — in-the-moment transfers actually happen; "I'll get you back" decays. → *Expect:* venue fully paid; transfers visibly initiated on phones before coats go on.
5. **The payer states the received total matches.** "Got it from everyone — we're square." → *Expect:* public closure; no one privately unsure whether they paid.

## Decision points

- Small disparity in an even split (your dish was cheaper by a little) → absorb it; even-split's speed is worth small noise, and it averages out across dinners. *Large* disparity → itemized was the right method; say so next time at step 1.
- Someone invited the group ("my treat" energy ambiguous) → one explicit offer/decline exchange: "Are we splitting, or—?" resolves it; don't perform wallet-reaching theater.
- One person chronically short/slow to repay → prefer venue-side splitting (everyone pays their own at the counter) with that group; structure beats resentment.
- Someone can't afford the venue's tier → the kind version happens at *restaurant-choosing* time, not bill time.

## Failure modes & recovery

- **F1 Bill math dissolving into chaos (tired group, complex orders):** revert to even split by acclamation, or the most-sober person becomes calculator for itemized; both beat a 15-minute audit.
- **F2 Venue won't split cards and nobody has the app/cash:** one pays; the group's job compresses to step 4's "transfer now" discipline — payer, name your handle out loud.
- **F3 Discovered later the payer was shorted:** payer messages the group matter-of-factly with the number; normal groups fix it in minutes. Chronic shorting → see the structural decision point.
- **F4 Currency/cash change puzzle (cash-only venue):** overpayers take change from underpayers directly; round generously toward the tip rather than engineering exact change.

## Verification

The venue was paid exactly once in full including service; every participant can name what they paid; the payer (if any) has received all transfers — confirmed aloud; and the method for this group next time got easier, not touchier.

## Variations

- Payment-app cultures (`cn` WeChat/Alipay, `us` Venmo, `eu` various): in-app group-split features do steps 3–5 mechanically — the social step 1 remains yours.
- `jp`: pay-at-counter individually ("betsu-betsu") is a normal ask; warikan (even split) is the default among peers.
- Recurring groups (weekly lunch crew): rotate the whole bill instead of splitting — cheapest in friction, self-balancing over time.

## Safety & privacy

Low risk. Money + friendship is the actual subject: the protective habits are choosing the method fast (1), transferring at the table (4), and closing publicly (5) — ambiguity, not amounts, is what damages groups.
