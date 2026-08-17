---
name: howto-new-car-owner
description: Keep it running and handle the bad days — oil to flat to insurance claim. Verified howto recipes for: New Car Owner.
---

# New Car Owner — howto skill

Keep it running and handle the bad days — oil to flat to insurance claim.

When the user needs any task below, follow its verified steps in order. Each step's **Expect** is the observation that confirms it worked; steps marked ⚠ are irreversible — confirm before doing them. For the full recipe (decision points, failure recovery, variations) use the howto MCP `get_howto(<id>)` or read the linked source.

## refuel a car  
`daily/refuel-a-car`

**Goal:** The car's tank is filled with the *correct* fuel, paid for, and you drive off with the cap closed and nothing on fire.

1. **Pull up with the filler side toward the pump; engine off.** No smoking, and leave the phone call for later — attention, not radiation, is the real reason.  → *Expect:* filler flap within hose reach; engine and cabin ignition sources off.
2. **Open the fuel door and uncap.** Release lever/button inside the car if it has one; hang or rest the cap per its tether.  → *Expect:* open filler neck.
3. **Authorize payment.** [BRANCH: card/phone at the pump → follow the screen | prepay inside → tell the cashier the pump number and amount | attended station → state fuel + amount and let them work]  → *Expect:* pump display resets to zero and shows "ready"/lifts to live.
4. ⚠ **Select the correct fuel and lift that nozzle.** Diesel nozzles are usually larger and color-coded differently — the *label*, not the hose color, is the truth. ⚠️ *Irreversible:* pumping the wrong fuel (especially petrol into diesel) means do-not-start-the-engine and a drained tank — triple-check the label against the flap sticker.  → *Expect:* nozzle in hand matching the car's required fuel exactly.
5. **Insert the nozzle fully into the filler neck and squeeze; latch if fitted.**  → *Expect:* fuel flowing, counter running; stay at the nozzle — this is not the moment to wander inside.
6. **Stop at the auto-click.** The first click means full — do not round up with extra squeezes ("topping off" floods the vapor system and spills).  → *Expect:* flow stopped by itself; counter shows the final amount.
7. **Return the nozzle, cap the tank until it clicks, close the flap.**  → *Expect:* cap clicked (a loose cap triggers the check-engine light later); flap flush.
8. **Collect the receipt and depart.** Prepay-inside stations: settle up if you pumped an open amount.  → *Expect:* paid in full; receipt if wanted; pump area left as found.

**Done when:** The pumped fuel type matches the flap sticker, the auto-click ended the fill with no topping-off, the cap clicked shut, payment is settled, and the gauge reads full as you pull away.

## check your engine oil  
`daily/check-your-engine-oil`

**Goal:** You confirm the engine oil level is between the minimum and maximum marks and top up with the correct grade if it is low.

1. **Park safely and let the engine cool.** Use level ground, set the parking brake, turn the engine off, and wait several minutes after driving.  → *Expect:* the car is stable and the engine bay is not dangerously hot.
2. **Open the hood and locate the dipstick.** Look for a colored loop or handle labeled engine oil; check the manual if unsure.  → *Expect:* the dipstick is identified, not the transmission dipstick.
3. **Pull and wipe the dipstick.** Remove it fully and wipe oil off with the rag.  → *Expect:* the metal blade is clean enough for a fresh reading.
4. **Reinsert and seat the dipstick fully.** Push it all the way back into its tube, then wait a moment.  → *Expect:* the dipstick is seated at its normal depth.
5. **Pull it again and read the level.** Hold it horizontal and look where the oil film reaches relative to Min and Max, Low and Full, or the crosshatched zone.  → *Expect:* the oil level is visibly between, below, or above the marks.
6. **Decide whether to top up.** [BRANCH: between marks | below minimum | above maximum] leave it alone if in range, add oil if low, and do not drive hard if overfilled or very low.  → *Expect:* the next action matches the reading.
7. **Add small amounts only if low.** Open the oil-fill cap, add the manual-specified grade in small pours, wait, and recheck with the dipstick.  → *Expect:* the level moves toward the middle or upper part of the safe range.
8. **Close everything cleanly.** Tighten the oil cap, seat the dipstick, remove the rag, close the hood, and wipe spills.  → *Expect:* no tools or rags remain in the engine bay.

