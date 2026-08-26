---
name: sign-up-for-selective-service
domain: government
subdomain: civic
locale: [generic, us]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You register with the US Selective Service System when required and keep proof of registration for financial aid, employment, immigration, or other eligibility checks.

## Preconditions

- Your full legal name, date of birth, address, and Social Security number if you have one.
- You are checking requirements for a person who is male and age 18 through 25, or approaching age 18.
- Internet access to the official Selective Service website or a paper registration option.

## Steps

1. **Confirm whether registration is required.** Review the Selective Service "Who Needs to Register" guidance for US citizens, immigrants, dual citizens, and people without an SSN. → *Expect:* you know whether registration is required, optional, already done, or unavailable due to age.
2. **Use the official registration channel.** Go to sss.gov and choose online registration, status check, or printable form as appropriate. → *Expect:* the page is the official Selective Service System site.
3. **Enter identifying information exactly.** Provide legal name, date of birth, address, and SSN if available. → *Expect:* the form accepts the entries without identity-format errors.
4. **Review the registration.** ⚠️ *Irreversible:* confirm name, birth date, and address before submitting because incorrect records can interfere with later verification. → *Expect:* the summary matches the person's identity.
5. **Submit the registration.** → *Expect:* the system displays or sends a registration acknowledgment.
6. **Save proof.** Record the Selective Service number if issued and save a PDF, screenshot, or confirmation email. → *Expect:* proof is stored with other important identity documents.
7. **Verify status after processing.** Use the Selective Service status check if confirmation is not immediate. → *Expect:* the record shows registered or gives a clear next action.

## Decision points

- No Social Security number → follow Selective Service instructions for registering without one, which may require mail or direct contact.
- Age 26 or older and not registered → you generally cannot newly register; request a status information letter if an agency asks about nonregistration.
- Already registered → print or save the verification instead of submitting a duplicate.
- Transgender or nonbinary applicant → follow current Selective Service rules based on sex assigned at birth and consult the agency guidance for the specific situation.

## Failure modes & recovery

- **F1 Online form cannot verify identity:** detect repeated submission errors → use the paper form or contact Selective Service during business hours.
- **F2 Duplicate record warning:** detect a message that registration already exists → use status verification and save the existing record.
- **F3 Missed age window:** detect that the person is already 26 → request a status information letter and respond to the benefit agency with supporting context.
- **F4 Address outdated:** detect mail going to an old address → update the address through Selective Service if still within the update window.

## Verification

Selective Service status shows the person as registered, or you have a registration acknowledgment or Selective Service number saved with the submission date.

## Variations

- `us`: almost all male US citizens and male immigrants ages 18 through 25 must register; late registrations are accepted only before the 26th birthday.
- `citizen abroad`: US citizens abroad can register online or through US embassy or consular instructions.
- `paper form`: registration cards are also available through some post offices and school-based processes.

## Safety & privacy

Medium risk because nonregistration can affect eligibility for some benefits and because the form uses identity data. Use only sss.gov or official paper forms, and keep proof without sharing the SSN unnecessarily.
