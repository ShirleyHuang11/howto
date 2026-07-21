#!/usr/bin/env bash
# Validate all recipes (or the given paths) against the howto schema.
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 scripts/validate.py "$@"