**Done when:** With the engine off, cool, and the vehicle level, the dipstick oil film reads between the Min and Max marks after a wipe, reinsert, and reread.

## check tire pressure  
`daily/check-tire-pressure`

**Goal:** Set each tire to the vehicle maker's recommended cold pressure so the car handles predictably and tires wear evenly.

1. **Find the correct PSI.** Open the driver's door and read the tire placard on the door jamb, not the maximum pressure molded into the tire sidewall.  → *Expect:* front and rear PSI targets are known.
2. **Remove the first valve cap.** Put the cap in a pocket or cup holder so it cannot roll away.  → *Expect:* the valve stem is exposed and the cap is not on the ground.
3. **Press the gauge on squarely.** Push firmly until the hiss stops and the gauge locks a reading.  → *Expect:* one clear PSI number appears without continued air leakage.
4. **Compare to the placard.** [BRANCH: low | high | correct] low needs air, high needs a brief bleed, correct moves to the next tire.  → *Expect:* you know the needed adjustment for that tire.
5. **Top up low tires in short bursts.** Add air for a few seconds, then recheck with the gauge instead of guessing by tire shape.  → *Expect:* the reading rises toward the placard PSI.
6. **Bleed high tires carefully.** Press the valve pin briefly with the gauge nub or a small tool, then recheck.  → *Expect:* the reading drops slowly and stays near target.
7. **Replace the valve cap.** Screw it on finger tight only.  → *Expect:* the valve is covered and the cap threads are not crossed.
8. **Repeat for all tires, including the spare if accessible.** Note any tire that was much lower than the rest.  → *Expect:* all checked tires match the placard within about 1 PSI.

**Done when:** Each tire's cold pressure matches the door-jamb placard within about 1 PSI, valve caps are installed, and no valve is hissing.

## change a flat tire  
`daily/change-a-flat-tire`

**Goal:** Replace a flat tire with the spare tire using the vehicle jack and lug wrench without putting yourself under an unstable car.

1. **Choose the safest stopping place.** Pull well off the road, avoid soft shoulders and slopes, and call roadside help if the location is unsafe.  → *Expect:* the car is stable and traffic is not passing close to your body.
2. **Secure the vehicle.** Shift to park or gear, set the parking brake, and place a wheel chock or heavy object opposite the flat if available.  → *Expect:* the car does not roll when gently rocked.
3. **Find the jack point.** Use the owner's manual or the notched reinforced point near the flat tire.  → *Expect:* the jack saddle lines up with reinforced metal, not plastic trim or a floor pan.
4. **Loosen lug nuts before lifting.** Turn each lug nut counterclockwise about a half turn while the tire is still on the ground.  → *Expect:* each nut breaks free without the wheel spinning.
5. ⚠ **Raise the car only enough.** Jack slowly until the flat tire clears the ground by about 1 inch. ⚠️ *Irreversible:* a slipping jack can crush or kill; never put any part of your body under the car.  → *Expect:* the jack stands vertical and the tire spins free.
6. **Remove the flat tire.** Finish removing the lug nuts, keep them together, and pull the wheel straight off.  → *Expect:* the hub is exposed and no lug nut is missing.
7. **Mount the spare.** Lift the spare onto the studs, then hand-thread all lug nuts with the tapered side facing the wheel.  → *Expect:* every nut turns several threads by hand without cross-threading.
8. **Snug in a star pattern.** Tighten the nuts lightly across from each other while the wheel is still raised.  → *Expect:* the spare sits flat against the hub.
9. **Lower and tighten firmly.** Lower the car until the tire touches ground, tighten in a star pattern, then lower fully and remove the jack.  → *Expect:* the wheel is secure and the car rests normally.
10. **Check pressure and limits.** Read the spare's speed and distance limit, then get the lug torque checked with a torque wrench soon.  → *Expect:* you know the temporary spare limit and the flat is stored safely.

