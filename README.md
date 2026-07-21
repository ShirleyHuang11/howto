# 📖 howto

**An open library of everyday procedural knowledge — structured how-to recipes for training agents and robots.**

[`agency-agents`](https://github.com/msitarzewski/agency-agents) curates **who an agent is**. `howto` curates **what an agent knows how to do**: how to ride a subway, buy and return a product, create an account, make coffee, load a dishwasher, wait in line, pay at a cashier.

Every human knows these procedures. No corpus writes them down. This one does — in a strict, machine-readable schema:

```markdown
---
name: ride-a-subway
domain: transit
interface: physical
risk: low
status: draft            # draft → reviewed → verified (agent-executability tested)
---
## Goal                   # the end state, in one sentence
## Preconditions          # what must be true before starting
## Steps                  # every step ends with → *Expect:* the confirming observation
## Decision points        # where the path branches, and what decides it
## Failure modes & recovery
## Verification           # checkable end-state predicate → compiles into a success checker
## Variations             # locale and platform differences
## Safety & privacy       # irreversible steps are marked ⚠️ inline
```

## Why

Agents — web agents, computer-use agents, household robots — fail at everyday tasks less from weak reasoning than from **missing grounded procedural knowledge**: canonical step order, the expected observation after each step, the decision branches, the recovery paths, and which steps are irreversible.

The schema turns prose into training substrate. One corpus yields, simultaneously:

| Training product | Derived from |
|---|---|
| SFT / midtraining planning traces | Steps + expected observations |
| Agentic RL tasks with **verifiable rewards** | Goal + Preconditions + Verification |
| Curriculum / skill DAG | `prerequisites` links between recipes |
| Inference-time skill library (RAG) | Recipe chunks |
| Contamination-controlled evals | Held-out recipes and locale variants |
| 🤖 Robot task plans & sim task generation | Embodied recipes' `objects` / `affordances` / `workspace` / `safety` |

```bash
python3 scripts/export.py --format sft   # instruction-tuning pairs (JSONL)
python3 scripts/export.py --format eval  # task specs with success criteria (JSONL)
python3 scripts/export.py --format json  # full structured recipes
```

## What's inside

Recipes are separated by domain — one directory per domain, registered in [`domains.json`](domains.json):

| Track | Domains | Examples |
|---|---|---|
| 🧠 **Common sense** | `daily/` (self-care, food, home, social, errands) | brush your teeth · boil water · do the laundry · wait in line · use an ATM · get a haircut |
| 🤖 **Robot** | `embodied/` (kitchen, household, mobility, care) | make drip coffee · load a dishwasher · fold a t-shirt · open a door · use an elevator · tidy a room |
| 💻 **Digital** | `accounts/` `shopping/` `digital/` `finance/` | create an account · enable 2FA · buy & return a product · dispute a card charge · back up your files |
| 🚇 **Physical & services** | `transit/` `travel/` `communication/` `government/` `healthcare/` `housing/` | ride a subway · book a flight · send a package · renew a passport · refill a prescription |

Embodied recipes carry extra frontmatter that compiles into simulator tasks:

```yaml
objects: [dishwasher, plates, cutlery, detergent-pod]
affordances: [door-open, rack-slide, grasp, place]
workspace: kitchen
safety: {sharp_objects: true, fragile: [glasses], human_proximity: pause}
```

Check live per-domain coverage:

```bash
python3 scripts/stats.py
```

## Design principles

1. **Every step states its expected observation.** A step list without expectations is prose; the *Expect:* clause is what makes a recipe executable and trainable.
2. **Verification is a predicate, not a vibe.** "You are done when…" must be checkable by a program or a stranger — it compiles into a reward function.
3. **Irreversible steps are marked ⚠️ inline** — payments, deletions, hot liquids, handed-over packages. Agents must learn *where to stop and confirm*, and that signal lives in the data.
4. **Failure modes are first-class.** Real procedures go wrong in known ways; the recovery paths are half the knowledge.
5. **Generic first, locale variants second.** The `generic` recipe must stand alone; `us-nyc` / `jp-tokyo` / `cn-beijing` variants layer on top.

## Using the corpus

- **Read it** — it's a clean, ad-free life manual.
- **Retrieve it** — chunk recipes into an agent's skill memory.
- **Train on it** — `export.py --format sft` for planning traces.
- **Build evals from it** — `export.py --format eval` for task specs with success criteria; `status: verified` recipes have passed agent-executability testing.
- **Compile sim tasks from it** — embodied recipes' frontmatter specifies scene, objects, and success predicates.

## Contributing

One recipe = one markdown file = one PR. Start from [`TEMPLATE.md`](TEMPLATE.md), read [CONTRIBUTING.md](CONTRIBUTING.md), and validate before pushing:

```bash
./scripts/validate.sh
```

The short rules: original content only (no copying wikiHow), every step needs an *Expect:*, verification must be checkable, irreversible steps get ⚠️, embodied recipes need the robot frontmatter. Locale expertise is especially welcome — recipes for how things work in *your* city and country make agents useful beyond the defaults.

## License

Code: [MIT](LICENSE). Recipe content: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
