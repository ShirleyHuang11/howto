---
name: make-salsa
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Fresh or cooked salsa is chopped or blended, balanced with acid, heat, and salt, rested, and ready to serve.

## Preconditions

- Tomatoes or tomatillos, onion, chile, cilantro if desired, lime or vinegar, and salt.
- Knife and board, or blender or food processor.
- Clean jar or bowl for resting.

## Steps

1. **Choose fresh or cooked.** [BRANCH: fresh: raw tomatoes and lime | cooked: roasted or simmered tomatoes or tomatillos] → *Expect:* style matches the flavor and storage time wanted.
2. **Prep ingredients.** Core tomatoes, peel onion, stem chiles, and wash herbs. → *Expect:* tough stems and bruised spots are removed.
3. **Control chile heat.** Remove seeds and ribs for milder salsa, or keep them for more heat. → *Expect:* chile quantity is intentional, not accidental.
4. **Dice or blitz.** Dice by hand for chunky salsa, or pulse in short bursts for smoother salsa. → *Expect:* texture is even and not watery puree unless desired.
5. **Balance acid.** Add lime juice or vinegar a teaspoon at a time. → *Expect:* tomato sweetness tastes brighter.
6. **Salt correctly.** Add salt, stir, wait 2 minutes, then taste again. → *Expect:* flavors become distinct and less flat.
7. **Rest the salsa.** Let sit 10-20 minutes so onion mellows and juices mingle. → *Expect:* salsa tastes more integrated than when first mixed.
8. **Adjust before serving.** [BRANCH: too sharp: add tomato | too hot: add tomato or avocado | dull: add salt and lime] → *Expect:* acid, heat, and salt are in balance.
9. **Store cold.** Refrigerate leftovers in a covered container. → *Expect:* salsa is chilled within 2 hours.

## Decision points

- Tomatoes are watery → seed them or drain chopped tomatoes before mixing.
- Onion is harsh → rinse chopped onion under cold water and drain.
- Want smoky flavor → char tomatoes, tomatillos, onion, and chiles before blending.

## Failure modes & recovery

- **F1 Salsa too watery:** detect by liquid pooling → drain through a sieve or add diced tomato, onion, or avocado.
- **F2 Too much heat:** detect by burning aftertaste → dilute with more tomato and acid; dairy on the side helps eaters.
- **F3 Bitter cooked salsa:** detect by acrid char → peel off blackened patches and add lime plus salt.
- **F4 Flat flavor:** detect by tomato water taste → add salt first, then acid, then a small pinch of sugar only if needed.

## Verification

Salsa has an even texture, tastes balanced for acid, heat, and salt, and has rested at least 10 minutes before serving.

## Variations

- `pico-de-gallo`: dice tomato, onion, chile, cilantro, lime, and salt; serve same day.
- `salsa-verde`: roast tomatillos and green chiles, then blend with onion and cilantro.
- `restaurant-style`: use canned tomatoes, onion, jalapeno, cilantro, lime, and pulse briefly.

## Safety & privacy

Low risk. Wash produce, avoid touching eyes after cutting chiles, and refrigerate because fresh salsa is not shelf-stable.
