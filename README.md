<p align="center">
  <a href="https://linkedin.com/in/wisrovi-rodriguez"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://wisrovi.dev"><img src="https://img.shields.io/badge/Author-wisrovi.dev-111827?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Portal" /></a>
  <a href="https://orcid.org/0009-0005-0710-1861"><img src="https://img.shields.io/badge/ORCID-0009--0005--0710--1861-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License" /></a>
</p>

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

---

## 👤 Autor & Afiliación Oficial

* **William Steve Rodriguez Villamizar (Wisrovi)**
* **Cargo:** Principal AI Engineer & Applied AI Solutions Architect | Scientific Researcher
* 📧 **Email:** [wisrovi.rodriguez@gmail.com](mailto:wisrovi.rodriguez@gmail.com)
* 🌐 **Portal Oficial:** [wisrovi.dev](https://wisrovi.dev)
* 💼 **LinkedIn:** [wisrovi-rodriguez](https://www.linkedin.com/in/wisrovi-rodriguez/)
* 🆔 **ORCID:** [0009-0005-0710-1861](https://orcid.org/0009-0005-0710-1861)
* 📦 **PyPI:** [pypi.org/user/wisrovi/](https://pypi.org/user/wisrovi/)
* 🐙 **GitHub:** [@wisrovi](https://github.com/wisrovi)
