---
name: transcribe-audio-to-text
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Turn an audio recording into readable text and verify the parts where accuracy matters.

## Preconditions

- You have permission to record or process the audio.
- You have the audio file and enough storage or upload bandwidth.

## Steps

1. **Confirm consent and sensitivity.** Check whether the recording includes private conversations, protected information, or people who did not consent. → *Expect:* you know whether transcription is allowed.
2. **Choose a transcription method.** [BRANCH: local app | cloud service] use local tools for sensitive audio; use cloud tools when allowed and convenient. → *Expect:* the service matches the privacy level.
3. **Prepare the audio.** Use the clearest file available, trim unrelated sections, and note speaker names if known. → *Expect:* the input is easier to transcribe accurately.
4. **Run transcription.** Upload or import the file and enable speaker labels, timestamps, or language settings when useful. → *Expect:* a draft transcript is produced.
5. **Review difficult sections.** Replay unclear, technical, accented, noisy, or high-stakes sections while editing the text. → *Expect:* important phrases are corrected.
6. **Export and label.** Save the transcript with date, source, language, and whether it is edited or machine-generated. → *Expect:* future readers know the transcript status.

## Decision points

- Legal, medical, HR, or research audio → follow consent, retention, and approved-tool rules.
- Multiple speakers overlap → use timestamps and manual review rather than relying on automatic labels.
- The transcript will be quoted publicly → verify the quote against the audio before publication.

## Failure modes & recovery

- **F1 Wrong speaker labels:** detect labels switch between speakers → recover by manually relabeling critical sections.
- **F2 Misheard terms:** detect garbled names, numbers, jargon, or dates → recover by replaying slowly and checking context.
- **F3 Upload prohibited:** detect the file contains restricted data → recover by using an approved local tool or not transcribing.

## Verification

The transcript opens in the chosen format, important sections have been checked against the audio, and unclear passages are marked rather than silently guessed.

## Variations

- `mobile-app`: use airplane mode or local transcription if the app supports it for sensitive recordings.
- `meetings`: export action items separately only after checking the transcript.
- `multilingual`: set the language explicitly and review names and code-switching carefully.

## Safety & privacy

Medium risk because voices can identify people and recordings may contain confidential details. Store audio and transcripts with the same care as the original conversation.
