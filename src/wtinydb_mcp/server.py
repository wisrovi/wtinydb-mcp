"""wtinydb-mcp: Model Context Protocol server for WTinyDB architecting and code generation."""

import argparse
import ast
import json
import logging
import os
import signal
import subprocess
import sys
from functools import lru_cache

from mcp.server.fastmcp import FastMCP

from wtinydb_mcp.catalog import PatternsCatalog
from wtinydb_mcp.templates import TemplateGenerator

# Setup logging strictly to stderr to avoid breaking MCP protocol
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stderr)
logger = logging.getLogger(__name__)

PID_FILE = os.path.expanduser("~/.wtinydb_mcp.pid")

# Create primary FastMCP Server instance
mcp = FastMCP("wtinydb-mcp-server")


@lru_cache(maxsize=1)
def get_catalog() -> PatternsCatalog:
    """Return shared patterns catalog instance."""
    return PatternsCatalog()


def _is_pydantic_model(cls: ast.ClassDef) -> bool:
    """Return True if class inherits from BaseModel or Mixins."""
    return any(
        isinstance(b, ast.Name) and b.id in ("BaseModel", "TimestampMixin", "SoftDeleteMixin", "AuditMixin")
        for b in cls.bases
    )


@mcp.tool()
def validate_model_schema(model_code: str) -> str:
    """Validate a Pydantic model definition for WTinyDB compatibility."""
    try:
        tree = ast.parse(model_code)
        issues = []
        warnings = []

        classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        model_classes = [c for c in classes if _is_pydantic_model(c)]

        if not model_classes:
            issues.append("No Pydantic BaseModel or WTinyDB Mixin subclass found.")

        result = "Valid Model Validation Result:\n"
        if issues:
            result += "Issues:\n" + "\n".join(f"  ❌ {i}" for i in issues) + "\n"
        if warnings:
            result += "Warnings:\n" + "\n".join(f"  ⚠️ {w}" for w in warnings) + "\n"
        if not issues and not warnings:
            result += "✅ Model looks good for WTinyDB document storage!"
        return result

    except SyntaxError as e:
        return f"❌ Syntax Error in model code: {e}"
    except Exception as e:
        return f"❌ Validation Error: {type(e).__name__}: {e}"


@mcp.tool()
def search_wtinydb_pattern(query: str) -> str:
    """Search for production-ready WTinyDB architectural patterns."""
    results = get_catalog().search(query)
    if not results:
        return f"No pattern matching '{query}' was found in WTinyDB catalog."

    response = "Found production-ready architectural patterns in wisrovi SUITE:\n\n"
    for p in results:
        response += f"🚀 [{p['origin']}] {p['name']}\n"
        response += f"   - Feature: {p['feature']}\n"
        response += f"   - Module: {p['module']}\n"
        response += f"   - Description: {p['description']}\n\n"
    return response


