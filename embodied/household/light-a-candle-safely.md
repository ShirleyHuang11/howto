---
name: light-a-candle-safely
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [candle, candle-holder, lighter, match, snuffer]
affordances: [grasp, place, strike, button-press, ignite, extinguish]
workspace: household
safety: {hot_surfaces: true, sharp_objects: false, fragile: [glass-holder], human_proximity: pause}
---

## Goal

A candle is lit in a stable, clear location and later extinguished without fire, wax, or burn hazards.

## Preconditions

- The candle is in a heat-safe holder or jar that is not cracked.
- The wick is visible and trimmed to about 6 mm if needed.
- The surface is flat, heat-resistant, and away from drafts.
- A lighter, match, or igniter and an extinguisher method are available.

## Steps

1. **Choose the location.** Set the candle on a stable surface away from curtains, paper, bedding, shelves, and edges. → *Expect:* there is at least 30 cm of clear space around and above the flame path.
2. **Check the holder and wax.** Confirm the candle stands upright and the holder will catch melted wax. → *Expect:* nothing wobbles, leans, or exposes bare flame to a fragile surface.
3. **Clear nearby movement.** Move sleeves, hair, pets, and children away before ignition. → *Expect:* no person or object crosses over the wick.
4. **Light the wick.** [BRANCH: lighter | match] hold flame to the wick base until it catches, then pull the flame source away. → *Expect:* the wick has a small steady flame.
5. **Adjust only from the holder.** If the candle needs repositioning, lift the holder, not the hot wax or flame area. ⚠️ *Irreversible:* an unattended flame can start a fire, so never leave the room while it is burning. → *Expect:* the candle remains upright and watched.
6. **Watch the first minute.** Look for high flame, smoking, tunneling, or nearby draft flicker. → *Expect:* the flame stays steady and contained.
7. **Burn within limits.** Follow label timing and stop before the candle burns near the bottom of the jar or holder. → *Expect:* wax pool remains controlled and the holder is not overheating.
8. **Extinguish deliberately.** Use a snuffer, wick dipper, or gentle breath from the side, then wait until smoke clears before moving it. → *Expect:* no glowing ember remains and the holder cools in place.

## Decision points

- Holder is cracked, plastic, or unstable → do not light the candle.
- Draft makes the flame lean or flutter hard → move the candle before lighting or extinguish it.
- Flame grows tall, smokes, or touches container soot → extinguish, cool, trim wick, and relight only if safe.
- You need to leave, sleep, shower, or focus elsewhere → extinguish first.

## Failure modes & recovery

- **F1 Wick will not catch:** detect flame going out immediately → trim charred wick, expose a little wax edge, and try once more.
- **F2 Wax spill:** detect liquid wax on a surface → let it cool before scraping, then clean residue.
- **F3 Smoke after blowing out:** detect lingering smoke or ember glow → snuff again or dip the wick into wax and lift it back.
- **F4 Nearby item warms:** detect heat on shelf, wall, or object above → extinguish and move the candle to open space.

## Verification

While lit, the candle has a steady flame in a stable holder with clear surroundings; when finished, the wick is fully out and no ember glows.

## Variations

- `jar-candle`: keep the wax pool free of matches and stop use when wax is low.
- `taper-candle`: use a snug holder that keeps the candle vertical.
- `power-outage`: use a flashlight first, and place candles where they cannot be knocked over.

## Safety & privacy

Medium risk from open flame, hot wax, hot glass, and smoke. Keep candles away from sleeping areas, oxygen tanks, aerosols, and anything loose or flammable. Never leave a burning candle unattended.
