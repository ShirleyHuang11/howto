---
name: use-a-hotel-safe
domain: travel
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Store travel valuables in a hotel room safe in a way that reduces casual theft and prevents leaving items behind at checkout.

## Preconditions

- The room safe opens and is physically attached or built into furniture.
- You have valuables that do not need to stay on your person.
- You can set your own code rather than using a default code.
- You understand the hotel may limit liability for room-safe losses.

## Steps

1. **Inspect the safe before use.** Open it, check for previous guests' items, loose hinges, low battery warnings, and a reset button. → *Expect:* the safe is empty, closes cleanly, and shows no obvious fault.
2. **Set your own code.** Choose a code you can remember but that is not your room number, birthday, passport year, or repeated digits. → *Expect:* the safe accepts the new code.
3. **Test before storing valuables.** Lock the empty safe, reopen it with the code, then lock it again. → *Expect:* the code works reliably while the safe is empty.
4. **Store the right items.** Put passport, spare card, extra cash, jewelry, backup phone, and travel documents inside; keep daily cash and one payment method with you. → *Expect:* critical spares are secured but you can still function outside the room.
5. **Avoid overloading or trapping essentials.** Do not jam the door or store medicine, only glasses, or the only room key if you may need them quickly. → *Expect:* the door closes without pressure and essentials remain accessible.
6. **Lock and verify.** Close the door, enter the code if required, tug the handle, and wait for the locked indicator. → *Expect:* the safe stays closed when pulled.
7. **Set a checkout reminder.** Put a phone alarm or packing-list item labeled hotel safe for checkout morning. → *Expect:* there is a reminder outside the safe.
8. **Empty it before final room sweep.** [BRANCH: normal checkout | code failure] remove all items during packing; if the code fails, call the front desk while still in the room. → *Expect:* the safe is empty before you leave the hotel.

## Decision points

- The safe is loose, broken, or uses a default code → ask the hotel for repair, another room, or front-desk safe storage.
- Items exceed casual-theft value → consider the front desk safe deposit process and receipt.
- You share the room → agree who knows the code and who checks the safe at checkout.
- You need the passport daily → store a copy in the safe and carry the passport as local rules require.

## Failure modes & recovery

- **F1 Forgotten code:** detect by repeated failed unlocks, recover by contacting the front desk with ID and staying present while it is opened.
- **F2 Dead battery:** detect by dim display or no keypad response, recover by asking staff for battery replacement or override.
- **F3 Items left behind:** detect by checkout reminder or post-checkout realization, recover by calling the hotel immediately with room number and item list.
- **F4 False sense of full security:** detect by assuming the safe covers all loss, recover by limiting stored value and checking hotel liability terms.

## Verification

The safe locks and unlocks with your code, contains only intended valuables during the stay, and is empty before you return the room key or leave checkout.

## Variations

- Safe with card swipe: use an unimportant card, not a primary payment card, if the safe supports it.
- Front-desk safe: request a receipt listing the envelope or deposit box identifier.
- Shared lodging: use a portable lock pouch if no trustworthy safe exists.

## Safety & privacy

Low risk, but passports, cards, and devices are high-value personal items. A room safe deters casual access; it is not a guarantee against staff override, theft, fire, or legal access.
