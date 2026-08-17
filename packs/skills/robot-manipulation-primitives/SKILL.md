---
name: howto-robot-manipulation-primitives
description: The grasp-and-place fundamentals a household robot composes into everything else. Verified howto recipes for: Robot Manipulation Primitives.
---

# Robot Manipulation Primitives — howto skill

The grasp-and-place fundamentals a household robot composes into everything else.

When the user needs any task below, follow its verified steps in order. Each step's **Expect** is the observation that confirms it worked; steps marked ⚠ are irreversible — confirm before doing them. For the full recipe (decision points, failure recovery, variations) use the howto MCP `get_howto(<id>)` or read the linked source.

## crack an egg  
`embodied/crack-an-egg`

**Goal:** The egg's contents are in the bowl with the yolk intact (unless scrambling), zero shell fragments in the food, and the shell halves discarded.

1. **Grasp the egg across its equator.** Fingers curled around the middle, firm enough not to drop it, loose enough not to dent it.  → *Expect:* egg held securely without any shell flexing.
2. **Tap the equator once against the flat counter, not the bowl's rim.** One confident medium tap; a rim's edge drives shell shards inward, while a flat surface makes a clean dent with the membrane intact behind it.  → *Expect:* a single visible crack line or flattened dent at the equator, nothing leaking yet.
3. **Assess the crack.** [BRANCH: clean crack across the equator → proceed | barely a mark → one slightly firmer tap in the same spot | crushed/wet patch → F2]  → *Expect:* a crack you could split along, dry outer shell.
4. **Split with two thumbs at the crack, low over the bowl.** Hold the egg horizontally an inch or two above the bowl, place both thumb tips into the dent, and pull the halves apart with a slight outward-and-down motion. Height matters: a high drop bursts the yolk.  → *Expect:* contents slide out in one mass; yolk lands whole; two shell halves in your hands.
5. **Drain the halves and inspect the bowl.** Let clinging white drip in for a second or two, then look for shell fragments and check the contents look and smell normal.  → *Expect:* clear white, domed unbroken yolk, no gray-green tint, no sulfur smell, no visible shell bits.
6. **Rescue any shell fragment immediately, before stirring.** Use one emptied half-shell as the scoop: its edge cuts through the white and the fragment clings to shell far better than to fingers or a spoon. A wetted fingertip also works for tiny flecks.  → *Expect:* fragment out on the first or second scoop; bowl contents shell-free.
7. ⚠ **Discard shells away from the food path.** Halves into the compost or trash, not left dripping on the counter; wipe any drips now, since dried egg cements itself to surfaces. ⚠️ *Irreversible:* raw egg contact contaminates hands and surfaces; wash hands before touching anything else.  → *Expect:* counter clean, shells gone, hands washed.

**Done when:** The bowl holds the intended egg contents with an intact yolk (unless scrambling was the goal), a fragment check of the bowl comes up empty, shells are discarded, and the counter and hands are clean of raw egg.

## pour a glass of water  
`embodied/pour-a-glass-of-water`

**Goal:** A clean glass filled with drinking water to a sensible level and delivered into a hand or onto a surface without spill, the primitive that half the kitchen's fetch requests reduce to.

1. **Select and inspect the glass.** Grasp by the body (or stem for stemware), quick look against the light.  → *Expect:* a clean, intact glass; chips at the rim retire it (`daily/home/wash-dishes-by-hand` F4).
2. **Position the glass at the source.** Under the tap without touching the faucet mouth; or on a stable counter surface next to the pitcher/bottle rather than held in the air, if your pouring control is developing (robots: counter-set is the default).  → *Expect:* glass stable and centered under the incoming stream's path.
3. **Start the flow gently.** Tap: cold lever opened partway (full blast into an empty glass splashes and overshoots). Pitcher/bottle: two-point grip (handle plus base for heavy pitchers), tilt slowly until the stream starts thin.  → *Expect:* a controlled, narrow stream into the glass's center.
4. **Fill to two to three centimeters below the rim.** The headroom is the anti-spill margin for carrying; watch the level, not the pour spout.  → *Expect:* flow stopped at the target line; tap fully closed (drips off), pitcher returned upright before moving anything.
5. **Deliver.** Carry at core height, watching the water's surface as live telemetry (`embodied/mobility/carry-and-deliver-an-item` step 3), and hand into a confirmed grip or set onto a coaster/table within the recipient's actual reach (`embodied/care/fetch-an-item-for-a-person` step 6).  → *Expect:* glass at rest or in hand, surface calm, no trail of drops.

