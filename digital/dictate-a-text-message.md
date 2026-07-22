---
name: dictate-a-text-message
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

You can speak a text message, include punctuation, review the transcription, and send it only after confirming it says what you mean.

## Preconditions

- A phone with a working microphone.
- Dictation or speech-to-text enabled in keyboard settings.
- A messaging app with permission to use the microphone.

## Steps

1. **Enable dictation.** In keyboard settings, turn on dictation, voice typing, or speech input for your language. → *Expect:* a microphone button appears on the keyboard.
2. **Open the conversation.** Choose the intended recipient before starting voice input. → *Expect:* the message field is active in the correct chat.
3. **Start dictation.** Tap the microphone on the keyboard or in the message field. → *Expect:* the phone shows a listening indicator.
4. **Speak in short phrases.** Say the message naturally, then say punctuation such as "comma," "period," or "question mark." → *Expect:* words and punctuation appear in the draft.
5. **Pause to stop.** Stop speaking or tap the microphone again when the draft is complete. → *Expect:* the keyboard returns to normal editing mode.
6. **Review before sending.** Read the full message, especially names, numbers, dates, and any sensitive wording. → *Expect:* mistakes are visible while the message is still unsent.
7. **Fix errors manually.** [BRANCH: small typo | badly wrong] edit small errors by keyboard, or delete and redictate if the meaning changed. → *Expect:* the draft matches your intended message.
8. **Send deliberately.** Tap Send only after the recipient and message are both correct. → *Expect:* the message appears in the conversation as sent.

## Decision points

- You are in a noisy room → move closer to the microphone, use earbuds with a mic, or type instead.
- The message is private → wait until you are away from people who can overhear.
- Dictation repeatedly misses a name → type the name once, then dictate the rest.

## Failure modes & recovery

- **F1 Microphone button missing:** detect when the keyboard has no voice key, recover by enabling dictation in keyboard settings and granting microphone access.
- **F2 Wrong language detected:** detect garbled words from another language, recover by switching the keyboard or dictation language.
- **F3 Background noise corrupts text:** detect repeated wrong words, recover by moving to a quieter spot or using a headset microphone.
- **F4 Message sent with an error:** detect after sending, recover by sending a correction immediately or using edit/unsend if your app supports it.

## Verification

A dictated draft includes the intended words and punctuation, is reviewed before sending, and appears in the correct conversation after you tap Send.

## Variations

- `iphone`: dictation is usually enabled under Settings > General > Keyboard > Enable Dictation.
- `android`: Gboard voice typing is usually controlled through Settings > System > Keyboard or the Gboard app.
- `car`: use hands-free systems only when it is legal and safe, and keep messages short.

## Safety & privacy

Dictation may send audio or text to the platform for processing depending on device and settings. Do not dictate passwords, payment details, medical details, or anything you cannot safely say out loud nearby.
