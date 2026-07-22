---
name: reset-a-boiler
domain: housing
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 10min-20min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A boiler in lockout is checked once, reset according to its manual, and either returns to normal operation or is left safely for an engineer.

## Preconditions

- You can access the boiler controls, pressure gauge, thermostat, and user manual or front-panel instructions.
- You are not smelling gas, seeing water near electrics, or seeing scorch marks.
- Gas, combustion, and boiler faults are high risk; if you smell gas, suspect carbon monoxide, see leaks, or the lockout repeats, stop and call a licensed heating engineer.

## Steps

1. **Check for immediate danger.** Look for gas smell, carbon monoxide alarm, scorch marks, leaks, or unusual noise. → *Expect:* no emergency signs are present before touching controls.
2. **Confirm demand.** Set the thermostat to call for heat or hot water. → *Expect:* the boiler has a reason to run.
3. **Read the display.** Note any lockout code, fault light pattern, or pressure reading before resetting. → *Expect:* you have information for the engineer if needed.
4. **Check pressure.** Compare the gauge to the normal cold range in the manual, often around 1 to 1.5 bar for many sealed systems. → *Expect:* pressure is within the manual's safe range or clearly abnormal.
5. **Do not refill blindly.** [BRANCH: pressure normal | pressure low] if normal, continue; if low, follow the manual only if you know the filling loop procedure, otherwise call an engineer. → *Expect:* no valve is opened without certainty.
6. **Press reset once.** Hold or press the reset button exactly as the label or manual states. → *Expect:* the lockout light clears or the boiler begins an ignition sequence.
7. **Observe ignition.** Stand nearby without opening sealed covers and listen for normal startup. → *Expect:* the boiler runs quietly or shows a new fault code.
8. **Wait for heat.** Allow several minutes for radiators or hot water pipes to warm. → *Expect:* heat output begins if the reset succeeded.
9. **Watch the pressure again.** Check that pressure stays in range while heating starts. → *Expect:* the gauge does not spike or fall rapidly.
10. **Stop after one failed reset.** If lockout returns, record the code and leave the boiler off if the manual says to. → *Expect:* you avoid repeated unsafe ignition attempts.

## Decision points

- Gas smell or carbon monoxide alarm → leave the area, avoid switches, call emergency gas services or local emergency number.
- Repeated lockout after one reset → call a licensed heating engineer.
- Pressure too high, too low, or changing fast → do not keep resetting; call an engineer.
- User manual forbids reset for the displayed code → follow the manual and stop.

## Failure modes & recovery

- **F1 Reset does nothing:** display stays locked out, record the code and call a heating engineer.
- **F2 Pressure abnormal:** gauge is outside the manual range, stop and get professional help unless the manual gives a user-safe correction you understand.
- **F3 Heat starts then stops:** boiler relocks within minutes, stop repeated resets and call an engineer.
- **F4 Leak appears:** water drips from boiler or pipework, turn off according to the manual and call for service.

## Verification

The boiler completes one reset, stays out of lockout, shows pressure within the manual's normal range, and supplies heat or hot water for at least ten minutes.

## Variations

- Combination boilers: hot water demand may be easier to test than central heating.
- Older boilers: pilot-light procedures may be separate and should follow the appliance label.
- Rental housing: report lockouts to the landlord or building manager as required.

## Safety & privacy

High risk: boilers involve gas, combustion, pressure, hot water, and electricity. Never remove sealed covers, never repeat resets to force ignition, and call a licensed heating engineer for gas smell, lockout codes, leaks, pressure faults, or carbon monoxide concerns.
