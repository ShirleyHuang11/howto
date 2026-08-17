---
name: pair-a-bluetooth-device
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Pair a Bluetooth accessory such as headphones, keyboard, mouse, speaker, or controller with your device.

## Preconditions

- Bluetooth is available on the computer, phone, or tablet.
- The accessory is charged or has working batteries.
- You know how to put the accessory in pairing mode.

## Steps

1. **Turn on Bluetooth.** Open Bluetooth settings and enable Bluetooth. → *Expect:* the device shows Bluetooth as on.
2. **Put the accessory in pairing mode.** Hold the pairing button or follow the accessory's pairing instructions. → *Expect:* a light flashes or the accessory announces pairing mode.
3. **Find the accessory.** In Bluetooth settings, wait for the accessory name to appear under available devices. → *Expect:* the accessory is listed.
4. **Select the accessory.** Click or tap the accessory name and choose `Pair`, `Connect`, or equivalent. → *Expect:* the device starts pairing or asks for a code.
5. **Confirm any code.** If a code appears, verify it matches on both devices or enter it as instructed. → *Expect:* pairing completes and the accessory shows connected.
6. **Test the accessory.** Play audio, type, move the pointer, or press controls depending on the device. → *Expect:* the accessory works with the paired device.

## Decision points

- Accessory is already paired elsewhere → disconnect it from the other device or reset pairing mode.
- A code appears unexpectedly → pair only if the accessory name and code match what you expect.
- Audio device connects but sound is elsewhere → choose it as the audio output device.

## Failure modes & recovery

- **F1 Accessory not listed:** detect it does not appear → move closer, recharge, restart pairing mode, or toggle Bluetooth off and on.
- **F2 Pairing fails:** detect an error or timeout → forget the accessory on both devices and pair again.
- **F3 Connected but not working:** detect no audio, typing, or pointer movement → select the accessory as output/input or restart it.

## Verification

Bluetooth settings show the accessory as connected, and the accessory performs its expected function.

## Variations

- `windows`: Settings > Bluetooth & devices > Add device.
- `mac`: System Settings > Bluetooth.
- `mobile-app`: iOS and Android list available accessories in Bluetooth settings.

## Safety & privacy

Pair only with accessories you recognize. Unknown Bluetooth devices can request access or create confusing input and audio behavior.
