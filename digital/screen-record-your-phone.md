---
name: screen-record-your-phone
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You record a short phone screen video with the right audio setting, stop it cleanly, trim it, and confirm it is safe to share.

## Preconditions

- An iPhone or Android phone with screen recording available in quick controls.
- Enough storage for a video, especially if recording more than a minute.

## Steps

1. **Add the screen-recording control if missing.** On iPhone, add Screen Recording in Control Center settings; on Android, edit Quick Settings and add Screen Record if it is not already visible. → *Expect:* the recording tile or button is available from quick controls.
2. **Prepare the screen.** Close private apps, clear notifications, and open the app or page you need to show. → *Expect:* only intended content is visible.
3. **Choose the audio setting.** [BRANCH: no audio | device audio | microphone] use no audio for visual bugs, device audio for playback issues, or microphone when explaining steps aloud. → *Expect:* the recorder shows the selected audio mode before starting.
4. **Start recording.** Tap the screen-recording control, confirm any privacy prompt, and wait for the countdown. → *Expect:* a red status indicator, timer, or recording icon appears.
5. **Perform the action slowly.** Reproduce the issue or demonstrate the task with pauses between taps so the viewer can follow. → *Expect:* the important sequence is captured once without rushing.
6. **Stop the recording.** Tap the red status bar, notification, or quick setting, then confirm Stop if asked. → *Expect:* the phone saves the video to Photos, Gallery, or Movies.
7. **Trim the start and end.** Open the video editor and remove countdown time, accidental swipes, and idle ending. → *Expect:* the saved clip starts near the useful action and ends after the result.
8. **Check size and privacy before sending.** Watch the clip, listen if audio was recorded, and compress or shorten if the file is too large. → *Expect:* the clip is understandable, shareable, and does not expose avoidable private details.

## Decision points

- Recording a bug for support → include the app version or error message if it is safe to show.
- Recording payment, health, school, or work content → use the shortest clip and redact or avoid sensitive screens.
- Need taps to be visible → enable show taps on Android developer options only if you understand how to turn it off later.
- Audio not needed → leave microphone off to avoid capturing room conversations.

## Failure modes & recovery

- **F1 Screen Record tile is missing:** detect: quick controls do not show it, recover: edit Control Center or Quick Settings and add it.
- **F2 App blocks recording:** detect: saved video is black or the app warns recording is disabled, recover: describe the issue with screenshots or use the app's export feature.
- **F3 No audio captured:** detect: playback is silent when audio was expected, recover: repeat with microphone or device-audio option enabled.
- **F4 File is too large:** detect: share sheet fails or upload rejects it, recover: trim shorter, lower resolution if available, or use a trusted compressor.
- **F5 Notifications leak information:** detect: banners appear in the clip, recover: enable Do Not Disturb and record again.

## Verification

The saved video plays from start to finish, shows the intended phone actions, uses the intended audio mode, and is short enough to share.

## Variations

- `ios`: Control Center Screen Recording can include microphone audio by long-pressing the control before Start Recording.
- `android`: Labels vary by manufacturer, such as Screen Record, Screen Recorder, or Record Screen.
- `samsung`: The recorder often includes options for media sounds, mic, and tap indicators.
- `pixel`: Screen Record usually appears in Quick Settings and saves to Photos.

## Safety & privacy

Screen recordings capture notifications, passwords typed on screen, contacts, photos, location, and voices if the microphone is on. Use Do Not Disturb, keep clips short, and review the whole video before sharing.
