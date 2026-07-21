---
name: navigate-a-layover
domain: travel
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Move through a layover efficiently, including terminal changes, security, customs, and tight-connection decisions.

## Preconditions

- Boarding pass or reservation for the onward flight.
- Arrival and departure airport, terminals, and boarding time known if available.
- Passport, visa, or entry documents ready for international connections.

## Steps

1. **Check the real connection time.** Use arrival gate time, boarding time, and door-close time, not just scheduled departure. → *Expect:* you know how many usable minutes remain.
2. **Confirm the onward gate.** Check the airline app, airport screens, or gate monitors. → *Expect:* you have a current gate or know it is not posted yet.
3. **Follow transfer signs first.** Look for "Connections," "Transfers," or the terminal train instead of exiting blindly. → *Expect:* you stay inside the correct passenger flow when possible.
4. **Handle terminal changes.** [BRANCH: airside transfer | landside transfer] use trains, buses, or walking routes based on airport signage. → *Expect:* you know whether security will be encountered again.
5. **Account for security.** If you leave the secure area or change certain terminals, join screening early. → *Expect:* liquids, laptop, and documents are ready before the checkpoint.
6. **Account for customs and immigration.** On many international arrivals, you may need passport control, bag claim, customs, recheck, and security. → *Expect:* you do not assume an international transfer behaves like a domestic one.
7. **Move differently when tight.** Tell airline staff you have a tight connection, walk directly, and skip food and bathrooms unless urgent. → *Expect:* every minute goes toward the gate.
8. **Watch for gate changes.** Recheck screens after each major move, especially after trains or security. → *Expect:* you do not arrive at an abandoned gate.
9. **Board when called.** Be at the gate before boarding closes, with documents out if international. → *Expect:* the gate agent can scan you without delay.
10. **React quickly if missed.** Go to the airline service desk or app rebooking flow. → *Expect:* you enter the recovery queue before later passengers.

## Decision points

- Minimum connection time is unrealistic after a delay → ask airline staff about protection and rebooking before sprinting blindly.
- Checked bag must be reclaimed → follow baggage-transfer instructions, not just passenger-transfer signs.
- Separate tickets → assume no protection, collect bags if needed, and allow much more time.
- Airport requires transit visa → resolve with airline or border staff; do not ignore document checks.

## Failure modes & recovery

- **F1 Wrong terminal exit:** detect when signs switch to baggage claim or public arrivals, recover by asking staff how to reach connections.
- **F2 Security line eats time:** detect boarding starting while still queued, recover by alerting staff politely and showing the boarding pass.
- **F3 Gate changed:** detect mismatch between app and monitor, recover by trusting the newest airport or airline display and rechecking.
- **F4 Missed connection:** detect gate closed or flight departed, recover through airline rebooking, hotel, meal, and bag-tracking procedures.

## Verification

You arrive at the correct onward gate before boarding closes, or you have started official rebooking if the connection is missed.

## Variations

- Domestic same-airline layover: often airside and fastest, but still check terminal changes.
- International to domestic: often requires immigration, customs, bag recheck, and security.
- Long layover: confirm whether leaving the airport requires a visa and enough buffer to return through security.

## Safety & privacy

Medium risk from missed flights, immigration rules, and document exposure. Keep passport and boarding pass secure, and do not leave the secure area unless you know the return requirements.
