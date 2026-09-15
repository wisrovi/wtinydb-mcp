#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== Building Docker test image for wtinydb-mcp ==="
docker build -t wtinydb-mcp-tests -f "$SCRIPT_DIR/Dockerfile" "$REPO_DIR"

echo "=== Running wtinydb-mcp Unit Tests inside Docker ==="
docker run --rm wtinydb-mcp-tests
