---
name: delimit-context-clearly
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

You wrap instructions, user input, retrieved context, and examples in clear boundaries so the model can distinguish commands from data and downstream code can audit the prompt.

## Preconditions

- A prompt that combines multiple content sources.
- A renderer or template where variables can be escaped or clearly separated.
- Test cases containing adversarial text with fake instructions and delimiter-like strings.

## Steps

1. **Inventory prompt sections.** List system rules, task instructions, user input, retrieved context, examples, and output format. → *Expect:* every prompt line belongs to one named section.
2. **Choose unambiguous delimiters.** Use XML-like tags, fenced blocks, or structured message fields consistently. → *Expect:* rendered prompts have matching open and close delimiters.
3. **Mark untrusted sections.** Label user and retrieved content as data that must not override instructions. → *Expect:* the prompt explicitly says untrusted sections are not instructions.
4. **Escape delimiter collisions.** Replace or encode user text that can close your chosen tags. → *Expect:* a test input containing `</context>` cannot break the rendered structure.
5. **Add metadata to context chunks.** Include source id, timestamp, and trust level outside the chunk body. → *Expect:* citations can refer to stable source ids.
6. **Snapshot rendered prompts.** Test that section order and boundaries do not change accidentally. → *Expect:* prompt rendering tests pass for normal and adversarial inputs.

## Decision points

- The API supports separate message roles → use roles plus internal delimiters for long untrusted blocks.
- User content may contain markup → escape it or use a serialization format such as JSON.
- Prompt injection tests fail → strengthen boundary language and enforce action policy in code.

## Failure modes & recovery

- **F1 Broken boundary:** detect unmatched tags in rendered prompt → add a structural render test.
- **F2 Delimiter injection:** detect user closes a section early → escape user-controlled delimiters.
- **F3 Citation ambiguity:** detect duplicate or missing source ids → assign stable ids before rendering.
- **F4 Instruction confusion:** detect model follows context instructions → label context as untrusted evidence and add injection cases.

## Verification

Run `pytest tests/test_prompt_boundaries.py`; tests must confirm all rendered prompts have balanced delimiters, escaped adversarial closers, stable source ids, and no untrusted text outside its assigned section.

## Variations

- `XML tags`: useful for readable prompts and source blocks.
- `JSON serialization`: useful when prompt variables are structured and need escaping.
- `chat roles`: useful when the provider preserves system, user, assistant, and tool channels separately.

## Safety & privacy

Clear boundaries reduce but do not eliminate injection risk. Treat user and retrieved text as untrusted, keep secrets out of context, and validate tool calls in code before action.
