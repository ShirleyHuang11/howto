---
name: connect-a-second-monitor
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

Connect and configure a second monitor for extending or mirroring your screen.

## Preconditions

- You have a monitor, power cable, and compatible video cable or adapter.
- Your computer is powered on and unlocked.

## Steps

1. **Connect power.** Plug the monitor into power and turn it on. → *Expect:* the monitor power light turns on.
2. **Connect video.** Plug HDMI, DisplayPort, USB-C, Thunderbolt, VGA, or an adapter into the monitor and computer. → *Expect:* the monitor detects a signal or the computer shows a display change.
3. **Select monitor input.** Use the monitor buttons to choose the input matching the cable. → *Expect:* the monitor shows the computer image or a waiting-for-signal message on the right input.
4. **Open display settings.** [BRANCH: Windows | Mac] Windows: Settings > System > Display; Mac: System Settings > Displays. → *Expect:* two displays are shown.
5. **Choose layout.** Select extend, mirror, duplicate, or use as main display. → *Expect:* windows move according to the chosen layout.
6. **Arrange displays.** Drag display thumbnails to match their physical positions. → *Expect:* the pointer crosses between screens in the expected direction.
7. **Set resolution or scaling.** Choose recommended settings for each display. → *Expect:* both screens look sharp and readable.

## Decision points

- Presenting to others → mirror displays if everyone should see the same content.
- Working with more space → extend displays and arrange them physically.
- Monitor says no signal → check input, cable direction, adapter support, and computer port.

## Failure modes & recovery

- **F1 Monitor not detected:** detect only one display in settings → reseat cables, change input, try another port, then use Detect.
- **F2 Pointer moves wrong direction:** detect the cursor exits the wrong screen edge → rearrange display thumbnails.
- **F3 Image looks poor:** detect blur, stretching, or wrong size → choose recommended resolution and refresh rate.

## Verification

Both displays are visible in display settings, and the pointer or mirrored image behaves according to the selected layout.

## Variations

- `windows`: use `Windows+P` for quick Project options.
- `mac`: use Displays settings to arrange, mirror, or set the main display.
- `usb-c`: some cables charge only and do not carry video; use a video-capable cable.

## Safety & privacy

When mirroring or presenting, the second monitor can expose notifications, private tabs, chats, or documents. Hide sensitive content before connecting in public or shared rooms.
