---
name: prompt-for-a-specific-tone
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

Produce model outputs in a target tone while preserving factual content, brand constraints, and measurable quality checks.

## Preconditions

- A target audience and use case, such as support replies, executive summaries, or classroom feedback.
- 5-20 examples of acceptable and unacceptable tone, ideally from approved copy.
- A way to evaluate outputs, such as rubric labels, pairwise preference, or style-classifier checks.

## Steps

1. **Define tone as observable rules.** Convert vague words like "friendly" into rules such as `use contractions`, `avoid sarcasm`, and `include one concrete next step`. → *Expect:* a tone guide with 5-8 checkable rules.
2. **Separate facts from style.** Put source facts in one section and style instructions in another so the model does not invent content to sound better. → *Expect:* a prompt template with `SOURCE FACTS` and `STYLE RULES` delimiters.
3. **Add positive and negative examples.** Show one or two outputs that match the tone and one that violates it with a short explanation. → *Expect:* examples demonstrate the tone without changing the task.
4. **Constrain sensitive language.** List forbidden claims, promises, jokes, or affective language that would be unsafe for the domain. → *Expect:* the prompt blocks risky phrasing before generation.
5. **Generate candidates deterministically.** [BRANCH: Anthropic | OpenAI | open model] Use low temperature for production copy and log prompt version, model, and output. → *Expect:* reproducible outputs with traceable prompt metadata.
6. **Score tone and factuality separately.** Run a checklist or judge prompt for tone compliance, then verify factual claims against the source. → *Expect:* each output has `tone_score` and `factuality_pass`.
7. **Reject outputs that trade accuracy for tone.** If the tone is good but facts drift, revise the prompt to prioritize source faithfulness. → *Expect:* accepted copy passes both style and factual checks.

## Decision points

- Tone rules conflict with compliance language → compliance wins; keep required wording exact.
- Audience is distressed or high stakes → use calm, direct tone and avoid humor.
- Style score improves but factuality drops → reduce creative language and require source-grounded phrasing.
- Brand examples are proprietary → keep them in a private prompt registry and avoid external logging.

## Failure modes & recovery

- **F1 Style overreach:** detect invented details or promises → add `do not add facts` and factuality validation.
- **F2 Inconsistent tone:** detect high variance across similar inputs → add examples and lower temperature.
- **F3 Unsafe warmth:** detect emotional manipulation or excessive intimacy → add forbidden phrases and human review for sensitive contexts.
- **F4 Locale mismatch:** detect idioms inappropriate for the audience → add locale and reading-level constraints.

## Verification

Evaluate at least 30 representative inputs. Accepted outputs must score `>= 0.85` on a tone rubric, pass a source-factuality check with `0` unsupported factual claims, and contain none of the forbidden phrases or claims in an automated string or classifier check.

## Variations

- `support`: include empathy, ownership, and a concrete next step; ban blaming language.
- `technical docs`: prioritize precision and brevity over warmth.
- `marketing`: use stronger brand voice but still run claim substantiation checks.

## Safety & privacy

Tone prompting can mask uncertainty or make unsafe advice sound trustworthy. Keep required disclaimers, validate factual claims, redact private examples before third-party API use, and require review for regulated or crisis-sensitive messaging.
