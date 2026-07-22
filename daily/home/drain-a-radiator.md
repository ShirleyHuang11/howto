---
name: drain-a-radiator
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A radiator is drained without flooding the room, then the heating system is refilled and bled so it can run normally again.

## Preconditions

- Heating is off and the radiator is completely cool.
- You have a radiator key, adjustable spanner, hose or tray, towels, bucket, and gloves.
- You know how to refill or repressurize the heating system after draining.

## Steps

1. **Turn heating off and wait.** Let the radiator and pipework cool fully before touching valves. → *Expect:* metal and water are safe to handle.
2. **Close both radiator valves.** Turn the thermostatic or hand valve off and close the lockshield, counting turns. → *Expect:* the radiator is isolated and settings are noted.
3. **Protect the floor.** Lay towels, position a tray or hose at the drain point, and keep a bucket nearby. → *Expect:* any first spill lands on protection.
4. **Open the bleed valve.** Crack the top bleed valve to admit air once draining starts. → *Expect:* air can enter so water will leave smoothly.
5. **Open the drain or loosen the union.** [BRANCH: drain cock | valve union] use the drain cock if fitted, otherwise loosen the lower union carefully. → *Expect:* water begins flowing into the tray, hose, or bucket.
6. **Catch and empty water patiently.** Keep draining until flow stops, tightening briefly when swapping buckets. → *Expect:* the radiator is light enough or empty enough for the next task.
7. **Close and reseal.** Close the drain, retighten the union, close the bleed valve, and reopen radiator valves to their noted positions. → *Expect:* joints are closed and dry.
8. **Refill and rebleed.** Repressurize the system if needed, bleed the radiator, and top pressure back up. → *Expect:* the radiator refills without gurgling.

## Decision points

- Water is black or gritty → expect staining and consider system cleaning.
- Union nut will not move → do not force it against old pipework, call a heating engineer.
- Boiler pressure falls below safe range → stop running heat until refilled by the manual.
- You are removing the radiator from the wall → cap open pipe ends before moving it.

## Failure modes & recovery

- **F1 Joint leaks after refilling:** detect drips at the valve union, recover by closing valves, draining pressure locally, and reseating or replacing the washer.
- **F2 Boiler will not restart:** detect low-pressure lockout, recover by refilling to the specified cold pressure.
- **F3 Air remains trapped:** detect cold top or gurgling, recover by bleeding again after the pump has circulated.
- **F4 Floor gets stained:** detect dirty water on fabric or wood, recover by blotting immediately and using more towels next time.

## Verification

After refilling, the radiator heats evenly, the boiler pressure is in range, and all disturbed joints remain dry for 10 minutes.

## Variations

- `combi-boiler`: repressurize with the filling loop according to the boiler manual.
- `open-vented-system`: header tanks may refill automatically, but trapped air still needs bleeding.
- `decorating`: leave valves capped if the radiator will stay off the wall.

## Safety & privacy

Medium risk from hot water, dirty water stains, and pressure loss. Start cold, control the water path, and do not run a boiler with inadequate pressure.
