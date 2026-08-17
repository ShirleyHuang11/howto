---
name: set-up-a-custom-gpt
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create a custom chatbot configuration for a specific task with clear instructions, safe knowledge handling, and a test set that catches obvious failures.

## Preconditions

- You have access to a platform that supports custom chatbots or GPT-style assistants.
- You know the intended users, task boundaries, and data sensitivity.

## Steps

1. **Define the job.** Write the assistant's purpose, audience, allowed tasks, refused tasks, and escalation rules. → *Expect:* the scope is narrow enough to test.
2. **Configure instructions.** Enter behavior rules, preferred format, tone, uncertainty handling, and privacy limits. → *Expect:* the assistant has explicit operating rules.
3. **Add knowledge carefully.** [BRANCH: no files | approved files] skip uploads if not needed; upload only documents you have rights to use and that are allowed for the platform. → *Expect:* knowledge sources are intentional and permitted.
4. **Set tool access.** Enable browsing, code, actions, connectors, or image tools only when the task requires them. → *Expect:* the assistant has no unnecessary capabilities.
5. **Test with normal and adversarial prompts.** Try expected questions, unclear requests, prompt-injection attempts, and requests outside scope. → *Expect:* useful answers stay in scope and risky requests are handled safely.
6. **Publish with the right visibility.** Choose private, workspace, link-only, or public visibility according to data and audience. → *Expect:* only intended users can access it.
7. **Monitor and revise.** Review feedback, failures, and outdated instructions on a recurring schedule. → *Expect:* there is a maintenance path after launch.

## Decision points

- Uploaded documents contain confidential, personal, or licensed content → restrict access or do not upload them.
- The assistant can take actions in other apps → test write actions and require confirmation for risky changes.
- Public sharing is desired → remove private knowledge and test for leakage before publishing.

## Failure modes & recovery

- **F1 Scope drift:** detect answers outside the intended job → recover by tightening instructions and adding refusal examples.
- **F2 Knowledge leakage:** detect private file content shown to unintended users → recover by unpublishing, removing files, and narrowing visibility.
- **F3 Tool misuse:** detect unwanted external actions or browsing → recover by disabling tools or adding confirmation rules.

## Verification

The custom GPT answers the test prompts correctly, refuses or redirects out-of-scope prompts, uses only approved knowledge and tools, and is visible only to the intended audience.

## Variations

- `work`: align instructions with company AI, data retention, and admin review policies.
- `education`: include citation and academic integrity rules.
- `support`: include escalation language and do not let the bot invent policy.

## Safety & privacy

Medium risk because custom assistants can expose uploaded knowledge or take actions through connected tools. Treat instructions, files, and visibility as security controls, not cosmetic settings.
