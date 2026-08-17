---
name: write-a-good-ai-prompt
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

Write a prompt that gives an AI system enough context, constraints, and success criteria to produce a useful first draft without exposing unnecessary private information.

## Preconditions

- You know the task outcome you want.
- You can identify any sensitive details that should be removed, generalized, or replaced with placeholders.

## Steps

1. **State the task plainly.** Begin with one sentence that names the deliverable, audience, and purpose. → *Expect:* the prompt has a clear verb such as draft, compare, summarize, plan, or rewrite.
2. **Add relevant context.** Include only facts the model needs, replacing private names, account numbers, medical details, and secrets with labels like `[client]` or `[account]`. → *Expect:* the prompt is useful without revealing avoidable personal data.
3. **Define constraints.** Specify format, length, tone, sources allowed, assumptions to avoid, and anything the answer must not do. [BRANCH: creative | factual] creative prompts can allow options; factual prompts should require uncertainty labels and source checks. → *Expect:* the model has boundaries to follow.
4. **Give examples when helpful.** Add one short example of a good output or a bad output to avoid. → *Expect:* the requested style or structure is easier to infer.
5. **Ask for questions or caveats.** Tell the model to ask clarifying questions if blocked and to flag low-confidence claims instead of inventing details. → *Expect:* the prompt discourages hallucinated certainty.
6. **Test and revise.** Run the prompt once, compare the result with your goal, then tighten vague wording. → *Expect:* the next version fixes the biggest mismatch you observed.

## Decision points

- The answer will affect money, health, law, safety, or identity → require citations or expert review and treat the AI output as a draft only.
- The model lacks current information → tell it to browse or provide current sources if the tool supports that; otherwise verify externally.
- The output must match a brand, policy, or rubric → paste the relevant excerpt instead of relying on the model's memory.

## Failure modes & recovery

- **F1 Vague answer:** detect generic advice that could fit any task → recover by adding audience, constraints, and an example.
- **F2 Hallucinated facts:** detect unsupported names, dates, statistics, or links → recover by asking for sources and checking them outside the chat.
- **F3 Privacy leak:** detect secrets or personal data in the prompt → recover by deleting the chat if possible, rotating exposed credentials, and using placeholders next time.

## Verification

The prompt names the deliverable, audience, context, constraints, output format, and uncertainty behavior, and a test response satisfies those requirements without using private details unnecessarily.

## Variations

- `web`: use a text box and keep a reusable prompt template in notes.
- `mobile-app`: dictate the prompt, then proofread names, numbers, and negations before sending.
- `work`: include the internal policy excerpt that governs the answer.

## Safety & privacy

Low risk for ordinary drafts, but prompts can reveal sensitive business, health, legal, or identity data. Never paste passwords, API keys, private tokens, or confidential documents unless the tool and account are approved for that data.
