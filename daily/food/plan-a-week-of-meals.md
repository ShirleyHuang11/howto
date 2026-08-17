---
name: plan-a-week-of-meals
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: basic
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

A realistic week of meals is planned around schedule, budget, ingredients, leftovers, and food safety.

## Preconditions

- Calendar or schedule, pantry inventory, shopping list, budget target, and dietary needs for the people eating.
- Refrigerator and freezer space for planned leftovers.

## Steps

1. **Check the week.** Mark busy nights, eating-out plans, and days needing packed food. → *Expect:* each day has a realistic cooking time estimate.
2. **Inventory food.** Note perishable ingredients, pantry staples, and frozen items to use first. → *Expect:* list highlights foods near expiration.
3. **Choose anchor meals.** Pick 3-5 main meals that share ingredients without feeling identical. → *Expect:* proteins, grains, and vegetables repeat efficiently.
4. **Plan leftovers.** Assign leftovers to lunches or a second dinner within safe storage time. → *Expect:* cooked foods are scheduled within 3-4 days or frozen.
5. **Balance the plate.** Include a protein, vegetable or fruit, and starch or grain for most meals. → *Expect:* meals are filling and not all one food group.
6. **Write the shopping list.** Group missing items by store section and quantity. → *Expect:* list contains only gaps between plan and inventory.
7. **Prep selectively.** Choose 1-3 tasks such as washing greens, cooking grains, or marinating protein. [BRANCH: prep day | cook nightly] → *Expect:* prep saves time without creating more food than you can store.
8. **Post or save the plan.** Put the plan where cooks and eaters can see it. → *Expect:* meals, leftovers, and shopping needs are visible before the week starts.

## Decision points

- Week is unpredictable → plan flexible components like grain bowls, eggs, frozen vegetables, and pantry pasta.
- Budget is tight → choose legumes, eggs, seasonal vegetables, and meals that reuse herbs and sauces.
- Raw meat is planned late in week → freeze it or buy closer to cooking day.

## Failure modes & recovery

- **F1 Overplanned week:** detect meals skipped by day 3 → freeze components and plan fewer cooked dinners next week.
- **F2 Food waste:** detect produce wilting unused → schedule fragile produce earlier and sturdy vegetables later.
- **F3 Missing ingredient:** detect recipe blocked at cooking time → substitute within the same role, such as acid for acid or grain for grain.
- **F4 Unsafe leftovers:** detect cooked food older than 4 days or left out over 2 hours → discard rather than reheat.

## Verification

The plan covers the week, matches the schedule, uses existing perishables, has a shopping list, and assigns leftovers within safe storage windows.

## Variations

- `family`: include each person's constraints and one fallback meal.
- `single-person`: plan freezer portions to avoid eating the same dish all week.
- `meal-prep`: cook components in batches rather than fully assembled meals.

## Safety & privacy

Low risk, mainly food storage and household preference privacy. Keep dietary restrictions visible to cooks, label leftovers with dates, and avoid sharing sensitive medical diets casually.
