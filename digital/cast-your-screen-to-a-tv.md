---
name: cast-your-screen-to-a-tv
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

Your phone, tablet, or computer displays content on a TV or streaming device, and you can stop casting when finished.

## Preconditions

- A TV or streaming device that supports Chromecast, Google Cast, AirPlay, Miracast, or screen mirroring.
- The casting device and TV are on the same Wi-Fi network unless the product supports direct pairing.

## Steps

1. **Put both devices on the same Wi-Fi.** Check the TV or streaming device network and the phone or computer network. Guest networks may block discovery. → *Expect:* both devices use the same normal home or room Wi-Fi.
2. **Open the content or screen-mirroring control.** [BRANCH: cast icon in an app | AirPlay | system screen mirror] use the app's Cast icon for YouTube or streaming apps, AirPlay for Apple devices, or system mirroring for the whole screen. → *Expect:* a device list appears.
3. **Choose the correct TV.** Select the room name or streaming device, then enter any code shown on the TV if prompted. → *Expect:* the TV changes to the cast session or mirrored screen.
4. **Confirm audio output.** Play a short clip and check whether sound comes from the TV, receiver, or phone. → *Expect:* audio comes from the expected speakers.
5. **Adjust orientation and privacy.** For full-screen mirroring, close private apps and notifications; rotate the phone if landscape content matters. → *Expect:* the TV shows only content you intend others to see.
6. **Expect some latency.** Use casting for video, slides, photos, and casual browsing. Avoid it for precise gaming or fast cursor work unless latency is acceptable. → *Expect:* video may lag slightly behind the device.
7. **Stop casting deliberately.** Tap the Cast icon, AirPlay control, or Screen Mirroring control, then choose Stop, Disconnect, or the device name again. → *Expect:* the TV returns to its previous app or home screen.

## Decision points

- App has a Cast icon → prefer it over whole-screen mirroring because it is cleaner and often saves battery.
- Apple device to Apple TV or AirPlay TV → use AirPlay or Screen Mirroring from Control Center.
- Windows laptop to compatible TV → use Cast or Wireless Display if the TV supports Miracast.
- Hotel or office Wi-Fi → device discovery may be blocked; use HDMI if available.

## Failure modes & recovery

- **F1 TV does not appear:** detect: device list is empty or missing the TV, recover: put both devices on the same Wi-Fi, leave guest Wi-Fi, and restart the TV app or streamer.
- **F2 Code prompt fails:** detect: TV code is rejected or expires, recover: cancel and start casting again with a fresh code.
- **F3 Video plays but no audio:** detect: TV image works but sound comes from the phone or nowhere, recover: check app volume, TV input volume, and audio output settings.
- **F4 Lag is too high:** detect: cursor, game, or call is delayed, recover: switch to app casting, move closer to Wi-Fi, or use HDMI.
- **F5 Private notifications appear:** detect: messages or alerts show on TV, recover: enable Do Not Disturb and restart mirroring.

## Verification

The selected TV shows the intended content, audio plays from the expected output, and the device can disconnect the session on command.

## Variations

- `chromecast`: The Cast icon sends media to the TV while the phone acts mostly as a remote.
- `airplay`: iPhone, iPad, and Mac use AirPlay controls and may ask for a one-time TV code.
- `roku`: Casting support depends on app and settings; screen mirroring may need to be enabled.
- `hdmi`: A cable avoids Wi-Fi discovery problems and latency, but may require an adapter.

## Safety & privacy

Screen mirroring can expose notifications, tabs, passwords, and messages to everyone in the room. Stop casting before opening private apps, and verify the TV is disconnected before walking away.
