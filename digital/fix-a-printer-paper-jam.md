---
name: fix-a-printer-paper-jam
domain: digital
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min-30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

The jammed paper is removed without tearing rollers or sensors, and the printer is reset to print normally.

## Preconditions

- A printer showing a paper jam, misfeed, or carriage-blocked message.
- Enough light to see inside, clean hands, and no loose jewelry near moving parts.

## Steps

1. **Stop the print job.** Cancel the job from the computer or phone before touching the printer. → *Expect:* the queue stops sending new pages.
2. **Power off and unplug.** Turn the printer off, then unplug power so rollers cannot start while your hands are inside. → *Expect:* the display and status lights go dark.
3. **Open the designed access points.** Open the paper tray, rear door, duplexer, cartridge door, or automatic document feeder cover, using latches rather than prying panels. → *Expect:* the paper path is visible from at least one side.
4. **Pull paper with the paper path.** Grip the largest visible part of the sheet with both hands and pull slowly in the direction paper normally travels, not backward against the rollers. → *Expect:* the sheet slides out in one piece or exposes the next safe grip point.
5. **Remove loose scraps.** Use a flashlight to check corners, rollers, the rear door, and the output slot for torn pieces. → *Expect:* no scraps, labels, staples, or curled corners remain.
6. **Check the carriage path.** [BRANCH: inkjet | laser] Inkjet: slide the printhead carriage gently only if the manual allows it. Laser: leave hot fuser areas alone until cool. → *Expect:* no paper blocks the moving path.
7. **Reload paper flat.** Remove wrinkled sheets, square the stack, set guides snugly, and keep below the fill line. → *Expect:* the tray feeds one clean stack without bowed paper.
8. **Close and reset.** Close all covers, plug in, power on, and follow any on-screen clear-jam prompt. → *Expect:* the jam message clears or changes to a specific cover or tray warning.
9. **Print one test page.** Send a simple one-page print before resuming the full job. → *Expect:* one page feeds and exits without skewing or stopping.

## Decision points

- Paper is visible from both front and rear → pull from the side that follows the normal paper path with the least resistance.
- You feel firm resistance → stop pulling and open another access door to avoid ripping the sheet.
- Labels or photo paper were used → inspect extra carefully because adhesive scraps can stay on rollers.

## Failure modes & recovery

- **F1 Paper tears:** detect a torn sheet or missing corner, recover by unplugging again and removing every scrap with fingers or plastic tweezers.
- **F2 Jam message remains:** detect the same alert after restart, recover by reopening each door, reseating the tray, and checking the rear duplex unit.
- **F3 Repeated jams:** detect another jam within a few pages, recover by replacing damp or curled paper and cleaning feed rollers per the manual.
- **F4 Hot laser area:** detect heat warning labels or a hot fuser, recover by waiting 20 minutes before touching nearby paper.

## Verification

The printer completes a one-page test print with no jam, skew, grinding noise, or leftover jam message.

## Variations

- Automatic document feeder: open the feeder lid and pull originals in the feeder direction, then check for tiny torn corners near sensors.
- Rear-feed printers: the jam may clear best from the back because that is the normal path.
- Duplex printers: remove and reseat the duplexer, since a half-turned sheet often hides there.

## Safety & privacy

Unplug before reaching inside. Laser printers can have hot fusers, and jammed pages may contain private print content, so dispose of damaged pages appropriately.
