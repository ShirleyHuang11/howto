---
name: use-a-chatbot-safely
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Use a chatbot for drafting, brainstorming, learning, and routine assistance while controlling privacy, hallucination, and overreliance risks.

## Preconditions

- You have access to a chatbot account or app.
- You know whether the chat may be used for training, logging, or workplace review.

## Steps

1. **Check the data setting.** Review whether chats are saved, used for training, or shared with an organization administrator. → *Expect:* you know the privacy boundary before typing.
2. **Remove sensitive data.** Replace names, account numbers, credentials, client details, and private health or legal facts with placeholders unless the tool is approved for them. → *Expect:* the prompt does not expose unnecessary personal data.
3. **Use it for bounded tasks.** Ask for drafts, checklists, explanations, transformations, or options instead of asking it to make final high-stakes decisions. → *Expect:* the answer is a starting point you can review.
4. **Demand uncertainty.** Ask the chatbot to flag assumptions, missing information, and claims that require current sources. → *Expect:* unsupported points are visible.
5. **Verify important output.** [BRANCH: low-stakes | high-stakes] proofread low-stakes output yourself; verify high-stakes claims with authoritative sources or professionals. → *Expect:* no important claim is accepted solely because the chatbot said it.
6. **Clean up when needed.** Delete sensitive chats if available and avoid saving private outputs in shared workspaces. → *Expect:* retained chat history matches your privacy needs.

## Decision points

- The task involves credentials, confidential work, medical details, legal strategy, or minors → use only approved tools or do not use a chatbot.
- The chatbot asks you to install software, run commands, or change settings → inspect the action and source before doing it.
- The answer seems confident but surprising → verify before acting.

## Failure modes & recovery

- **F1 Hallucinated answer:** detect confident claims without verifiable support → recover by asking for sources and checking them independently.
- **F2 Sensitive disclosure:** detect private data was pasted → recover by deleting the chat if possible and rotating exposed credentials.
- **F3 Automation mistake:** detect the chatbot suggests a destructive or unsafe action → recover by stopping and getting human review.

## Verification

The chatbot account settings, prompt content, and review process match the sensitivity of the task, and any important factual claim has been checked outside the chat.

## Variations

- `work`: follow the employer's approved AI tools and data classification rules.
- `school`: disclose AI use when required and do not submit generated work as your own if prohibited.
- `mobile-app`: check microphone and photo permissions before using voice or image features.

## Safety & privacy

Medium risk: chatbots can store prompts, invent facts, and sound authoritative when wrong. Treat them as assistants, not authorities, for health, legal, financial, safety, or identity decisions.
