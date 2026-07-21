---
name: bleed-a-radiator
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

Trapped air is released from a hot-water radiator so it heats evenly top to bottom, and the boiler system pressure is restored to its normal cold reading afterwards.

## Preconditions

- A radiator that is cold or lukewarm at the top while hot at the bottom (the signature of trapped air), or that gurgles.
- A radiator bleed key (square-socket key; a flat screwdriver fits some modern valves).
- A cloth and a shallow cup or jar to catch water.
- Access to the boiler's pressure gauge and filling loop if the system is sealed (most modern combi systems).

## Steps

1. **Turn the heating off and let the system go cold.** Wait at least 30-60 min after shutoff. Bleeding a hot system sprays scalding water and the running pump drags air around the circuit so it never collects at the valve. → *Expect:* radiators cool to the touch, pump silent.
2. **Note the boiler's cold pressure before starting.** Read the gauge. Typical sealed-system cold pressure is 1.0-1.5 bar. → *Expect:* a baseline reading written down or remembered.
3. **Find the bleed valve.** It is at one top corner of the radiator: a small square-socket screw inside a round nut, sometimes under a plastic cap. → *Expect:* the key seats snugly on the square socket.
4. **Open the valve a quarter to half turn counterclockwise.** Hold the cloth under the valve and the cup below that. Do not open more than one full turn; the screw can come all the way out and is miserable to reseat against escaping water. → *Expect:* a steady hiss of escaping air.
5. **Wait through the hiss.** The hiss may run from a few seconds to a minute on a badly aired radiator. → *Expect:* hiss weakens, then water starts to sputter.
6. **Close the valve when water runs in a steady dribble.** Sputtering means air is still mixed in; a solid dribble means the air is out. Turn clockwise until snug, not forced. → *Expect:* water flow stops completely; valve body dry after a wipe.
7. **Repeat for other cold-topped radiators.** [BRANCH: one problem radiator → done after it | whole-system bleed → work from the lowest floor outward from the boiler, ending with the highest and farthest radiator, where air collects most] → *Expect:* every bled radiator ends on a steady dribble, valve closed.
8. **Check and restore boiler pressure.** Bleeding removes water volume; the gauge will read lower than your baseline. On a sealed system, open the filling loop valves slowly until the gauge reaches 1.0-1.5 bar cold, then close both loop valves fully. → *Expect:* gauge steady in the green zone; filling loop closed and not hissing.
9. **Run the heating and re-check.** Turn heating on, wait 20-30 min, feel each bled radiator top and bottom. → *Expect:* radiators hot across their full height, no gurgling, no drips at any bleed valve.

## Decision points

- No pressure gauge anywhere (open-vented system with a loft tank) → skip step 8; the tank tops the system up by itself, but check the loft tank's ballcock is actually feeding.
- Radiator cold at the bottom but hot at the top → that is sludge, not air; bleeding will not fix it, the circuit needs flushing.
- Every radiator needs bleeding every few weeks → air is entering the system (leak or failing component); book a service rather than treating the symptom.

## Failure modes & recovery

- **F1 No hiss and no water at the open valve:** system pressure is at or near zero → close the valve, repressurize at the filling loop first, then bleed.
- **F2 Bleed screw seized:** do not force the small key until it rounds the socket → grip the valve nut with pliers while turning the screw with the key, or apply penetrating oil and wait 10 min.
- **F3 Valve drips after closing:** re-snug a quarter turn → still weeping means a worn valve seat; wind PTFE tape on the screw threads or replace the bleed screw (cheap, standard sizes).
- **F4 Screw came fully out under water flow:** stay calm, the flow is a dribble on a cold depressurized system → push the screw back into the hole and thread it in; keep the cloth over it while starting the thread.
- **F5 Pressure keeps falling over days after a correct top-up:** the system has a leak or a failing expansion vessel → this is a service call, not a bleeding problem.

## Verification

With the heating running for 30 min, every treated radiator is hot over its entire surface, no bleed valve shows moisture, and the boiler gauge reads within its normal band (typically 1.0-1.5 bar cold, up to about 2 bar hot).

## Variations

- Towel-rail radiators: bleed valve is often on the top rail end; same procedure, they trap air constantly by design.
- Modern self-bleeding valves (auto air vents) fitted on some radiators: no manual bleed needed unless the vent itself has clogged.
- Underfloor heating manifolds: different procedure entirely; do not apply this recipe.

## Safety & privacy

Medium risk: radiator water in a recently run system can scald, and it is dirty enough to stain carpets permanently (hence the cloth and cup). Never bleed with the pump running, never open the valve more than a turn, and never leave the filling loop open unattended; overpressurizing lifts the relief valve and dumps water outside.
