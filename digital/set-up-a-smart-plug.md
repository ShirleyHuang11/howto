---
name: set-up-a-smart-plug
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min-25min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A smart plug is paired to its app, named clearly, connected to Wi-Fi, and running any schedule or away routine you choose.

## Preconditions

- A smart plug, phone, maker app account if required, and the home Wi-Fi password.
- The device you plan to control is within the plug's rated wattage and is safe to switch automatically.

## Steps

1. **Check the load rating.** Read the plug's amperage and wattage limits before plugging in lamps, fans, heaters, or appliances. → *Expect:* the planned device is below the rating.
2. **Install the maker app.** Download the official app named on the box or manual and sign in if required. → *Expect:* the app opens to an add-device flow.
3. **Plug in near the router.** Put the smart plug in a wall outlet for setup, avoiding power strips for the first pairing attempt. → *Expect:* the indicator light turns on or blinks.
4. **Put the plug in pairing mode.** Hold the button until the light blinks in the pattern the app requests. → *Expect:* the app can start scanning or asks for Wi-Fi details.
5. **Connect to the right Wi-Fi band.** [BRANCH: 2.4 GHz only | dual-band supported] Use 2.4 GHz for most smart plugs, or the listed band if the plug supports both. → *Expect:* the app reports successful Wi-Fi connection.
6. **Name the plug by purpose.** Use names such as `Living Room Lamp`, not `Plug 1`, especially if using voice assistants. → *Expect:* the app shows the clear name in the device list.
7. **Test manual control.** Turn the plug off and on from the app while watching the connected device. → *Expect:* the device power changes within a few seconds.
8. **Create a schedule or away routine.** Set on/off times, sunrise/sunset options, or randomized away mode only for suitable devices. → *Expect:* the schedule appears enabled with the correct days and time zone.
9. **Move to final outlet.** Place the plug where it will be used and test control again. → *Expect:* the app still shows online and controls the device.

## Decision points

- Device is a heater, iron, medical device, pump, or anything hazardous unattended → do not automate it with a basic smart plug.
- Pairing fails on a combined router SSID → temporarily use a 2.4 GHz network or move closer to the router.
- Voice assistant desired → link accounts after the plug works in its own app.

## Failure modes & recovery

- **F1 Pairing timeout:** detect app cannot find the plug, recover by resetting pairing mode, using 2.4 GHz Wi-Fi, and disabling VPN on the phone.
- **F2 Wrong time:** detect schedules fire early or late, recover by setting home location and time zone in the app.
- **F3 Plug offline:** detect app shows offline, recover by moving it closer to Wi-Fi or power cycling the outlet and plug.
- **F4 Overload warning:** detect heat, buzzing, tripped breaker, or app warning, recover by unplugging immediately and using a properly rated switch.

## Verification

The smart plug appears online, switches the connected device from the app, and shows the intended schedule or away routine enabled.

## Variations

- Matter plugs: pair through Apple Home, Google Home, Alexa, or SmartThings using the Matter QR code.
- Outdoor plugs: use weather-rated outlets and outdoor-rated plugs only.
- Energy-monitoring plugs: calibrate or label the device before trusting usage reports.

## Safety & privacy

Smart plugs can reveal occupancy patterns through schedules and cloud logs. Do not automate heat-producing or safety-critical devices unless the plug and device are explicitly rated for that use.
