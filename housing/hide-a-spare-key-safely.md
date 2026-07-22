---
name: hide-a-spare-key-safely
domain: housing
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Create an emergency entry option without leaving a spare key in an obvious place that compromises the home.

## Preconditions

- You have permission to duplicate and store the key.
- You know who should be able to access the home in an emergency.
- You have a lockbox, trusted neighbor, trusted local contact, or digital access option.
- You can identify whether the lock uses restricted, tagged, or landlord-controlled keys.

## Steps

1. **Reject obvious hiding places.** ⚠️ *Irreversible:* do not leave a key under a mat, planter, fake rock, mailbox, door ledge, car, or nearby loose brick because discovery can compromise the home immediately. → *Expect:* no spare key is stored in a predictable spot.
2. **Choose a safer method.** [BRANCH: lockbox | trusted person | digital alternative] pick the option that fits your access needs and risk. → *Expect:* the spare is protected by a person, code, or access system.
3. **Use a rated lockbox if hiding on site.** Choose a weather-resistant, combination or keyed lockbox with mounting hardware. → *Expect:* the key is not loose or visible.
4. **Mount the lockbox discreetly.** Place it away from the front door sightline and attach it to solid structure where allowed. → *Expect:* casual visitors do not notice it.
5. **Set and protect the code.** Use a non-obvious code and share it only when needed. → *Expect:* access can be granted without permanent key exposure.
6. **Use a trusted neighbor or contact.** Give one labeled-without-address key to someone reliable and nearby. → *Expect:* emergency access does not depend on a hidden object.
7. **Consider digital access.** Use a smart lock guest code, garage keypad, or building-approved access method when appropriate. → *Expect:* access can be logged and revoked.
8. **Test the recovery path.** Lock yourself out only in a controlled way with phone and backup contact available. → *Expect:* the spare method actually opens the door.
9. **Review after changes.** Update or retrieve spares after roommate changes, contractor access, breakups, or lost-code events. → *Expect:* old access paths are closed.

## Decision points

- Rental key cannot be copied → ask landlord for the approved lockout process.
- High-crime or visible-entry home → prefer trusted person or monitored smart access over outdoor storage.
- Frequent guest access needed → use expiring smart codes rather than a shared physical spare.
- Elderly or medical access need → coordinate with emergency contacts and local rules.

## Failure modes & recovery

- **F1 Key hidden in obvious spot:** detect common hiding location → remove it immediately and change locks if exposure is suspected.
- **F2 Lockbox code shared too widely:** detect unknown access or many recipients → change code and consider rekeying.
- **F3 Trusted person moves away:** detect unavailable contact → retrieve or replace the spare.
- **F4 Spare key corrodes or jams:** detect failed test → replace the key and weatherproof storage.
- **F5 Digital access fails:** detect dead battery, outage, or app lockout → keep a physical backup path.

## Verification

There is no spare in an obvious hiding place, and the chosen lockbox, trusted-person, or digital backup method has been tested and can be revoked or recovered.

## Variations

- `apartment`: building rules may ban hallway lockboxes.
- `short-term-rental`: use a managed lockbox or smart code process with code rotation.
- `shared-house`: track who has keys and collect them when residents leave.
- `remote-property`: use two backup methods because a trusted neighbor may not be nearby.

## Safety & privacy

A hidden key can turn a lockout solution into an easy entry path. Avoid address labels, predictable codes, and public-facing lockboxes. Medium risk comes from burglary, stalking, and unauthorized access by former guests or residents.
