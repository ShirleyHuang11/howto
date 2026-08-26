---
name: add-air-to-a-tire
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: [transit/vehicle/check-your-tire-pressure]
status: draft
last_verified: 2026-08-25
---

## Goal

You inflate a tire to the vehicle manufacturer's recommended cold PSI without overinflating it.

## Preconditions

- You know the target PSI from the vehicle placard or owner's manual.
- You have a tire gauge and access to an air compressor.
- The tire is not shredded, off the rim, or unsafe to inflate.

## Steps

1. **Park safely near the air hose.** Set the parking brake and keep clear of traffic. → *Expect:* the hose reaches the tire without stretching across a moving lane.
2. **Check the current pressure.** Use a gauge before adding air. → *Expect:* you know how many PSI the tire needs.
3. **Set the compressor if it has a preset.** Enter the target PSI from the vehicle placard. → *Expect:* the machine is ready to stop at the target pressure.
4. **Remove the valve cap.** Keep it in your pocket or another safe place. → *Expect:* the valve stem is exposed.
5. **Attach the air chuck squarely.** Press it straight onto the valve or lock the lever if present. → *Expect:* air flows into the tire with little or no leakage.
6. **Inflate in short bursts if there is no preset.** Add air for a few seconds, then recheck with your gauge. → *Expect:* the pressure rises toward the target.
7. **Release extra air if needed.** Press the small valve pin briefly, then recheck. → *Expect:* the pressure is at the recommended PSI within about 1 PSI.
8. **Replace the valve cap and repeat.** Check the other tires while the compressor is available. → *Expect:* all adjusted tires are capped and at target pressure.

## Decision points

- Tire will not hold air → do not keep driving normally; install the spare or seek tire repair.
- Tire is hot from highway driving → inflate to a safe near-target pressure now, then recheck cold later.
- Compressor gauge disagrees with your gauge → trust a known-good handheld gauge over a worn public compressor gauge.

## Failure modes & recovery

- **F1 Air leaks loudly at the chuck:** remove and reseat the chuck straight on the valve.
- **F2 Valve stem leaks after inflation:** tighten or replace the valve core, or have a tire shop inspect it.
- **F3 Compressor times out:** restart it and continue in small increments.
- **F4 Overinflated tire:** bleed air slowly through the valve pin and recheck.

## Verification

The tire reads the manufacturer's recommended PSI on a reliable gauge, the valve cap is back on, and the tire does not visibly sag or leak.

## Variations

- `gas-station-preset`: the compressor may beep or stop automatically when the set PSI is reached.
- `portable-compressor`: connect to the battery or 12V outlet as instructed and avoid draining the vehicle battery.
- Nitrogen-filled tires: ordinary compressed air is safe to add when needed.

## Safety & privacy

Low risk if the tire is intact. Do not inflate a severely damaged tire, stand out of traffic, and do not exceed the vehicle placard or tire sidewall maximum.
