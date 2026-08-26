---
name: call-for-roadside-assistance
domain: transit
subdomain: vehicle
locale: [generic]
interface: phone-call
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You request the right roadside service, give a precise location, and stay safe until help arrives.

## Preconditions

- The vehicle is stopped or disabled and you are in the safest available location.
- You have a phone with battery and your membership, insurance, vehicle, or warranty assistance number if available.
- You know whether you need towing, jump-start, lockout, fuel delivery, tire service, or winching.

## Steps

1. **Make the scene visible.** Turn on hazard lights and move away from traffic exposure if safe. → *Expect:* the vehicle is easier for traffic and responders to see.
2. **Find your exact location.** Use GPS map, highway mile marker, exit number, cross street, direction of travel, parking-lot name, or landmark. → *Expect:* you can describe where the vehicle is without guessing.
3. **Call the correct provider.** [BRANCH: immediate danger or injury, call emergency services | no immediate danger, call insurer, auto club, vehicle roadside program, rental company, or local tow] → *Expect:* you reach a dispatcher who can send help.
4. **State the problem clearly.** Give service needed, vehicle year/make/model/color, plate, whether wheels roll, and any special conditions. → *Expect:* the provider selects the right truck or service vehicle.
5. **Confirm costs and destination.** Ask about coverage, out-of-pocket charges, tow mileage limits, payment method, and where the vehicle will go. → *Expect:* you understand the charge and destination before dispatch.
6. **Get the dispatch details.** Ask for ETA, company name, driver name if available, truck description, and reference number. → *Expect:* you can identify the assigned provider.
7. **Wait safely.** Stay belted inside if roadside exposure is high, or stand well behind a barrier if that is safer; keep phone available. → *Expect:* you are not standing in a strike zone.
8. **Verify the responder.** Before handing over keys, match the truck/company or reference number to the dispatch details. → *Expect:* the person assisting is the dispatched provider.

## Decision points

- Vehicle is in a live lane, tunnel, bridge, or blind curve → call emergency services or highway patrol first.
- Phone battery is low → send location to a trusted contact and keep calls short.
- Provider ETA is unsafe or excessive → ask for escalation, police/highway assistance, or another authorized provider.

## Failure modes & recovery

- **F1 Location unclear:** detect dispatcher cannot find you → use map coordinates, mile markers, nearby signs, or share a live location link if supported.
- **F2 Wrong truck dispatched:** detect tow truck cannot handle AWD, low clearance, EV, or heavy vehicle → stop hookup and request correct equipment.
- **F3 Surprise charge:** detect higher fee on arrival → call the dispatch line before authorizing service.
- **F4 Responder cannot find you:** detect missed calls or drive-bys → turn on hazards, describe direction of travel, and stay on the line if safe.

## Verification

A dispatch reference number, provider name, ETA, service type, and cost/coverage terms are recorded, and the arriving responder matches the dispatch information.

## Variations

- Rental car: call the rental company's roadside number because unauthorized towing can create fees.
- EV: specify electric vehicle, battery state, and whether it can roll; flatbed towing may be required.
- `us`: highway service patrols exist in many regions and may assist free on major roads.

## Safety & privacy

Medium risk from roadside exposure, payment fraud, and vehicle custody. Confirm the provider before surrendering keys, share location only with trusted parties, and prioritize emergency services when traffic danger is immediate.
