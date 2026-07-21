---
name: reset-a-wifi-router
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Restore a home internet connection by using the right router reset method without accidentally erasing network settings.

## Preconditions

- You can physically reach the modem, router, or combined gateway.
- You know whether you want a temporary power-cycle or a factory reset.
- The router label, ISP account info, or admin login is available if a factory reset is required.

## Steps

1. **Identify the devices.** Find the modem, router, or combined gateway and note which cables go where. → *Expect:* you can tell the power cable from Ethernet or coax/fiber cables.
2. **Choose reset type.** [BRANCH: power-cycle for normal outage | factory reset for forgotten settings or bad configuration] use power-cycle first for most problems. → *Expect:* you know whether settings will be preserved.
3. **Power off cleanly.** Unplug the power from the router and modem, or the combined gateway. → *Expect:* lights turn off within a few seconds.
4. **Wait 30 seconds.** Leave power disconnected long enough for capacitors and sessions to clear. → *Expect:* the devices remain fully dark.
5. **Reconnect modem first.** Plug in the modem or gateway and wait for internet, online, or WAN lights to stabilize. → *Expect:* the service light becomes steady or follows the normal ready pattern.
6. **Reconnect router second.** If separate, plug in the router after the modem is ready. → *Expect:* Wi-Fi lights begin blinking and then settle.
7. **Wait before reconnecting.** Give devices 3 to 5 minutes before judging the result. → *Expect:* your phone or laptop sees the Wi-Fi network again.
8. **Test internet.** Connect to Wi-Fi and open a new website or run a speed test. → *Expect:* pages load without captive portal or DNS errors.
9. **Factory reset only if needed.** Hold the recessed reset button for the manual's required time, often 10 to 15 seconds. ⚠️ *Irreversible:* factory reset erases Wi-Fi name, password, and custom settings; confirm you can reconfigure them first. → *Expect:* lights flash or the router reboots into default settings.
10. **Call the ISP if service stays down.** Contact the provider when modem online lights never stabilize or the outage affects multiple devices. → *Expect:* the ISP can check line status, outages, and provisioning.

## Decision points

- Only one device has trouble → restart that device before resetting network hardware.
- Modem online light stays off after 10 minutes → suspect ISP line or account issue.
- You rent ISP equipment → use the ISP app or support instructions before a factory reset.

## Failure modes & recovery

- **F1 Wrong reset used:** detect missing custom Wi-Fi name after button reset, recover by logging in with default credentials and reconfiguring.
- **F2 No modem sync:** detect blinking online light that never steadies, recover by checking coax/fiber and calling the ISP.
- **F3 Wi-Fi missing:** detect no network name after router reboot, recover by checking router power and waiting another 5 minutes.
- **F4 Devices will not reconnect:** detect saved-password failures, recover by forgetting the network and joining with the current password.

## Verification

At least one device connects to the Wi-Fi network and loads a fresh external website after the router finishes restarting.

## Variations

- `mesh-system`: power-cycle the main node first, then satellites after the main node is online.
- `router-app`: some routers provide a restart button in the app that preserves settings like a power-cycle.

## Safety & privacy

Medium risk because a factory reset can expose a default Wi-Fi name and erase security settings. Use a strong Wi-Fi password after any factory reset and do not share ISP account details unnecessarily.
