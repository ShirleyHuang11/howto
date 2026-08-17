---
name: howto-kitchen-starter
description: Cook anything — the ten fundamentals every other recipe builds on. Verified howto recipes for: Kitchen Starter.
---

# Kitchen Starter — howto skill

Cook anything — the ten fundamentals every other recipe builds on.

When the user needs any task below, follow its verified steps in order. Each step's **Expect** is the observation that confirms it worked; steps marked ⚠ are irreversible — confirm before doing them. For the full recipe (decision points, failure recovery, variations) use the howto MCP `get_howto(<id>)` or read the linked source.

## boil water  
`daily/boil-water`

**Goal:** A container of water is brought to a full boil and is available for use (tea, cooking, sterilizing) without spills or burns.

1. **Choose the method for the amount needed.** [BRANCH: electric kettle (fastest, ≤ its max line) | stovetop pot (any volume) | microwave (single cup only — see Variations for the superheating precautions)]  → *Expect:* container capacity ≥ needed volume with ≥ 2 cm headroom.
2. **Fill with cold tap water to the needed level.** Kettle: between MIN and MAX marks. Pot: no more than 2/3 full.  → *Expect:* water level within the safe marks; outside of the container is dry.
3. **Start heating.** Kettle: seat it on its base, close the lid, press the switch. Stovetop: pot centered on the burner, lid on, burner to high.  → *Expect:* kettle switch light on / burner flame or coil visibly on; faint heating sound builds within ~1 min.
4. **Wait, staying within earshot.** Do not leave the building with a stove on.  → *Expect:* progression of sound: quiet → hissing → rolling rumble; steam appears from the spout or lid edge.
5. **Recognize the boil.** Kettle: clicks off automatically. Pot: large bubbles break the surface continuously (a "rolling boil"); lid may rattle.  → *Expect:* kettle switch has flipped off, or the pot shows a sustained rolling boil.
6. ⚠ **Turn off the heat (stovetop) and move the container safely.** Use the handle; for a pot, lift the lid tilted *away* from your face to vent steam away. ⚠️ *Irreversible:* boiling-water scalds — never carry a full open pot across the room; bring the destination (cup, pan) near the kettle/pot instead.  → *Expect:* heat source off; container resting on the dry stable surface.
7. **Use or pour the water at once.** Pour slowly, spout close to the target vessel.  → *Expect:* target vessel filled without splash; remaining water left in the container, not in your path.

**Done when:** The water reached a sustained rolling boil (or the kettle auto-clicked off), the heat source is now off, and the hot container sits on a stable dry surface — no water on the floor or stovetop, no one scalded.

## cook rice  
`daily/cook-rice`

**Goal:** A batch of rice cooked to fluffy, separate (or intentionally sticky) grains — not burnt, crunchy, or gluey.

1. **Measure the rice.** ~¾ cup dry per hungry person.  → *Expect:* rice in a bowl or the cooker pot, quantity known in "cups".
2. **Rinse until the water runs mostly clear.** Cover with cold water, agitate with fingers, pour off the cloudy water; repeat 2–3×.  → *Expect:* rinse water goes from milky to nearly clear — this is what prevents gluey rice.
3. **Add water by ratio.** Long-grain white: 1 : 1.5 (rice : water). Rice cooker: fill to the matching numbered line instead.  → *Expect:* correct water level; a pinch of salt in if desired.
4. **Bring to a boil uncovered, then drop to the lowest heat and lid on.** [BRANCH: rice cooker → press cook and skip to step 6]  → *Expect:* brief visible boil, then a quiet simmer under a closed lid.
5. **Simmer ~15 min without lifting the lid.** The trapped steam is doing the cooking; every peek costs it.  → *Expect:* faint hissing that quiets near the end; no burnt smell (burnt smell → F2).
6. **Rest 10 minutes off the heat, lid still on.** Rice cooker: after it clicks to "keep warm", same rest.  → *Expect:* untouched pot; the rest lets moisture equalize so the bottom isn't wet and the top isn't dry.
7. **Fluff with a fork or paddle and serve.** Gentle folding, not stirring.  → *Expect:* grains separate and tender all the way through.

**Done when:** Grains are tender through the center, distinct (unless sticky was intended), nothing is burnt to the pot beyond a light film, and quantity matches the plan.

## fry an egg  
`daily/fry-an-egg`

**Goal:** An egg fried to your chosen doneness — runny sunny-side-up through fully-set over-hard — with an intact yolk (unless scrambled was the plan) and no burnt edges.

