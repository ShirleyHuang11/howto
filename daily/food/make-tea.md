---
name: make-tea
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: [daily/food/boil-water]
status: draft
last_verified: 2026-07-20
---

## Goal

A cup or pot of properly steeped tea, at drinking temperature, matched to the tea type.

## Preconditions

- Tea (bag or loose leaf) and a cup/pot; an infuser or strainer for loose leaf.
- Hot water capability (`daily/food/boil-water`).

## Steps

1. **Match water temperature to the tea.** Black/herbal: fully boiling. Oolong: ~90 °C. Green/white: 70–80 °C (boil, then wait 2–3 min or add a splash of cool water). → *Expect:* water at the right band — boiling water on green tea is the classic bitterness mistake.
2. **Warm the cup/pot (optional but real).** Swirl a little hot water in and dump it. → *Expect:* vessel warm to the touch; the tea won't crash in temperature on contact.
3. **Dose the tea.** One bag or ~1 tsp loose leaf per cup (~250 ml); leaves in the infuser with room to expand. → *Expect:* infuser at most half-full of dry leaf.
4. **Pour the water over the tea and start a timer.** Black: 3–5 min. Green: 1–3 min. Herbal: 5+. → *Expect:* leaves unfurling/bag steeping, color developing; a timer actually running.
5. **Remove the tea at time.** Pull the bag without wringing it (wringing squeezes bitter tannins); lift the infuser and let it drip a moment. → *Expect:* liquor at the expected color; leaves out of the water.
6. **Adjust and serve.** Milk/sugar/lemon per taste (milk pairs with black; lemon curdles milk — pick one). ⚠️ *Irreversible:* it's near-boiling liquid — carry cup-half-full if walking, and test a sip's temperature at the lip first. → *Expect:* drinkable within a few minutes; no scalded tongue.

## Decision points

- Re-steeping loose oolong/green: quality leaf takes 2–3 infusions — keep the leaves, extend later steeps slightly.
- Making iced tea → double the leaf dose, steep normally, pour over a full glass of ice.
- No timer instinct ("I'll just wait a bit") → the recipe fails here more than anywhere; use a real timer.

## Failure modes & recovery

- **F1 Bitter/astringent:** water too hot or steeped too long — for this cup, dilute with hot water and a little milk/sugar; next cup, fix temperature and time.
- **F2 Weak/watery:** underdosed or pulled early — steep a fresh bag briefly in the same cup; adjust dose next time (not endless steeping, which adds bitterness before strength).
- **F3 Leaf fragments in the cup:** finer strainer, or rinse-and-reseat the infuser; bagged tea sidesteps it.

## Verification

The tea's color and strength match its type, it tastes intended (not accidentally bitter), and the steeping tea/bag has been removed rather than left in.

## Variations

- `uk` builder's tea: strong black, bag in mug, boiling water, milk after removing the bag.
- `cn` gongfu style: small pot, high leaf ratio, many very short steeps — a distinct recipe worth its own file.
- `jp` sencha: 70 °C and ~1 min; kyusu pot with built-in strainer.

## Safety & privacy

Medium risk only from the near-boiling water — the pour and the first sip are the scald moments (steps 4, 6).
