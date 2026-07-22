---
name: restart-a-frozen-phone
domain: digital
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min-15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A frozen phone is restarted with a soft reset, preserving data and avoiding a factory reset.

## Preconditions

- The phone is charged enough to restart or is connected to a known-good charger.
- You can identify whether it is an iPhone or Android model.

## Steps

1. **Confirm it is frozen.** Try the power button, volume buttons, touch screen, and charging cable for a minute. → *Expect:* the phone either responds or remains stuck on the same screen.
2. **Avoid erase options.** Do not choose reset all content, factory reset, recovery erase, or wipe data. ⚠️ *Irreversible:* factory reset deletes local data unless a backup exists. → *Expect:* no erase confirmation screen is accepted.
3. **Use the iPhone button combo.** [BRANCH: iPhone with Face ID or iPhone 8 or later | older iPhone] Newer: press Volume Up, press Volume Down, then hold Side until the Apple logo appears. Older: hold the documented Home plus Side or Top combo. → *Expect:* the Apple logo appears.
4. **Use the Android button combo.** Hold Power for 20 to 30 seconds, or hold Power plus Volume Down for 10 to 20 seconds on models that require it. → *Expect:* the screen goes black or the maker logo appears.
5. **Wait through reboot.** Leave the phone alone for several minutes, especially after an update or low-battery crash. → *Expect:* the lock screen or startup screen appears.
6. **Unlock and check basics.** Enter the passcode after restart, then check touch, cellular, Wi-Fi, and battery level. → *Expect:* the phone responds normally.
7. **Charge and cool if needed.** If the phone froze while hot or nearly empty, charge it on a hard surface and remove the case temporarily. → *Expect:* battery and temperature stabilize.
8. **Update or uninstall the trigger app.** If the same app caused the freeze, update it or remove it after data is backed up. → *Expect:* the freeze does not recur immediately.

## Decision points

- Phone shows a low-battery icon → charge at least 15 minutes before deciding the restart failed.
- Phone is physically hot → cool it before repeated restart attempts.
- Phone enters recovery mode → exit without erase if possible, or seek device-specific support before wiping.

## Failure modes & recovery

- **F1 Button combo fails:** detect no logo after 30 seconds, recover by checking the model-specific combo and trying while connected to power.
- **F2 Boot loop:** detect repeated logo cycling, recover by charging, removing recent problem apps if it boots, or using official repair tools.
- **F3 Touch still dead:** detect buttons work but touch does not, recover by removing screen accessories and seeking hardware service if unchanged.
- **F4 Storage full freeze:** detect warnings after reboot, recover by deleting large backed-up media and clearing app caches.

## Verification

The phone reaches the lock screen, accepts the passcode, and responds to touch and buttons for several minutes.

## Variations

- iPhone: emergency SOS can share button combos, so release if the SOS countdown appears and restart with the correct sequence.
- Samsung and many Android phones: Power plus Volume Down is common for forced restart.
- Phones with removable batteries: remove the battery only if the maker designed it to be removable.

## Safety & privacy

A soft reset restarts the phone and should not erase data. Factory reset, wipe data, and recovery erase are different actions and should be treated as destructive.
