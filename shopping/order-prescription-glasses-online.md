---
name: order-prescription-glasses-online
domain: shopping
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Order prescription glasses online with correct prescription, pupillary distance, frame fit, lens options, and return terms.

## Preconditions

- You have a current eyeglass prescription, not just a contact lens prescription.
- You know or can measure pupillary distance.
- You have a pair of glasses that fits well or face measurements for frame sizing.

## Steps

1. **Check prescription validity.** Confirm sphere, cylinder, axis, add power if needed, expiration date, and doctor contact. → *Expect:* the prescription can legally and accurately be used.
2. **Measure pupillary distance.** Use the doctor's value, old glasses order, or retailer measurement tool with repeat checks. → *Expect:* PD is recorded for single or dual-eye entry.
3. **Choose frame size.** Compare lens width, bridge, temple length, frame width, and lens height to glasses that fit. → *Expect:* candidate frames should sit comfortably.
4. **Select lens type.** [BRANCH: single vision | progressive | bifocal | readers] match the prescription and daily use. → *Expect:* the lens category fits the prescription.
5. **Choose lens options carefully.** Compare index, anti-reflective coating, scratch resistance, blue-light claims, photochromic tint, polarization, and sunglasses. → *Expect:* upgrades are useful rather than automatic.
6. **Review insurance and discounts.** Check out-of-network reimbursement, HSA or FSA eligibility, coupons, shipping, taxes, and return fees. → *Expect:* total cost and reimbursement path are known.
7. **Enter prescription exactly.** Copy plus or minus signs, decimals, cylinder, axis, add, prism, and PD into the order form. → *Expect:* the order preview matches the prescription.
8. **Place the order.** Confirm frame, prescription, PD, lens options, shipping address, and return policy before payment. ⚠️ *Irreversible:* custom prescription lenses may have limited refunds, so verify all numbers before paying. → *Expect:* confirmation shows all prescription and product details.
9. **Check glasses on arrival.** Test distance, reading, frame fit, lens defects, and headaches or distortion over the allowed adjustment period. → *Expect:* you know whether to keep, adjust, or remake them.

## Decision points

- Prescription is strong, has prism, or needs progressives → consider local optician fitting or a retailer with remake support.
- PD measurement varies between attempts → ask the eye doctor or optical shop for the measurement.
- Frames are final sale → order only if sizing confidence is high.
- Vision feels wrong on arrival → stop driving with them and request remake or verification.

## Failure modes & recovery

- **F1 Plus-minus entry error:** detect vision very blurry, recover by comparing order confirmation to prescription.
- **F2 PD wrong:** detect eye strain or distortion, recover by requesting lens verification and remake.
- **F3 Frame poor fit:** detect slipping, pinching, or eyelashes touching lenses, recover by adjustment, exchange, or return.
- **F4 Insurance denied:** detect missing itemized receipt, recover by requesting an invoice with provider and product details.
- **F5 Progressive adaptation failure:** detect persistent swim or reading blur, recover through retailer remake policy.

## Verification

The order confirmation matches the prescription and PD, and the delivered glasses provide clear vision and acceptable fit within the return or remake window.

## Variations

- `us`: prescription release, insurance reimbursement, HSA, and FSA rules may apply.
- Children: fit, durability, and professional adjustment are more important.
- Safety glasses: require appropriate impact-rating and workplace standards.

## Safety & privacy

Prescription orders expose health data, payment details, and address. Do not drive or do hazardous work with glasses that distort vision.
