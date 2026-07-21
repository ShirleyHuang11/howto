---
name: kebab-case-task-name          # must match the filename (without .md)
domain: daily                        # top-level directory the recipe lives in
subdomain: food                      # required only for domains with subdirectories (embodied, daily)
locale: [generic]                    # generic first; add variants like us-nyc, jp-tokyo, cn-beijing
interface: physical                  # physical | web | mobile-app | phone-call | mixed
difficulty: basic                    # basic | intermediate | advanced
est_time: 10min
risk: low                            # low | medium (money/identity involved) | high (irreversible)
prerequisites: []                    # recipe names (e.g. accounts/log-in) or capability tags
status: draft                        # draft | reviewed | verified
last_verified: 2026-07-20
# --- embodied extension: required when domain is embodied ---
# objects: [kettle, cup]             # object classes the task manipulates
# affordances: [button-press, pour]  # manipulation primitives required
# workspace: kitchen                 # scene class, used for sim task compilation
# safety: {hot_surfaces: true, fragile: [], human_proximity: continue}
# --- multimodal extension: optional, any recipe ---
# media:                             # assets live in <domain-dir>/assets/<recipe-name>/
#   - path: assets/task-name/step4.svg
#     step: 4                        # omit for recipe-level assets
#     role: diagram                  # action-demo | expected-observation | diagram | warning | overview
#     alt: "One-sentence text description; required, it is the text-only fallback"
---

## Goal

One or two sentences: the end state this recipe achieves, from the actor's perspective.

## Preconditions

- What must already be true before starting (possessions, access, location, knowledge).
- Reference other recipes for non-trivial preconditions: requires `accounts/log-in`.

## Steps

1. **Imperative step name.** Concrete action. → *Expect:* the observation that confirms the step worked.
2. **Next step.** [BRANCH: option A | option B] when the path forks — describe each briefly or link a Decision point.
   - ⚠️ *Irreversible:* mark any step that cannot be undone (payment, deletion, physical damage) and state what to confirm first.
3. Continue until the Goal is reached. Every step gets an *Expect* unless the effect is instantaneous and obvious.

## Decision points

- Condition that changes the path → what to do (reference a Failure mode or another recipe if applicable).

## Failure modes & recovery

- **F1 Short failure name:** how to detect it → how to recover.
- **F2 …:** each failure mode observed in practice gets an entry.

## Verification

The checkable end-state predicate: how the actor (or a program) confirms the task succeeded. Be concrete — this section compiles into a success checker.

## Variations

- `locale-or-platform`: what differs (fares, UI labels, regulations, appliance types).

## Safety & privacy

Risk notes: what personal data is exposed, what money is at stake, what physical hazards exist, and which steps require explicit confirmation.
