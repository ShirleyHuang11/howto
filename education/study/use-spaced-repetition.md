---
name: use-spaced-repetition
domain: education
subdomain: study
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min-30d
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You review material at increasing intervals so important knowledge stays retrievable without rereading everything every day.

## Preconditions

- Material that benefits from memory: vocabulary, facts, formulas, procedures, diagrams, cases, or definitions.
- A calendar, spreadsheet, paper box, or spaced-repetition app.
- Time for short daily or near-daily review sessions.

## Steps

1. **Select durable knowledge to review.** Choose facts, concepts, examples, and procedures that you must remember later. → *Expect:* the review set excludes one-time administrative details.
2. **Convert each item into a prompt.** Write questions, cloze deletions, flashcards, or problem starters that require recall. → *Expect:* every item asks you to produce an answer before seeing it.
3. **Schedule the first reviews close together.** Review new items after about one day and again after several days. → *Expect:* weak memories are caught before they disappear.
4. **Increase intervals for correct items.** Push easy items farther out and keep difficult items closer. → *Expect:* study time shifts toward what you are likely to forget.
5. **Keep sessions short and consistent.** Review due items before adding many new ones. → *Expect:* the daily queue remains manageable.
6. **Edit bad prompts.** Split cards that test multiple facts, add context, and remove ambiguous wording. → *Expect:* wrong answers reflect memory gaps rather than confusing card design.
7. **Add mixed practice for application.** Periodically use problems, essays, or oral explanation so memorized facts connect to performance. → *Expect:* you can use the knowledge outside the flashcard format.

## Decision points

- The daily review pile is growing too large → stop adding new items and reduce or suspend low-value cards.
- You always miss the same item → rewrite it, add an example, or relearn the underlying concept.
- An exam is near → keep spaced reviews but add timed mixed practice and past papers.

## Failure modes & recovery

- **F1 Too many new cards:** detect review sessions expanding beyond available time → cap new items until the backlog clears.
- **F2 Recognition without recall:** detect cards you answer only after seeing hints → remove hints or require a full answer first.
- **F3 Isolated memorization:** detect good flashcard scores but poor problem performance → add applied practice sessions.
- **F4 Ambiguous prompts:** detect multiple plausible answers → rewrite with one clear target and enough context.

## Verification

Your system shows due items completed for the day, difficult items scheduled soon, easy items scheduled later, and at least one applied task confirms you can use the material.

## Variations

- `paper Leitner box`: move correct cards to a less frequent box and missed cards back to the first box.
- `flashcard app`: use the app's rating buttons honestly; do not mark a card easy because the answer looked familiar.
- `exam review`: shorten intervals temporarily, but keep retrieval practice rather than rereading as the core method.

## Safety & privacy

Low risk. Do not put confidential clinical cases, student records, private client data, or restricted exam content into third-party flashcard systems unless allowed.