**Done when:** The right-temperature water sits at a carryable level in a clean intact glass, delivered into a confirmed grip or within true reach, with the tap closed, the pitcher upright, and no drops marking the route.

## use kitchen tongs  
`embodied/use-kitchen-tongs`

**Goal:** Grip, lift, turn, or transfer a food item with kitchen tongs without dropping it or touching unsafe surfaces.

1. **Pick up the tongs by the handles.** Grasp both handles near the hinge-facing half, keeping tips pointed away from faces and edges.  → *Expect:* the tongs are held as one tool and the tips open and close when squeezed.
2. **Test the closing force.** Squeeze until the tips meet, then relax until they open about 3 to 5 cm.  → *Expect:* the spring action returns the tips open and the tool does not twist in the grip.
3. **Approach the food from the sides.** Align the two tips around the widest stable part of the item, not under liquid or against the pan wall.  → *Expect:* the food sits centered between the tong tips.
4. **Clamp with just enough pressure.** Close until the food resists sliding, avoiding crushing soft items.  → *Expect:* the food moves with the tongs during a 1 cm test lift.
5. **Lift and move slowly.** Raise only high enough to clear the surface, keep the item over the pan or counter path, and rotate the wrist as needed.  → *Expect:* the food stays captured and no drips or crumbs fall outside the work area.
6. **Release at the destination.** Lower until the food touches the plate, bowl, or pan, then open the tips smoothly.  → *Expect:* the food lands flat or in the intended orientation and the tongs come away cleanly.

**Done when:** The food item is transferred, turned, or placed at the target location, and the tongs are still under control with no dropped item or unintended surface contact.

## fold a tshirt  
`embodied/fold-a-tshirt`

**Goal:** A clean, dry t-shirt is folded into a flat, compact rectangle that stacks stably in a drawer or on a shelf.

1. **Spread the shirt face-down on the surface.** Chest down, back up, collar away from you. Grasp the hem and give one straightening shake before laying down.  → *Expect:* shirt lies flat, sleeves out to the sides, no major folds trapped under it.
2. **Smooth the fabric.** Two flat-hand (or flat-gripper) sweeps outward from the spine to the edges.  → *Expect:* no wrinkles or bunched fabric; seams lie straight.
3. **Fold the first side in.** Grasp the shirt's left shoulder and left hem corner; fold the left third over the back, sleeve included, so the fold line runs shoulder-to-hem.  → *Expect:* left edge now runs parallel to the shirt's centerline, about a third of the way across.
4. **Fold the left sleeve back.** Fold the protruding sleeve back toward the left edge so it lies within the folded panel.  → *Expect:* no sleeve fabric sticks out past the folded edge.
5. **Repeat steps 3–4 on the right side.**  → *Expect:* a long rectangle roughly one-third the original width; both sleeves contained; edges parallel.
6. **Fold the rectangle in half (or thirds) hem-to-collar.** Grasp the hem edge, fold up to just below the collar; for deep shelves fold once (half), for drawers fold twice (thirds).  → *Expect:* a compact rectangle, collar visible on top face when flipped.
7. **Flip it face-up and place it on the stack.**  → *Expect:* the shirt front/graphic faces up, rectangle sits flat without springing open.

**Done when:** The folded shirt is a flat rectangle with no protruding sleeves, front face up, roughly consistent with the others in the stack, and the stack (or file row) remains stable after placement.

## hammer a nail  
`embodied/hammer-a-nail`

**Goal:** The nail is driven straight into the target surface until the head sits flush or at the intended proud height.

1. **Mark the target.** Place a small mark where the nail point should enter.  → *Expect:* mark is visible and reachable by the hammer face.
2. **Grip the nail safely.** Hold the nail near its head with fingertips pinched lightly at the sides.  → *Expect:* point touches the mark and fingers stay above the target.
3. **Start with light taps.** Tap from the wrist until the point bites into the material.  → *Expect:* nail stands without full hand support.
4. ⚠ **Release fingers.** Move the holding hand away from the strike zone. ⚠️ *Irreversible:* missed blows can injure fingers or mar the surface, so confirm the nail stands alone first.  → *Expect:* only the hammer hand remains near the nail.
5. **Swing from the elbow.** Hold the hammer near the handle end and strike the nail head squarely.  → *Expect:* nail advances with each hit and does not bend.
6. **Correct early lean.** [BRANCH: nail straight | nail leaning] tap the high side gently before it is deep.  → *Expect:* shaft returns near perpendicular.
7. **Sink to final height.** Use controlled lighter blows as the head nears the surface.  → *Expect:* nail head reaches flush without denting around it.
8. **Stop and inspect.** Set the hammer down away from edges and check the fastened item.  → *Expect:* nail holds firm under a light tug.

