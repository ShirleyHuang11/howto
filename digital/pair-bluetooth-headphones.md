---
name: pair-bluetooth-headphones
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your Bluetooth headphones are paired with the intended phone, computer, tablet, or TV and play audio reliably from that device.

## Preconditions

- Headphones with enough battery and the device you want to pair them with.
- Bluetooth enabled on the phone, computer, tablet, or TV.

## Steps

1. **Charge and reset the obvious state.** Put the headphones near the device, charge them if uncertain, and turn them off and back on. → *Expect:* the headphones power on and announce or show battery.
2. **Enter pairing mode.** Hold the Bluetooth, power, or case button until the light flashes or the voice prompt says pairing. For earbuds, the case button often matters. → *Expect:* the headphones are discoverable, usually with a blinking blue or white light.
3. **Open Bluetooth settings on the device.** [BRANCH: phone | computer | TV] go to Bluetooth or connected devices and start scanning if needed. → *Expect:* the headphones appear by model name or brand.
4. **Select the headphones.** Tap or click the correct name and approve pairing prompts. Ignore duplicate low-energy entries unless the manual says otherwise. → *Expect:* the device reports connected for audio.
5. **Play a test sound.** Start music, a video, or the system test sound and raise volume on both the device and headphones. → *Expect:* sound comes through the headphones.
6. **Handle multi-device switching.** If the headphones connect to an old phone or laptop instead, pause Bluetooth there or disconnect them from that device. → *Expect:* the intended device becomes the active audio source.
7. **Check call microphone if needed.** Make a test recording or call, then choose the headphone mic in app settings if available. → *Expect:* both playback and microphone work for the intended app.
8. **Use forget-and-repair if unstable.** Remove the headphones from Bluetooth settings on the device, reset pairing mode, and pair again. → *Expect:* the device creates a fresh trusted pairing.

## Decision points

- Headphones do not appear → confirm pairing mode, not just power-on mode.
- Two devices fight for the connection → disconnect or forget the headphones on the device you are not using.
- TV pairing fails → some TVs only support Bluetooth audio on specific menus or require a transmitter.
- Need low latency for gaming or video editing → Bluetooth may lag; wired or low-latency adapters can be better.

## Failure modes & recovery

- **F1 Not discoverable:** detect: the headphones never appear in scanning, recover: hold the pairing button longer, charge them, or check the manual for reset.
- **F2 Paired but no sound:** detect: device shows connected but speakers play instead, recover: choose the headphones as the output device and raise both volume controls.
- **F3 Connects to the wrong device:** detect: audio starts on an old phone or laptop, recover: disconnect there or disable Bluetooth temporarily.
- **F4 One earbud silent:** detect: only one side plays, recover: put both earbuds in the case, close it, reopen, then pair again.
- **F5 Choppy audio:** detect: dropouts occur near other electronics or at distance, recover: move closer, reduce obstacles, and disconnect unused Bluetooth devices.

## Verification

The intended device lists the headphones as connected for audio, test playback is audible through them, and any needed microphone test succeeds.

## Variations

- `ios`: Open Settings, Bluetooth, then select the headphones under Other Devices.
- `android`: Open Settings, Connected devices, Pair new device; exact labels vary by manufacturer.
- `windows`: Use Settings, Bluetooth & devices, Add device, Bluetooth.
- `macos`: Use System Settings, Bluetooth, then Connect beside the headphone name.

## Safety & privacy

Bluetooth range is limited but not private by magic. Pair only your own headphones, avoid approving unknown pairing requests, and keep volume at a safe level before playing test audio.
