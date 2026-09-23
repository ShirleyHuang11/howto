---
name: transcribe-audio-to-text
domain: ai
subdomain: multimodal
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You convert audio into accurate text with timestamps, speaker handling if needed, and measurable transcription quality.

## Preconditions

- Audio files you are authorized to process.
- A transcription engine such as Whisper-style local models, a hosted speech-to-text API, or a managed call-transcription service.
- A small labeled sample for word error rate evaluation when quality matters.

## Steps

1. **Inspect audio properties.** Use `ffprobe input.wav` to check duration, channels, sample rate, codec, and loudness. → *Expect:* audio metadata is recorded and files are readable.
2. **Normalize the audio copy.** Convert to a supported format, for example `ffmpeg -i input.m4a -ac 1 -ar 16000 work/input.wav`. → *Expect:* a model-ready audio file is created.
3. **Select transcription settings.** Set language, timestamp granularity, diarization need, and profanity or punctuation policy. → *Expect:* settings match the intended transcript use.
4. **Run transcription.** [BRANCH: local model | hosted API] Transcribe the normalized audio. ⚠️ *Data leaves your control:* hosted transcription sends voice data to a third party. → *Expect:* text segments with timestamps are returned.
5. **Post-process cautiously.** Normalize punctuation and casing, but keep a raw transcript copy. → *Expect:* raw and cleaned transcript files both exist.
6. **Evaluate quality.** Compute WER on a labeled sample and inspect low-confidence segments. → *Expect:* WER and confidence summaries are available.
7. **Export the final transcript.** Save JSON with timestamps, plain text, and optional SRT/VTT subtitles. → *Expect:* downstream tools can load the transcript and align text to audio.

## Decision points

- Audio contains multiple speakers → use diarization or speaker labels and verify them separately.
- Audio is noisy or accented → try a stronger model, language hint, or audio enhancement.
- Transcript is used for legal, medical, or employment decisions → require human review.
- Data cannot leave your environment → use a local model and local storage.

## Failure modes & recovery

- **F1 Unsupported format:** detect decoder errors → convert with ffmpeg to WAV or FLAC at a supported sample rate.
- **F2 Hallucinated speech in silence:** detect text during silent regions → use voice activity detection and review low-audio segments.
- **F3 Speaker mix-up:** detect diarization labels switching incorrectly → merge or manually correct speaker segments.
- **F4 High WER:** detect quality below threshold → improve audio, set language, use a stronger model, or send to human transcription.

## Verification

The transcription run passes only if every audio file produces a timestamped JSON transcript, schema validation succeeds, WER on the labeled sample is below the declared threshold, and low-confidence segments are listed for review.

## Variations

- `local Whisper-style model`: best when privacy matters and local compute is available.
- `hosted API`: easier scaling and diarization features, with data-transfer review.
- `subtitles`: export SRT or VTT and verify timestamps do not overlap or exceed duration.

## Safety & privacy

Medium risk because voice can identify people and may include sensitive speech. Obtain consent where required, avoid unnecessary retention, encrypt files, and approve any third-party transcription use before upload.