**Done when:** The spare tire is mounted flush, all lug nuts are tightened in a star pattern, the jack is removed, and the car can roll slowly without wobble or scraping.

## jump start a car  
`daily/jump-start-a-car`

**Goal:** Start a car with a weak battery using another car or jump pack without reversing polarity, sparking at the battery, or touching moving parts.

1. **Position the power source.** Park the good car close enough for cables to reach, but keep the vehicles from touching.  → *Expect:* both batteries are reachable and the cable path avoids belts, fans, and hot exhaust.
2. **Turn everything off.** Switch off ignitions, lights, climate controls, radios, and chargers in both cars.  → *Expect:* dashboards are dark except any unavoidable security indicators.
3. **Identify terminals and bare metal.** Find dead positive, good positive, good negative, and an unpainted metal ground on the dead car away from the battery.  → *Expect:* plus and minus marks are visible and the ground point is solid engine or chassis metal.
4. **Connect red to dead positive.** Clamp the red cable to the dead battery positive terminal.  → *Expect:* the clamp grips clean metal and does not touch any other part.
5. **Connect red to good positive.** Clamp the other red end to the good battery positive terminal.  → *Expect:* both red clamps are on positive terminals only.
6. **Connect black to good negative.** Clamp the black cable to the good battery negative terminal.  → *Expect:* the black clamp is secure on the good car negative post.
7. ⚠ **Connect black to dead-car metal ground.** ⚠️ *Irreversible:* wrong cable order or polarity can damage electronics or ignite battery gas; confirm red is on positive before placing this final black clamp.  → *Expect:* the final black clamp is on bare metal away from the dead battery.
8. **Start the good car, then the dead car.** Run the good car for 2 to 5 minutes, then crank the dead car for no more than 5 seconds at a time.  → *Expect:* the dead car starts or the starter sound improves after each rest.
9. **Remove cables in reverse order.** Remove black from dead-car metal, black from good negative, red from good positive, then red from dead positive.  → *Expect:* no clamp touches another clamp or loose metal during removal.
10. **Keep the revived car running.** Drive or idle it in a safe place for at least 20 minutes, then arrange a battery and charging-system check.  → *Expect:* the engine keeps running after cables are removed.

**Done when:** The revived car starts, cables are removed in reverse order, all clamps are clear of metal, and both vehicles show no warning smoke, smell, or exposed cable damage.

## replace a windshield wiper  
`daily/replace-a-windshield-wiper`

**Goal:** Replace a worn windshield wiper blade with the correct size so it clears water without streaking or scratching the glass.

1. **Measure or confirm the blade size.** Check the owner's manual, parts lookup, or the old blade length before opening the package.  → *Expect:* each side's blade length is known and the new blades match.
2. **Lift one wiper arm carefully.** Raise it until it holds itself away from the windshield, then lay a folded towel under the bare arm path.  → *Expect:* the arm is stable and the glass is protected.
3. **Find the release tab.** Rotate the blade slightly and look for the tab, latch, or button where the blade meets the arm.  → *Expect:* the locking point is visible before you pull.
4. **Release the old blade.** [BRANCH: tab | button | clip] press the tab, push the button, or open the clip while sliding the blade off the arm.  → *Expect:* the blade separates without bending the arm.
5. ⚠ **Keep control of the arm.** Hold the metal arm with one hand while the blade is off. ⚠️ *Irreversible:* a dropped bare arm can crack or scratch the windshield, so do not let it snap down.  → *Expect:* the arm stays raised and controlled.
6. **Install the new blade.** Slide or click the new blade into the same connector path until the lock seats.  → *Expect:* you hear or feel a firm click and the blade cannot slide free with a light tug.
7. **Lower the blade onto the towel.** Guide the arm down slowly, then remove the towel after the rubber rests on the glass.  → *Expect:* the rubber edge sits flat against the windshield.
8. **Repeat on the other side.** Match the second blade to its side because left and right lengths may differ.  → *Expect:* both new blades are installed and locked.
9. **Test with washer fluid.** Turn the key to accessory mode if needed and run the washers with one wipe cycle.  → *Expect:* both blades sweep smoothly without chatter or hitting trim.
10. **Do the smear check.** Look through the cleaned area in daylight or with headlights on glass.  → *Expect:* no broad streaks, missed arcs, or oily smears remain.

