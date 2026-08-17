---
name: read-a-recipe-before-cooking
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

A recipe is reviewed before cooking so timing, equipment, ingredients, risks, and decision points are known.

## Preconditions

- Recipe text, kitchen workspace, available ingredients, equipment, and enough time to read without cooking pressure.
- Any dietary restrictions or allergies are known before selecting substitutions.

## Steps

1. **Read the title and yield.** Check what the recipe makes and how many servings. → *Expect:* quantity matches the meal need or needs scaling.
2. **Scan total time.** Separate active time from resting, chilling, rising, marinating, or baking time. → *Expect:* hidden waiting steps are visible before starting.
3. **Read ingredients fully.** Note exact forms such as melted butter, cooked rice, divided sugar, or room-temperature eggs. → *Expect:* prep requirements are marked.
4. **Read all steps once.** Look for branches, timing overlaps, and points where heat or speed matters. → *Expect:* no step is surprising during cooking.
5. **Check equipment.** Identify pans, bowl sizes, thermometer, blender, mixer, parchment, or storage containers. → *Expect:* required tools are present or substitutes are chosen.
6. **Plan food safety.** Note raw meat temperatures, cooling steps, fermentation rules, or hot-oil precautions. → *Expect:* safety-critical steps are flagged before ingredients are handled.
7. **Prepare mise en place.** Measure, chop, preheat, and group ingredients by when they are used. [BRANCH: simple recipe | fast recipe] → *Expect:* fast steps have ingredients ready within reach.
8. **Commit or change plan.** Start only if time, ingredients, and equipment fit. ⚠️ *Irreversible:* do not begin irreversible heating, frying, fermenting, or mixing until substitutions are decided. → *Expect:* recipe is ready to execute without avoidable stops.

## Decision points

- Missing a key ingredient → choose a tested substitution or pick another recipe.
- Time does not fit → choose a shorter recipe before opening perishable ingredients.
- Recipe source is vague on safety → verify internal temperatures or fermentation ratios from a reliable source.

## Failure modes & recovery

- **F1 Ingredient surprise:** detect a step calling for an unprepared form → pause, prep it, and adjust timing.
- **F2 Equipment mismatch:** detect pan or appliance missing mid-recipe → switch to an equivalent size or stop before wasting ingredients.
- **F3 Timing collision:** detect two urgent steps at once → lower heat, pause where safe, and set timers.
- **F4 Unsafe assumption:** detect unclear meat doneness, oil temperature, or fermentation salt level → use thermometer, stop frying, or use a validated ratio.

## Verification

Before cooking starts, ingredients, equipment, timing, substitutions, allergens, and safety-critical steps are identified and feasible.

## Variations

- `baking`: check ingredient temperatures, pan size, and whether measurements are by weight.
- `stir-fry`: prep every ingredient before heat starts because cooking is too fast to pause.
- `fermentation`: verify salt percentage, clean vessel, temperature range, and discard criteria.

## Safety & privacy

Low risk, but this step prevents higher-risk mistakes. Protect dietary and medical information, identify allergens, and confirm safety notes before opening raw meat, heating oil, or starting fermentation.
