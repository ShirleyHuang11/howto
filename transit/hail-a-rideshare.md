---
name: hail-a-rideshare
domain: transit
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 30min
risk: medium
prerequisites: [accounts/create-an-online-account, have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

A rideshare (Uber/Lyft/Didi/Grab-class) takes you from pickup to destination — the right car, the fare you agreed to, and the ride's safety checks actually performed.

## Preconditions

- The locally dominant app installed with account and payment set (`accounts/create-an-online-account`).
- Phone charged enough to survive the ride (the app *is* your ticket, receipt, and safety system).

## Steps

1. **Set the destination first, then the pickup point.** Type the destination; then check the app's guessed pickup pin — drag it to where a car can actually stop (not mid-block on a highway, not inside the pedestrian mall). Airports/malls: use the app's designated pickup zones. → *Expect:* fare estimate and ETA shown for a pickup point a car can legally reach.
2. **Choose the tier and confirm the price.** Economy/shared/XL per group size and luggage; the up-front price is the agreement — surge pricing shows here, and "wait 10 minutes" is a legitimate response to a surge multiplier. → *Expect:* a booked ride with driver name, photo, car model, and **plate number** on screen.
3. **Match the car before you touch the door.** Plate first (the unfakeable one), then model/color, then the driver's face. ⚠️ *Irreversible:* getting into an unverified car is the category's central risk — the plate check is non-negotiable, and asking "who are you here for?" (making *them* say your name) beats announcing yours. → *Expect:* plate, car, and driver all match the app; they said your name.
4. **Ride with the app open.** Seatbelt on; the app's route trace runs; share-trip-status with a contact for night rides (one tap, built-in). A driver going firmly off-route without explanation → speak up, and the in-app safety button exists. → *Expect:* the blue dot follows roughly the app's proposed route to your destination.
5. **End the ride and check out clean.** Confirm you're at the destination (or a sane drop point you approved), take your belongings — phone, wallet, the bag in the trunk — *before* the car leaves. → *Expect:* everything in hand; the ride auto-completes and charges the stored payment.
6. **Verify the receipt.** The charged fare ≈ the quoted fare (tolls/wait fees legitimately add); rate/tip per the local norm. → *Expect:* receipt matches the agreement; anomalies → F3.

## Decision points

- Long wait vs. walk: dragging your pickup pin 200 m to a main road often cuts the ETA more than any other action.
- Cash-payment markets (`some Grab/Didi regions`): confirm the payment method *before* booking — the end-of-ride cash scramble is avoidable.
- Kids/car-seat needs, accessibility, extra luggage → the tier options encode these (car-seat tiers, assist tiers, XL); book the right one rather than negotiating curbside.

## Failure modes & recovery

- **F1 Driver can't find you / phones you:** state the pickup pin's landmark, or re-drag the pin and let the app re-route them; noisy locations have designated boards (airport zone C, etc.) — name the sign you're under.
- **F2 Wrong car stopped at your feet (right place, different plate):** it's someone else's ride or an unbadged tout — wave it off; your car's plate is on your screen.
- **F3 Fare surprise (route detour, unexpected fees):** the app's trip-history dispute flow with the map trace as evidence — it works and refunds; do it same-day.
- **F4 Left something in the car:** the app's lost-item flow calls the driver through masked numbers; act immediately (drivers loop the same zones), expect a return fee to be fair.
- **F5 Ride canceled on you repeatedly (destination discrimination, surge fishing):** rebook without preamble; report the cancellations — the pattern is policed, your report is the data.

## Verification

Plate-matched car, route roughly as proposed, arrived at the intended destination with all belongings, charged what was quoted (± legitimate fees), and the receipt sits in trip history for any dispute window.

## Variations

- `cn` Didi: virtual plates/codes at busy pickups — you match a 4-digit code instead of announcing names; `sea` Grab: cash common, motorbike tiers exist; street taxis with app-hailing hybrids (`jp`, `de`): the plate-match rule survives every variant.
- No-app fallback (dead phone): licensed taxi ranks at stations/airports are the analog channel with its own recipe.

## Safety & privacy

Medium risk with three locks: the plate match (step 3), the they-say-your-name rule, and the in-app trace/share while riding. Your home address accumulates in ride history — use a nearby corner as the saved "home" if that bothers you (it reasonably might).
