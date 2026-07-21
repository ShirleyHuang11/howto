---
name: make-a-salad
domain: daily
subdomain: food
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

A salad that people actually want to eat: washed and dried greens, balanced components, and a dressing applied at the right moment so nothing arrives wilted or swimming.

## Preconditions

- A base green (lettuce, spinach, arugula, cabbage), at least one crunchy element, and ideally a protein if it is a meal rather than a side.
- Oil, an acid (vinegar or citrus), salt, and pepper cover the dressing even with nothing else in the house.
- A large bowl (bigger than seems polite; tossing needs headroom), and a salad spinner or clean towel for drying.

## Steps

1. **Wash the greens properly.** Separate leaves, submerge in a bowl of cold water, agitate, lift the greens out (grit sinks; pouring the bowl back over them re-grits everything). Repeat for sandy greens like spinach. → *Expect:* no grit at the bowl's bottom on the final pass.
2. **Dry the greens completely.** Spinner, or rolled loosely in a clean towel and patted. This is the least glamorous and most important step: dressing slides off wet leaves and pools at the bottom. → *Expect:* leaves dry to the touch.
3. **Tear or cut into fork-sized pieces.** Bite-sized beats knife-and-fork wrestling at the table. → *Expect:* pieces that fit on a fork without folding engineering.
4. **Build the body.** Crunch (cucumber, peppers, carrots, radish), something sweet or juicy (tomato, apple, orange segments), something rich (cheese, avocado, nuts, seeds), and the protein for meal salads (eggs, beans, chicken, tuna). Aim for three to five components beyond the greens; more becomes compost-drawer roulette. → *Expect:* a bowl with contrast in texture, color, and richness.
5. **Make the dressing in the ratio 3:1 oil to acid.** Three spoons oil, one spoon vinegar or lemon, salt, pepper, and optionally a dab of mustard or honey to bind. Shake in a jar or whisk in the bowl's bottom before the greens go in. → *Expect:* a dressing that tastes slightly too sharp alone; it mellows across the leaves.
6. **Dress at the last minute, less than you think, and toss thoroughly.** Half the dressing, toss with hands or two spoons from the bottom up, taste a leaf, add more only if needed. ⚠️ *Irreversible in effect:* overdressing cannot be undone; underdressing takes ten seconds to fix. → *Expect:* every leaf lightly coated, nothing pooling below.
7. **Finish and serve immediately.** Delicate toppings (croutons, seeds, cheese shavings) go on after the toss so they stay crisp and visible. → *Expect:* salad on the table within minutes of dressing.

## Decision points

- Meal-prep salads: dressing at the bottom of the jar, sturdy items next, greens on top, shaken at eating time. Layering is the anti-wilt architecture (`daily/food/pack-a-lunch`'s wet-dry separation applied vertically).
- Sturdy vs delicate greens: cabbage and kale tolerate (and improve with) early dressing and a massage; butter lettuce dies in minutes. Match the dressing moment to the leaf.
- No spinner, guests arriving: towel-dry earlier in the day and refrigerate the leaves rolled in the towel; they crisp up as they chill.

## Failure modes & recovery

- **F1 Wilted, soggy salad:** dressed too early or on wet leaves. For the current bowl, add fresh undressed greens and toss to redistribute; for the future, steps 2 and 6 are the whole religion.
- **F2 Dressing pooled at the bottom, leaves bland:** wet leaves again, or too-timid tossing. Toss properly from the bottom; hands are the best tool.
- **F3 Gritty bite:** the lift-don't-pour rule in step 1 was skipped. Nothing rescues served grit; re-wash what remains.
- **F4 Overdressed and heavy:** more undressed greens and body ingredients dilute it back to acceptable; there is no other direction.

## Verification

Leaves are dry-crisp with no grit, the components cover crunch, sweetness, and richness, every leaf carries a light coat with no pool at the bottom, and delicate toppings arrived crisp on top at serving time.

## Variations

- Grain bowls swap half the greens for cooked grains (`daily/food/cook-rice` leftovers reborn) and tolerate advance dressing far better.
- Regional axes: 3:1 vinaigrette is the French baseline; creamy dressings suit sturdy greens; sesame-soy variants pair with cabbage and carrot bases.

## Safety & privacy

Low risk: knife discipline from `daily/food/cut-an-onion` for the components, and honest produce washing. The only casualty risk in salad is the will to eat it, which steps 2 and 6 protect.
