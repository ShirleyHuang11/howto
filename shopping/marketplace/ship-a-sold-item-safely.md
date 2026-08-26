---
name: ship-a-sold-item-safely
domain: shopping
subdomain: marketplace
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You pack and ship a sold marketplace item so it reaches the buyer with tracking, proof, and seller-protection requirements satisfied.

## Preconditions

- A paid order shown inside the marketplace account.
- The exact item sold and all included accessories.
- Packaging materials, scale, tape, label access, and carrier drop-off or pickup.

## Steps

1. **Verify the order in-platform.** Confirm paid status, buyer name, platform-provided address, shipping service, and deadline. → *Expect:* the order is eligible to ship.
2. **Match the item to the order.** Check model, size, color, serial, condition, quantity, and included accessories. → *Expect:* the package contents match the listing exactly.
3. **Document condition before packing.** Photograph or video the item working, flaws already disclosed, accessories, and serial/model details if appropriate. → *Expect:* evidence exists for disputes.
4. **Choose protective packaging.** Use the right box, padding, waterproofing, anti-static bag, or double-boxing for fragile or valuable items. → *Expect:* the item cannot shift or break under normal handling.
5. **Weigh and measure accurately.** Enter packed weight and dimensions before buying a label. → *Expect:* postage matches the actual parcel.
6. **Buy or print the correct label.** Use the marketplace label when seller protection depends on it, and ship only to the order address. → *Expect:* tracking is linked to the order.
7. **Seal and label the package.** Remove old barcodes, attach the label flat, and include any required invoice or customs form. → *Expect:* the carrier can scan and route the package.
8. **Hand the parcel to the carrier.** ⚠️ *Irreversible:* confirm payment and address before release because you cannot retrieve the package easily after acceptance. → *Expect:* you receive an acceptance scan, receipt, or pickup confirmation.
9. **Upload or verify tracking.** Ensure the marketplace order shows shipped and tracking is active. → *Expect:* buyer and platform can see shipment progress.
10. **Keep records until the dispute window ends.** Save photos, receipt, label, tracking, and messages. → *Expect:* evidence is ready if the buyer claims damage or non-receipt.

## Decision points

- Label address differs from buyer message → ship only to the platform address or cancel.
- Item is high value → require signature, insurance, or platform-approved premium service.
- Package weight exceeds label → buy the correct label before drop-off.
- Fragile item cannot be packed safely → cancel or use professional packing before shipping.

## Failure modes & recovery

- **F1 No carrier scan:** detect tracking never starts → contact carrier with receipt; use staffed-counter scans for future high-value shipments.
- **F2 Damaged in transit:** detect buyer photos of damage → submit packing photos, insurance claim, and platform response.
- **F3 Wrong item shipped:** detect mismatch after drop-off → contact buyer and platform immediately; arrange return or correction.
- **F4 Postage adjustment:** detect carrier charges extra → verify measurements and dispute only with evidence.
- **F5 Lost package:** detect tracking stalled beyond carrier window → open carrier claim and platform case with tracking proof.

## Verification

The marketplace order shows shipped with valid tracking to the platform-provided address, the carrier has accepted the package, and packing/order evidence is saved until payout and dispute windows close.

## Variations

- International shipment: complete customs forms accurately and check prohibited exports.
- Local courier: use tracked, insured delivery if platform protection requires it.
- Fragile item: double-box and photograph each packing layer.

## Safety & privacy

Medium risk because shipping releases property and exposes addresses. Ship only after in-platform payment, use the provided address, hide unnecessary personal data, and keep proof.