@mcp.tool()
def deploy_wtinydb_scaffolding(
    target_dir: str,
    project_name: str = "wtinydb_project",
    scaffold_type: str = "standard",
) -> str:
    """Deploys a professional WTinyDB project structure following wisrovi standards."""
    try:
        if not os.path.isabs(target_dir):
            return "Error: target_dir must be an absolute path."

        for folder in TemplateGenerator.get_folders(scaffold_type):
            os.makedirs(os.path.join(target_dir, folder), exist_ok=True)

        blueprints = TemplateGenerator.get_files_blueprint(scaffold_type, project_name)
        for rel_path, content in blueprints.items():
            full_path = os.path.join(target_dir, rel_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

        return f"Success: WTinyDB architecture '{project_name}' deployed at {target_dir}"
    except Exception as e:
        return f"Error deploying scaffolding: {str(e)}"


@mcp.tool()
def get_wtinydb_architect_blueprints() -> str:
    """Complete reference with read/write/update examples for every WTinyDB feature."""
    crud_code = (
        "from pydantic import BaseModel, Field\n"
        "from wtinydb import WTinyDB, SoftDeleteMixin\n\n"
        "class Article(SoftDeleteMixin, BaseModel):\n"
        "    title: str\n"
        "    content: str\n"
        "    tags: list[str] = []\n\n"
        "db = WTinyDB(Article, db_path='articles.json')\n"
        "# WRITE\n"
        "art = db.insert(Article(title='Intro', content='Hello World'))\n"
        "# READ\n"
        "all_articles = db.get_all()\n"
        "art1 = db.get(1)\n"
        "# UPDATE\n"
        "db.update(1, {'title': 'Updated Title'})\n"
        "# DELETE\n"
        "db.delete(1, hard=False)\n"
    )

    async_code = (
        "import asyncio\n"
        "from wtinydb import WTinyDB, AsyncWTinyDB\n\n"
        "async def main():\n"
        "    sync_db = WTinyDB(Article, db_path='articles.json')\n"
        "    db = AsyncWTinyDB(sync_db)\n"
        "    art = await db.insert(Article(title='Async Title', content='Text'))\n"
        "    rows = await db.get_all()\n"
        "    await db.close()\n"
    )

    query_code = (
        "from wtinydb import WTinyDB, Q\n\n"
        "db = WTinyDB(Article, in_memory=True)\n"
        "# Query with operators\n"
        "tech_articles = db.find(Q('tags').in_list('tags', ['tech', 'python']))\n"
        "regex_matches = db.find(Q('title').matches('title', r'^Intro'))\n"
    )

    return (
        "WTINYDB EXPERT BLUEPRINTS (COMPLETE REFERENCE)\n\n"
        "=== 1. MODEL & CRUD ===\n" + crud_code + "\n"
        "=== 2. ASYNC OPERATIONS ===\n" + async_code + "\n"
        "=== 3. FLUENT QUERY BUILDER ===\n" + query_code
    )


@mcp.tool()
def get_wtinydb_architect_manual() -> str:
    """Expert manual for building high-performance document database systems with WTinyDB."""
    manual_text = (
        "WTINYDB ARCHITECT MANUAL (ADVANCED)\n"
        "--- PROJECT STRUCTURE RULES (MANDATORY) ---\n"
        "1. CONFIG: All database settings MUST be centralized in `config/settings.py` as a `DatabaseSettings` dataclass.\n"
        "2. MODELS: All Pydantic models MUST be placed inside `models/` directory.\n"
        "3. REPOSITORIES: All data-access logic MUST live in `repositories/` wrapping `WTinyDB` or `AsyncWTinyDB`.\n"
        "4. ORCHESTRATOR: Service entrypoint MUST be `main.py` at root level.\n\n"
        "--- CORE RULES ---\n"
        "1. Always use Pydantic models for schema definitions.\n"
        "2. Use `SoftDeleteMixin` or `AuditMixin` for soft-deletion and automatic creation/update timestamps.\n"
        "3. Use `Q` fluent query builder for complex filtering.\n"
        "4. For FastAPI/async apps, wrap WTinyDB with `AsyncWTinyDB`.\n\n"
        "Generated by WTinyDB MCP by wisrovi"
    )
    return manual_text


@mcp.tool()
def generate_wtinydb_crud(model_code: str) -> str:
    """Generate repository CRUD wrapper code for a Pydantic model definition."""
    try:
        tree = ast.parse(model_code)
        classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and _is_pydantic_model(n)]
        if not classes:
            return "# Error: No Pydantic model found in provided code."

        model_name = classes[0]
        repo_name = f"{model_name}Repository"

        code = (
            f"from typing import List, Optional\n"
            f"from wtinydb import WTinyDB, Q\n"
            f"# Import {model_name} from models module\n\n"
            f"class {repo_name}:\n"
            f"    def __init__(self, db_path: str = '{model_name.lower()}.json', in_memory: bool = False):\n"
            f"        self.db = WTinyDB({model_name}, db_path=db_path, in_memory=in_memory)\n\n"
            f"    def create(self, item: {model_name}) -> {model_name}:\n"
            f"        return self.db.insert(item)\n\n"
            f"    def get_by_id(self, doc_id: int) -> {model_name}:\n"
            f"        return self.db.get(doc_id)\n\n"
            f"    def get_all(self) -> List[{model_name}]:\n"
            f"        return self.db.get_all()\n\n"
            f"    def update(self, doc_id: int, data: dict) -> {model_name}:\n"
            f"        return self.db.update(doc_id, data)\n\n"
            f"    def delete(self, doc_id: int, hard: bool = False) -> bool:\n"
            f"        return self.db.delete(doc_id, hard=hard)\n"
        )
        return code
    except Exception as e:
        return f"# Generation error: {e}"


def run_stdio():
    """Run MCP server in stdio mode."""
    mcp.run(transport="stdio")


def main():
    """Main CLI entrypoint for wtinydb-mcp server."""
    parser = argparse.ArgumentParser(description="wtinydb-mcp: WTinyDB Architect MCP Server")
    parser.add_argument("command", nargs="?", default="run", choices=["run", "help"])
    args = parser.parse_args()

    if args.command == "run":
        run_stdio()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
