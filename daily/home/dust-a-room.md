---
name: dust-a-room
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

A room dusted top-to-bottom in the order that means dust is removed once, not relocated twice, including the surfaces everyone skips.

## Preconditions

- A microfiber cloth or two (dry or barely damp; they trap dust electrostatically, unlike feather dusters which mostly fluff it airborne), and an extendable duster or the cloth on a broom head for high work.
- The vacuum on standby for the floor finish (`daily/home/vacuum-a-room` is the natural next act).
- Allergy-prone dusters: a mask turns this from a sneeze festival into a chore.

## Steps

1. **Top of the room first, always.** Ceiling corners and cobwebs, light fixtures (switched off, and cool if they were on), the tops of tall furniture, curtain rails, and the ceiling fan (an old pillowcase slipped over each blade wipes and *catches* instead of raining). → *Expect:* the high layer done; whatever fell is now the lower surfaces' problem, which is exactly why order matters.
2. **Work down through the mid-layer.** Shelves, picture frames (`daily/home/hang-a-picture`'s survivors, held steady with the free hand), window sills, the TV and its stand (dry microfiber only on screens, no sprays), lamps and shades. Lift objects, wipe under them, replace; wiping around things is the signature of fake dusting. → *Expect:* each surface cleared under its objects, not just in front of them.
3. **Hit the invisible standards.** Skirting boards, door tops and frames, radiator tops and fins (a damp cloth over a ruler slides between fins), light switches and door handles (the touched-surfaces get a damp pass), and vents. → *Expect:* the zones that make a "clean" room smell dusty are actually clean.
4. **Refold or swap the cloth as it loads.** A saturated cloth deposits; fold to a fresh face every few surfaces, and switch cloths when no faces remain. → *Expect:* always wiping with a face that looks cleaner than the surface.
5. **Electronics get the gentle version.** Screens: dry microfiber, light pressure. Keyboards and vents: a soft brush or air blower rather than a wet cloth. Cables and power strips behind furniture: unplug nothing, but the dust bunnies there are fuel for step 6. → *Expect:* electronics dust-free with zero moisture near them.
6. **Finish with the floor.** Everything that fell now gets vacuumed or swept (`daily/home/vacuum-a-room` or `daily/home/sweep-and-mop-a-floor`), including under the furniture edges you dusted above. → *Expect:* the room's dust actually in a bin or bag, not resettled by morning.

## Decision points

- Cadence: weekly for the mid-layer in lived-in rooms, monthly for the high layer, seasonally for the radiator-and-vent deep pass; pet households compress every interval.
- Damp or dry: dry microfiber for most surfaces and all electronics; barely damp for the touched surfaces and sticky kitchens; never wet on raw wood or inside anything powered.
- Products honestly: polish sprays are optional and mostly cosmetic; the cloth does the work, and spray-on-cloth (never on the surface, where it streaks and drips into electronics) is the rule when you do use them.

## Failure modes & recovery

- **F1 Room dusty again in two days:** the floor finish (step 6) was skipped, so the fallen layer recirculated; or a source runs unfiltered (fan, open window over a street, a filterless vacuum). Fix the source, not the schedule.
- **F2 Streaks on glossy furniture:** an overloaded or overly wet cloth; buff with a dry face, and respect step 4.
- **F3 Knocked something off a shelf:** the lift-wipe-replace rhythm with the free hand steadying neighbors is the prevention; the recovery is `daily/home/sort-recycling`'s wrapped-glass rule and honesty with the owner (`embodied/household/tidy-a-room` F3's spirit).
- **F4 Sneezing fits mid-task:** mask on, windows open, damp cloth instead of dry (traps more, launches less), and the fan-and-pillowcase trick for the worst offenders.

## Verification

High, mid, and invisible layers all wiped under-not-around, screens dry-wiped, cloth faces retired as they loaded, and the floor vacuumed last so the room passes the sunbeam test: light through the window showing air, not a snow globe.

## Variations

- Bedrooms add the headboard and under-bed (dust's favorite habitat); `daily/home/make-a-bed` daily plus this weekly keeps the sleep zone honest.
- Minimalist speed-run: top layer monthly, touched surfaces and sightline shelves weekly in five minutes; the order rule survives any compression.

## Safety & privacy

Low risk: cool bulbs before wiping, both feet on the stool for high work (`daily/home/change-a-lightbulb`'s ladder sanity), and moisture nowhere near powered things. Dust is the easiest opponent in the house; order is the entire strategy.
