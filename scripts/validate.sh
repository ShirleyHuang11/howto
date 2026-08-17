#!/usr/bin/env bash
# Validate all recipes (or the given paths) against the howto schema.
# With no arguments, also validates every journey (journeys/*.md).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/validate.py "$@"
if [ "$#" -eq 0 ]; then
  python3 scripts/validate_journeys.py
fi
