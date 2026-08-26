---
name: use-a-self-service-car-wash
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You wash a vehicle in a self-service bay without damaging paint, trim, electronics, or nearby people.

## Preconditions

- The vehicle fits inside the wash bay and has closed windows, sunroof, doors, and trunk.
- You have payment accepted by the wash equipment.
- The paint is cool enough to touch; washing hot paint in direct sun can leave spots.

## Steps

1. **Park centered in the bay.** Leave room to walk around the vehicle and keep the wand hose from dragging hard across paint. → *Expect:* the vehicle is stationary, closed, and reachable on all sides.
2. **Read the selector options.** Identify pre-soak, soap, rinse, wax, spot-free rinse, and any brush setting. → *Expect:* you know the sequence before the timer starts.
3. **Pre-rinse from top down.** Hold the pressure wand a safe distance from paint, sensors, decals, and seals. → *Expect:* loose dirt is removed without forcing water into gaps.
4. **Apply soap or pre-soak.** Cover the vehicle top to bottom, spending extra time on lower panels and wheels. → *Expect:* grime is softened and the surface is evenly wet.
5. **Use the brush cautiously.** [BRANCH: brush looks clean and soft, rinse it first and use light pressure | brush is gritty or damaged, skip it and use wand only] → *Expect:* no visible grit is being rubbed into paint.
6. **Rinse thoroughly.** Work top down until no soap remains in mirrors, trim, wheels, and panel gaps. → *Expect:* runoff is clear and no suds remain.
7. **Apply final rinse or wax if desired.** Use spot-free rinse last and do not rinse it off with regular water afterward. → *Expect:* the finish is evenly rinsed and ready to dry.
8. **Move to a drying area.** Dry glass and mirrors with clean towels if available, then leave the bay promptly for the next user. → *Expect:* the bay is clear and the vehicle is not dripping heavily.

## Decision points

- Vehicle has loose trim, damaged seals, temporary repairs, or roof cargo → avoid high pressure near those areas.
- Fresh paint, vinyl wrap, or ceramic coating → follow the installer's cure and wash instructions before using pressure or brushes.
- Heavy mud → rinse the bay floor and vehicle underside if allowed, but do not leave piles of debris for the next user.

## Failure modes & recovery

- **F1 Timer runs out mid-wash:** detect water stopping before rinse is complete → add time immediately and prioritize rinsing soap off glass and paint.
- **F2 Wand too close:** detect lifting decal edges, water intrusion, or paint chips → back off pressure and inspect damage after drying.
- **F3 Brush scratches:** detect visible grit or new marks → stop using the brush and rinse thoroughly; polish minor clear-coat marks later if appropriate.
- **F4 Payment accepted but equipment fails:** detect no spray or selector response → note bay number and request refund from the attendant or posted contact.

## Verification

The vehicle is rinsed free of soap, windows and mirrors are clear, no water is actively entering the cabin, and the wash bay is vacated cleanly.

## Variations

- Touchless bay: remain inside or follow posted instructions; secure antennae, wipers, and mirrors as directed.
- Winter road salt: prioritize underbody and wheel-well rinse when temperatures allow doors and locks to dry before freezing.
- Soft-top convertible: avoid high pressure on seams and windows.

## Safety & privacy

Low risk, with hazards from slippery floors and high-pressure spray. Do not point the wand at people, pets, skin, sensors at close range, or open electrical accessories.
