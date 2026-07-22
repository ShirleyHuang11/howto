---
name: set-up-broadband-in-a-new-home
domain: housing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h-3h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Order, install, and verify home broadband so the new home has usable internet with documented account and router details.

## Preconditions

- You know the exact service address, move-in date, and access constraints.
- You can approve installation work or have landlord permission if drilling or new cabling may be needed.
- You have a payment method and contact number for installation updates.
- You know your speed needs for work, streaming, gaming, calls, or smart devices.

## Steps

1. **Check availability by exact address.** Use provider and independent coverage checkers, including unit number. → *Expect:* a short list of actual service types and speeds available at the home.
2. **Compare plan terms.** Check speed, upload rate, data caps, contract length, install fees, equipment fees, and cancellation rules. → *Expect:* the chosen plan matches your usage and stay length.
3. **Order ahead.** Book as soon as you have a move-in date because install appointments can have lead time. → *Expect:* an install or activation date near move-in.
4. **Prepare the install location.** Find the existing coax, fiber, phone, or network point and clear access around it. → *Expect:* the technician or self-install kit can reach the entry point.
5. **Install or receive the router.** [BRANCH: technician install | self-install kit] let the technician finish line activation or connect modem and router per labels. → *Expect:* router lights show service, internet, and Wi-Fi readiness.
6. **Place the router sensibly.** Put it high, central, ventilated, and away from thick walls, metal cabinets, and electrical clutter. → *Expect:* main living and work areas get stronger signal.
7. **Secure Wi-Fi.** Change the admin password if allowed, use WPA2 or WPA3, set a strong network password, and disable unsafe defaults. → *Expect:* unknown users cannot join or manage the router.
8. **Test speed and latency.** Run tests near the router and in normal work areas, preferably wired and wireless. → *Expect:* speeds are close to the plan near the router and acceptable where you use devices.
9. **Save account and equipment details.** Record account number, support contact, install date, router login method, Wi-Fi name, and return obligations. → *Expect:* support calls and future moves are easier.

## Decision points

- Fiber is available but costs more → choose it if upload speed, reliability, or remote work matters.
- Only mobile broadband is available → test signal indoors before committing to a long contract.
- Landlord restricts drilling → request written permission or choose a no-drill option.
- Poor coverage in one room → add mesh nodes, wired backhaul, or powerline only after testing router placement.

## Failure modes & recovery

- **F1 Provider says no service after order:** detect canceled install or failed activation → ask for the reason and check alternative technologies.
- **F2 Technician cannot access entry point:** detect missed install due to locked room or building area → rebook and coordinate access in writing.
- **F3 Speed far below plan:** detect repeated low wired tests → contact support with test times, device type, and modem status.
- **F4 Weak Wi-Fi:** detect good wired speed but bad room coverage → move router, reduce interference, then add mesh.
- **F5 Router credentials lost:** detect inability to manage settings → use provider account recovery or factory reset only if you know how to reconfigure service.

## Verification

The broadband account is active, the router is secured, and a speed test near the router plus one normal-use room meets the practical needs for the home.

## Variations

- `apartment`: building wiring, shared risers, and landlord access can control install timing.
- `rural`: satellite, fixed wireless, or cellular may be the realistic options.
- `short-term-rental`: avoid long contracts and confirm cancellation fees before ordering.
- `work-from-home`: prioritize upload speed, latency, and backup tethering over headline download speed.

## Safety & privacy

Do not let installers into private rooms without supervision. Router labels and account emails expose network access, so store them privately. Medium risk comes from contract costs, installation work, and household data exposure over an insecure network.