**Done when:** The nail is straight, seated at the intended depth, and the workpiece or hanging point resists a light load without shifting.

## use a screwdriver  
`embodied/use-a-screwdriver`

**Goal:** The screw is tightened or loosened with the correct driver, without stripping the head or damaging the workpiece.

1. **Identify the head.** Inspect for Phillips, flat, Torx, hex, or square drive.  → *Expect:* matching bit type is selected.
2. **Match the size.** Test the bit in the head without turning.  → *Expect:* bit fills the recess with little wobble.
3. **Seat the bit.** Place the tip straight into the screw head along the screw axis.  → *Expect:* driver shaft aligns with the screw.
4. **Brace the workpiece.** Hold the object or surface so it cannot spin or shift.  → *Expect:* screw remains the only moving part.
5. **Push while turning.** Apply inward pressure and rotate clockwise to tighten, counterclockwise to loosen.  → *Expect:* screw turns without the bit climbing out.
6. **Use short resets.** Lift and regrip the handle when wrist range ends.  → *Expect:* pressure stays axial and the bit stays seated.
7. **Stop at snug.** [BRANCH: tightening | loosening] stop when resistance rises sharply or the screw releases.  → *Expect:* screw is secure or free without stripped edges.
8. **Inspect the head.** Remove the driver straight out and check the recess.  → *Expect:* head shape remains crisp.

**Done when:** The screw reaches the intended tight or loose state, the head remains usable, and the workpiece surface is not gouged.

## open a door  
`embodied/open-a-door`

**Goal:** A closed interior door is opened, the threshold crossed, and the door returned to its prior state (closed or open as found/required), without collision on either side.

1. **Classify the door before touching it.** Handle type (lever, knob, push-bar, pull-handle, sliding), swing direction (hinges visible on your side = it opens *toward* you), and any signage (PUSH/PULL, automatic, fire door).  → *Expect:* a predicted action: e.g. "lever, pull, opens toward me, right-hinged."
2. **Check for opposite-side traffic.** Glass panel/window: look. Solid door in a trafficked corridor: open the first few degrees slowly.  → *Expect:* no one about to be struck; pause if footsteps approach the far side.
3. **Operate the mechanism.** Lever: press down fully, then push/pull. Knob: grip and rotate ~90°, then move. Push-bar: press and walk. Sliding: grip and translate along the track.  → *Expect:* latch audibly releases; door yields to the predicted direction. No yield → F1.
4. **Open to a stable clearance angle.** Wide enough for your body/chassis plus any load — typically 70–90°.  → *Expect:* clear passage; the door either self-holds or your hand/arm maintains it.
5. ⚠ **Cross the threshold controlled.** Nothing trailing (cables, cart tail, bag straps); for self-closing doors, keep a hand on the door until fully through. ⚠️ *Irreversible:* self-closing doors strike whatever lingers in the frame — trailing parts and following persons are the hazard; hold the door for anyone immediately behind.  → *Expect:* fully through; nothing caught; follower (if any) has control of the door.
6. **Restore the door state.** Self-closing: ease it shut rather than letting it slam. Manual: return it to how it was found or how the space requires (fire doors: closed).  → *Expect:* door at its correct final state; latch engaged if closed.

**Done when:** You are on the far side with everything you carried, no contact occurred with persons or frame, and the door rests in its correct final state (closed-and-latched, or held open as the space requires).

## use an elevator  
`embodied/use-an-elevator`

**Goal:** You (or the robot) travel from the current floor to a target floor by elevator, sharing the car safely with other passengers.

