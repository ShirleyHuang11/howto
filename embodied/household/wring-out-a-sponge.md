---
name: wring-out-a-sponge
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [sponge, water, sink, faucet, hand]
affordances: [grasp, squeeze, twist, release, inspect]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

Excess water is removed from the sponge over the sink until it no longer drips under normal handling.

## Preconditions

- Sponge is safe to touch and does not contain harsh chemical residue.
- Sink basin is available below the sponge.
- Hands can grip the sponge without dropping it.

## Steps

1. **Move over the sink.** Hold the sponge fully above the basin, not over the counter or floor. → *Expect:* any water falls into the sink.
2. **Set the grip.** Wrap fingers around the sponge with thumbs opposed. → *Expect:* sponge is enclosed but not yet compressed.
3. **Squeeze evenly.** Press both hands inward until water streams out. → *Expect:* flow exits downward into the basin.
4. **Release slightly.** Let the sponge expand while keeping it over the sink. → *Expect:* sponge rebounds and draws in air.
5. **Repeat compression.** Squeeze again with firmer pressure. → *Expect:* water output drops from stream to drips.
6. **Add twist if needed.** [BRANCH: soft sponge | stiff sponge] twist opposite ends gently only if it will not tear. → *Expect:* remaining water expresses from the center.
7. **Check drip rate.** Hold the sponge still for two seconds. → *Expect:* no steady drip forms.
8. **Place or reuse.** Set the sponge on its holder or return it to cleaning. → *Expect:* no puddle forms under it.

## Decision points

- Sponge contains cleaner → rinse before final wringing if residue matters.
- Sponge crumbles or tears → stop twisting and replace it.
- Water is hot → wait or cool under the faucet before gripping firmly.

## Failure modes & recovery

- **F1 Counter drip:** sponge leaves water outside the sink → move fully over basin and wipe the spill.
- **F2 Weak squeeze:** sponge still drips steadily → increase hand coverage and repeat.
- **F3 Tear from twist:** material splits at the edge → stop twisting and use straight squeezes.
- **F4 Chemical exposure:** hands feel slippery or irritated → rinse hands and sponge thoroughly.

## Verification

The sponge can be held over the counter for two seconds without releasing a steady drip.

## Variations

- Large sponge: fold it once before squeezing to increase compression.
- Delicate cellulose sponge: avoid twisting and use repeated flat presses.

## Safety & privacy

Low risk. Avoid wringing unknown cleaners onto skin, food-prep surfaces, or electronic devices.
