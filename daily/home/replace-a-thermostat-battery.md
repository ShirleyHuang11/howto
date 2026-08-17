---
name: replace-a-thermostat-battery
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min-10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

The thermostat batteries are replaced and the display and HVAC commands work normally.

## Preconditions

- You have fresh batteries in the type marked on the thermostat.
- You can remove the thermostat faceplate without pulling wires from the wall plate.
- Call HVAC service if the display stays blank with new batteries or wires detach from terminals.

## Steps

1. **Set the system off.** Move the thermostat mode to Off before opening the faceplate. → *Expect:* heating and cooling calls stop.
2. **Open the battery area.** Slide out the battery tray or pull the faceplate straight from the wall plate. → *Expect:* batteries and polarity marks are visible.
3. **Remove old batteries.** Take out every battery and check for corrosion. → *Expect:* the contacts are clean and intact.
4. **Install new batteries.** Match plus and minus ends to the compartment marks. → *Expect:* the batteries sit firmly in the holder.
5. **Reattach the faceplate.** Align pins and press the thermostat back onto the wall plate. → *Expect:* the faceplate sits flush without bent pins.
6. **Restore settings.** Set the date, time, mode, and schedule if they were lost. → *Expect:* the display shows normal room temperature and settings.
7. **Test a call.** Set heat or cool a few degrees beyond room temperature, then return to normal. → *Expect:* the system responds, then stops when set back.

## Decision points

- Batteries show corrosion → clean light residue with the thermostat removed; replace the thermostat if contacts are damaged.
- Faceplate resists removal → look for a latch or manual instead of prying.
- HVAC does not respond after the display returns → check breaker and furnace switch, then call service.

## Failure modes & recovery

- **F1 Blank display:** no screen after new batteries → recheck polarity, try a second fresh set, and reseat the faceplate.
- **F2 Lost schedule:** program resets → re-enter the schedule from notes or use a temporary hold.
- **F3 Loose wire:** a wire pulls free → turn system power off and call HVAC service if terminal labeling is unclear.

## Verification

The thermostat display is readable, low-battery warning is gone, and a heat or cool test command starts and stops the HVAC system correctly.

## Variations

- Hardwired thermostats: batteries may only preserve memory during outages.
- Smart thermostats: some use rechargeable internal batteries and require HVAC power troubleshooting instead.

## Safety & privacy

Low risk: thermostat wires are low voltage, but shorting them can damage controls. Do not let loose wires touch, and recycle old batteries properly.