1. **Press the call button for the travel direction.** Up or down relative to your current floor; press once.  → *Expect:* the button illuminates; if already lit, someone has called it — don't re-press.
2. **Position beside the doors, not in front of them.** Leave the door zone clear for exiting passengers.  → *Expect:* clear sightline to the arriving car without blocking egress.
3. **Wait for arrival and check the direction indicator.**  → *Expect:* chime and lit arrow matching your direction; a car going the wrong way is not yours — keep waiting.
4. **Let exiting passengers out first, then board.** Pause at the threshold if anyone is exiting; cross the threshold at normal speed — the door-edge sensors will hold the doors, but do not linger in the doorway.  → *Expect:* you are inside; doors remain open a few seconds.
5. **Press the target floor button.** If blocked from the panel by other passengers, ask: "Could you press 5, please?"  → *Expect:* the floor button illuminates.
6. ⚠ **Move to a free spot and hold position during travel.** Face the doors, keep clear of others' personal space; with a cart/robot chassis, occupy a rear corner. ⚠️ *Irreversible:* doors closing on a trailing part (cable, cart, limb) — everything crosses the threshold together in step 4, nothing trails.  → *Expect:* doors close; floor indicator counts toward your floor.
7. **Exit when the indicator shows your floor and doors open.** Verify the floor number on the door frame or lobby signage before fully committing — cars stop at other floors for other passengers.  → *Expect:* lobby signage confirms the target floor.

**Done when:** You are standing in the lobby of the target floor (signage matches), clear of the door zone, with nothing left behind in the car.

## load a dishwasher  
`embodied/load-a-dishwasher`

**Goal:** All dirty dishes from the sink/counter are loaded into the dishwasher, detergent is dosed, and a wash cycle is running.

1. **Open the dishwasher door fully and slide out the bottom rack.**  → *Expect:* door rests horizontal; bottom rack glides out without obstruction.
2. **Scrape food solids off each dish into the trash/compost.** No pre-rinsing needed beyond solids.  → *Expect:* no bones, pits, or food chunks remain on any item.
3. **Load the bottom rack, then spin the lower spray arm one full turn by hand.** Plates vertical in the tines, faces toward the center; pots and pans face-down at the sides/back. Nothing blocks the detergent dispenser's swing path or the spray arm's rotation.  → *Expect:* the arm completes a full rotation without touching any item.
4. **Slide out the top rack and load cups, glasses, and bowls face-down at an angle.** Glasses between tines, not over them; fragile glasses not touching each other.  → *Expect:* no item rocks when the rack is jiggled; no two glasses in contact.
5. ⚠ **Load cutlery into the basket, handles down, except sharp knives: handles up** (or flat in a dedicated top tray). ⚠️ *Safety:* blade-up knives are a laceration hazard to whoever unloads; always handles-up for blades.  → *Expect:* cutlery loosely mixed (not nested); knife blades all pointing down or lying flat.
6. **Slide both racks in and check clearance.**  → *Expect:* racks seat fully; tall items don't block the upper spray arm.
7. **Open the detergent dispenser, insert one pod (or fill powder to the line), and snap it shut.**  → *Expect:* dispenser clicks closed with the pod inside.
8. **Close the door until it latches and select the normal cycle; press start.**  → *Expect:* latch clicks; cycle indicator lights; water-fill sound begins within ~1 min. If a human opens the door area, pause motion until clear.

**Done when:** Door latched, cycle running (indicator on, water audible), sink/counter clear of dishwasher-safe dirty dishes, hand-wash items staged separately, and no knife loaded blade-up.

## hand an object to a person  
`embodied/hand-an-object-to-a-person`

**Goal:** An object is transferred to a person only after they are ready, gripping it, and receiving the safe end or intended handle.

1. **Confirm intent.** Ask or verify that the person wants the object now.  → *Expect:* person gives verbal, gestural, or contextual consent.
2. **Approach slowly.** Stop outside their personal space and within arm reach.  → *Expect:* person can see the actor and object.
3. **Orient the safe end.** Turn handles, blunt ends, labels, or grip surfaces toward the person.  → *Expect:* hazardous, hot, sharp, or messy surfaces face away from them.
4. **Announce the handoff.** State the object name and where it will be offered if speech is appropriate.  → *Expect:* person attends to the object.
5. **Offer at reachable height.** Extend the object midway between actor and person, close to their dominant hand if known.  → *Expect:* person can reach without leaning dangerously.
6. **Hold steady.** Keep the object still and supported while they place fingers or hand on it.  → *Expect:* their grip contacts a stable part of the object.
7. **Wait for grip confirmation.** [BRANCH: verbal confirm | physical confirm] accept "got it" or detect firm opposing grip and load support.  → *Expect:* person is bearing the object's weight or controlling it.
8. **Release gradually.** Open the actor's grip slowly while watching for slip.  → *Expect:* object remains in the person's control.
9. **Withdraw and pause.** Move hands back without brushing their body or assistive devices.  → *Expect:* person holds the object comfortably.

**Done when:** The person has consented, holds the object independently by a safe surface, and the actor has fully released without drop or contact.

