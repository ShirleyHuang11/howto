---
name: clean-a-coffee-maker
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Clean and descale a drip coffee maker so water flows normally and brewed coffee no longer tastes stale or sour.

## Preconditions

- The coffee maker is unplugged or off before handling removable parts.
- White vinegar, water, dish soap, a sponge, and a clean towel are available.
- The machine has no paper filter, grounds, or coffee left in it.

## Steps

1. **Empty removable parts.** Remove old grounds, paper filters, and leftover coffee from the basket and carafe. → *Expect:* no loose grounds or stale coffee remain.
2. **Wash the basket and carafe.** Clean them with warm soapy water, rinse well, and set them back in place. → *Expect:* oily residue and coffee film are gone.
3. **Mix descaling solution.** Fill the reservoir with equal parts white vinegar and water unless the manual says otherwise. → *Expect:* the reservoir is filled below its max line.
4. **Run half a brew cycle.** Start brewing until about half the solution has moved into the carafe, then stop the machine. → *Expect:* hot vinegar-water is in the carafe and the reservoir is partly full.
5. **Let it soak.** Wait 20 minutes so scale loosens inside the heater and lines. → *Expect:* the machine sits idle with solution in the system.
6. **Finish the brew cycle.** Turn the machine back on and let the rest of the solution run through. → *Expect:* the reservoir is empty and the carafe contains used solution.
7. **Discard and rinse.** Pour the hot solution down the sink and rinse the carafe. → *Expect:* no vinegar-water remains in the carafe.
8. **Run first rinse cycle.** Fill the reservoir with plain water and brew a full cycle. → *Expect:* the water smells less like vinegar.
9. **Run second rinse cycle.** Repeat with another full reservoir of plain water. → *Expect:* the brewed water smells neutral.
10. **Dry and reassemble.** Wipe the exterior, leave the lid open briefly, and return clean parts. → *Expect:* the machine is clean, dry at the edges, and ready to brew.

## Decision points

- Manual forbids vinegar → use the manufacturer descaler and follow its dilution.
- Water flow is still slow → repeat the descaling cycle once after the machine cools.
- Coffee maker is used daily with hard water → descale monthly; otherwise descale every 2 to 3 months.

## Failure modes & recovery

- **F1 Vinegar taste remains:** detect sharp vinegar smell in rinse water, recover by running another plain-water cycle.
- **F2 Overflowing basket:** detect water backing up into grounds area, recover by cleaning the basket valve and carafe lid alignment.
- **F3 Weak flow:** detect slow dripping after descaling, recover by repeating descaling or checking the manual for clogged-line service.
- **F4 Cracked carafe:** detect leaks or sharp edges, recover by replacing it before brewing again.

## Verification

A full plain-water brew cycle runs through at normal speed and the output has no vinegar smell.

## Variations

- `single-serve`: run vinegar-water through the largest cup setting, then run at least two water-only tanks.
- `thermal-carafe`: wash the inside with dish soap and a bottle brush because stains hide on the steel walls.

## Safety & privacy

Low risk from hot liquid and mild acid. Do not mix vinegar with bleach or other cleaners, and let hot parts cool before washing by hand.
