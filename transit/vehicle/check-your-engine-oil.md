---
name: check-your-engine-oil
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You measure engine oil level correctly and decide whether the vehicle needs oil added or service.

## Preconditions

- The vehicle is parked on level ground.
- The engine is off; follow the owner's manual for whether to check warm after waiting or cold.
- A clean rag or paper towel is available.

## Steps

1. **Let oil settle.** Turn off the engine and wait several minutes unless the manual specifies a cold check. → *Expect:* oil has drained back into the pan for an accurate reading.
2. **Open and secure the hood.** Use the hood prop or struts. → *Expect:* the engine bay is safely accessible.
3. **Find the dipstick.** Look for a yellow, orange, or labeled handle; some vehicles use an electronic oil-level menu instead. → *Expect:* you can access the oil-level indicator.
4. **Wipe the dipstick clean.** Pull it out, wipe it fully, and reinsert it all the way. → *Expect:* the first smear is removed.
5. **Read the level.** Pull it out again and compare the oil film with the min/max marks or crosshatched area. → *Expect:* the level is identified as low, acceptable, or overfull.
6. **Inspect oil condition.** Look for milky fluid, metal glitter, burnt smell, or no oil on the stick. → *Expect:* any warning signs are noticed before driving far.
7. **Decide next action.** [BRANCH: level in range, replace dipstick and close hood | level low, add the correct oil gradually | level overfull or contaminated, seek service] → *Expect:* the vehicle is not driven with a known unsafe oil condition.

## Decision points

- Oil is below the minimum mark → add correct oil in small amounts and recheck.
- No oil appears on the dipstick → do not run the engine except as necessary to move to safety; seek service.
- Oil looks milky or foamy → possible coolant contamination; schedule service.

## Failure modes & recovery

- **F1 Cannot find dipstick:** check the owner's manual; some modern cars display oil level electronically.
- **F2 Reading is smeared:** wipe and reinsert again, keeping the dipstick oriented consistently.
- **F3 Hood will not latch after check:** reopen, inspect for obstruction, and close firmly before driving.
- **F4 Oil level changes by slope:** move to level ground and repeat.

## Verification

The oil level is confirmed within the marked acceptable range or a clear low/overfull/contaminated condition has been identified for correction.

## Variations

- `electronic-level`: use the dashboard or infotainment oil-level menu with the vehicle parked as instructed.
- `diesel`: oil may look dark soon after a change; level and contamination signs matter more than color alone.
- `dry-sump-performance-car`: follow the exact warm-engine procedure in the manual.

## Safety & privacy

Low risk, but hot engine parts can burn skin and incorrect oil level can damage the engine. Keep hands, hair, and clothing away from moving belts and fans.
