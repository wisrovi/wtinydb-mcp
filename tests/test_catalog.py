"""Unit tests for PatternsCatalog in wtinydb-mcp.

Validates catalog search functionality and pattern matching.
"""

from wtinydb_mcp.catalog import PatternsCatalog


def test_catalog_search():
    """Validates searching catalog for patterns by query string.

    Asserts that searching for 'Pydantic' returns the Pydantic Document Repository pattern.
    """
    catalog = PatternsCatalog()

    results = catalog.search("Pydantic")
    assert len(results) >= 1
    assert any(p["id"] == "pydantic-crud" for p in results)

    async_results = catalog.search("async")
    assert len(async_results) >= 1

    empty_results = catalog.search("nonexistent_pattern_xyz")
    assert len(empty_results) == 0