**Done when:** Both wiper blades are locked to the arms, sweep the windshield without contact or chatter, and leave a clear view after one washer cycle.

## get car insurance quotes  
`daily/get-car-insurance-quotes`

**Goal:** Collect comparable car insurance quotes and identify the best value for the coverage you actually need.

1. **Gather current coverage.** Pull your declarations page or write down liability limits, collision, comprehensive, uninsured motorist, medical coverages, deductibles, and extras.  → *Expect:* you have a baseline policy to match.
2. **Prepare driver and vehicle information.** Collect VIN, mileage, use type, annual distance, parking location, safety features, and driver histories.  → *Expect:* each quote can be entered consistently.
3. **Choose quote sources.** [BRANCH: direct insurers | broker or comparison site] use at least three sources and include one human agent if your situation is complex.  → *Expect:* you have multiple legitimate quote channels.
4. **Compare like for like.** Set the same liability limits, deductibles, excess, rental coverage, roadside assistance, and optional endorsements across quotes.  → *Expect:* price differences are not caused by hidden lower coverage.
5. **Test deductible tradeoffs.** Raise or lower collision and comprehensive deductibles only to amounts you could pay after a claim.  → *Expect:* you can see how excess affects premium.
6. **Check discounts and terms.** Ask about bundling, mileage, telematics, student, defensive driving, anti-theft, and paid-in-full discounts.  → *Expect:* each quote includes applicable discounts and policy fees.
7. **Review claim reputation.** Look at complaint indexes, repair network rules, rental limits, and customer service reputation.  → *Expect:* the cheapest quote is not evaluated on price alone.
8. ⚠ **Save quote details.** Keep quote numbers, effective dates, coverage pages, and expiration times before deciding. ⚠️ *Irreversible:* do not cancel an old policy until the new policy is bound and active.  → *Expect:* you can bind coverage without a gap.

**Done when:** You have at least three quote records with matching core coverages, clear deductibles or excess, total premium, and effective dates.

## file a car insurance claim  
`daily/file-a-car-insurance-claim`

**Goal:** Open a car insurance claim with accurate crash information, a claim number, and a clear next step for repair or payout.

1. **Make the scene safe first.** Move to a safe location if possible, turn on hazards, and call emergency services for injuries, blocked lanes, suspected impairment, or major damage.  → *Expect:* people are safer than the vehicles.
2. **Exchange required information.** Get names, phone numbers, driver licenses, plate numbers, insurance details, vehicle descriptions, and witness contacts.  → *Expect:* you can identify every involved party.
3. **Document the scene.** Photograph vehicle positions, damage, plates, road signs, signals, skid marks, debris, weather, and injuries if appropriate.  → *Expect:* photos show context before vehicles are moved or repaired.
4. **Avoid admitting fault.** Stick to facts with drivers, police, tow operators, and insurers.  → *Expect:* you have not guessed blame or accepted private pressure.
5. **Contact your insurer.** [BRANCH: app or web | phone] report the date, time, location, vehicles, people, police report number if any, and what happened.  → *Expect:* the insurer opens or prepares a claim.
6. **Record the claim number.** Save the claim number, adjuster contact, repair instructions, rental rules, and upload link.  → *Expect:* you can refer to one claim record in later calls.
7. **Ask about deductible and coverage.** Confirm whether collision, comprehensive, liability, uninsured motorist, rental, towing, or glass coverage applies.  → *Expect:* you know what costs may come out of pocket.
8. ⚠ **Follow repair and inspection steps.** Use approved estimates, photos, repair shops, or adjuster appointments as instructed. ⚠️ *Irreversible:* settling or signing a release can close rights, so read payout and injury documents before accepting.  → *Expect:* the next claim action is scheduled or submitted.

