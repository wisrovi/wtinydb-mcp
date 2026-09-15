FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml requirements.txt README.md ./
COPY src/ ./src/
COPY tests/ ./tests/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -e .

CMD ["pytest", "--cov=wtinydb_mcp", "--cov-report=term-missing", "tests/"]
