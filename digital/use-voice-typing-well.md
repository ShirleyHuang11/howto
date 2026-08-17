---
name: use-voice-typing-well
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Use voice typing to produce accurate text faster while protecting privacy and correcting speech-recognition errors.

## Preconditions

- Your device has a microphone and voice typing or dictation enabled.
- You are in a place where speaking the content aloud is appropriate.

## Steps

1. **Check microphone and language.** Select the correct input language, keyboard, and microphone source. → *Expect:* the dictation control responds when you speak.
2. **Choose a private setting.** Move away from people if the text includes names, work content, passwords, health details, or financial information. → *Expect:* sensitive speech cannot be easily overheard.
3. **Dictate in short chunks.** Speak one or two sentences at a time and say punctuation where the system expects it. → *Expect:* text appears with fewer long-range errors.
4. **Use commands deliberately.** [BRANCH: plain dictation | editing commands] dictate words normally; use supported commands such as new paragraph or delete only when you know they work. → *Expect:* commands change formatting instead of appearing as text.
5. **Proofread before sending.** Check names, numbers, negations, dates, medications, addresses, and tone. → *Expect:* recognition mistakes are corrected.
6. **Turn off dictation.** Stop listening mode when finished and check that the microphone indicator is off. → *Expect:* the device is no longer capturing speech for the text field.

## Decision points

- The message is high-stakes or emotional → type or review slowly before sending.
- Background noise is high → use a headset microphone or wait.
- The app sends audio to cloud processing → avoid dictating sensitive content unless approved.

## Failure modes & recovery

- **F1 Wrong language:** detect many phonetic errors → recover by changing dictation language or keyboard.
- **F2 Dangerous substitution:** detect wrong numbers, names, or negations → recover by manual proofreading before sending.
- **F3 Microphone stays active:** detect the listening indicator remains on → recover by tapping stop or revoking microphone permission.

## Verification

The final text matches what you intended, critical details are manually checked, and dictation is stopped after use.

## Variations

- `mobile-app`: keyboard dictation is usually available anywhere text can be typed.
- `desktop`: browser, OS, and app dictation may have different commands.
- `accessibility`: create custom vocabulary or shortcuts for repeated terms when supported.

## Safety & privacy

Low risk for casual text, but voice input can expose spoken content to nearby people, app providers, or cloud transcription. Never dictate passwords or secrets.
