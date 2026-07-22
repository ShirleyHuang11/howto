---
name: program-a-thermostat
domain: housing
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min-30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A programmable thermostat follows a realistic heating or cooling schedule that matches daily routines while preserving comfort and saving energy.

## Preconditions

- You know the usual wake, leave, return, and sleep times for the home.
- You can access thermostat programming controls, the manual if needed, and the heating or cooling mode.
- If thermostat wiring is exposed, damaged, or the HVAC system behaves unexpectedly, stop and call an HVAC technician.

## Steps

1. **Identify system mode.** Set the thermostat to heat, cool, or auto according to the season and system. → *Expect:* the display shows the active mode.
2. **Open schedule settings.** Press schedule, program, menu, or the equivalent control. → *Expect:* weekday and time periods are editable.
3. **Choose schedule structure.** [BRANCH: 5-2 | 7-day | daily] use weekday-weekend, each-day, or identical daily scheduling based on routine. → *Expect:* the thermostat is ready for the right pattern.
4. **Set wake time and temperature.** Program the comfort temperature shortly before people wake. → *Expect:* the first period reflects morning comfort.
5. **Set away period.** Program a setback when the home is empty. → *Expect:* heating lowers or cooling rises during away hours.
6. **Set return period.** Program comfort to resume before people arrive home. → *Expect:* the house will recover before normal use.
7. **Set sleep period.** Program a nighttime temperature suitable for sleeping. → *Expect:* the overnight period is saved.
8. **Review hold settings.** Learn temporary hold versus permanent hold so the schedule is not accidentally disabled. → *Expect:* the display indicates schedule, hold, or resume clearly.
9. **Save and exit.** Confirm or done the schedule and return to the main screen. → *Expect:* the next scheduled period appears.
10. **Test a small change.** Temporarily adjust the setpoint, then press resume schedule. → *Expect:* the thermostat returns to programmed control.

## Decision points

- Heat pump system → avoid large setbacks unless the manual recommends them, because auxiliary heat can erase savings.
- Home occupied all day → use smaller setbacks focused on sleep comfort.
- Pets, plants, pipes, or humidity need limits → keep temperatures within safe ranges.
- Frequent manual holds → adjust the schedule rather than fighting it daily.

## Failure modes & recovery

- **F1 Schedule not running:** display says permanent hold, press run, resume, or cancel hold.
- **F2 Wrong day or time:** heating starts at odd times, correct clock, date, and AM or PM.
- **F3 Comfort poor:** house is cold or hot at return, start recovery earlier or reduce setback.
- **F4 System short cycles:** HVAC turns on and off rapidly, restore prior settings and call a technician if it continues.

## Verification

The thermostat main screen shows schedule or run mode, the next period matches the intended time and temperature, and temporary hold can be cancelled back to the schedule.

## Variations

- Smart thermostats: use app schedules, geofencing, and eco modes only after basic heating and cooling work correctly.
- Radiant heat: use smaller changes because floors recover slowly.
- Utility time-of-use plans: shift comfort recovery away from peak pricing if comfort allows.

## Safety & privacy

Low risk: thermostat settings affect comfort, energy cost, pets, humidity, and pipe-freeze risk. Smart thermostats may expose occupancy patterns, so review app privacy settings and shared household access.
