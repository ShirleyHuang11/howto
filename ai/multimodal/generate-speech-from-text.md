---
name: generate-speech-from-text
domain: ai
subdomain: multimodal
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Generate speech audio from text with controlled voice, format, and quality checks so the output can be programmatically validated before use.

## Preconditions

- Text you are allowed to synthesize and a policy for voice/likeness rights.
- A TTS provider or local model, plus audio tools such as `ffprobe` or Python `soundfile`.
- A target audio format, sample rate, loudness range, and maximum duration.

## Steps

1. **Normalize the input text.** Expand ambiguous abbreviations, remove hidden control characters, and cap length per request. → *Expect:* normalized UTF-8 text with a logged character count.
2. **Choose voice and rights policy.** [BRANCH: stock provider voice | licensed cloned voice | local voice] Use only voices you have the right to use. → *Expect:* a voice id and license note are recorded.
3. **Generate audio.** Call the TTS endpoint or local model with explicit format, speed, and voice settings. ⚠️ *Data leaves your control:* hosted TTS receives the submitted text, which may include private content. → *Expect:* an audio file is returned with a successful HTTP status or local process exit code 0.
4. **Validate audio properties.** Run `ffprobe -v error -show_entries format=duration -show_streams speech.mp3`. → *Expect:* duration, codec, sample rate, and channel count match the requested target.
5. **Check intelligibility and content.** Transcribe the generated audio with ASR and compare normalized transcript to the input using word error rate. → *Expect:* WER is below the acceptance threshold, such as `<= 0.05` for short scripted text.
6. **Store output with provenance.** Save audio, text hash, voice id, model/provider, and generation parameters. → *Expect:* the audio can be reproduced or audited without storing sensitive raw text where unnecessary.

## Decision points

- WER is too high → slow speech, change voice, split long text, or fix pronunciation hints.
- Text includes sensitive user data → use local TTS or obtain explicit approval for hosted synthesis.
- Voice resembles a real person → verify consent and add disclosure where users could be misled.

## Failure modes & recovery

- **F1 Unsupported format:** detect missing codec or failed `ffprobe` → request a supported format or transcode with a logged conversion.
- **F2 Truncated audio:** detect duration much shorter than expected or ASR missing tail text → split input and regenerate.
- **F3 Pronunciation error:** detect high WER on names or terms → add phonetic spelling or SSML where supported.
- **F4 Voice rights violation:** detect unlicensed cloned voice use → stop generation and switch to an approved stock voice.

## Verification

The generated audio exists, `ffprobe` reports the expected codec/sample rate/channel count, duration is within configured bounds, and ASR comparison gives word error rate `<= 0.05` on the target script.

## Variations

- `hosted TTS`: simple and high quality; review data retention and voice policy.
- `local TTS`: stronger privacy; requires GPU/CPU planning and quality evaluation.
- `SSML-capable provider`: use SSML for pauses, pronunciation, and emphasis, then validate audio the same way.

## Safety & privacy

Do not synthesize deceptive impersonations or private text without consent. Disclose synthetic speech where appropriate, avoid logging raw sensitive scripts, and enforce cost and duration limits to prevent abuse.
