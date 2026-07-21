---
name: reset-a-gfci-outlet
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A tripped GFCI outlet is identified, reset, and tested so protected outlets work again without ignoring an active electrical fault.

## Preconditions

- Access to the affected outlet and nearby outlets in the same room or circuit.
- Dry hands and a dry floor.
- A small plug-in lamp, outlet tester, or device charger.
- No visible burn marks, melting, smoke, or buzzing at the outlet.

## Steps

1. **Unplug loads.** Remove appliances or chargers from the dead outlet and nearby protected outlets → *Expect:* nothing is drawing power from the affected receptacles.
2. **Check for obvious danger.** Look for water, scorching, cracked covers, or heat before touching buttons → *Expect:* the outlet face is intact, dry, and cool.
3. **Find the tripped GFCI.** Search bathrooms, kitchen counters, garage, basement, laundry, exterior, and nearby rooms for an outlet with TEST and RESET buttons → *Expect:* you locate the controlling GFCI or confirm none is visible.
4. **Press RESET firmly.** Push RESET until it clicks and stays in [BRANCH: button holds | button pops back out] → *Expect:* the button remains engaged if the fault is cleared.
5. **Test power.** Plug in a lamp or tester at the original dead outlet → *Expect:* the device powers on or the tester shows a normal pattern.
6. **Run the built-in test.** Press TEST on the GFCI, then confirm power shuts off at the protected outlet → *Expect:* the lamp or tester turns off.
7. **Reset again.** Press RESET after the test → *Expect:* power returns and the reset button stays latched.
8. **Reconnect loads one at a time.** Plug devices back in separately so a bad device can reveal itself → *Expect:* power remains on after each device is connected.

## Decision points

- RESET will not stay in → leave devices unplugged and treat it as a fault, wet outlet, failed GFCI, or upstream power issue.
- No GFCI is visible → check another room, garage, basement, exterior outlet, or the breaker panel.
- GFCI trips when one appliance is plugged in → stop using that appliance until it is inspected or replaced.
- Breaker also trips → do not keep resetting; call a qualified electrician.

## Failure modes & recovery

- **F1 Wrong GFCI:** detect no power restored, recover by checking other GFCIs on the same circuit path.
- **F2 Wet outlet:** detect recent splashes or outdoor rain exposure, recover by leaving it off until dry and inspected if needed.
- **F3 Failed reset mechanism:** detect a button that will not click or latch, recover by replacing the GFCI through a qualified person.
- **F4 Hidden upstream trip:** detect several outlets dead, recover by checking the breaker and upstream GFCIs.
- **F5 Recurring trip:** detect repeated trips with normal use, recover by unplugging loads and arranging electrical inspection.

## Verification

The GFCI TEST button cuts power, RESET restores power, and the original protected outlet powers a tester or lamp afterward.

## Variations

- Newer self-test GFCIs may show a status light that changes color when tripped.
- Older homes may protect multiple rooms from one GFCI in a bathroom, garage, or basement.
- Outdoor outlets may need an in-use weather cover to prevent nuisance trips.
- Some breakers are GFCI breakers with TEST buttons in the panel instead of at the outlet.

## Safety & privacy

Medium electrical risk. Do not reset a wet, hot, buzzing, or visibly damaged outlet. If the GFCI trips repeatedly, it is doing its job and should not be bypassed.
