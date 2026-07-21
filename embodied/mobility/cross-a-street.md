---
name: cross-a-street
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [crosswalk, traffic-signal, curb, vehicles, pedestrian-button]
affordances: [button-press, wait, observe, threshold-cross, gap-judge]
workspace: outdoor-urban
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

You (or a sidewalk robot) get from one side of a street to the other at a legal crossing point, with every approaching-traffic check actually performed — the procedure everyone "knows" and fatalities keep proving isn't followed.

## Preconditions

- A crossing point: signalized crosswalk (preferred), marked zebra crossing, or — only where legal and visibility allows — an unmarked low-traffic crossing.
- Attention available: headphones down/one ear out, phone pocketed. The recipe's inputs are eyes and ears; anything consuming them raises the risk class.

## Steps

1. **Position at the crossing point, on the curb, facing traffic-side first.** Stand back from the curb edge (mirrors and turning trucks overhang it); locate the signal or assess the street type. → *Expect:* you know which crossing regime applies: signal, zebra priority, or gap-judgment.
2. **Signalized: press the button (where present) and wait for the walk signal — *and then still check*.** The green man grants right-of-way, not physics: turning vehicles cross the crosswalk on your green in most road systems. → *Expect:* walk signal lit *and* the turning lanes visibly yielding before your first step.
3. **Look in the full sequence: near-lane direction, far-lane direction, near-lane again — plus the over-the-shoulder turn check.** (Left-right-left in right-driving countries; right-left-right in left-driving ones — see Variations for the tourist trap.) Listen between looks; electric vehicles defeat ears. → *Expect:* every lane you'll cross has been personally verified empty or stopping.
4. **Make eye contact / confirm yielding with any near vehicle.** A slowing car with a visible driver looking at you is yielding; a car whose driver you can't see hasn't agreed to anything. At zebra crossings, priority is *taken by confirmation*, not assumed. → *Expect:* mutual acknowledgment with the nearest threat vehicle, or you wait.
5. **Cross briskly and straight — no diagonal, no stopping, no phone.** Continue scanning the far lanes as you go; walk, don't run (running trades observation and footing for seconds). → *Expect:* steady progress; each lane re-checked as you enter it.
6. **Handle the mid-crossing signal change without panic.** Flashing/countdown while you're in the road: continue at pace to the far side (or the refuge island where present) — the clearance interval is designed for exactly you. Never reverse mid-street on impulse. → *Expect:* far curb reached; done.

## Decision points

- No crossing infrastructure in reasonable distance, low-speed street → the gap-judgment crossing *doubles* every check in step 3 and demands a gap you could walk twice in; high-speed or multi-lane roads without crossings → walk to the crossing, full stop, however inconvenient — this is the decision that separates statistics.
- Children/robots/mobility-device users in your care → the crossing starts when *the slowest member* can complete it in the gap; hold hands at the curb, not mid-street.
- Night/rain → visibility collapses both ways: reflective/light clothing, double the yield-confirmation standard, and prefer signalized crossings even at detour cost.

## Failure modes & recovery

- **F1 Vehicle runs the crossing while you're in it:** the continuous-scanning in step 5 is what buys the reaction — stop or step back per the vehicle's line, don't freeze in the lane it needs; anger is for the far curb.
- **F2 Signal never gives a walk phase (broken button/beg-button ignored):** wait one full cycle; then treat it as an unsignalized crossing with maximum checks, or use the next crossing — a dead signal doesn't upgrade your rights, it removes protections.
- **F3 Dropped item mid-crossing:** complete the crossing *first*; retrieve only with a fresh full crossing procedure — objects are replaceable in a way step-3 shortcuts are not.
- **F4 Tourist-brain looked the wrong way first:** the London-painted "LOOK RIGHT" exists because this kills; in an unfamiliar country make the full both-ways sequence mechanical and slow for the first days.

## Verification

You're on the far curb having crossed at a crossing point, with the walk signal (or confirmed yields) obtained, the full look-sequence performed including the turn check, and no step of it delegated to assumption, right-of-way, or headphones.

## Variations

- Left-driving countries (`uk`, `jp`, `au`): the look-sequence mirrors — right-left-right — and visiting pedestrians from right-driving countries are a known casualty class (F4).
- `de`/`jp` signal-compliance cultures: red-man waiting is normative even on empty streets (and children are watching); `vn`/`in`-style continuous-traffic streets: the local technique (steady predictable pace through negotiating traffic) is genuinely different — learn it by shadowing locals through their first crossings, not by improvising.
- Robot/AV sidewalk agents: signalized crossings only, conservative gap thresholds, and the eye-contact step becomes explicit yield-detection with a no-go default.

## Safety & privacy

High risk — this file's rating is earned by the statistics, not the difficulty. The three lines that carry it: green-then-still-check (step 2), the full look-sequence with the turn check (step 3), and confirmation-not-assumption of yields (step 4). Attention is the whole input: the phone stays pocketed from curb to curb.
