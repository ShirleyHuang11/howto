---
name: use-contactless-payment-on-transit
domain: transit
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

Pay for a transit ride with a contactless card, phone wallet, or wearable while avoiding fare errors, duplicate charges, and penalty fares.

## Preconditions

- Your transit agency accepts contactless payment on the route you plan to use.
- Your card or device is enabled for contactless payment and has funds or credit available.
- You know whether the system requires tapping out at the end of the ride.

## Steps

1. **Choose one payment token.** Pick one physical card, phone wallet card, or wearable and use it for the whole trip. → *Expect:* you know exactly what will be tapped at every reader.
2. **Confirm fare rules.** Check whether the system charges flat fare, distance fare, daily cap, weekly cap, or transfer discount. → *Expect:* you know whether a tap out or same-token transfer is required.
3. **Check balance or credit.** Make sure the account can cover the maximum fare or preauthorization. → *Expect:* the payment method is unlikely to be declined at the gate.
4. **Tap in deliberately.** Hold the chosen token flat on the reader until it confirms. → *Expect:* the reader shows accepted, green light, beep, or gate opens.
5. **Keep the token separate.** Do not wave a wallet with multiple contactless cards near the reader. → *Expect:* only the intended card or device was charged.
6. **Ride and transfer with the same token.** [BRANCH: transfer within system | exit and re-enter] tap the same token so caps and transfers connect. → *Expect:* the system treats the ride as one linked journey where eligible.
7. **Tap out if required.** At the destination, use the same token at the exit reader before leaving the paid area. ⚠️ *Irreversible:* skipping a required tap out can charge the maximum fare, so confirm the exit reader accepted before walking away. → *Expect:* the reader confirms exit or fare completion.
8. **Check charges later.** Review the transit account, bank feed, or wallet history after posting. → *Expect:* charges match the fare, cap, or maximum-fare correction rules.
9. **Dispute errors promptly.** Use the agency fare account or support form with date, station, route, and token type. → *Expect:* a case number or correction request is recorded.

## Decision points

- System has daily caps → keep using the same token all day or the cap will not apply.
- Traveling with another person → each rider needs a separate card, device, or fare product.
- Low battery phone → use a physical card before the phone dies if phone wallet access is uncertain.
- Distance fare system → tap out is part of payment, not an optional exit step.

## Failure modes & recovery

- **F1 Card clash:** detect unexpected decline or wrong card charged, recover by removing extra cards and using one token at the reader.
- **F2 Low balance or declined card:** detect red light or blocked gate, recover by topping up, using another eligible token, or buying a ticket.
- **F3 Missed tap out:** detect maximum fare or incomplete journey, recover through the agency's fare correction process.
- **F4 Duplicate charge:** detect two payments for one rider, recover by collecting timestamps and filing a dispute.
- **F5 Cap not applied:** detect charges above the cap, recover by checking whether different tokens were used.

## Verification

The same accepted payment token was used for every required tap, the ride completed without fare inspection issue, and the posted charge or cap is explainable.

## Variations

- Phone wallet: the card inside the wallet may have a different token number than the plastic card.
- Regional fare card: stored value may need online registration before disputes or lost-card protection.
- Bus only: some systems require tap in only, but proof of payment may still be inspected.
- Fare gates: wait for the gate to open for you before the next person taps.

## Safety & privacy

Medium financial risk from maximum fares and duplicate charges. Contactless travel records can reveal movement patterns, so protect account access and dispute only through official agency channels.
