# 🗺️ Journeys — long-horizon tasks

A **journey** is a task a single recipe can't hold: it spans calendar time, waits on third
parties, accumulates persistent state, branches, and forces **re-planning** when new information
arrives — buying a home, recovering from identity theft, getting out of debt, switching jobs.

A journey is a **temporal DAG whose leaf nodes are ordinary [`howto` recipes](../INDEX.md)**. It
plans; the recipes execute. The one rule that keeps a journey from decaying into a generic
listicle — and it is **machine-enforced** by [`scripts/validate_journeys.py`](../scripts/validate_journeys.py):

> **Every leaf must reference a real, validated recipe id, and every milestone carries
> machine-usable structure — a gate, a verify predicate, and a re-plan trigger — not just prose.**

Journeys are a small, hand-curated tier (not a mass-generated domain): a bad journey on a
high-stakes task is worse than none. They are counted and validated **separately** from recipes.

## The four journeys

| Journey | Horizon | Composes | What's hard about it |
|---|---|---|---|
| [`recover-from-identity-theft`](recover-from-identity-theft.md) | 1mo–12mo | 18 recipes | parallel bureau tracks, 30-day dispute clocks, a monitoring loop that can restart everything |
| [`buy-a-home`](buy-a-home.md) | 2mo–12mo | many | irreversible commitments (offer, closing), financing gated on appraisal/underwriting |
| [`get-out-of-debt`](get-out-of-debt.md) | 3mo–36mo | many | a control loop, not a one-shot; delayed reward over years |
| [`job-search-and-switch`](job-search-and-switch.md) | 4wk–4mo | many | never resign before the offer is signed; ghosting and re-planning throughout |

## Frontmatter

| Field | Meaning |
|---|---|
| `name` | kebab-case, equals the filename stem |
| `kind` | always `journey` |
| `domain` | primary domain (a journey pulls recipes from many) |
| `locale` | `[generic]` first; jurisdiction variants matter far more than for recipes |
| `horizon` | elapsed calendar time, e.g. `2wk-3mo`, `6mo-2yr` (units: `min h d wk mo yr`) |
| `difficulty` | `basic \| intermediate \| advanced` |
| `risk` | `low \| medium \| high` |
| `actors` | other parties in the loop, e.g. `[you, lender, credit-bureaus]` |
| `status` | `draft \| reviewed \| verified` |
| `last_verified` | `YYYY-MM-DD` |

## Body sections (fixed order)

`Goal` → `Outcome state` → `Preconditions` → `Milestones` → `Dependency graph` (a `mermaid`
flowchart) → `Decision points` → `Failure modes & recovery` → `Re-plan triggers` → `Verification`
→ `Variations` → `Safety & privacy`.

Each milestone is a `### M<n> — Title` block carrying **Track**, **Gate**, **Do** (backticked
recipe ids), **Wait**, **Verify**, and **Re-plan if**. See [`TEMPLATE.md`](TEMPLATE.md) and any of
the four journeys for the exact shape.

## What a journey compiles into (training value)

- **Hierarchical planning traces** — goal → milestones → recipe steps.
- **Long-range gating / dependency episodes** — "blocked on M2 and a 30-day clock".
- **Re-planning episodes** — a trigger fires, the plan is revised; rare, valuable supervision.
- **Verifiable leaves** — every node bottoms out in a recipe with a checkable predicate, so the
  journey stays auditable even though its terminal reward is delayed.

Export the planning traces with `python3 scripts/export.py --format journeys`.
