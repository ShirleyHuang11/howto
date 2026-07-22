---
name: change-a-door-lock
domain: housing
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Replace a door lock or cylinder so the door latches, locks, unlocks, and closes securely with the new keys.

## Preconditions

- You are allowed to change the lock or have owner or landlord permission.
- You know the existing lock type: cylinder, deadbolt, knob lock, mortise, or multipoint.
- You have the replacement lock, screwdriver, measuring tape, and all supplied screws and keys.
- The door and frame are structurally sound enough to hold the lock.

## Steps

1. **Identify and measure the lock.** Measure cylinder length, backset, latch size, door thickness, and screw spacing as applicable. → *Expect:* the replacement matches the door before removal begins.
2. **Open the door and keep it open.** Work with the door open so a mistake does not lock you out. → *Expect:* both sides of the lock are reachable.
3. **Remove the old hardware.** Unscrew the interior plate, knobs or handles, cylinder retaining screw, latch, and strike parts as needed. → *Expect:* the old lock comes out without damaging the door edge.
4. **Fit the new latch or cylinder.** Insert the replacement in the same orientation and fasten it loosely at first. → *Expect:* parts sit flush without forcing.
5. **Install handles, thumb turn, or deadbolt body.** Align spindles and screws, then tighten evenly. → *Expect:* the handle or bolt moves freely.
6. **Fit or adjust the strike plate.** Close the door gently and align the latch or deadbolt with the frame opening. → *Expect:* the bolt enters the strike without scraping or lifting the door.
7. **Test with every key.** Try lock, unlock, latch, and deadbolt operation from inside and outside while the door remains open. → *Expect:* all keys work smoothly.
8. **Test closed operation.** Close the door and repeat locking and unlocking from both sides. [BRANCH: smooth | binding] keep or adjust the strike, screws, or latch position. → *Expect:* the door secures without slamming.
9. **Store spare keys deliberately.** Label key copies without writing the address and give copies only to approved people. → *Expect:* access is controlled and documented.

## Decision points

- Rental property → ask before changing locks and provide keys if the lease requires it.
- Multipoint or high-security door → use a compatible cylinder and avoid altering the mechanism.
- Deadbolt does not extend fully → adjust the strike before relying on the lock.
- Exterior door has no deadbolt → consider adding one if permitted and structurally feasible.

## Failure modes & recovery

- **F1 Replacement does not fit:** detect mismatched length, backset, or screw holes → reinstall the old lock and buy the correct size.
- **F2 Door locks but will not unlock smoothly:** detect binding or stuck key → loosen screws, realign, and test open before testing closed.
- **F3 Latch misses strike:** detect rattling or no catch → move or shim the strike plate.
- **F4 Key works only one side:** detect cylinder orientation error → remove and reinstall in the correct direction.
- **F5 Door frame is weak:** detect split wood or loose screws → repair frame or call a locksmith before relying on it.

## Verification

With the door open and then closed, every new key locks and unlocks the latch and deadbolt smoothly from the intended sides, and the bolt fully enters the strike.

## Variations

- `euro-cylinder`: measure each side from the center screw to avoid a protruding cylinder.
- `us-deadbolt`: match backset and door bore size before buying.
- `mortise-lock`: replacement often requires exact case dimensions.
- `shared-entry`: do not change common-entry locks without formal approval.

## Safety & privacy

Work with the door open to avoid lockout. Do not leave old keys in circulation if the goal is access control. Medium risk comes from lockout, lease breach, weak installation, and personal security if the lock fails.
