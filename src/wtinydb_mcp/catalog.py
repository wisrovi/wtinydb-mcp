"""WTinyDB Architectural Patterns Catalog."""

from typing import Dict, List, Optional


class PatternsCatalog:
    """Catalog of production-ready patterns for WTinyDB document database architectures."""

    PATTERNS = [
        {
            "id": "pydantic-crud",
            "name": "Pydantic Document Repository",
            "feature": "CRUD & Models",
            "module": "wtinydb.core.database",
            "description": "Standard repository pattern wrapping WTinyDB with Pydantic model validation.",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "async-wtinydb",
            "name": "Async Document Operations",
            "feature": "Async / FastAPI Integration",
            "module": "wtinydb.core.async_db",
            "description": "Non-blocking ThreadPoolExecutor wrapper for high-throughput async APIs.",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "fluent-query",
            "name": "Fluent Query Builder",
            "feature": "Queries & Filtering",
            "module": "wtinydb.core.query",
            "description": "Chainable query builder (Q) for NoSQL field matching, regex search, and list filters.",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "soft-delete-audit",
            "name": "Soft Delete & Audit Trailing",
            "feature": "Audit & Lifecycle",
            "module": "wtinydb.models",
            "description": "Mixins for automatic created_at, updated_at timestamps and logical deletion.",
            "origin": "wisrovi SUITE",
        },
    ]

    def search(self, query: str) -> List[Dict[str, str]]:
        """Search patterns matching query string across name, feature, or description."""
        q = query.lower()
        results = []
        for p in self.PATTERNS:
            if q in p["name"].lower() or q in p["feature"].lower() or q in p["description"].lower():
                results.append(p)
        return results
