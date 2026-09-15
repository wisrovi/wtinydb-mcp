# wtinydb-mcp: Model Context Protocol Server for WTinyDB

`wtinydb-mcp` is an official **Model Context Protocol (MCP)** server built on top of **FastMCP** that equips AI agents with tools to architect, validate, scaffold, and generate code for **WTinyDB** (TinyDB + Pydantic document database engine).

## Key Technologies & Libraries

- **[MCP Protocol](https://modelcontextprotocol.io/)**: Open standard connecting AI models to external tools and context.
- **[FastMCP](https://github.com/jlowin/fastmcp)**: Python framework for fast MCP server implementation.
- **[WTinyDB](file:///home/william.rodriguez/Documents/w_libraries/w_libraries/wtinydb_os/wtinydb)**: Pydantic-powered document database engine on top of TinyDB.
- **[Pydantic v2](https://docs.pydantic.dev/)**: Data schema validation and Python AST inspection.
- **[Pytest](https://docs.pytest.org/)**: Modern Python testing framework.
- **[Pytest-Cov](https://pytest-cov.readthedocs.io/)**: Code coverage measurement for pytest.
- **[Docker](https://www.docker.com/)**: Containerized test execution environment.

---

## MCP Tools Exposed

1. **`validate_model_schema(model_code: str)`**: Validates Pydantic document models for WTinyDB compatibility.
2. **`search_wtinydb_pattern(query: str)`**: Searches the official wisrovi SUITE catalog for WTinyDB architectural patterns.
3. **`deploy_wtinydb_scaffolding(target_dir: str, project_name: str, scaffold_type: str)`**: Deploys project scaffolding with repository, config, models, and tests.
4. **`get_wtinydb_architect_blueprints()`**: Returns code reference and blueprints for WTinyDB features.
5. **`get_wtinydb_architect_manual()`**: Returns the comprehensive WTinyDB architecting manual.
6. **`generate_wtinydb_crud(model_code: str)`**: Automatically generates repository CRUD class for Pydantic models.

---

## Running Unit Tests & Coverage

### Local Pytest Execution

```bash
# Install editable package
pip install -e .

# Run pytest test suite
pytest tests/

# Calculate code coverage
./scripts/run_coverage.sh
```

### Docker Containerized Test Execution

```bash
./scripts/run_tests_docker.sh
```

---

*Part of the wisrovi SUITE ecosystem.*