1. **Heat the pan on medium, not high.** Add a small knob of butter or ~1 tsp oil.  → *Expect:* butter foams gently without browning / oil shimmers without smoking. Smoking pan → too hot, F1.
2. **Crack the egg.** Tap firmly once on a *flat* surface (not the pan edge — drives shell in), part the shell with thumbs close to the pan or into a bowl first, and slide it in low.  → *Expect:* yolk intact, white contained, no shell fragments (fragment → fish out with a shell half, it attracts the piece).
3. **Let it set undisturbed on medium-low.** Salt and pepper the top.  → *Expect:* white turning opaque from the edges inward within a minute; gentle sizzle, not violent sputtering.
4. **Choose the finish.** [BRANCH: sunny-side-up → cover with a lid 1 min so steam sets the top | over-easy → flip gently when the white is set, 20–30 s on side two | over-hard → flip and press yolk to break, cook till firm]  → *Expect:* whites fully set (no clear slime) in every finish; yolk state per choice.
5. **Slide onto the plate.** Spatula fully under before lifting; tilt the pan to help.  → *Expect:* egg lands intact; runny yolk unbroken until you break it on purpose.
6. **Kill the heat and move the pan off the burner.**  → *Expect:* stove off; pan cooling on an idle burner.

**Done when:** Whites fully opaque and set, yolk in the chosen state, no burnt frill, egg intact on the plate, and the burner is off.

## cook pasta  
`daily/cook-pasta`

**Goal:** Pasta cooked to al dente, seasoned from the water, married to its sauce, and on the table without a starch-glued colander disaster.

1. **Boil abundant water.** Roughly a liter per 100 g of pasta; crowded pasta cooks unevenly and glues. Lid on for speed (`daily/food/boil-water`).  → *Expect:* a full rolling boil before any pasta enters.
2. **Salt the water generously.** About a tablespoon per few liters, into the boil. Salted water is the only chance to season the pasta itself; the old line is it should taste like the sea.  → *Expect:* visibly salted, briefly calmer, then boiling again.
3. **Add the pasta and stir within the first minute.** Long shapes fan into the pot and soften down; the first-minute stir is what prevents sticking, more than any oil (oil in the water mostly coats the drain).  → *Expect:* pasta fully submerged and moving freely after the stir.
4. **Cook at a lively boil, stirring occasionally, and set a timer for two minutes under the packet time.** The packet number lands soft; the check starts early.  → *Expect:* timer running; occasional stirs; foam managed by lowering heat slightly or resting a spoon across the pot.
5. **Test by biting.** From the timer's ring, fish a piece every minute: al dente means tender with a slight firm core, no white chalky center.  → *Expect:* the bite test, not the clock, makes the call.
6. ⚠ **Reserve a cup of the cooking water, then drain.** Cup first, always, because the colander move is irreversible. Drain promptly; do not rinse (the surface starch is what lets sauce cling; rinsing is only for cold pasta salads). ⚠️ *Irreversible:* the pour is a steam-and-boiling-water moment; pour away from yourself, face back from the steam.  → *Expect:* pasta in the colander, starchy water saved, nobody steamed.
7. **Marry pasta and sauce in the pan, loosening with the reserved water.** Pasta into the sauce (never sauce ladled onto naked pasta on plates, ideally), a splash of the starchy water, and a minute of tossing over heat until the sauce coats and clings.  → *Expect:* glossy, coated pasta; the water's starch visibly binding sauce to noodle.
8. **Serve immediately.** Pasta continues softening as it sits; the table waits for pasta, not the reverse.  → *Expect:* plates out within minutes, cheese and pepper at the table.

**Done when:** The pasta passes the bite test at al dente, tastes seasoned on its own, wears its sauce glossily thanks to the reserved water, reached the table promptly, and the stove shows no boil-over archaeology.

## make a stir fry  
`daily/make-a-stir-fry`

**Goal:** A stir-fry with seared (not steamed) protein and crisp-tender vegetables, glazed in sauce, served over rice or noodles within minutes of finishing.

