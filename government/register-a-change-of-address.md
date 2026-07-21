---
name: register-a-change-of-address
domain: government
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

After a move, your new address is registered where the law requires it, your mail follows you, and the institutions that matter (bank, employer, insurance, subscriptions) all point at the new address, in the right order.

## Preconditions

- A completed or imminent move with the new address in its exact official form.
- Knowledge of your country's registration regime. Some countries require formal residence registration within a deadline (Germany, Japan, the Netherlands, and many others); some have no central registration and address changes happen per-institution (US, UK, Australia).
- Documents for formal registration where it applies: ID or passport, the lease or a landlord confirmation, and the local form.

## Steps

1. **Establish your country's rule and deadline first.** Search the official municipal or government site for "change of address" or the local term (Anmeldung/Ummeldung, 転居届, verhuizing doorgeven). Note the deadline; several countries fine late registration. → *Expect:* you know whether you owe a formal registration, to whom, and by when.
2. **Do the formal registration where required.** Book the municipal appointment (slots run out; book the moment the move date is known), bring the document set, and leave with the confirmation certificate. That certificate unlocks banks, contracts, and utilities in registration countries, so store it carefully. → *Expect:* registration completed within the deadline, certificate in hand or in the mail.
3. **Set up postal forwarding before the move if possible.** The postal service's mail-forwarding product (USPS change of address, Royal Mail redirection, Nachsendeauftrag) buys you months of catching whatever you forgot. Pay for the longest sensible window. → *Expect:* mail addressed to the old place arrives at the new one, each piece a reminder of an institution still to update.
4. **Update the money layer next.** Bank and cards, payroll or pension, tax authority, insurance policies. Copy the address exactly from the registration or lease; inconsistent formats across institutions cause verification failures later (`finance/open-a-bank-account` step 2's lesson in reverse). → *Expect:* the institutions that send legally important mail all show the new address.
5. **Update the identity layer.** Driving licence and vehicle registration where required (often with its own deadline), voter registration, national ID where it carries an address. → *Expect:* every government-issued document that shows an address either updated or its update in progress.
6. **Sweep the long tail with the forwarded mail as your checklist.** Doctor and dentist (`healthcare/book-a-doctors-appointment` records), phone and internet (`housing/set-up-utilities` step 8 closes the old, this step opens the new), online shopping default addresses (`shopping/buy-a-product-online` will otherwise ship to your past), subscriptions, loyalty programs, school or university. Each forwarded envelope names a laggard; update it and the stream dries up. → *Expect:* forwarded mail volume visibly declining month over month.
7. **Tell the humans.** A short new-address message to family and friends, and neighbors at both ends where relevant (`daily/social/greet-a-neighbor` begins at the new place). → *Expect:* people who send you things know where you are.

## Decision points

- Moving countries rather than within one: deregistration at the old country can matter as much as registration at the new (tax residency, health insurance), and the order of operations is worth an hour of official-site reading before the move.
- Shared or temporary housing where the landlord resists registration: in registration countries you generally have a legal right to register where you actually live, and the landlord confirmation is an obligation. Tenant associations know the local mechanics.
- Privacy-sensitive situations: several registries offer address confidentiality programs. Ask at registration rather than assuming the register is private by default.

## Failure modes & recovery

- **F1 Missed a registration deadline:** register now anyway. Fines scale with delay and with whether you volunteered or were caught, so late beats never by a wide margin.
- **F2 Important mail went to the old address after forwarding lapsed:** contact the sender for a resend to the updated address, and treat it as the trigger to finally update that institution. New occupants forwarding a stray envelope deserve thanks.
- **F3 Verification failures because addresses differ across systems ("Str." vs "Strasse", unit number placement):** pick the format on your registration certificate as canonical and correct the others toward it.
- **F4 Old-address accounts drifting into strangers' hands (packages, 2FA letters):** this is the security cost of an incomplete sweep. Prioritize anything that mails codes or cards (step 4's layer) and audit `accounts/review-account-security` recovery paths for stale addresses.

## Verification

Formal registration (where required) is done within deadline with the certificate stored, mail forwarding is active, the money and identity layers show the new address, forwarded mail has slowed to junk, and nothing that mails you codes, cards, or legal notices still believes in the old address.

## Variations

- `de`: Anmeldung within two weeks, appointment culture, the certificate (Meldebescheinigung) is a master document; `jp`: moving-out and moving-in notifications at the respective city offices within 14 days; `us`: no central registry, so USPS forwarding plus the per-institution sweep is the whole system; `uk`: similar, with the electoral roll doubling as an address anchor.
- Students moving for a term: some countries have simplified or exempt rules for temporary stays. Check rather than over-registering.

## Safety & privacy

Medium risk in two forms: fines for missed legal deadlines, and identity exposure through mail sent to your past. The forwarding product and the money-layer-first ordering are the mitigations. The registration certificate itself is an identity document; store it like one.
