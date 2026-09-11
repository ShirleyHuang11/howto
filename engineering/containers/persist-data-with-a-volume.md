---
name: persist-data-with-a-volume
domain: engineering
subdomain: containers
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You attach persistent storage to a container so important data survives container replacement and can be backed up or removed intentionally.

## Preconditions

- The application data directory inside the container is known.
- Docker, Podman, or Compose is available.
- You understand whether the data is disposable local state or important production-like data.

## Steps

1. **Identify the data path.** Read the image docs or config for directories such as `/var/lib/postgresql/data` or `/data`. → *Expect:* only the real state directory is selected.
2. **Create a named volume.** Run `docker volume create myapp-data`. → *Expect:* `docker volume inspect myapp-data` exits 0.
3. **Mount the volume at runtime.** Run `docker run -d --name myapp -v myapp-data:/data IMAGE`. → *Expect:* the container starts with the volume mounted at the data path.
4. **Write a sentinel record.** Use the app, database client, or `docker exec` to create a test record or file. → *Expect:* the data exists inside the mounted path.
5. **Recreate the container.** Run `docker rm -f myapp` and start a new container with the same `-v myapp-data:/data`. → *Expect:* the sentinel record remains.
6. **Document backup and cleanup commands.** Use image-specific backup tooling or volume archive commands, and remove with `docker volume rm` only when data is disposable. → *Expect:* operators know how to preserve or intentionally delete the state.

## Decision points

- Data is a database → prefer database-native backup and restore over copying live files.
- Need host-editable files → use a bind mount, but expect host permission differences.
- Running in Kubernetes → use a PersistentVolumeClaim instead of a Docker named volume.

## Failure modes & recovery

- **F1 Data disappears after recreate:** detect missing sentinel → verify the mount target and that the app writes to that path.
- **F2 Permission denied:** detect write errors → align container user ownership or initialize the volume with correct permissions.
- **F3 Accidental anonymous volume:** detect unnamed volumes in `docker inspect` → switch to explicit named volumes in commands or Compose.
- **F4 Corrupt backup:** detect restore failure → stop writes or use app-native consistent backup commands.

## Verification

Run a recreate test: write a sentinel inside the mounted path, remove the container, start a new one with the same named volume, and run `docker exec myapp test -f /data/sentinel`; the final command exits 0.

## Variations

- `Docker Compose`: define named volumes under top-level `volumes` and mount them by service.
- `Bind mount`: use `-v "$PWD/data:/data"` for local file inspection.
- `Kubernetes`: use `volumeMounts` plus a `persistentVolumeClaim`.

## Safety & privacy

Medium risk because persistent volumes may hold databases, uploads, or personal data. Confirm before deleting volumes, restrict host permissions, encrypt backups when needed, and do not mount sensitive host paths unless required.
