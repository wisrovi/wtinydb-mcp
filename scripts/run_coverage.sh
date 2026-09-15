#!/usr/bin/env bash
set -e

echo "=== Running wtinydb-mcp Code Coverage Analysis ==="
pytest --cov=wtinydb_mcp --cov-report=term-missing --cov-report=html:coverage_html tests/
echo "=== Coverage report generated in coverage_html/ index.html ==="
