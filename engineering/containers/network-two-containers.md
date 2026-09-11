---
name: network-two-containers
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You connect two local containers on a private Docker network so one service can reach the other by container name without exposing unnecessary host ports.

## Preconditions

- Docker or Podman is installed.
- Two images or services are available, such as an app and a database.
- You know the internal port the target service listens on.

## Steps

1. **Create a user-defined network.** Run `docker network create myapp-net`. → *Expect:* `docker network inspect myapp-net` exits 0.
2. **Start the dependency on the network.** Run `docker run -d --name db --network myapp-net -e POSTGRES_PASSWORD=local postgres:16`. → *Expect:* the dependency container status is `Up`.
3. **Start the client on the same network.** Run `docker run --rm --network myapp-net IMAGE <client-command>`. → *Expect:* the client can resolve `db` as a hostname.
4. **Use internal service ports.** Configure the client with `db:5432`, not `localhost:5432`, for container-to-container traffic. → *Expect:* connections go over the private network.
5. **Expose only what the host needs.** Add `-p` only for services accessed from the host browser or tools. → *Expect:* internal-only dependencies have no published host ports.
6. **Test DNS and connectivity.** Run a temporary tool container such as `docker run --rm --network myapp-net curlimages/curl:latest curl -sS http://service:PORT/health`. → *Expect:* DNS resolves and the target responds.
7. **Clean up when done.** Stop containers and run `docker network rm myapp-net` after disconnecting them. → *Expect:* the temporary network is removed.

## Decision points

- Services are already in Compose → use the Compose-created default network and service names.
- Need isolation between projects → create separate networks per project or stack.
- Need host-to-container access → publish only the specific required port.

## Failure modes & recovery

- **F1 Uses localhost incorrectly:** detect connection refused from one container to `localhost` → change host to the target container or service name.
- **F2 Name not resolvable:** detect DNS errors → verify both containers are attached to the same user-defined network.
- **F3 Port confusion:** detect connecting to published host port from another container → use the container's internal listening port.
- **F4 Network removal fails:** detect active endpoint errors → stop or disconnect containers before removing the network.

## Verification

Run `docker network inspect myapp-net`, then from a container on that network run a health or socket check such as `docker run --rm --network myapp-net curlimages/curl:latest curl -f http://web:3000/health`; both commands exit 0.

## Variations

- `Docker Compose`: services reach each other by service name on the default project network.
- `Podman`: use pods or user-defined networks depending on the desired topology.
- `Kubernetes`: use Services and DNS names rather than Docker networks.

## Safety & privacy

Low risk for local networking. Avoid publishing databases or admin tools to the host unless necessary, use local-only credentials, and remove temporary networks that connect unrelated test services.
