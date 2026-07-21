---
name: take-a-licensed-taxi
domain: transit
locale: [generic]
interface: physical
difficulty: basic
est_time: 30min
risk: low
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

You get into a genuinely licensed taxi, reach your destination by a fair route, pay a metered or pre-agreed fare, and leave with a receipt and all your belongings.

## Preconditions

- A destination you can name or show on a map.
- Local currency in small notes plus a card, since not every taxi takes cards.
- A rough sense of the fair fare or route (a maps app estimate is enough).

## Steps

1. **Pick a genuinely licensed taxi.** [BRANCH: taxi rank at a station or airport (safest, ordered queue) | flag a marked cab on the street | phone or app dispatch] → *Expect:* an official livery, visible license/medallion number, and a driver ID displayed inside.
2. **Confirm it is real before getting in.** Licensed cabs have a company name, plate, and a working meter; be wary of unmarked cars touting for fares at airports. → *Expect:* a meter visible on the dash and identification on show.
3. **State the destination and agree the basis.** Say the address or landmark; confirm "on the meter" or, where flat rates are normal (some airports), agree the fixed price first. → *Expect:* driver acknowledges the destination and either starts the meter or states the flat fare.
4. **Watch the meter start correctly.** It should begin at the standard flag-fall, not a random high number, and run only while moving or per the local tariff. → *Expect:* meter reads the known starting fare and increments sensibly.
5. **Keep light route awareness.** Glance at your maps app; a fair route is roughly the app's route. Traffic detours are normal, but a wildly longer path is not. → *Expect:* the cab broadly follows a sensible route toward your destination.
6. **Arrive and read the final fare.** Note the meter total plus any legitimate surcharges (night, luggage, airport), which should be posted. → *Expect:* a total consistent with the meter and any posted extras.
7. **Pay and get a receipt.** Pay by the agreed method; ask for a printed or written receipt showing fare, date, and the cab number. ⚠️ *Irreversible:* cash handed over is gone. Count your change before stepping out. → *Expect:* correct change or card charge, and a receipt in hand.
8. **Do a seat sweep before closing the door.** Check the seat and footwell for phone, bag, and documents. → *Expect:* you are on the pavement with every item you arrived with.

## Decision points

- Driver refuses the meter or quotes an inflated flat rate → decline and take the next cab; at a rank, note the cab number and use the one behind.
- No meter exists in this locale (fares are always negotiated) → agree the full price before departure and do not move until it is clear.
- Card reader "broken" and only cash accepted at the end → this is a common tactic; carry enough cash to avoid being stranded, and prefer app dispatch where payment is automatic.

## Failure modes & recovery

- **F1 Meter runs suspiciously fast:** total climbs faster than distance → ask the driver to explain, note the cab number, and pay under protest if needed; report with the receipt and cab number afterward.
- **F2 Deliberate long detour:** route diverges far from the app with no traffic reason → speak up early and name the direct route; drivers usually correct when they see you are watching.
- **F3 No receipt offered:** you cannot document the ride → insist before paying; a licensed cab must provide one. Photograph the cab number if refused.
- **F4 Item left behind:** you realize after the cab leaves → call the taxi company or app with the cab/receipt number; licensed operators log trips and can trace the driver.

## Verification

You reached your destination, paid a fare consistent with the meter or agreed price, hold a receipt with the cab number, and have all your belongings.

## Variations

- `airport`: use the official rank and ignore touts inside the terminal; many airports post fixed zone fares, so confirm the flat rate up front.
- `app-dispatch`: fare and route are tracked in-app and payment is cashless, which removes most meter and receipt disputes; the licensed-vehicle check still applies.

## Safety & privacy

Low risk. Main exposures are fare overcharging and, rarely, unlicensed drivers. Prefer ranks or app dispatch after dark, sit where you can see the meter, share your live trip with someone if travelling alone, and never enter an unmarked car that approaches you touting for a fare.
