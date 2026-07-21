<div align="center">

# 📖 howto

### An open library of everyday procedural knowledge

**Structured how-to recipes for training agents 🤖 and robots 🦾, readable by humans 🧑**

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Recipes](https://img.shields.io/badge/recipes-100-brightgreen.svg)](domains.json)
[![Domains](https://img.shields.io/badge/domains-12-blueviolet.svg)](domains.json)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

[**Why**](#-why-this-exists) · [**What's inside**](#%EF%B8%8F-whats-inside) · [**Quick start**](#-quick-start) · [**Design principles**](#-design-principles) · [**Contributing**](#-contributing)

</div>

---

## 🐘 How do you put an elephant into a fridge?

Everyone knows this one:

> 1. Open the fridge. 2. Put the elephant in. 3. Close the fridge.

That is how most datasets think tasks work. Here is how `howto` writes it:

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

**Things are always more complicated than "open, put, close", and the complications are exactly the knowledge agents are missing.** Every human knows the real steps, the expected observations, the branches, the failure modes. No corpus writes them down. This one does.

---

## 🧠 Why this exists

[`agency-agents`](https://github.com/msitarzewski/agency-agents) curates **who an agent is**. `howto` curates **what an agent knows how to do**: ride a subway, buy and return a product, create an account, make coffee, load a dishwasher, wait in line, pay at a cashier.

Web agents, computer-use agents, and household robots fail at everyday tasks less from weak reasoning than from **missing grounded procedural knowledge**: canonical step order, the observation that confirms each step worked, the decision branches, the recovery paths, and which steps are irreversible.

The schema turns prose into training substrate. One corpus yields, simultaneously:

| Training product | Derived from |
|---|---|
| 🎓 SFT / midtraining planning traces | Steps + expected observations |
| 🏋️ Agentic RL tasks with **verifiable rewards** | Goal + Preconditions + Verification |
| 📚 Curriculum / skill DAG | `prerequisites` links between recipes |
| 🔎 Inference-time skill library (RAG) | Recipe chunks |
| 🧪 Contamination-controlled evals | Held-out recipes and locale variants |
| 🦾 Robot task plans & sim task generation | Embodied `objects` / `affordances` / `workspace` / `safety` |

---

## ⚡ Quick start

```bash
git clone https://github.com/ShirleyHuang11/howto.git && cd howto

./scripts/validate.sh                    # ✅ validate every recipe against the schema
python3 scripts/stats.py                 # 📊 per-domain coverage dashboard
python3 scripts/export.py --format sft   # 🎓 instruction-tuning pairs (JSONL)
python3 scripts/export.py --format eval  # 🧪 task specs with success criteria (JSONL)
python3 scripts/export.py --format json  # 📦 full structured recipes
```

Or just read one: [`transit/ride-a-subway.md`](transit/ride-a-subway.md) · [`embodied/kitchen/load-a-dishwasher.md`](embodied/kitchen/load-a-dishwasher.md) · [`daily/social/pay-at-a-cashier.md`](daily/social/pay-at-a-cashier.md)

---

## 🗂️ What's inside

One task = one markdown file, separated by domain ([`domains.json`](domains.json) is the registry). Every recipe shares one skeleton:

```
Goal → Preconditions → Steps (every step ends with → *Expect:* …)
→ Decision points → Failure modes & recovery → Verification
→ Variations (locale/platform) → Safety & privacy (⚠️ irreversible steps inline)
```

<details open>
<summary><b>🧠 Common sense — <code>daily/</code></b> (the largest track: what everyone knows and no one wrote down)</summary>
<br>

| Subdomain | Recipes |
|---|---|
| `self-care/` | brush your teeth · floss · shower · tie shoelaces · bedtime · trim nails · dress for the weather |
| `food/` | boil water · make tea · cook rice · fry an egg · sandwich · cut an onion · microwave · instant noodles · pack a lunch · store leftovers · read food labels |
| `home/` | do the laundry · make a bed · sweep & mop · vacuum · clean a bathroom · sort recycling · unclog a drain · change a lightbulb · change batteries |
| `social/` | pay at a cashier · wait in line · order at a restaurant · split a bill · answer a phone call · greet a neighbor · give directions · ask for help in a store · small talk · borrow & return |
| `errands/` | use an ATM · mail a letter · refuel a car · vending machine · self-checkout · buy groceries · get a haircut · public library |

</details>

<details>
<summary><b>🦾 Robot track — <code>embodied/</code></b> (recipes that compile into simulator tasks)</summary>
<br>

| Subdomain | Recipes |
|---|---|
| `kitchen/` | make drip coffee · load a dishwasher · set a table · store groceries · make toast |
| `household/` | fold a t-shirt · water houseplants · take out the trash · tidy a room |
| `mobility/` | open a door · use an elevator · carry & deliver · cross a street |
| `care/` | fetch an item for a person |

Embodied frontmatter specifies the sim scene:

```yaml
objects: [dishwasher, plates, cutlery, detergent-pod]
affordances: [door-open, rack-slide, grasp, place]
workspace: kitchen
safety: {sharp_objects: true, fragile: [glasses], human_proximity: pause}
```

</details>

<details>
<summary><b>💻 Digital — <code>accounts/</code> <code>shopping/</code> <code>digital/</code> <code>finance/</code></b></summary>
<br>

create an account · log in · enable 2FA · recover a password · delete an account · security review · buy & return a product · track a delivery · compare before buying · install an app · unsubscribe · back up files · connect to wifi · update safely · pay a bill · dispute a charge · send money to a friend

</details>

<details>
<summary><b>🚇 Physical & services — <code>transit/</code> <code>travel/</code> <code>communication/</code> <code>government/</code> <code>healthcare/</code> <code>housing/</code></b></summary>
<br>

ride a subway · take a bus · hail a rideshare · navigate with maps · book a flight · check in · book a hotel · send a package · schedule a meeting · renew a passport · book a doctor's appointment · refill a prescription · set up utilities

</details>

📊 Live coverage anytime: `python3 scripts/stats.py`

---

## 📐 Design principles

1. **Every step states its expected observation.** A step list without expectations is prose; the *Expect:* clause is what makes a recipe executable and trainable.
2. **Verification is a predicate, not a vibe.** "You are done when…" must be checkable by a program or a stranger — it compiles into a reward function.
3. **Irreversible steps are marked ⚠️ inline** — payments, deletions, hot liquids, handed-over packages. Agents must learn *where to stop and confirm*, and that signal lives in the data.
4. **Failure modes are first-class.** Real procedures go wrong in known ways; the recovery paths are half the knowledge.
5. **Generic first, locale variants second.** The `generic` recipe stands alone; `us-nyc` / `jp-tokyo` / `cn-beijing` variants layer on top.

---

## 🤝 Contributing

One recipe = one markdown file = one PR.

1. Copy [`TEMPLATE.md`](TEMPLATE.md) into the right domain directory
2. Write the procedure you actually know (original content only)
3. `./scripts/validate.sh` until green ✅
4. Open the PR

The short rules: every step needs an *Expect:* · verification must be checkable · irreversible steps get ⚠️ · embodied recipes need the robot frontmatter. Full rules in [CONTRIBUTING.md](CONTRIBUTING.md).

**🌍 Locale expertise is especially welcome.** Recipes for how things work in *your* city make agents useful beyond the defaults.

---

<div align="center">

📜 Code: [MIT](LICENSE) · Content: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

*Now you know how to put an elephant in a fridge. The giraffe is a different recipe:<br>its Preconditions include "remove the elephant first."* 🦒

**⭐ Star this repo if your agent ever confidently walked the wrong way out of a subway station.**

</div>
