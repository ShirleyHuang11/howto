---
name: make-instant-noodles
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

A serving of instant noodles is cooked to proper texture with its seasoning correctly applied — cup or pot variant — and eaten without a scald.

## Preconditions

- A packet (pot method) or cup (pour method) of instant noodles.
- Boiling water (`daily/food/boil-water`); pot method also needs a small pot and a bowl.

## Steps

1. **Read the packet's own instructions once.** Water volume and minutes vary by brand and matter more than habit. → *Expect:* target water amount and time known (typ. 400–500 ml, 3–4 min).
2. **Sort the sachets.** Dry seasoning, oil/paste, dried vegetables — set them aside; note which the instructions add *after* cooking. → *Expect:* sachets out of the packet, not boiled with their plastic.
3. **Cook the noodles.** [BRANCH: pot → noodles into boiling water, simmer per the stated minutes, loosening with chopsticks/fork halfway | cup → fill to the marked line with boiling water, lid on, steep the stated minutes *unopened*] → *Expect:* pot: noodles softening and separating; cup: lid sealed (weight a corner with the sachet), timer running.
4. **Add seasonings at the right stage.** Pot: powder into the broth in the final minute (or into the serving bowl); oil/paste after the heat's off. Cup: per its lid printing, usually after steeping. → *Expect:* fully dissolved seasoning, no dry pockets.
5. **Transfer/open with steam awareness.** ⚠️ *Irreversible:* the classic instant-noodle injury is a lap scald from carrying an overfull cup or bowl — peel the cup lid *away* from you, carry half-covered, or eat where it cooked. → *Expect:* noodles at the table intact; no splash en route.
6. **Cool the first bites.** Noodles hold heat in their strands — lift, blow, test. → *Expect:* first mouthful hot but not scalding.

## Decision points

- Upgrading (egg, greens, leftover protein) → pot method: egg in for the last 1–2 min, greens with 1 min left; cup method: only pre-cooked add-ins, it can't cook anything.
- Less sodium wanted → use half the seasoning sachet; the flavor curve is flat past half.
- No kettle/stove (office, dorm) → the cup + hot-water dispenser is the designed path; microwave *only* if the container says microwave-safe — many cups are not.

## Failure modes & recovery

- **F1 Mushy noodles:** oversteeped/overboiled — eat as-is (soft, not spoiled) and cut 30–60 s next round; cups keep steeping under the lid, so open on time.
- **F2 Bland or salt-bomb:** sachet misjudged — dilute with hot water (salt-bomb) or add the held-back half (bland); calibrate to this brand.
- **F3 Cup tipped/soft cup crushed in hand:** grip cups by the rim, carry on a plate/tray; contain the spill first (`embodied/carry-and-deliver-an-item` F2), noodles are replaceable.
- **F4 Foam boil-over in the pot:** starch foam rises fast — lower heat and stir; a chopstick across the pot rim breaks the foam's dome.

## Verification

Noodles at intended texture, seasoning dissolved and balanced, sachets' plastic accounted for in the trash (not the broth), and the transit from kettle/stove to mouth happened without a burn.

## Variations

- `jp`/`kr`/`cn` styles differ in sachet count and stage rules (kr stews often *boil* the powder; jp cups steep everything) — step 1's read-the-packet covers all of them.
- Dry/stir types (mixing noodles): drain the water after steeping, then mix the sauce — the packet says so, and skipping the drain makes soup-sauce sludge.

## Safety & privacy

Medium risk entirely from boiling water in light containers: the peel-away-and-don't-carry-full rule (step 5) is the recipe's one serious line. Everything else is dinner.
