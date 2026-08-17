---
name: troubleshoot-slow-internet
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min-1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Identify whether slow internet comes from the device, Wi-Fi, router, modem, ISP, or a specific service, then apply the right fix.

## Preconditions

- You can access the router or mesh app.
- You know the internet plan speed or can check the provider account.
- At least one phone or computer can run a speed test.

## Steps

1. **Define the symptom.** Note whether everything is slow, one app is slow, Wi-Fi drops, or uploads are the problem. → *Expect:* the problem is described clearly enough to test.
2. **Run a baseline speed test.** Test near the router on Wi-Fi and record download, upload, latency, and time of day. → *Expect:* you have numbers to compare against the plan.
3. **Test another device.** Run the same test on a second phone or computer. → *Expect:* you know whether the issue follows one device or the network.
4. **Restart network equipment.** Unplug modem and router or mesh for 30 seconds, plug modem first, then router, and wait until lights stabilize. → *Expect:* internet returns and equipment shows normal status.
5. **Compare wired or close-range performance.** Use Ethernet if possible, or stand beside the router and retest. → *Expect:* you know whether Wi-Fi distance is the bottleneck.
6. **Check router or mesh status.** Open the router app/admin page and look for offline nodes, firmware updates, connected-device load, or ISP outage notices. → *Expect:* obvious network health warnings are resolved or noted.
7. **Reduce local congestion.** Pause large downloads, cloud backups, game updates, and video streams, then retest. → *Expect:* speeds or latency improve if local traffic was the cause.
8. **Contact the ISP with evidence.** If wired or near-router speed remains far below plan after restart, report timestamps and test results. → *Expect:* the ISP can check line signal, outage, provisioning, or modem issues.

## Decision points

- One device is slow → focus on that device's Wi-Fi, VPN, browser, or malware.
- Wired speed is good but Wi-Fi is bad → improve router placement, channel, mesh coverage, or device band.
- Upload is slow only during backups → schedule backups outside calls and gaming.
- Latency is high but speed is fine → look for congestion, VPN, or bufferbloat rather than plan speed.

## Failure modes & recovery

- **F1 Speed test varies wildly:** detect large swings between runs → test at three times and compare wired versus Wi-Fi.
- **F2 Router app unreachable:** detect admin page or app cannot connect → restart router and use the printed admin address or app reset path.
- **F3 ISP blames Wi-Fi:** detect poor wired speed too → provide wired test results and modem signal evidence.
- **F4 Smart-home devices disconnect after changes:** detect devices offline → restore the previous Wi-Fi name/password or reconnect them manually.

## Verification

A current test identifies the bottleneck, and after the fix the affected device or location reaches an acceptable speed and latency for browsing, calls, or streaming.

## Variations

- Mesh Wi-Fi: test near each node and check node backhaul quality.
- Apartments: neighboring networks can crowd Wi-Fi, so router placement and band selection matter.
- Cellular home internet: signal strength and tower congestion may dominate speed.

## Safety & privacy

Low risk. Do not share router admin passwords or ISP account details in public forums, and avoid factory resetting equipment unless you have setup information.
