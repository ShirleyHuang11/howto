---
name: collect-and-sort-mail
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [mailbox, envelopes, packages, magazines, recycling-bin, shredder, mail-tray]
affordances: [grasp, open-door, close-door, carry, sort, place, tear]
workspace: household-entry
safety: {hot_surfaces: false, sharp_objects: false, fragile: [packages], human_proximity: continue}
---

## Goal

All mail is retrieved from the box, sorted by recipient and class, junk is safely diverted, and each remaining piece sits in its recipient's known spot with nothing left in transit.

## Preconditions

- Access to the mailbox (key for locking cluster boxes; know which slot is yours).
- An agreed per-recipient landing spot in the home (tray, shelf slot, or desk).
- A recycling bin and, for anything bearing personal data, a shredder or a tear-and-split routine.

## Steps

1. **Retrieve everything from the box.** Open the box, take all contents including flyers wedged at the back, and check for a package slip or an overflow parcel below or beside the box. Close and (if locking) relock the door. → *Expect:* box visibly empty, door shut, key back in pocket before walking away.
2. **Carry it all inside in one stack.** Sort at a table, not standing at the box: wind and one-handed sorting at the box is how checks end up in the hedge. → *Expect:* full stack on a flat surface indoors.
3. **First pass: sort by recipient.** Deal the stack into one pile per person in the household, plus a pile for former residents or wrong addresses. Check the name line, not just the surname, in shared households. → *Expect:* every piece in exactly one pile; the misdelivered pile set apart.
4. **Second pass: sort each recipient's pile by class.** [BRANCH: action mail (bills, official notices, anything with a deadline) | personal correspondence | periodicals and catalogs | junk] The envelope tells you: window envelopes and government or bank return addresses are action mail; bulk-rate markings and "resident" addressing are junk. → *Expect:* each pile split into at most four sub-stacks.
5. **Divert the junk stream immediately.** Plain unaddressed flyers go straight to recycling. Anything showing a name plus address, and especially prefilled credit or loan offers, goes to the shredder pile, never whole into the bin. ⚠️ *Irreversible:* shredding: confirm a piece is truly junk before it enters the shred pile; real notices in bulk envelopes exist, so open anything ambiguous first. → *Expect:* junk gone from the sorted piles; shred pile contains only confirmed junk with personal data.
6. **Handle the misdelivered pile.** Neighbor's mail: hand-deliver or leave in their box. Former residents: mark "not at this address, return to sender" and put it back in outgoing mail; do not open it (opening others' mail is illegal in most locales) and do not bin it. → *Expect:* misdelivered pile empty by end of task or staged in outgoing mail.
7. **Deliver each pile to its recipient's spot.** Action mail on top of each stack, deadline side up. Tell present recipients about anything that looks urgent. → *Expect:* every landing spot holds only its owner's mail; your own action mail is in your workflow, not back in the tray.
8. **Run the shredder.** Shred the confirmed-junk pile now; a "shred later" pile becomes a data-breach drawer. → *Expect:* shred pile empty, shreds in the bin.

## Decision points

- Package too large for the box or a delivery slip instead of a parcel → follow the slip's pickup instructions the same day; carrier hold windows lapse.
- Official-looking envelope for a household member who is away long-term → store it flat in their spot and message them a photo of the envelope front; do not open it.
- Mail volume shows days of buildup (after travel) → sort by class first across all recipients to catch deadlines, then split by person.

## Failure modes & recovery

- **F1 A real bill was nearly shredded:** detected by weight or a window glimpse mid-tear → stop, open every ambiguous piece before it enters the shred pile; bulk-rate postage with a window envelope is the classic disguise.
- **F2 Mail for the household keeps landing in one undifferentiated heap:** the landing spots are not agreed or not labeled → label the tray slots by name once; the sorting habit follows the furniture.
- **F3 Box key jams or the box will not relock:** do not force a cluster-box lock → note the box number and report it to the carrier or building manager; take all mail with you rather than leaving it in an unlockable box.
- **F4 Damp or damaged mail:** wet envelopes tear when opened → let them dry flat first, then open by slitting a dry edge.

## Verification

The mailbox is empty and locked, every retrieved piece is either in its recipient's spot, in outgoing mail marked return-to-sender, recycled, or shredded, and no stack remains on the sorting table. Anyone in the household can find their mail without asking.

## Variations

- Locking cluster boxes and PO boxes: retrieval requires the key trip; outgoing return-to-sender goes in the outgoing slot, not back in your own box.
- Door-slot mail: no box to lock; add a floor-side basket so mail is not stepped on, and sort from there.
- Buildings with a mailroom: package pickup is a separate signed step; the sorting recipe applies from the mailroom counter onward.

## Safety & privacy

Medium risk, driven by identity exposure rather than physical hazard: names, addresses, account numbers, and prefilled credit offers in the junk stream are exactly what mail-based identity theft uses, so shred rather than bin them. Do not open mail addressed to others, and never leave sorted action mail in view of an open door or window.