1. **Prep every single ingredient before the burner goes on.** Slice protein thin against the grain; cut vegetables bite-size, grouped hard vs. soft; mince aromatics; stir the sauce together in a bowl; mix the slurry. Once the pan is hot there is zero time to chop.  → *Expect:* all ingredients in separate bowls arranged in cooking order beside the stove, sauce mixed, empty plate staged for the protein.
2. **Heat the dry pan until it is screaming hot.** High heat, 1-2 minutes empty, then add oil and swirl. Water flicked on the surface should bead and skitter, not sit and sizzle.  → *Expect:* oil shimmers and runs thin immediately; the first wisp of smoke is the go signal.
3. **Sear the protein in a single layer and leave it alone for 30-60 seconds.** Then toss until just cooked. Crowding drops the pan temperature and boils the meat in its own juices; cook in two batches if needed.  → *Expect:* browned edges and a sear crust; protein removed to the staged plate at barely-done.
4. **Re-heat the pan, add oil, then the hard vegetables.** Carrots, broccoli, peppers first; toss every 15-20 seconds, letting them sit briefly between tosses to char. A tablespoon of water with a quick lid, 30 seconds, steams dense broccoli through.  → *Expect:* blistered spots on the vegetables, colors brightened, still snappy.
5. **Add soft vegetables and aromatics late.** Snow peas, leafy greens, then garlic and ginger for the final 30-60 seconds only; burnt garlic is bitter and unfixable.  → *Expect:* greens just wilted, aromatics fragrant and golden, not brown.
6. **Return the protein, pour the sauce around the pan's edge, and toss.** Pouring down the hot pan wall sizzles off raw sauce taste.  → *Expect:* everything reunited, sauce bubbling hard within seconds.
7. ⚠ **Thicken with the slurry and kill the heat.** Re-stir the slurry (cornstarch settles), add half, toss 15 seconds; add the rest only if the glaze is still thin. ⚠️ *Irreversible:* over-thickening turns the sauce to gravy-glue; you can always add more slurry but never remove it.  → *Expect:* sauce clings to each piece with a glossy coat; no pool of liquid in the pan bottom.
8. **Serve immediately over the rice or noodles.** A stir-fry degrades by the minute; steam softens the sear.  → *Expect:* plated and eaten hot, wok soaking in the sink.

**Done when:** Protein shows sear color and is cooked through, vegetables retain a slight snap and bright color, the sauce coats as a glossy glaze with no watery pool, and the dish hit the table within ~2 minutes of the heat going off.

## roast vegetables  
`daily/roast-vegetables`

**Goal:** A tray of vegetables roasted until browned and caramelized at the edges, tender inside, seasoned and ready to serve.

1. **Preheat the oven hot: 220 °C / 425 °F.** High heat is the whole method; a 180 °C oven steams vegetables instead of browning them.  → *Expect:* oven fully preheated before the tray goes in.
2. **Cut vegetables into even pieces, grouped by density.** Bite-size, uniform within each group: hard roots (potato, carrot, beet) in one group, quick cookers (zucchini, peppers, broccoli) in another. Uniformity matters more than the exact size.  → *Expect:* pieces of matching thickness within each group; hard and soft vegetables kept separate.
3. **Dry the vegetables thoroughly.** Pat with a towel after washing; surface water is the enemy of browning.  → *Expect:* no visible moisture on the pieces.
4. **Toss with oil and salt in a bowl, not on the tray.** Enough oil to give every piece a thin sheen (roughly 1-2 tbsp per tray), a generous pinch of salt, pepper. Tossing in a bowl coats evenly; drizzling on the tray leaves dry patches that scorch.  → *Expect:* every piece glistens lightly; no oil pooling in the bowl bottom.
5. ⚠ **Spread in a single layer with space between pieces.** ⚠️ *Irreversible:* a crowded tray traps steam and the batch comes out pale and soggy; no amount of extra time fixes it. Use a second tray rather than piling. Cut-side down for maximum browning.  → *Expect:* one layer, pieces not touching, flat faces against the metal.
6. **Roast 20-35 minutes, flipping once at the halfway point.** [BRANCH: mixed-density batches on separate trays → start the hard tray 10-15 min before the soft one | single-density batch → one timer] Hard roots run 30-40 min total, soft vegetables 15-25.  → *Expect:* at the flip, undersides show deep golden-brown patches; pieces release from the tray without tearing.
7. **Pull when edges are browned and a fork slides in easily.** Judge by color and tenderness, not the clock; deep brown edges (short of black) are flavor.  → *Expect:* caramelized edges, tender centers, a few dark crispy bits.
8. **Finish and serve hot.** Taste one piece; adjust salt, add any delicate finishers now (lemon, herbs, parmesan, a vinegar splash).  → *Expect:* seasoning bright, vegetables served before they soften on the tray.

**Done when:** Every piece shows browned, caramelized edges; a fork enters the thickest piece without resistance; nothing is soggy or blackened beyond edge char; the oven is off and the tray is on a trivet, not a bare counter.

## make a salad  
`daily/make-a-salad`

