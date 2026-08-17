---
name: scan-an-item-at-self-checkout
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [item, barcode, scanner, checkout-scale, bagging-area]
affordances: [grasp, orient, sweep, scan, place, observe]
workspace: self-checkout station
safety: {hot_surfaces: false, sharp_objects: false, fragile: [item-packaging], human_proximity: slow}
---

## Goal

One merchandise item is scanned successfully and placed in the bagging area for purchase.

## Preconditions

- Self-checkout station is active and ready to scan.
- Item has a visible barcode or lookup code.
- The bagging area is clear enough for the item.

## Steps

1. **Pick up the item securely.** Grasp the rigid or strongest packaging area without covering the barcode. → *Expect:* the item is controlled and the barcode remains visible.
2. **Locate the scanner window.** Identify the glass scanner or handheld scanner light. → *Expect:* the active scan area is visible.
3. **Orient the barcode toward the scanner.** Rotate the item so the barcode lines face the scanner window at close range. → *Expect:* the barcode is unobstructed and roughly parallel to the scanner face.
4. **Sweep slowly across the scanner.** Move the barcode 2-10 cm above the window or in front of the handheld scanner beam. → *Expect:* the terminal beeps or the item appears on screen.
5. **Place item in bagging area.** Lower it onto the scale or bagging platform without removing previously scanned items. → *Expect:* the item rests fully in the bagging area.
6. **Check screen confirmation.** Read the displayed item name or price before scanning the next item. → *Expect:* the screen shows one added line item matching the product.

## Decision points

- Barcode is damaged → use the on-screen item lookup or ask attendant help.
- Item is produce without barcode → use produce lookup rather than scanning.
- Age-restricted or security-tagged item → wait for attendant approval.

## Failure modes & recovery

- **F1 Scan not recognized:** detect by no beep or line item → flatten the barcode, change angle, and sweep more slowly.
- **F2 Wrong item appears:** detect by mismatched name or price → call attendant or remove the item before continuing.
- **F3 Bagging error:** detect by station alert after placement → leave the item still and wait for prompt or attendant reset.

## Verification

The checkout screen shows the correct item as a line item and the physical item is in the bagging area.

## Variations

- Handheld scanner: hold the trigger and aim the beam across the full barcode.
- Large items: scan in cart if the station allows it, then follow on-screen placement instructions.

## Safety & privacy

This task affects payment. Confirm the correct item and price before checkout, and avoid exposing payment cards or loyalty details.
