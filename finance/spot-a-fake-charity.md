---
name: spot-a-fake-charity
domain: finance
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A charity request is checked for legitimacy before you donate, and any gift is made only through the charity's official channel.

## Preconditions

- You have the charity name, campaign name, caller, message, website, or social media post.
- You have not already sent money or payment details.
- You can search official charity registries or trusted watchdog sources for your country.
- You can pause the request long enough to verify it.

## Steps

1. **Pause the appeal.** Do not donate during the call, doorstep visit, message thread, or emotional pitch. → *Expect:* you have time to verify without pressure.
2. **Record the claimed name.** Write down the exact charity name, website, phone number, and fundraiser name. → *Expect:* spelling and contact details are available for comparison.
3. **Search official registration.** Check the charity regulator, tax-exempt database, or nonprofit registry for the exact name. → *Expect:* registration status, legal name, and identifier match or do not match.
4. **Compare contact details.** Use the registry or official charity website to compare phone, domain, address, and donation page. → *Expect:* the solicitation details match trusted records.
5. **Look for pressure tells.** Notice urgency, secrecy, vague programs, celebrity claims, or refusal to send written information. → *Expect:* any manipulation signs are identified before payment.
6. **Reject unsafe payment methods.** Refuse gift cards, wire transfers, crypto, payment apps to individuals, or cash pickup. → *Expect:* only traceable donation channels remain.
7. **Donate through the official site.** Type the official web address yourself or use the registry's link. → *Expect:* payment goes to the confirmed charity domain or mail address.
8. **Save the receipt.** Keep confirmation, amount, date, and charity identifier for records. → *Expect:* proof of donation is stored.

## Decision points

- Name is similar but not exact -> treat it as unverified until registry details match.
- Caller refuses a callback -> end the interaction and contact the charity through official details.
- Disaster or crisis appeal feels urgent -> donate to an established charity already verified.
- You already paid -> contact the payment provider and report the suspected fraud.

## Failure modes & recovery

- **F1 Imposter website:** domain differs from the official charity, close it and navigate from the registry listing.
- **F2 High-pressure fundraiser:** solicitor demands immediate payment, end the contact and verify independently.
- **F3 Unsafe payment request:** gift card, wire, or crypto is requested, refuse and report the solicitation.
- **F4 Fake receipt:** confirmation lacks charity identity or tax details, contact the official charity to verify.

## Verification

The charity registration and contact details match official records, and any donation is made through the verified official channel.

## Variations

- `us`: check IRS tax-exempt search and state charity registration where applicable.
- `uk`: check the Charity Commission register for England and Wales, Scotland, or Northern Ireland as appropriate.
- `workplace-giving`: verify the payroll platform and charity selection inside the employer's official system.

## Safety & privacy

Medium financial risk. Do not share card, bank, ID, or tax details with unsolicited fundraisers, and never donate by gift card, wire, or crypto to a charity appeal.
