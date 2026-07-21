---
name: join-an-online-meeting
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Join an online meeting with working audio and video, use basic etiquette, and recover quickly from common connection problems.

## Preconditions

- Meeting link, meeting ID, or calendar invitation.
- Device with internet access.
- Speaker or headphones.
- Microphone, and camera if video is expected.
- Permission to install the meeting app if required.

## Steps

1. **Open the invitation early.** Click the meeting link or copy the meeting ID from the calendar invite 5 to 10 minutes before start. → *Expect:* a browser page or meeting app opens.
2. **Choose app or browser.** [BRANCH: installed app | browser join] Use the app for best features or browser if installation is blocked. → *Expect:* the meeting lobby or preview screen appears.
3. **Enter your display name.** Use the name attendees will recognize. → *Expect:* the preview shows the correct participant name.
4. **Test audio output.** Play the test sound or check device speaker selection. → *Expect:* you hear the test sound clearly.
5. **Test microphone and camera.** Speak and watch the level meter, then preview the camera if needed. → *Expect:* the meter moves and video shows the intended view.
6. **Join muted unless speaking immediately.** Turn microphone off before entering if you are not the presenter. → *Expect:* the meeting controls show the microphone muted.
7. **Use meeting etiquette.** Keep background noise low, unmute only to talk, and use chat or raise-hand controls when appropriate. → *Expect:* others can hear you only when intended.
8. **Share screen only when ready.** Close private windows, choose the specific window or tab, then start sharing. → *Expect:* the meeting shows a screen-share indicator and the intended content only.
9. **Leave correctly.** Click Leave or End, then close any browser tab if needed. → *Expect:* your name no longer appears in the meeting.

## Decision points

- Link asks for a password → use the passcode from the invitation, not one sent by an unknown person.
- App install is blocked → use the browser join option or call-in number.
- You are presenting → join early and test screen share with the exact content.
- Room is noisy → use headphones and stay muted.
- Confidential meeting → verify the host and attendee list before sharing sensitive content.

## Failure modes & recovery

- **F1 No audio:** detect silence during test or meeting; recover by selecting the correct speaker, checking volume, or reconnecting headphones.
- **F2 Microphone blocked:** detect no input meter; recover by granting browser or system microphone permission.
- **F3 Camera not available:** detect black preview or wrong camera; recover by closing other apps and selecting the right camera.
- **F4 Link fails:** detect invalid meeting or expired link; recover by checking the calendar invite, requesting a fresh link, or dialing in.
- **F5 Screen share exposes private content:** detect wrong window shared; recover by stopping share immediately and sharing only the intended window.

## Verification

You are listed in the meeting, can hear others, can be heard when unmuted, and can leave without the meeting app staying active.

## Variations

- `zoom`: check the audio menu arrow for microphone and speaker selection.
- `google-meet`: browser permissions are often the main blocker.
- `microsoft-teams`: work accounts may require tenant sign-in before joining.
- `webinar`: camera and microphone may be disabled for attendees.
- `phone-call`: use the dial-in number and meeting PIN when internet is unreliable.

## Safety & privacy

Meeting links can reveal private conversations and calendars. Do not post links publicly, and check what is visible before turning on camera or sharing a screen.