**Done when:** The insurer has issued a claim number and you have documented the next required action, deductible status, and contact channel.

## renew your car registration  
`daily/renew-your-car-registration`

**Goal:** Renew your vehicle registration before the deadline and place any new sticker or document where required.

1. **Read the renewal reminder.** Check the plate number, VIN, expiration date, fee, and any missing requirement listed.  → *Expect:* you know the deadline and what blocks renewal.
2. **Gather documents.** Have registration notice, plate number, VIN, odometer if requested, insurance proof, inspection result, emissions result, and payment.  → *Expect:* the renewal form can be completed without searching mid-process.
3. **Choose the renewal channel.** [BRANCH: online | mail or in-person] use online if eligible, or choose a licensing office, kiosk, or mail option if documents need review.  → *Expect:* you are using an accepted channel for your vehicle.
4. **Confirm vehicle and owner details.** Verify name, address, plate, VIN, and vehicle description before paying.  → *Expect:* the renewal shows the correct vehicle and mailing address.
5. ⚠ **Pay the fees.** Submit the required fee and save the receipt or confirmation number. ⚠️ *Irreversible:* renewal fees and penalties may not be refundable, so confirm the plate and VIN first.  → *Expect:* payment is accepted and a confirmation appears.
6. **Receive the proof.** Download, print, or wait for the registration card, sticker, decal, or electronic record.  → *Expect:* you have temporary or final proof of renewal.
7. **Install the sticker correctly.** Clean the plate or windshield area and apply the new sticker exactly where local rules specify.  → *Expect:* the displayed month or year matches the renewed period.
8. **Store the document.** Put the registration card in the vehicle or approved digital wallet, and discard old copies that could confuse a stop.  → *Expect:* the vehicle carries current proof.

**Done when:** The vehicle record, registration card, or sticker shows a current expiration date for the correct plate and VIN.

## deal with a car that wont start  
`daily/deal-with-a-car-that-wont-start`

**Goal:** Diagnose the likely reason a car will not start and choose a safe next action.

1. **Make the location safe.** Shift to park or neutral, set the parking brake, turn on hazard lights if near traffic, and stay visible.  → *Expect:* the vehicle will not roll and other drivers can see it.
2. **Check the dashboard and lights.** Turn the key or press start and watch whether interior lights, headlights, and warning lights work.  → *Expect:* you know if electrical power is present.
3. **Listen during start.** [BRANCH: rapid clicks | one click | silence | cranks normally but will not start] use the sound to guide the next check.  → *Expect:* the symptom category is clear.
4. **Check simple lockouts.** Confirm the transmission is in park or neutral, clutch is pressed if manual, brake pedal is pressed if required, and steering wheel is not locked.  → *Expect:* start interlocks are satisfied.
5. **Check the key or fob.** Hold the fob near the start button or use the backup key method from the manual.  → *Expect:* the car recognizes the key if fob battery was weak.
6. **Treat dim lights or rapid clicks as a battery problem.** Jump-start only with correct polarity and a safe donor battery or jump pack.  → *Expect:* the engine starts or cranks stronger after the jump.
7. **Treat one solid click as possible starter trouble.** Do not keep trying repeatedly if the battery seems strong.  → *Expect:* you avoid overheating wiring or draining the battery.
8. **Treat normal cranking as fuel, ignition, or engine-management trouble.** Check fuel level and warning messages, then stop extended cranking.  → *Expect:* the battery is preserved for diagnosis or towing.
9. **Call for help when the quick checks fail.** Contact roadside assistance, a mechanic, or emergency services if stopped in a dangerous location.  → *Expect:* a jump, tow, or traffic protection is arranged.

**Done when:** The car starts and can be moved safely, or the likely failure category is identified and roadside assistance, a mechanic, tow, or emergency service has been contacted.

