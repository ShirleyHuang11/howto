---
name: change-the-system-volume
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Raise, lower, or mute the device's main sound volume.

## Preconditions

- The device is on and outputting sound or ready to play sound.
- Speakers, headphones, or a Bluetooth audio device are connected if needed.

## Steps

1. **Find volume controls.** Use keyboard volume keys, side buttons, menu bar, taskbar, Control Center, or quick settings. → *Expect:* a volume slider or on-screen volume indicator appears.
2. **Adjust the level.** Move the slider or press volume up/down to the desired level. → *Expect:* the volume number or bar changes.
3. **Mute if needed.** Click or tap the speaker icon or mute button. → *Expect:* the icon shows muted and sound stops.
4. **Check the output device.** If sound is wrong or absent, open sound output settings and choose the intended device. → *Expect:* the selected speaker or headphones are listed as active.
5. **Test audio.** Play a short sound, video, or system test tone. → *Expect:* sound plays at the intended loudness or remains muted.

## Decision points

- No sound from expected speaker → change output device before raising volume further.
- App is quiet but system is loud → adjust the app's own volume or mixer.
- In a meeting or public place → mute before opening media.

## Failure modes & recovery

- **F1 Wrong output device:** detect sound comes from another speaker → select the correct output in sound settings.
- **F2 Volume keys control something else:** detect the on-screen indicator does not change system volume → use the system tray, menu bar, or settings slider.
- **F3 Still no sound:** detect test audio is silent → check mute, cable, Bluetooth connection, app volume, and output device.

## Verification

The system volume indicator shows the intended level or mute state, and test audio behaves accordingly.

## Variations

- `windows`: use taskbar sound icon, Settings > System > Sound, or volume mixer.
- `mac`: use Control Center, keyboard keys, or System Settings > Sound.
- `mobile-app`: use side buttons or quick settings; call volume and media volume may be separate.

## Safety & privacy

High volume can be uncomfortable or harmful through headphones. Lower volume before switching devices or playing unknown media in public.