**Goal:** A salad that people actually want to eat: washed and dried greens, balanced components, and a dressing applied at the right moment so nothing arrives wilted or swimming.

1. **Wash the greens properly.** Separate leaves, submerge in a bowl of cold water, agitate, lift the greens out (grit sinks; pouring the bowl back over them re-grits everything). Repeat for sandy greens like spinach.  → *Expect:* no grit at the bowl's bottom on the final pass.
2. **Dry the greens completely.** Spinner, or rolled loosely in a clean towel and patted. This is the least glamorous and most important step: dressing slides off wet leaves and pools at the bottom.  → *Expect:* leaves dry to the touch.
3. **Tear or cut into fork-sized pieces.** Bite-sized beats knife-and-fork wrestling at the table.  → *Expect:* pieces that fit on a fork without folding engineering.
4. **Build the body.** Crunch (cucumber, peppers, carrots, radish), something sweet or juicy (tomato, apple, orange segments), something rich (cheese, avocado, nuts, seeds), and the protein for meal salads (eggs, beans, chicken, tuna). Aim for three to five components beyond the greens; more becomes compost-drawer roulette.  → *Expect:* a bowl with contrast in texture, color, and richness.
5. **Make the dressing in the ratio 3:1 oil to acid.** Three spoons oil, one spoon vinegar or lemon, salt, pepper, and optionally a dab of mustard or honey to bind. Shake in a jar or whisk in the bowl's bottom before the greens go in.  → *Expect:* a dressing that tastes slightly too sharp alone; it mellows across the leaves.
6. ⚠ **Dress at the last minute, less than you think, and toss thoroughly.** Half the dressing, toss with hands or two spoons from the bottom up, taste a leaf, add more only if needed. ⚠️ *Irreversible in effect:* overdressing cannot be undone; underdressing takes ten seconds to fix.  → *Expect:* every leaf lightly coated, nothing pooling below.
7. **Finish and serve immediately.** Delicate toppings (croutons, seeds, cheese shavings) go on after the toss so they stay crisp and visible.  → *Expect:* salad on the table within minutes of dressing.

**Done when:** Leaves are dry-crisp with no grit, the components cover crunch, sweetness, and richness, every leaf carries a light coat with no pool at the bottom, and delicate toppings arrived crisp on top at serving time.

## store leftovers  
`daily/store-leftovers`

**Goal:** Leftover cooked food is safely cooled, containerized, labeled, and stored so it stays edible — and anything past its window is recognized and discarded.

1. **Start the clock check.** Food sitting out beyond ~2 hours at room temperature is not safe to store — it's discard territory, however wasteful that feels.  → *Expect:* what you're storing has been out < 2 h.
2. **Portion into shallow containers.** Divide large amounts (a pot of soup, a roast) into shallow layers ≤ 5 cm deep — big warm masses cool too slowly in the middle, which is where bacteria win.  → *Expect:* several shallow portions instead of one deep vessel; portion sizes match how you'll actually eat them.
3. **Let steam off briefly, then lid and refrigerate — don't wait for full cooling on the counter.** Modern fridges handle warm (not scalding) food; loosely lid until steaming stops, then seal.  → *Expect:* containers sealed and in the fridge well inside the 2-hour window.
4. **Label each container.** Contents + today's date on tape or the lid.  → *Expect:* every container answers "what and when" at a glance — unlabeled leftovers become mystery hazards by day 3.
5. **Place correctly in the fridge.** Leftovers on upper/middle shelves; never above raw meat's drip zone — raw meat lives on the bottom shelf.  → *Expect:* leftovers cold-stored away from raw-food contamination paths.
6. **Freeze what you won't eat within the window.** Fridge window for cooked leftovers: 3–4 days. [BRANCH: eating within 3–4 days → fridge | later → freezer, with a freezer-safe container leaving expansion headspace]  → *Expect:* anything beyond the 4-day horizon is in the freezer, labeled.
7. ⚠ **Reheat safely when eating.** Reheat only the portion you'll eat, until steaming hot throughout (see `daily/use-a-microwave`); frozen portions thaw in the fridge overnight, not on the counter. ⚠️ *Irreversible:* repeated reheat-cool cycles make food unsafe — reheat once; what's reheated and unfinished is discarded.  → *Expect:* portion steaming at the center; remainder still stored untouched.

**Done when:** All leftovers are in labeled, dated, sealed containers in the correct zone (fridge shelf or freezer), nothing has been out over 2 hours, and nothing older than 4 days remains in the fridge unlabeled or unfrozen.

## read food labels  
`daily/read-food-labels`

