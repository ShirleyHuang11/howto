# Contributing a recipe

One task = one markdown file in its domain directory. Copy `TEMPLATE.md`, fill every
required section, run `./scripts/validate.sh` locally until green, and open a PR.
The frontmatter is formally specified in `schema/recipe.schema.json`.

## Rules

1. **Original content only.** Write from your own knowledge and experience. Do not copy
   from wikiHow, blogs, or manuals. Content is released under CC-BY-4.0, code under MIT.
2. **In scope:** legal, everyday, benign tasks. Out of scope: anything designed to harm,
   defraud, evade enforcement, or endanger. New domains require a maintainer discussion first.
3. **One domain per recipe.** Cross-domain dependencies go in `prerequisites`
   (e.g. `shopping/return-a-product` requires `accounts/log-in`), never by duplicating steps.
4. **Every step needs an *Expect:*** — the observation that confirms the step worked.
   This is what makes a recipe trainable; a step list without expectations is prose.
5. **Verification must be checkable.** Write the end-state predicate a program (or a
   stranger) could evaluate, not "you should be done now."
6. **Mark irreversible steps** with ⚠️ and state what to confirm before executing them.
7. **`generic` locale first.** Add locale variants (`us-nyc`, `jp-tokyo`, `cn-beijing`, …)
   under Variations or as separate frontmatter locales only after the generic recipe stands alone.
8. **Embodied recipes** (`embodied/`) must include `objects`, `affordances`, `workspace`,
   and `safety` frontmatter — they compile into simulator tasks.
9. **Multimodal assets are welcome but optional.** Diagrams, photos, and short clips go in
   `<domain-dir>/assets/<recipe-name>/` and are declared in the `media` frontmatter block
   (see TEMPLATE.md): each entry needs a `path`, a `role` (`action-demo`,
   `expected-observation`, `diagram`, `warning`, or `overview`), and an `alt` text that
   fully describes the asset — the alt is the text-only training fallback, so write it as
   a real description, not a caption. Anchor step-specific assets with `step: N` and embed
   them inline in the body with normal markdown images so they render on GitHub. Prefer
   SVG for diagrams (diffable, small) and keep photos free of faces, plates, and personal
   information. Only original or CC-licensed media you have the right to contribute.

## Status ladder

- `draft` — passes schema validation.
- `reviewed` — a domain reviewer confirmed correctness and completeness.
- `verified` — an agent following only the recipe completed the task in a real or
  simulated environment. Verified recipes carry evidential weight for training; do not
  self-assign this status.

**How recipes get promoted:** `reviewed` is granted by a PR from a second person that
flips the status field and includes a short checklist comment (steps correct, Expect
clauses realistic, failure modes real, verification checkable). `verified` requires
attaching evidence to the PR: an agent transcript, log, or sim run showing the task
completed from the recipe alone. Volunteering to review or verify existing recipes is
as valuable as writing new ones.

## Wanted

The corpus is growing toward 200 recipes. High-value contributions right now:

- **Locale variants** for existing recipes (`jp-tokyo`, `cn-beijing`, `de-berlin`,
  `in-mumbai`, your city): add a Variations entry or a locale to the frontmatter with
  what actually differs. Beginner-friendly.
- **Verification evidence** for any recipe you can test (see promotion above).
- **Multimodal assets**: a diagram or photo for a step you know well (rule 9 below).
- **New recipes** in the thinnest domains: `government/`, `healthcare/`, `housing/`,
  `communication/`, and `embodied/care/`.

## Local validation

```bash
./scripts/validate.sh              # everything
./scripts/validate.sh daily/       # one domain
```
