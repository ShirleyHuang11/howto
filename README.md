<div align="center">

# 📖 howto

**An open library of everyday procedural knowledge —<br>structured how-to recipes for training agents and robots.**

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Recipes](https://img.shields.io/badge/recipes-76-brightgreen.svg)](domains.json)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

*for agents 🤖 · for robots 🦾 · for humans 🧑*

</div>

---

## 🐘 How do you put an elephant into a fridge?

Easy — everyone knows this one:

> 1. Open the fridge.
> 2. Put the elephant in.
> 3. Close the fridge.

That's how most datasets think tasks work. Here's how `howto` writes it:

```markdown
## Steps
1. **Open the fridge.** → *Expect:* door open, shelves visible, light on.
2. **Insert the elephant.** [BRANCH: elephant does not fit → F1]
   - ⚠️ *Irreversible:* obtain the elephant's consent before this step.
3. **Close the fridge.** → *Expect:* door latched; no trunk protruding.

## Failure modes & recovery
- **F1 Elephant exceeds fridge capacity:** acquire a larger fridge, or a smaller elephant.
- **F2 Door won't latch:** check for protruding trunk; re-seat elephant; see F1.

## Verification
Opening the fridge reveals exactly one (1) chilled, consenting elephant.
```

**Things are always more complicated than "open, put, close" — and the complications are exactly the knowledge agents are missing.** Every human knows the real steps, the expected observations, the branches, the failure modes. No corpus writes them down. This one does.

---

## 🧠 Why this exists

[`agency-agents`](https://github.com/msitarzewski/agency-agents) curates **who an agent is**. `howto` curates **what an agent knows how to do**: ride a subway, buy and return a product, create an account, make coffee, load a dishwasher, wait in line, pay at a cashier.

Agents — web agents, computer-use agents, household robots — fail at everyday tasks less from weak reasoning than from **missing grounded procedural knowledge**: canonical step order, the observation that confirms each step worked, the decision branches, the recovery paths, and which steps are irreversible.

The schema turns prose into training substrate. One corpus yields, simultaneously:

| Training product | Derived from |
|---|---|
| 🎓 SFT / midtraining planning traces | Steps + expected observations |
| 🏋️ Agentic RL tasks with **verifiable rewards** | Goal + Preconditions + Verification |
| 📚 Curriculum / skill DAG | `prerequisites` links between recipes |
| 🔎 Inference-time skill library (RAG) | Recipe chunks |
| 🧪 Contamination-controlled evals | Held-out recipes and locale variants |
| 🦾 Robot task plans & sim task generation | Embodied `objects` / `affordances` / `workspace` / `safety` |

```bash
python3 scripts/export.py --format sft   # instruction-tuning pairs (JSONL)
python3 scripts/export.py --format eval  # task specs with success criteria (JSONL)
python3 scripts/export.py --format json  # full structured recipes
```

---

## 🗂️ What's inside

One task = one markdown file, separated by domain ([`domains.json`](domains.json) is the registry):

| Track | Domains | Examples |
|---|---|---|
| 🧠 **Common sense** | `daily/` — self-care · food · home · social · errands | brush your teeth · boil water · do the laundry · wait in line · use an ATM · get a haircut |
| 🦾 **Robot** | `embodied/` — kitchen · household · mobility · care | make drip coffee · load a dishwasher · fold a t-shirt · open a door · use an elevator · tidy a room |
| 💻 **Digital** | `accounts/` `shopping/` `digital/` `finance/` | create an account · enable 2FA · buy & return a product · dispute a charge · back up your files |
| 🚇 **Physical & services** | `transit/` `travel/` `communication/` `government/` `healthcare/` `housing/` | ride a subway · book a flight · send a package · renew a passport · refill a prescription |

Every recipe carries the same skeleton:

```
Goal → Preconditions → Steps (with → *Expect:* after every step)
→ Decision points → Failure modes & recovery → Verification
→ Variations (locale/platform) → Safety & privacy
```

Embodied recipes add robot frontmatter that compiles into simulator tasks:

```yaml
objects: [dishwasher, plates, cutlery, detergent-pod]
affordances: [door-open, rack-slide, grasp, place]
workspace: kitchen
safety: {sharp_objects: true, fragile: [glasses], human_proximity: pause}
```

📊 Live coverage: `python3 scripts/stats.py`

---

## 📐 Design principles

1. **Every step states its expected observation.** A step list without expectations is prose; the *Expect:* clause is what makes a recipe executable and trainable.
2. **Verification is a predicate, not a vibe.** "You are done when…" must be checkable by a program or a stranger — it compiles into a reward function.
3. **Irreversible steps are marked ⚠️ inline** — payments, deletions, hot liquids, handed-over packages. Agents must learn *where to stop and confirm*, and that signal lives in the data.
4. **Failure modes are first-class.** Real procedures go wrong in known ways; the recovery paths are half the knowledge.
5. **Generic first, locale variants second.** The `generic` recipe stands alone; `us-nyc` / `jp-tokyo` / `cn-beijing` variants layer on top.

---

## 🚀 Using the corpus

- 📖 **Read it** — it's a clean, ad-free life manual.
- 🔎 **Retrieve it** — chunk recipes into an agent's skill memory.
- 🎓 **Train on it** — `export.py --format sft` for planning traces.
- 🧪 **Build evals from it** — `export.py --format eval`; `status: verified` recipes have passed agent-executability testing.
- 🦾 **Compile sim tasks from it** — embodied frontmatter specifies scene, objects, and success predicates.

---

## 🤝 Contributing

One recipe = one markdown file = one PR. Start from [`TEMPLATE.md`](TEMPLATE.md), read [CONTRIBUTING.md](CONTRIBUTING.md), validate before pushing:

```bash
./scripts/validate.sh
```

The short rules: original content only · every step needs an *Expect:* · verification must be checkable · irreversible steps get ⚠️ · embodied recipes need the robot frontmatter. **Locale expertise is especially welcome** — recipes for how things work in *your* city make agents useful beyond the defaults.

---

<div align="center">

📜 Code: [MIT](LICENSE) · Content: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

*Now you know how to put the elephant in the fridge. The giraffe is a different recipe —<br>its Preconditions include "remove the elephant first."* 🦒

</div>