**Goal:** Given any packaged food, you can extract the four decisions the label answers — is it safe to eat (dates), what's actually in it (ingredients), what it does nutritionally (panel), and is the marketing lying (front vs. back) — in under a minute.

1. **Dates first, and know which kind you're reading.** "Use by" = safety deadline — respect it for meat, fish, dairy, ready meals. "Best before/best by" = quality estimate — food is commonly fine after it, judged by look and smell (`daily/food/store-leftovers` senses check).  → *Expect:* you know whether the date on this item is a law or a suggestion.
2. **Read the ingredients list as a ranked ballot.** Ingredients descend by weight: the first three *are* the product. "Whole grain" bragging with wheat flour first and whole grain fifth = the label answered the marketing. Sugar hides under aliases (syrups, -ose endings, juice concentrates) — count how many appear.  → *Expect:* a one-sentence truth: "this is mostly X and Y, with Z for flavor."
3. **Read the nutrition panel against the serving-size trick.** Find the serving size *first* — panels normalize to servings that can be comically small (the 250 ml bottle that's "2 servings"). Then scan the few numbers that drive most decisions: calories, salt/sodium, sugars, saturated fat, fiber, protein — per *your actual portion*.  → *Expect:* the numbers mentally rescaled to what you'd really eat.
4. **Use the per-100g column (where present) to compare products.** Same-units comparison is the honest one — two cereals at per-100g sugar tells you instantly which is dessert. Traffic-light labels (where used) do this pre-digested.  → *Expect:* an apples-to-apples verdict between the two packages in your hands.
5. **Check allergens the fast way.** Allergen paragraphs in bold ("contains: milk, soy") plus "may contain" cross-contamination lines — that bolded block is legally curated for exactly this scan.  → *Expect:* a clear yes/no for the allergies at your table.
6. **Audit the front against the back once.** "No added sugar" (but dates and juice concentrate), "protein!" (as much as regular yogurt), "natural" (regulates almost nothing) — the front is advertising, the back is regulated.  → *Expect:* the front's biggest claim confirmed or quietly filed under marketing.

**Done when:** For the package in your hand you can state: safety-vs-quality date status, what it mostly is (top-3 ingredients), its numbers at your real portion, its allergen status, and whether the front-of-pack claim survived the back-of-pack read.

## sharpen a kitchen knife  
`daily/sharpen-a-kitchen-knife`

**Goal:** A dull kitchen knife is restored to a working edge with the tools you actually own, tested safely, and the truth absorbed that a sharp knife is the safe knife (`daily/food/cut-an-onion`'s first precondition, delivered).

1. **Diagnose before sharpening.** The paper test: slice a held sheet of paper. Clean slice: the knife is fine, hone it and stop. Tears or slides off a tomato skin: proceed to actual sharpening.  → *Expect:* an honest verdict; most "dull" knives that were recently sharpened just need honing (step 5).
2. **Pull-through sharpener path: anchor it, then draw the knife through with light, even pulls.** Coarse slot first (3 to 5 pulls, heel to tip, light downward pressure), then the fine slot the same way.  → *Expect:* even resistance each pull; a faint gritty sound; no sawing back and forth.
3. **Whetstone path: soak or wet the stone per its type, then hold the blade at roughly 15 to 20 degrees and sweep.** Edge trailing, moderate pressure away and light pressure back, covering heel to tip in overlapping strokes; equal strokes per side; coarse side until a burr forms along the whole edge (a faint catch you can feel with a careful thumb across, never along, the edge), then the fine side to refine it.  → *Expect:* a consistent angle held throughout; a burr raised on each side then polished off.
4. **Deburr and clean.** A few very light alternating strokes on the fine surface, then wash and dry the knife; abrasive dust does not belong in food.  → *Expect:* clean blade, no metal-slurry residue.
5. **Hone as the finishing pass and as the between-times habit.** Steel held point-down on the board, blade at the same shallow angle, 4 to 6 light alternating strokes per side, heel to tip.  → *Expect:* the edge aligned; this thirty-second habit, done weekly, delays the next real sharpening by months.
6. ⚠ **Test the result the safe way.** Paper slice, or a tomato: a sharp knife bites the skin at zero pressure. ⚠️ Never test an edge with a thumb along the blade or by casual chopping at speed; the newly sharp knife is exactly when old dull-knife force habits cause cuts.  → *Expect:* clean paper slice; the first real cutting session done deliberately slower than usual.

**Done when:** The paper test passes cleanly, the knife is washed of grit, the honing steel is stationed where the knife lives, and the first cutting session afterward was consciously slower with the claw grip intact.

