---
name: apply-for-a-child-passport
domain: government
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Submit a complete child passport application with proof of citizenship, parental relationship, consent, photo, and fees.

## Preconditions

- The child is eligible for the passport type requested.
- You have the child's proof of citizenship, proof of parental relationship, parent/guardian IDs, passport photo, completed unsigned application, and fee payments.
- Both parents or legal guardians can appear, or the absent-parent consent/court-order exception is documented.
- You know travel date and whether routine, expedited, or urgent service is needed.

## Steps

1. **Read the official child passport instructions.** Check age category, in-person requirement, parental consent rules, fees, and current processing times. → *Expect:* you know whether to use routine, expedited, or urgent service.
2. **Complete the application without signing.** Fill the official form online or in print, using the child's legal name, birth details, Social Security number if applicable, and parent information. → *Expect:* the form is complete but unsigned.
3. **Gather citizenship and relationship proof.** Prepare original or certified birth certificate, prior passport, consular report, adoption decree, or court order as applicable. → *Expect:* the documents prove both citizenship and parental relationship or list the missing proof.
4. **Prepare parent or guardian identification.** Bring government photo ID for each appearing parent/guardian and photocopies if required. → *Expect:* identity documents match the adults giving consent.
5. **Handle consent.** [BRANCH: both parents appear | one parent appears with notarized consent | one parent has sole authority | special family circumstance] Prepare the required consent form, notarization, court order, or statement. → *Expect:* the acceptance agent can document lawful consent.
6. **Get a compliant passport photo.** Use a recent color photo with correct size, background, face visibility, and no disallowed accessories. → *Expect:* the photo meets official requirements and is not visibly rejected.
7. **Book or choose an acceptance facility.** Use a post office, clerk, library, or passport agency appointment if required. → *Expect:* you have the location, time, and accepted payment methods.
8. **Submit in person.** The child and required parent/guardian appear, the agent witnesses the signature, reviews documents, and collects fees. ⚠️ *Irreversible:* fees are generally nonrefundable once accepted, so confirm documents, spelling, service speed, and mailing address first. → *Expect:* you receive an application receipt or tracking information.
9. **Track and receive the passport.** Monitor status after the posted delay and watch for separate mailings of passport book/card and returned originals. → *Expect:* the passport arrives and original documents are returned.

## Decision points

- Travel is within urgent-service windows → use the official passport agency urgent-travel process and bring itinerary proof.
- One parent cannot be reached → read the special-family-circumstances rule before appointment; unsupported explanations may be rejected.
- Child has a prior passport → renewal may still require in-person application for children.
- Name changed by adoption or court order → bring certified legal name-change documents.

## Failure modes & recovery

- **F1 Missing consent:** detect appointment rejection for absent parent/guardian → recover with notarized consent, court order, or the official exception statement.
- **F2 Photo rejected:** detect acceptance-agent refusal → recover by retaking the photo at the facility or nearby service.
- **F3 Original document unavailable:** detect lack of certified birth/adoption/citizenship proof → recover by ordering a certified copy before rebooking.
- **F4 Processing delay:** detect no status change past published timelines → recover by contacting passport support and requesting upgrade if travel is near.
- **F5 Name or birth date error:** detect incorrect printed passport → recover by using the official correction process before travel.

## Verification

The application is accepted with a receipt, and later the child has a passport whose name, birth date, sex marker, expiration date, and photo are correct.

## Variations

- `us`: children under 16 generally must apply in person with two-parent consent or a documented exception.
- `passport-card`: useful for limited land/sea travel where accepted, but not for international air travel.
- `urgent-travel`: appointment availability and proof requirements change; check official instructions close to travel.
- `non-us`: consent, citizenship proof, and child age cutoffs vary by country.

## Safety & privacy

Child passport applications expose sensitive identity and family-court information. Carry originals carefully, do not email scans unless the agency instructs it, and store the passport securely after delivery.
