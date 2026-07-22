---
name: use-a-voice-assistant
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Your voice assistant responds to the right wake word, handles common commands, and has history and privacy settings you understand.

## Preconditions

- A phone, speaker, computer, car system, or smart display with a voice assistant.
- Internet access for setup and most assistant features.
- Account access for reminders, calls, calendars, or smart-home controls.

## Steps

1. **Choose the assistant entry point.** Open the assistant app or device settings for Siri, Google Assistant, Alexa, or another installed assistant. → *Expect:* assistant setup or settings are visible.
2. **Enable the wake word.** Turn on the wake phrase only on devices where hands-free use is helpful. → *Expect:* the device listens for the selected wake word.
3. **Train voice recognition if offered.** Read the sample phrases so the assistant can distinguish your voice. → *Expect:* setup confirms your voice model or personal results.
4. **Test common commands.** Ask for the weather, a timer, a reminder, and a calendar check. → *Expect:* each command returns an answer or asks for a missing permission.
5. **Connect useful permissions.** [BRANCH: reminders | calls | smart home] allow only the services you actually plan to use. → *Expect:* the assistant can complete those specific tasks.
6. **Set communication rules.** If using calls or messages, confirm the assistant asks before sending or calling when possible. → *Expect:* outgoing actions require clear confirmation.
7. **Review history settings.** Open assistant privacy or activity history and choose whether voice recordings or transcripts are saved. → *Expect:* you know where to view and delete past activity.
8. **Place devices carefully.** Keep always-listening speakers out of bathrooms, guest rooms, and sensitive work areas. → *Expect:* the assistant is available without sitting in the most private spaces.

## Decision points

- You only need occasional use → turn off the wake word and launch the assistant manually.
- Multiple devices answer at once → disable wake word on the less useful device or change room placement.
- Children or guests use the space → restrict purchases, explicit content, and personal results.

## Failure modes & recovery

- **F1 Assistant does not wake:** detect when the wake word gets no response, recover by checking microphone mute, battery, network, and wake-word settings.
- **F2 Wrong device answers:** detect when another room responds, recover by moving devices apart or disabling wake word on one device.
- **F3 Reminder lands in wrong account:** detect missing reminders later, recover by checking the active account and default list.
- **F4 History keeps recordings:** detect saved audio or transcripts in activity settings, recover by deleting history and changing retention settings.

## Verification

The assistant responds from the intended device, completes a timer and reminder correctly, and its history settings match your privacy choice.

## Variations

- `iphone`: Siri settings control "Listen for," personal requests, and message confirmation behavior.
- `android`: Google Assistant and Gemini features vary by device, account, and region.
- `smart-speaker`: household profiles, purchases, and voice recognition matter more than on a single-user phone.

## Safety & privacy

Voice assistants may process recordings, transcripts, contact names, location, smart-home devices, and calendar data. Limit permissions, review saved history, and require confirmation for calls, messages, purchases, and unlock-related actions.
