<div align="center">

# 📖 howto

### An open library of everyday procedural knowledge

**Structured how-to recipes for training agents 🤖 and robots 🦾, readable by humans 🧑**

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Recipes](https://img.shields.io/badge/recipes-337-brightgreen.svg)](INDEX.md)
[![Domains](https://img.shields.io/badge/domains-12-blueviolet.svg)](domains.json)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

[**Why**](#why) · [**What's inside**](#inside) · [**Quick start**](#quickstart) · [**Roadmap**](#roadmap) · [**Contributing**](#contributing) · [**Citing**](#citing)

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
3. **Close the fridge.** → *Expect:* door latched; no trunk protruding.

## Failure modes & recovery
- **F1 Elephant exceeds fridge capacity:** acquire a larger fridge, or a smaller elephant.

## Verification
Opening the fridge reveals one chilled elephant.
```

**Things are always more complicated than "open, put, close", and the complications are exactly the knowledge agents are missing.** Every human knows the real steps, the expected observations, the branches, the failure modes. No corpus writes them down. This one does.

And here is a real one, from [`transit/ride-a-subway.md`](transit/ride-a-subway.md):

```markdown
3. **Obtain or validate fare.** [BRANCH: tap-to-pay bank card | transit card with
   balance | ticket machine | transit app QR] At a machine: select destination or fare
   type, pay, take the ticket. ⚠️ *Irreversible:* multi-day passes and non-refundable
   tickets — confirm fare type before paying. → *Expect:* you hold a valid fare medium.
4. **Pass the fare gate.** Tap or insert; walk through on green/open. → *Expect:* gate
   opens and (on card systems) displays balance or fare; if rejected, F1.
...
- **F2 Boarded the wrong direction:** exit at the next station, cross to the opposite
  platform (may require staying inside the paid area), reverse.
```

---

<a id="why"></a>
## 🧠 Why this exists

Web agents, computer-use agents, and household robots fail at everyday tasks less from weak reasoning than from **missing grounded procedural knowledge**: canonical step order, the observation that confirms each step worked, the decision branches, the recovery paths, and which steps are irreversible.

[`agency-agents`](https://github.com/msitarzewski/agency-agents) (134k stars) covers **who an agent is**. `howto` is the complement: **what an agent knows how to do**. Ride a subway, buy and return a product, create an account, make coffee, load a dishwasher, wait in line, pay at a cashier.

The schema turns prose into training substrate. One corpus yields, simultaneously:

| Training product | Derived from |
|---|---|
| SFT / midtraining planning traces | Steps + expected observations |
| Agentic RL tasks with **verifiable rewards** | Goal + Preconditions + Verification |
| Curriculum / skill DAG | `prerequisites` links between recipes |
| Inference-time skill library (RAG) | Recipe chunks |
| Contamination-controlled evals | Held-out recipes and locale variants |
| Robot task plans & sim task generation | Embodied `objects` / `affordances` / `workspace` / `safety` |

---

<a id="quickstart"></a>
## ⚡ Quick start

```bash
git clone https://github.com/ShirleyHuang11/howto.git && cd howto
pip install pyyaml                       # the only dependency

./scripts/validate.sh                    # validate every recipe against the schema
python3 scripts/stats.py                 # per-domain coverage dashboard
python3 scripts/export.py --format sft   # instruction-tuning pairs (JSONL)
python3 scripts/export.py --format eval  # task specs with success criteria (JSONL)
python3 scripts/export.py --format json  # full structured recipes
```

Or just read one: [`transit/ride-a-subway.md`](transit/ride-a-subway.md) · [`embodied/kitchen/load-a-dishwasher.md`](embodied/kitchen/load-a-dishwasher.md) · [`daily/social/pay-at-a-cashier.md`](daily/social/pay-at-a-cashier.md)

---

<a id="inside"></a>
## 🗂️ What's inside

One task = one markdown file, separated by domain ([`domains.json`](domains.json) is the registry, [`INDEX.md`](INDEX.md) is the full linked index, and the frontmatter is formally specified in [`schema/recipe.schema.json`](schema/recipe.schema.json)). Every recipe shares one skeleton:

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
6. **Multimodal, with text as the floor.** Recipes can attach diagrams, photos, and clips per step via the `media` frontmatter (roles: action-demo, expected-observation, diagram, warning, overview), each with a full alt description so every recipe still trains text-only models. See the fare-gate diagram in [`transit/ride-a-subway.md`](transit/ride-a-subway.md) and the rack layout in [`embodied/kitchen/load-a-dishwasher.md`](embodied/kitchen/load-a-dishwasher.md).

---

<a id="roadmap"></a>
## 🗺️ Roadmap

The corpus is at **337 recipes, growing to 200**, all currently `draft` status. Where help lands hardest:

- [ ] 200 recipes across all 12 domains (thinnest today: government, healthcare, housing, communication)
- [ ] Locale variant packs: `jp-tokyo`, `cn-beijing`, `de-berlin`, and yours
- [ ] First `reviewed` and `verified` promotions (agent-executability evidence; see CONTRIBUTING)
- [ ] Embodied recipes → simulator task compiler
- [ ] Multimodal coverage: a diagram for every embodied recipe
- [ ] Pre-built SFT/eval exports as tagged releases

---

<a id="contributing"></a>
## 🤝 Contributing

One recipe = one markdown file = one PR.

1. Copy [`TEMPLATE.md`](TEMPLATE.md) into the right domain directory
2. Write the procedure you actually know (original content only)
3. `./scripts/validate.sh` until green ✅
4. Open the PR

The short rules: every step needs an *Expect:* · verification must be checkable · irreversible steps get ⚠️ · embodied recipes need the robot frontmatter. Full rules in [CONTRIBUTING.md](CONTRIBUTING.md).

**🌍 Locale expertise is especially welcome.** Recipes for how things work in *your* city make agents useful beyond the defaults.

---

<a id="citing"></a>
## 📎 Citing and using the data

Recipe content is CC-BY-4.0: training (including commercial) is fine with attribution; see [LICENSE](LICENSE). Export formats are documented in [`scripts/export.py`](scripts/export.py)'s header, and each JSONL record carries the recipe `id` for attribution. If you use the corpus in research:

```bibtex
@misc{howto2026,
  title  = {howto: an open library of everyday procedural knowledge for training agents and robots},
  author = {{howto contributors}},
  year   = {2026},
  url    = {https://github.com/ShirleyHuang11/howto}
}
```

---

<div align="center">

Code: [MIT](LICENSE) · Content: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

**⭐ Star this repo if your agent ever confidently walked the wrong way out of a subway station.**

</div>
