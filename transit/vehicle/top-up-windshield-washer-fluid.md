---
name: top-up-windshield-washer-fluid
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You refill the windshield washer fluid reservoir with the correct fluid so the washers spray reliably.

## Preconditions

- Windshield washer fluid appropriate for the climate.
- The vehicle is parked, engine off, and hood safely opened.
- You can identify the washer reservoir cap.

## Steps

1. **Choose the correct fluid.** Use washer fluid rated for freezing temperatures if winter conditions are possible; do not use plain water in freezing weather. → *Expect:* the fluid label suits your climate.
2. **Open and secure the hood.** Engage the hood prop if needed. → *Expect:* the engine bay is stable and accessible.
3. **Find the washer reservoir.** Look for a cap with a windshield spray symbol, usually blue or black. → *Expect:* you identify the washer-fill opening, not coolant or brake fluid.
4. **Open the cap.** Flip or unscrew it carefully. → *Expect:* the filler neck is open.
5. **Pour fluid slowly.** Use a funnel if the opening is small and stop before overflowing. → *Expect:* the reservoir is full or near full.
6. **Close the cap firmly.** Wipe spills if needed. → *Expect:* the cap is sealed and fluid is not pooled on components.
7. **Test the washers.** Turn the ignition to accessory or start the car and spray briefly. → *Expect:* fluid sprays onto the windshield and wipers clear it.

## Decision points

- Fluid does not spray after refill → check for frozen lines, clogged nozzles, empty rear reservoir, or a pump issue.
- Wrong reservoir opened → close it without adding anything and confirm symbols in the manual.
- Winter is approaching → use low-temperature washer fluid before the first freeze.

## Failure modes & recovery

- **F1 Added washer fluid to wrong reservoir:** stop driving if it entered coolant, brake, or oil systems; seek service before operating.
- **F2 Nozzles clogged:** clean gently with washer-nozzle tool or seek service; do not force pins deep into nozzles.
- **F3 Fluid freezes:** move vehicle to warmth and refill with winter-rated fluid after thawing.
- **F4 Reservoir leaks:** look for fluid puddles after filling and schedule repair.

## Verification

The washer reservoir is filled with appropriate fluid, the cap is closed, and washer spray reaches the windshield.

## Variations

- `rear-wiper-vehicles`: the rear washer may share the front reservoir or have a separate reservoir.
- `concentrate`: dilute only according to the product label and climate rating.
- `ev-frunk`: washer fill may be under a front trunk panel; follow the manual.

## Safety & privacy

Low risk, but washer fluid can be poisonous and flammable depending on formula. Keep it away from children, avoid eye contact, and never pour it into brake, oil, or coolant reservoirs.
