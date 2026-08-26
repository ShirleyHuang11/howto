---
name: apply-for-an-electronic-travel-authorization
domain: travel
subdomain: prep
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You obtain the correct electronic travel authorization or visa waiver for a destination before departure and link it to the passport you will use.

## Preconditions

- Valid passport, itinerary, destination and transit countries, lodging address if required, and payment card.
- Official government site for the authorization program.
- Email address you can access while traveling.

## Steps

1. **Confirm whether authorization is required.** Check the destination government's official entry requirements for your nationality, passport type, transit route, and purpose of travel. → *Expect:* you know whether you need an ETA, ESTA, eTA, ETA-IL, K-ETA, ETIAS, eVisitor, or another authorization.
2. **Use the official application site.** Navigate from the destination government's immigration, border, or foreign ministry page. → *Expect:* the web address and branding match the official government program.
3. **Check passport validity first.** Confirm your passport number, expiration date, and blank-page or validity requirements. → *Expect:* the passport is acceptable for the trip or you know it must be renewed.
4. **Complete the application exactly.** Enter name, birth date, passport number, nationality, travel purpose, contact details, and eligibility answers as shown on the passport. → *Expect:* the review screen matches the passport character for character.
5. **Review before payment.** ⚠️ *Irreversible:* wrong passport numbers or eligibility answers can cause denial or boarding refusal; confirm every field before submitting. → *Expect:* all details are correct before final submission.
6. **Pay the official fee.** Use the accepted payment method and save the receipt. → *Expect:* the site provides a confirmation number or application reference.
7. **Wait for approval before relying on it.** Check email and the official status portal until approved, not merely submitted. → *Expect:* status shows approved, granted, or authorized.
8. **Save proof and link it to travel documents.** Download, print, or screenshot approval and record its expiration date and passport number. → *Expect:* approval proof is accessible offline and matches the travel passport.

## Decision points

- Transit through a country → check transit authorization rules even if you do not leave the airport.
- Passport will be renewed before travel → apply only after receiving the new passport if authorization is passport-linked.
- Application asks about criminal, immigration, or health history → answer truthfully and seek official guidance if unsure.
- Approval is pending near departure → contact the official program or airline and consider delaying travel if boarding is not allowed.

## Failure modes & recovery

- **F1 Third-party site used accidentally:** detect inflated fees or vague branding → stop before payment if possible and reapply through the official site.
- **F2 Typo in passport number:** detect mismatch after submission → follow the program's correction rules or submit a new application if required.
- **F3 Authorization denied:** detect denied or not authorized status → follow official visa instructions; do not attempt to travel on a denied waiver.
- **F4 Approval not found at check-in:** detect airline cannot verify it → show confirmation, verify passport number, and check the official status portal.

## Verification

The official authorization status is approved for the correct passport number, traveler name, destination, and travel dates, and proof is saved offline.

## Variations

- `us-esta`: ESTA is for Visa Waiver Program travel to the United States and should be requested through the official DHS site.
- `canada-eta`: Canada's eTA is linked electronically to the passport used to apply.
- `eu-etias`: ETIAS rules apply to eligible visa-exempt travelers when the program is in force; confirm current official status before relying on it.

## Safety & privacy

Medium risk because errors can prevent boarding or entry and applications collect identity data. Use official sites, confirm passport-linked details before submitting, and avoid paying unofficial services unless you intentionally choose representation.
